/**
 * Created by bogdan on 2/24/17.
 */
$(document).ready(function () {
    var proxyTable = $('#proxyTable').dataTable({
        "ajax": '/ajax_get_proxy_list',
        "bProcessing": true,
        "bLengthChange": true,
        "bFilter": true,
        "bSortable": true,
        "lengthMenu": [[10, 25, 50, 100, 200], [10, 25, 50, 100, 200]],
        "pageLength": 10,
        "bInfo": true,
        "bSearchable": true,
        "bAutoWidth": false,
        "bStateSave": false,
        "aoColumnDefs": [
            {
                "aTargets": [0]
            },
            {
                "aTargets": [1]
            },
            {
                "aTargets": [2]
            },
            {
                "aTargets": [3]
            },
            {
                "mRender": function (data, type, row) {
                    if (data === 'Available') {
                        return '<p><img style="width: 15px; heigth: 15px" src="http://image.flaticon.com/icons/svg/148/148767.svg"> Available</p>'
                    }
                    else if (data === 'Unreachable')
                    {
                        return '<p><img style="width: 15px; heigth: 15px" src="http://image.flaticon.com/icons/svg/148/148766.svg"> Unreachable</p>'
                    }
                    else
                    {
                        return 'Unchecked'
                    }
                },
                "aTargets": [4],
                "bSortable": true
            },
            {
                "mRender": function (data, type, row) {
                    if (data) {
                        return '<p><span hidden>true</span><img style="width: 15px; heigth: 15px" src="http://image.flaticon.com/icons/svg/148/148767.svg"></p>'
                    }
                    else
                    {
                        return '<p><span hidden>false</span></p><img style="width: 15px; heigth: 15px" src="http://image.flaticon.com/icons/svg/148/148766.svg"></p>'
                    }
                },
                "aTargets": [5]
            },
            {
                "aTargets": [6]
            },
            {
                "aTargets": [7]
            }
        ]
    });
    $('#available-filter', this).change( function () {
        proxyTable.fnFilter( $(this).val(), 4);
    });
    $('#anonymity-filter', this).change( function () {
        proxyTable.fnFilter( $(this).val(), 5);
    });
    $('#country-filter', this).change( function () {
        proxyTable.fnFilter( $(this).val(), 2)
    });
    $('#connection-filter', this).change( function () {
        proxyTable.fnFilter( $(this).val(), 3)
    });
    $.ajax({
        type: "GET",
        url: '/ajax_get_country_list',
        data: {},
        dataType: 'json',
        success: function(data) {
            data.forEach(function(i) {
                $('#country-filter').append($('<option>', {
                    value: i,
                    text: i
                }))
            });

        }
    })
});

$(document).ajaxStart(function() {
    $('#show-datatable').hide();
    $('#load-animation').show();
}).ajaxStop(function(){
    $('#load-animation').hide();
    $('#show-datatable').show();
});