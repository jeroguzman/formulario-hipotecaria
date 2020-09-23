const regexName = /^([a-zA-Z ]{3,50})$/;

//Mask inputs
$('.money').mask('000,000,000', {
    reverse: true
});

// $('.celularInput').mask('(000) 000-0000');

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
        $(this).parent().parent().parent().parent().parent().hide();
    })
})

//Marca las opciones seleccionadas
$('.opcion').click(function () {
    $('.opcion').removeClass('opcion-active');
    $(this).addClass('opcion-active');
    $(this).siblings('.emsg').addClass('hidden');
});

//Boton siguiente
$('.btnNext').each(function () {
    const target = $('#' + $(this).attr('for'));
    const opcion = $(this).parent().siblings('.opcion');
    const valor = $(this).parent().parent().find('input[name=valor]')
    const nombre = $(this).parent().parent().find('input[name=nombre]')
    $(this).click(function () {
        const targetOption = $('#' + $(this).parent().siblings('.opcion-active').attr('for'));
        if (opcion.hasClass('opcion-active') ||
            (valor.length && (valor.cleanVal() > 500000 && valor.cleanVal() < 180000000)) ||
            (nombre.length && nombre.val().match(regexName))) {
            if (target.length) {
                target.fadeIn(100);
            } else {
                targetOption.fadeIn(100);
            }

            $(this).parent().parent().parent().parent().parent().parent().hide();
        } else {
            $(this).parent().siblings('.emsg').removeClass('hidden');
        }
    });

});

//Boton anterior
$('.btnAnt').each(function () {
    const target = $('#' + $(this).attr('for'));
    $(this).click(function () {
        target.fadeIn(100);
        $(this).parent().parent().parent().parent().parent().parent().hide();
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

$('.result').html('this is the result');