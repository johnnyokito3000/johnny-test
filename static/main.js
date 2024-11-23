$(document).ready(function() {
    $(document).on('click', '.btn-delete', function() {
        var client_id = $(this).prop('id');
        var country = $('#country').val();

        if (confirm('Are you sure you want to delete this client?')) {
            $.ajax({
                url: '/ajax_delete',
                dataType: 'json',
                data: {client_id: client_id, country: country},
                success: function(res) {
                    rebuild_table(res);
                }
            });
        }

    });

    $('#country').on('change', function() {
        var country = $(this).val();

        $.ajax({
            url: '/ajax_client/'+country,
            type: 'GET',
            dataType: 'json',
            success: function(res) {
                rebuild_table(res);
            }
        });
        
        
    });
});

function rebuild_table(res) {
    if (res.success) {
        var content = '';
        for (i=0; i<res.data.length; i++) {
            var client = res.data[i];
            content += '<tr>';
            content += '<td>' + client.firstname + '</td>';
            content += '<td>' + client.lastname + '</td>';
            content += '<td>' + client.email + '</td>';
            content += '<td>' + client.age + '</td>';
            content += '<td>' + client.address + '</td>';
            content += '<td>' + client.notes + '</td>';
            content += '<td>' + client.country + '</td>';
            content += '<td>';
            content += '<a id="' + client.id + '" class="btn btn-sm btn-warning btn-delete">Delete</a>';
            content += '</td>';
            content += '</tr>';
        }

        $('#client-table tbody').html(content)
    } else {
        alert(res.message);
    }
}
