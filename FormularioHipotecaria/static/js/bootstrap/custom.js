//cuestionario

function desplegar() {
    mi = document.getElementById("contenido");

    if (document.getElementById("compra").innerHTML == "Ocultar") {
        document.getElementById("compra").innerHTML = "desplegar";
        mi.style.visibility = "visible";


    } else {
        document.getElementById("compra").innerHTML = "Ocultar";
        mi.style.visibility = "hidden";

    }

}