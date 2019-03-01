$(document).ready(function() {
       setInterval(function(){
           $.ajax({
               url: "http://127.0.0.1:8000/chat/",
               success: function(dat){
                    $('#mes').replaceWith("<i id=mes'>"+dat+"</i>");
        }
        });
    }, 2000);


});
