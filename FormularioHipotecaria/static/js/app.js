$('.arrow').hide();

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


// $('.btnNext').click(function () {
//     $(this).fadeOut(100);
// })

// $('.formaIngreso').click(function () {
//     $('.formaIngreso').removeClass('ingreso-active');
//     $(this).addClass('ingreso-active');

//     $('#correo').fadeIn(500);
// })

$('.preguntas').hover(function () {
    const btnIngreso = $(this).find('.ingresoNext');
    const btnTelefono = $(this).find('.telefonoNext');
    const btnRfc = $(this).find('.rfcNext');
    const btnNombre = $(this).find('.nombreNext');

    const percibeIngreso = $(this).find('.percibeIngreso')
    const telefono = $(this).find('.telefono')
    const rfc = $(this).find('.rfc')
    const nombre = $(this).find('.nombre')
    const formaIngreso = $(this).find('.formaIngreso');
    const correo = $(this).find('#correo');

    btnIngreso.click(function () {
        percibeIngreso.fadeIn(500);
        $(this).fadeOut(100);
    });

    btnTelefono.click(function () {
        telefono.fadeIn(500);
        $(this).fadeOut(100);
    });
    btnRfc.click(function () {
        rfc.fadeIn(500);
        $(this).fadeOut(100);
    });
    btnNombre.click(function () {
        nombre.fadeIn(500);
        $(this).fadeOut(100);
    });

    formaIngreso.click(function () {
        $('.formaIngreso').removeClass('ingreso-active');
        $(this).addClass('ingreso-active');

        correo.fadeIn(500);
    });


})