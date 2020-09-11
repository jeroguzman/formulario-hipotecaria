$('.arrow').hide();

$('.col-lg-2').hover(function () {

    let circulo = $(this).find('.asesoria-circulo');
    let currenth5 = $(this).find('h5');
    let arrow = $(this).find('.arrow');

    circulo.click(function () {
        $('.asesoria-circulo').not(circulo).removeClass("active");
        circulo.toggleClass("active");

        $('h5').not(currenth5).removeClass('currenth5');
        currenth5.toggleClass('currenth5');

        $('.arrow').not(arrow).hide();
        arrow.toggle();
    });
});

$('.btnNext').click(function () {
    $('#panel2').show();
})