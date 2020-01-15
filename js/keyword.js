$('input[type=checkbox]').on('change', function (e) {
    if ($('input[type=checkbox]:checked').length > 5) {
        $(this).prop('checked', false);
        alert("Sorry. Only 5 keyword is allowed.");
    }
});

$('checkbox').children('input[type=checkbox]').click(function (e) {
    $(this).children().css('opacity','1');
});
