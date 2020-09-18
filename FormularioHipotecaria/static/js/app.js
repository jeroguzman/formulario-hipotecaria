$('.arrow').hide();

//Home page options
$('.col-lg-2').hover(function () {

    const circulo = $(this).find('.asesoria-circulo');
    const currenth5 = $(this).find('h5');
    const arrow = $(this).find('.arrow');


    circulo.click(function () {

        $('.asesoria-circulo').not(circulo).removeClass("active");
        circulo.toggleClass("active");

        $('h5').not(currenth5).removeClass('currenth5');
        currenth5.toggleClass('currenth5');

        $('.arrow').not(arrow).hide();
        arrow.toggle();

        window.scrollTo(0, circulo.offset().top + 500);

    });
});

//Mask inputs
$('.money').mask('000,000,000', {
    reverse: true
});

$('.celularInput').mask('(000) 000-0000');

$('.rfcInput').mask('ZZZZ-00-00-00', {
    translation: {
        'Z': {
            pattern: /[A-Za-z]/,
            optional: false
        }
    }
});

//Forms
$('.preguntas').hover(function () {
    const btn = $(this).find('.btnNext');
    const panel = $(this).find('.panel');

    const btnPanelEs1 = $(this).find('.btnPanelEs1');
    const panelEs1 = $(this).find('.panelEs1');
    const btnPanelEs2 = $(this).find('.btnPanelEs2');
    const panelEs2 = $(this).find('.panelEs2');
    const btnPanelEs3 = $(this).find('.btnPanelEs3');
    const panelEs3 = $(this).find('.panelEs3');

    btn.each(function (index) {
        const panelIndex = panel.eq(index);
        $(this).click(function () {
            panelIndex.fadeIn(500);
            $(this).hide();
            window.scrollTo(0, panelIndex.offset().top);
        });
    });

    btnPanelEs1.click(function () {
        $('.btnPanelEs1').removeClass('ingreso-active');
        $(this).addClass('ingreso-active');

        panelEs1.fadeIn(500);
        window.scrollTo(0, panelEs1.offset().top);
    });

    btnPanelEs2.click(function () {
        $('.btnPanelEs2').removeClass('ingreso-active');
        $(this).addClass('ingreso-active');

        panelEs2.fadeIn(500);
        window.scrollTo(0, panelEs2.offset().top);
    });

    btnPanelEs3.click(function () {
        $('.btnPanelEs3').removeClass('ingreso-active');
        $(this).addClass('ingreso-active');

        if ($(this).hasClass('no')) {
            panelEs3.hide();
            $('.alt').fadeIn(500)
            window.scrollTo(0, $('.alt').offset().top - 500);
        } else {
            $('.alt').hide()
            panelEs3.fadeIn(500);
            window.scrollTo(0, panelEs3.offset().top);
        }
    });

});

//Validations
const regexName = /^([a-zA-Z]{1,20})$/;
$('input[name=valor]').on('keypress keydown keyup', function () {
    if ($(this).cleanVal() < 500000 || $(this).cleanVal() > 180000000) {
        $(this).parent().siblings('.emsg').removeClass('hidden');
    } else {
        $(this).parent().siblings('.emsg').addClass('hidden');
    }
});

$('input[name=telefono]').on('keypress keydown keyup', function () {
    if ($(this).cleanVal().length < 10) {
        $(this).siblings('.emsg').removeClass('hidden');
    } else {
        $(this).siblings('.emsg').addClass('hidden');
    }
});

$('input[name=rfc]').on('keypress keydown keyup', function () {
    if ($(this).cleanVal().length < 10) {
        $(this).siblings('.emsg').removeClass('hidden');
    } else {
        $(this).siblings('.emsg').addClass('hidden');
    }
});

$('input[name=nombre]').on('keypress keydown keyup', function () {
    if (!$(this).val().match(regexName)) {
        $(this).siblings('.emsg').removeClass('hidden');
    } else {
        $(this).siblings('.emsg').addClass('hidden');
    }
});

$('input[name=mensualidad]').on('keypress keydown keyup', function () {
    if ($(this).cleanVal() < 2000 || $(this).cleanVal() > 240000) {
        $(this).parent().siblings('.emsg').removeClass('hidden');
    } else {
        $(this).parent().siblings('.emsg').addClass('hidden');
    }
});

$('input[name=montoALaFecha]').on('keypress keydown keyup', function () {
    if ($(this).cleanVal() < 250000 || $(this).cleanVal() > 40000000) {
        $(this).parent().siblings('.emsg').removeClass('hidden');
    } else {
        $(this).parent().siblings('.emsg').addClass('hidden');
    }
});

$('input[name=anios]').on('keypress keydown keyup', function () {
    if ($(this).val() < 5 || $(this).val() > 30) {
        $(this).siblings('.emsg').removeClass('hidden');
    } else {
        $(this).siblings('.emsg').addClass('hidden');
    }
});

$('form').submit(function (e) {

    const valor = $(this).find('input[name=valor]');
    const telefono = $(this).find('input[name=telefono]');
    const rfc = $(this).find('input[name=rfc]');
    const nombre = $(this).find('input[name=nombre]');
    const banco = $(this).find('select[name=banco]');
    const mensualidad = $(this).find('input[name=mensualidad]');
    const montoALaFecha = $(this).find('input[name=montoALaFecha]');
    const anios = $(this).find('input[name=anios]');
    if (valor.cleanVal() < 500000 || valor.cleanVal() > 180000000) {
        e.preventDefault();
        valor.focus();
        window.scrollTo(0, valor.offset().top - 50);

    } else if (banco.length && (banco.val() === "Elija...")) {
        e.preventDefault();
        banco.focus();
        banco.parent().siblings('.emsg').removeClass('hidden');
        window.scrollTo(0, banco.offset().top - 50);

    } else if (mensualidad.length && (mensualidad.cleanVal() < 2000 || mensualidad.cleanVal() > 240000)) {
        e.preventDefault();
        mensualidad.focus();
        window.scrollTo(0, mensualidad.offset().top - 50)

    } else if (montoALaFecha.length && (montoALaFecha.cleanVal() < 250000 || montoALaFecha > 40000000)) {
        e.preventDefault();
        montoALaFecha.focus();
        window.scrollTo(0, montoALaFecha.offset().top - 50)

    } else if (anios.length && (anios.val() < 5 || anios.val() > 30)) {
        e.preventDefault();
        anios.focus();
        window.scrollTo(0, anios.offset().top - 50)

    } else if (telefono.cleanVal().length < 10) {
        e.preventDefault();
        telefono.focus();
        window.scrollTo(0, telefono.offset().top - 50);

    } else if (rfc.cleanVal().length < 10) {
        e.preventDefault();
        rfc.focus();
        window.scrollTo(0, rfc.offset().top - 50);

    } else if (!nombre.val().match(regexName)) {
        e.preventDefault();
        nombre.focus();
        window.scrollTo(0, nombre.offset().top - 50);
    }

});