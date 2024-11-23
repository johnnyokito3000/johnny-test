from flask import Flask, render_template, url_for, request, redirect, flash
from db_conn import conn
import json

app = Flask(__name__)
app.secret_key = 'this is my secret key'

@app.route('/')
def home_page():
    my_cursor = conn.cursor(dictionary=True)

    country = request.args.get('country')

    if country == 'all' or country == None:
        sql = 'SELECT * FROM clients'
    else:
        sql = "SELECT * FROM clients WHERE country='{country}'".format(country=country)

    my_cursor.execute(sql)
    results = my_cursor.fetchall()

    return render_template('index.html', results=results, country=country)

@app.route('/client_form', methods=['GET', 'POST'])
def add_new_client():
    if request.method == 'GET':
        return render_template('client_form.html')
    else:
        # Process the form
        try:
            my_cursor = conn.cursor()

            firstname = request.form.get('firstname')
            lastname = request.form.get('lastname')
            age = request.form.get('age')
            email = request.form.get('email')
            address = request.form.get('address')
            notes = request.form.get('notes')
            country = request.form.get('country')

            sql = "INSERT INTO clients (firstname, lastname, age, email, address, notes, country) VALUE ('{fname}', '{lname}', {age}, '{email}', '{address}', '{notes}', '{country}')".format(fname=firstname, lname=lastname, age=age, email=email, address=address, notes=notes, country=country)
            my_cursor.execute(sql)

            conn.commit()

            flash('Client was created successfully!', 'success')
        except Exception as error:
            error_message = 'Something went wrong while deleting client: {error}'.format(error=error)
            flash(error_message, 'danger')

        return redirect(url_for('home_page'))

@app.route('/ajax_client/<country>')
def ajax_client(country):
    try:
        my_cursor = conn.cursor(dictionary=True)
        if country == 'all':
            sql = 'SELECT * FROM clients'
        else:
            sql = "SELECT * FROM clients WHERE country='{country}'".format(country=country)
        my_cursor.execute(sql)
        data = my_cursor.fetchall()
        results = {'success': True, 'data': data}
        res = json.dumps(results)
        return res
    except Exception as error:
        results = {'success': False, 'message': error}
        res = json.dumps(results)
        return res

@app.route('/delete/<int:id>')
def delete_client(id):
    my_cursor = conn.cursor()
    sql = "DELETE FROM clients WHERE id = {id}".format(id=id)
    my_cursor.execute(sql)
    conn.commit()
    flash('Client successfully deleted!', 'success')
    return redirect(url_for('home_page'))

@app.route('/ajax_delete')
def ajax_delete():
    try:
        # Delete the client
        my_cursor = conn.cursor()
        client_id = request.args.get('client_id')
        sql = "DELETE FROM clients WHERE id={client_id}".format(client_id=client_id)
        my_cursor.execute(sql)
        conn.commit()

        # Rebuild the table (just the body of the table!)
        my_cursor = conn.cursor(dictionary=True)
        country = request.args.get('country')

        if country == 'all':
            sql = 'SELECT * FROM clients'
        else:
            sql = "SELECT * FROM clients WHERE country='{country}'".format(country=country)

        my_cursor.execute(sql)
        data = my_cursor.fetchall()
        res = {'success': True, 'data': data}
        return json.dumps(res)

    except Exception as error:
        res = {'success': False, 'message': error}
        return json.dumps(res)

if __name__ == '__main__':
    app.run(port=3000, debug=True)