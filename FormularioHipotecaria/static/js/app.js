const section = $('.section');
const panel = $('.panel');

$('.opcionNext').each(function (index) {
    const sectionIndex = section.eq(index);
    $(this).click(function () {
        sectionIndex.fadeIn(100);
        $(this).parent().parent().parent().parent().parent().hide();
    });
});

$('.opcion').click(function () {
    $('.opcion').removeClass('opcion-active');
    $(this).addClass('opcion-active');
});

$('.btnNext').each(function (index) {
    const panelIndex = panel.eq(index + 1);
    const opcion = $(this).parent().siblings('.opcion');
    $(this).click(function () {
        if (opcion.hasClass('opcion-active')) {
            panelIndex.fadeIn(100);
            $(this).parent().parent().parent().parent().parent().parent().hide();
        } else {
            $(this).parent().siblings('.emsg').removeClass('hidden');
        }

    });
});

$('.btnAnt').each(function (index) {
    const panelIndex = panel.eq(index);
    $(this).click(function () {
        panelIndex.fadeIn(100);
        $(this).parent().parent().parent().parent().parent().parent().hide();
    });
});