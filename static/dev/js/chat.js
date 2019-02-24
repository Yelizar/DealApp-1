$(document).ready(function() {
       setInterval(function(){
           $.ajax({
               url: "http://127.0.0.1:8000/chat/",
               success: function(dat){
                    $('#mes').replaceWith("<p class='mes' id='mes'>"+dat+"</p>");
        }
        });
    }, 2000);


});
