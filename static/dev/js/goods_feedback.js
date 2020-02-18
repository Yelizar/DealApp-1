$(document).ready(function () {
    $('#goodsfeedback').on('change keyup keydown paste cut', 'textarea', function () {
        $(this).height(0).height(this.scrollHeight);

    }).find('textarea').change();

    $('.feedback-button').click(function () {
        if ($('.goodsfeedback').css('visibility') === 'hidden') {
            $('.goodsfeedback').css('visibility', 'visible');
            var name = $(this).attr('id');
            if (name !== undefined) {
                name = ucFirst(name);
                document.getElementById('replay-comment-id').value = name;
            }
            $('textarea').focus();
            // $('#id_text').val(name + ', ');
            $(this).setSelectionRange(0, 0);
        } else {
            $('.goodsfeedback').css('visibility', 'hidden');
            delete (name);
        }
    });

    $('.replay-reference').click(function () {
        var linkID = '#comment-' + $(this).attr('id').substring(5);
        if (('.linkID')) {
            console.log(linkID);
            $(linkID)   //$(linkID +' .author')
                .transition('fade up')
                .transition('fade up')
        }
    });
});

function ucFirst(str) {
    if (!str) return str;

    return str[0].toUpperCase() + str.slice(1);
}



