$(document).ready(function() {
       setInterval(function(){
           $.ajax({
               url: "http://127.0.0.1:8000/chat/",
               success: function(dat){
                    $('#mes').replaceWith("<p class='mes' id='mes'>"+dat+"</p>");
        }
        });
    }, 5000);

       setInterval(function(){
           var chat_id = 2;
           $.ajax({
               url: "http://127.0.0.1:8000/chat/"+chat_id+"/",
               data: {data: 'get_message'},
               success: function(last_message){
                    $('#chat-line').before(last_message);
        }
        });
    }, 5000);
});

