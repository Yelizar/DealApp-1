$(document).ready(function() {
    $('#goodsfeedback').on('change keyup keydown paste cut', 'textarea', function () {
        $(this).height(0).height(this.scrollHeight);

    }).find('textarea').change();

    $('.feedback-button').click(function () {
        if($('.goodsfeedback').css('visibility') === 'hidden') {
            $('.goodsfeedback').css('visibility', 'visible');
            var name = $(this).attr('id');
            if(name !== undefined){
                name = ucFirst(name);
                document.getElementById('replay-comment-id').value = name;
            }
            $('textarea').focus();
            // $('#id_text').val(name + ', ');
            $(this).setSelectionRange(0, 0);
        }
        else{
            $('.goodsfeedback').css('visibility', 'hidden');
            if(name) delete(name);
        }
    });
});

function ucFirst(str) {
  if (!str) return str;

  return str[0].toUpperCase() + str.slice(1);
}


