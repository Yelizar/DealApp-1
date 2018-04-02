$(document).ready(function() {
       $(".Red").focusin(function(){
           $.ajax({
               success: function(){
                    $('#mes').append(message);
        }
        });

    });
});