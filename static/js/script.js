document.addEventListener("DOMContentLoaded", function() {
    const alerta = document.querySelector(".alerta");
    const relojPuntuacion = document.getElementById("reloj-puntuacion");
    if (alerta) {
        relojPuntuacion.style.marginTop = '25px';
    }
    setTimeout(function() {
        if (alerta) {
            alerta.style.display = 'none';
            relojPuntuacion.style.marginTop = '0';
        }
    }, 2000);

    var tiempoRestante = 30;
    var temporizador = setInterval(function() {
        tiempoRestante--;

        document.getElementById("tiempo-restante").innerHTML = tiempoRestante;

        if (tiempoRestante <= 0) {
            clearInterval(temporizador);
            window.location.href = '/timeout';
        }
    }, 1000);
});

function seleccionar(contenedor) {
    var inputRadio = contenedor.querySelector('input[type="radio"]');
    inputRadio.checked = true;
     
    var formulario = contenedor.closest('form');
    formulario.submit();
}