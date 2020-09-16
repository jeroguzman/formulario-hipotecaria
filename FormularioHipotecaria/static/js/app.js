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

    });
});

//Mask inputs
$('.money').mask('000,000,000', {
    reverse: true
});

$('.celularInput').mask('(000) 000-0000');

$('.rfcInput').mask('ZZZZ-00-00-00-AAA', {
    translation: {
        'Z': {
            pattern: /[A-Za-z]/,
            optional: false
        }
    }
});

//Forms
$('.preguntas').hover(function () {
    const btnPanel1 = $(this).find('.btnPanel1');
    const btnPanel2 = $(this).find('.btnPanel2');
    const btnPanel3 = $(this).find('.btnPanel3');
    const btnPanel4 = $(this).find('.btnPanel4');
    const btnPanel5 = $(this).find('.btnPanel5');
    const btnPanel_1 = $(this).find('.btnPanel-1');
    const btnPanel_2 = $(this).find('.btnPanel-2');
    const btnPanel_3 = $(this).find('.btnPanel-3');
    const btnPanel_4 = $(this).find('.btnPanel-4');

    const panel1 = $(this).find('.panel1');
    const panel2 = $(this).find('.panel2');
    const panel3 = $(this).find('.panel3');
    const panel4 = $(this).find('.panel4');
    const panel5 = $(this).find('.panel5');
    const panel_1 = $(this).find('.panel-1');
    const panel_2 = $(this).find('.panel-2');
    const panel_3 = $(this).find('.panel-3');
    const panel_4 = $(this).find('.panel-4');

    const btnPanelEs1 = $(this).find('.btnPanelEs1');
    const panelEs1 = $(this).find('.panelEs1');
    const btnPanelEs2 = $(this).find('.btnPanelEs2');
    const panelEs2 = $(this).find('.panelEs2');
    const btnPanelEs3 = $(this).find('.btnPanelEs3');
    const panelEs3 = $(this).find('.panelEs3');

    btnPanel1.click(function () {
        panel1.fadeIn(500);
        $(this).fadeOut(100);
    });

    btnPanel2.click(function () {
        panel2.fadeIn(500);
        $(this).fadeOut(100);
        window.scrollTo(0, panel2.offset().top);

    });

    btnPanel3.click(function () {
        panel3.fadeIn(500);
        $(this).fadeOut(100);
        window.scrollTo(0, panel3.offset().top);
    });

    btnPanel4.click(function () {
        panel4.fadeIn(500);
        $(this).fadeOut(100);
        window.scrollTo(0, panel4.offset().top);
    });

    btnPanel5.click(function () {
        panel5.fadeIn(500);
        $(this).fadeOut(100);
        window.scrollTo(0, panel5.offset().top);
    });

    btnPanel_1.click(function () {
        panel_1.fadeIn(500);
        $(this).fadeOut(100);
        window.scrollTo(0, panel_1.offset().top);
    });

    btnPanel_2.click(function () {
        panel_2.fadeIn(500);
        $(this).fadeOut(100);
        window.scrollTo(0, panel_2.offset().top);
    });

    btnPanel_3.click(function () {
        panel_3.fadeIn(500);
        $(this).fadeOut(100);
        window.scrollTo(0, panel_3.offset().top);
    });

    btnPanel_4.click(function () {
        panel_4.fadeIn(500);
        $(this).fadeOut(100);
        window.scrollTo(0, panel_4.offset().top);
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
            panelEs3.fadeOut(100);
            $('.alt').fadeIn(500)
            window.scrollTo(0, $('.alt').offset().top);
        } else {
            $('.alt').fadeOut(100)
            panelEs3.fadeIn(500);
            window.scrollTo(0, panelEs3.offset().top);
        }


    });
});