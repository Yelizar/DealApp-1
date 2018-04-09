$(document).ready(function () {
    $('#string-mes').focusin(function() {
        $.ajax({
            type: 'GET',
            url: "http://127.0.0.1:8000/chat/",
            data: {data: 'get_page'},
            success: function (template) {

                $('#main-box').html(template)

            }
        })
    });

    $('#string-products').focusin(function() {
        $.ajax({
            type: 'GET',
            url: "http://127.0.0.1:8000/goods/",
            data: {data: 'get_page'},
            success: function (template) {

                $('#main-box').html(template)

            }
        })
    });

    $('#string-about').focusin(function() {
        $.ajax({
            type: 'GET',
            url: "http://127.0.0.1:8000/about/",
            data: {data: 'get_page'},
            success: function (template) {

                $('#main-box').html(template)

            }
        })
    });

    $('#string-clients').focusin(function() {
        var user_id;
            user_id = $('#string-clients').attr('data-q-id');
        $.ajax({
            type: 'GET',
            url: "http://127.0.0.1:8000/clients/",
            data: {data: user_id},
            success: function (template) {

                $('#main-box').html(template)

            }
        })
    })
})