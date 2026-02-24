// 1. Seleccionamos el título
const titulo = document.querySelector("h1");

// 2. Cambiamos su texto
titulo.textContent = "Nuevo Título Dinámico";

// 3. Cambiamos su color de fondo
titulo.style.backgroundColor = "yellow";

console.log("Terminal de [Tu Nombre] iniciada con éxito");
console.warn("Acceso de desarrollador detectado");
// 1. Seleccionamos el botón
const miBoton = document.querySelector("#champiñon");

// 2. Le pedimos que escuche el "click"
miBoton.addEventListener("click", function () {
    const articulos = document.querySelectorAll("article");

    articulos.forEach((a) => {
        a.style.transform = "scale(1.03)"
    })
});








