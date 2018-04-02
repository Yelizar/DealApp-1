$(document).ready(function() {
       $(".Red").focusin(function(){
           $.ajax({
               url: "http://127.0.0.1:8000/chat/",
               success: function(dat){
                    $('#mes').append('{{'+dat+'}}');
        }
        });

    });
});