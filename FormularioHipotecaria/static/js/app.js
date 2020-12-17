//const regexName = /^([a-zA-Z ]{3,50})$/; //Regex para la validacion de nombres (solo permite letras y espacios)
const regexName = /^[\w'\-,][^0-9_!¡.?÷?¿\/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}\s[\w'\-,][^0-9_!¡.?÷?¿\/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$/; //Regex para la validacion de nombres (solo permite letras y espacios)
const regexEmail = /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/
const correo = $('input[name=correo]');
const telefono = $('input[name=telefono]');
const nombre = $('input[name=nombre]');
const dinero = $('.money');

//Mask inputs
dinero.mask('000,000,000', {
    reverse: true
});

telefono.mask('(000)000-0000');

$('.panel').first().show();

//Marca las opciones seleccionadas
$('.panel').each(function () {
    const currentOptions = $(this).find('.opcion');
    currentOptions.click(function () {
        currentOptions.removeClass('opcion-active');
        $(this).addClass('opcion-active');
        $(this).siblings('.emsg').addClass('hidden');
    });
});

//Opciones de la pagina de inicio que lleva los formularios
$('.opcionNext').each(function () {
    const target = $('#' + $(this).attr('for'));
    $(this).click(function () {
        target.fadeIn(100);
        target.addClass('path');
        target.find('input').prop('disabled', false); //Permite que nomas se llene el input del formulario especifico
        target.find('select').prop('disabled', false); //Permite que nomas se llene el input del formulario especifico
        $(this).parent().parent().parent().parent().parent().hide();

        //Toma el html de la opcion seleccionada para poder hacer submit en el form
        $('.opcion-input').each(function () {
            const choosenOption = $(this).siblings('.opcion-active').children().html();
            $(this).val(choosenOption);
        });
        
    })
})

//Boton final para enviar el formulario
$('.perfilamiento').each(function () {
    const correo = $(this).parent().parent().find('input[name=correo]');
    const telefono = $(this).parent().parent().find('input[name=telefono]');
    $(this).click(function (event) {
        if(!correo.val().match(regexEmail) && telefono.cleanVal().length !== 10 ){
            $(this).siblings('#emsg-correo').removeClass('hidden');
            $(this).siblings('#emsg-telefono').removeClass('hidden');
            event.preventDefault();
        }else if(!correo.val().match(regexEmail)){
            $(this).siblings('#emsg-correo').removeClass('hidden');
            event.preventDefault();
        }else if(telefono.cleanVal().length !== 10){
            $(this).siblings('#emsg-telefono').removeClass('hidden');
            event.preventDefault();
        }else{
            dinero.unmask();
        }
    })
});

$('.goToMenu').each(function(){
    const target = $('#' + $(this).attr('for'));
    const thisPanel = $(this).parent().parent().parent().parent().parent();   

    $(this).click(function(){
        target.fadeIn(100);
        thisPanel.hide();
        thisPanel.removeClass('path');
        
        const pathClass = $('.path').last().attr('id'); 
        const panelToRemove = $('#' + pathClass);
        panelToRemove.removeClass('path');
    });
});

//Boton siguiente
$('.btnNext').each(function () {
    const target = $('#' + $(this).attr('for'));
    const valor = $(this).parent().parent().find('.money');
    const nombre = $(this).parent().parent().find('input[name=nombre]');
    const scroll = $(this).parent().parent().find('select');
    const radio = $(this).parent().parent().find('input[name=radio]');
    
    $(this).click(function () {
        //Revisa si las validaciones son correctas para poder continuar
        if ((valor.length && (valor.cleanVal() > 0)) ||
            (nombre.length && nombre.val().match(regexName)) ||
            (scroll.attr('class') !== undefined) ||
            (radio.attr('class') !== undefined)) {

            target.fadeIn(100);
            target.addClass('path'); //Agrega la clase path a el panel para saber el camino que va tomanto el formulario
            target.find('input').prop('disabled', false); //Permite que nomas se llene el input del formulario especifico
            target.find('select').prop('disabled', false); //Permite que nomas se llene el input del formulario especifico

            $(this).parent().parent().parent().parent().parent().parent().hide();
        } else { //Si las validaciones no son correctas muestra un mensaje de error
            $(this).parent().siblings('.emsg').removeClass('hidden');
        }
    });

});

//Boton anterior
$('.btnAnt').each(function () {
    $(this).click(function () {
        const path = $('.path').eq(-2).attr('id');
        const target = $('#' + path);
        target.fadeIn(100); //muestra el penultimo panel con la clase 'path'
        const thisPanel = $(this).parent().parent().parent().parent().parent().parent();
        thisPanel.hide();
        thisPanel.find('input').prop('disabled', true);
        thisPanel.find('select').prop('disabled', true);
        thisPanel.removeClass('path');
    });
});

$('.antPer').each(function () {
    $(this).click(function () {
        const path = $('.path').eq(-2).attr('id');
        const target = $('#' + path);
        target.fadeIn(100); //muestra el penultimo panel con la clase 'path'
        const thisPanel = $(this).parent().parent().parent().parent().parent();
        thisPanel.hide();
        thisPanel.find('input').prop('disabled', true);
        thisPanel.find('select').prop('disabled', true);
        thisPanel.removeClass('path');
    });
});

//Validaciones
dinero.on('keypress keydown keyup', function () {
    if ($(this).cleanVal() < 0) {
        $(this).parent().siblings('.emsg').removeClass('hidden');
    } else {
        $(this).parent().siblings('.emsg').addClass('hidden');
    }
});

nombre.on('keypress keydown keyup', function () {
    if (!$(this).val().match(regexName)) {
        $(this).siblings('.emsg').removeClass('hidden');
    } else {
        $(this).siblings('.emsg').addClass('hidden');
    }
});

telefono.on('keypress keydown keyup', function () {
    if ($(this).cleanVal().length < 10) {
        $(this).siblings('.emsg:first-of-type').removeClass('hidden');
    } else {
        $(this).siblings('.emsg:first-of-type').addClass('hidden');
    }
});

correo.on('keypress keydown keyup', function () {
    if (!$(this).val().match(regexEmail)) {
        $(this).siblings('.emsg:last-of-type').removeClass('hidden');
    } else {
        $(this).siblings('.emsg:last-of-type').addClass('hidden');
    }
});