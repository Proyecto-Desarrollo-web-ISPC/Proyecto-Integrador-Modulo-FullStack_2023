// Define la función para abrir el pop-up
function abrirPopup() {
    var popup = document.getElementById("landingPagePopup");
    popup.style.display = "block";
}

// Llama a la función abrirPopup() cuando la página se cargue
window.addEventListener("load", function() {
    abrirPopup();
});

// Función para cerrar el pop-up
function cerrarPopup() {
    var popup = document.getElementById("landingPagePopup");
    popup.style.display = "none";
}
