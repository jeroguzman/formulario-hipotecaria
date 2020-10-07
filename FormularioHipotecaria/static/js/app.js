const regexName = /^([a-zA-Z ]{3,50})$/; //Regex para la validacion de nombres (solo permite letras y espacios)
const regexEmail = /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/


console.log($('.path').last())


//Mask inputs
$('.money').mask('000,000,000', {
    reverse: true
});

$('.celularInput').mask('(000) 000-0000');

// $('.rfcInput').mask('ZZZZ-00-00-00', {
//     translation: {
//         'Z': {
//             pattern: /[A-Za-z]/,
//             optional: false
//         }
//     }
// });


//Opciones de la pagina de inicio que lleva los formularios
$('.opcionNext').each(function () {
    const target = $('#' + $(this).attr('for'));
    $(this).click(function () {
        target.fadeIn(100);
        target.addClass('path')
        $(this).parent().parent().parent().parent().parent().hide();
    })
})

//Marca las opciones seleccionadas
// $('.opcion').click(function () {
//     $('.opcion').removeClass('opcion-active');
//     $(this).addClass('opcion-active');
//     $(this).siblings('.emsg').addClass('hidden');
// });

$('.panel').each(function () {
    const currentOptions = $(this).find('.opcion');
    currentOptions.click(function () {
        currentOptions.removeClass('opcion-active');
        $(this).addClass('opcion-active');
        $(this).siblings('.emsg').addClass('hidden');
    });
})

//Boton siguiente
$('.btnNext').each(function () {
    const target = $('#' + $(this).attr('for'));
    const opcion = $(this).parent().siblings('.opcion');
    const valor = $(this).parent().parent().find('input[name=valor]')
    const nombre = $(this).parent().parent().find('input[name=nombre]')
    const correo = $(this).parent().parent().find('input[name=correo]')
    const telefono = $(this).parent().parent().find('input[name=telefono]')
    $(this).click(function () {
        const targetOption = $('#' + $(this).parent().siblings('.opcion-active').attr('for'));


        //Revisa si las validaciones son correctas para poder continuar
        if (opcion.hasClass('opcion-active') ||
            (valor.length && (valor.cleanVal() > 500000 && valor.cleanVal() < 180000000)) ||
            (nombre.length && nombre.val().match(regexName)) ||
            ((correo.length && correo.val().match(regexEmail)) && (telefono.length && telefono.cleanVal().length === 10))) {

            //Toma el html de la opcion seleccionada para poder hacer submit en el form
            $('.opcion-input').each(function () {
                const choosenOption = $(this).siblings('.opcion-active').children().html();
                $(this).val(choosenOption);
            });

            //Revisa si va a ser direccionado por el boton siguiente o por la opcion que se eligio
            if ($(this).attr('for') !== 'none') {
                target.fadeIn(100);
                target.addClass('path');
                target.find('input').prop('disabled', false); //Permite que nomas se llene el input del formulario especifico
            } else {
                targetOption.fadeIn(100);
                targetOption.addClass('path');
                targetOption.find('input').prop('disabled', false);
            }

            $(this).parent().parent().parent().parent().parent().parent().hide();
        } else { //Si las validaciones no son correctas muestra un mensaje de error
            $(this).parent().siblings('.emsg').removeClass('hidden');
        }
    });

});

//Boton anterior
$('.btnAnt').each(function () {
    //const target = $('#' + $(this).attr('for'));
    $(this).click(function () {
        //const path = $('.path').last().prev().attr('id');
        const path = $('.path').eq(-2).attr('id');
        const target = $('#' + path);
        target.fadeIn(100);
        const thisPanel = $(this).parent().parent().parent().parent().parent().parent();
        thisPanel.hide();
        thisPanel.find('input').prop('disabled', true);
        thisPanel.removeClass('path');
    });
});

//Validaciones
$('input[name=valor]').on('keypress keydown keyup', function () {
    if ($(this).cleanVal() < 500000 || $(this).cleanVal() > 180000000) {
        $(this).parent().siblings('.emsg').removeClass('hidden');
    } else {
        $(this).parent().siblings('.emsg').addClass('hidden');
    }
});


$('input[name=nombre]').on('keypress keydown keyup', function () {
    if (!$(this).val().match(regexName)) {
        $(this).siblings('.emsg').removeClass('hidden');
    } else {
        $(this).siblings('.emsg').addClass('hidden');
    }
});

$('input[name=telefono]').on('keypress keydown keyup', function () {
    if ($(this).cleanVal().length < 10) {
        $(this).siblings('.emsg:first-of-type').removeClass('hidden');
    } else {
        $(this).siblings('.emsg:first-of-type').addClass('hidden');
    }
});

$('input[name=correo]').on('keypress keydown keyup', function () {
    if (!$(this).val().match(regexEmail)) {
        $(this).siblings('.emsg:last-of-type').removeClass('hidden');
    } else {
        $(this).siblings('.emsg:last-of-type').addClass('hidden');
    }
});