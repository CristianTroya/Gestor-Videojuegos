// 1. Seleccionamos el título
const titulo = document.querySelector("h1");

// 2. Cambiamos su texto
titulo.textContent = "Nuevo Título Dinámico";

// 3. Cambiamos su color de fondo
titulo.style.backgroundColor = "#8878bf";

console.log("Terminal de Carlos, Cristian y Elio iniciada con éxito");
console.warn("Acceso de desarrollador detectado");
// 1. Seleccionamos el botón
const miBoton = document.querySelector("#champiñon");

// 2. Le pedimos que escuche el "click"
miBoton.addEventListener("click", function () {
    const articulos = document.querySelectorAll("article");

    articulos.forEach((a) => {
        a.style.transform = a.style.transform ? null : "scale(1.03)";
    })
});

const btnModo = document.getElementById("btn-modo");
const sol = document.getElementById("sol");
const luna = document.getElementById("luna");

btnModo.addEventListener("click", function () {
    document.body.classList.toggle("darkmode");

    //  claro
    if (sol.hidden === true) {
        sol.hidden = false;
        luna.hidden = true;
    } else {
        sol.hidden = true;
        luna.hidden = false;
    }
})
