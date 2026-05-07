const btnModo = document.getElementById("btn-modo");
const sol = document.getElementById("sol");
const luna = document.getElementById("luna");

function toggle(esNoche) {
    console.log(esNoche + "toggle")
    document.body.classList.toggle("darkmode");
    
    //  claro
    if (sol.hidden === true) {
        sol.hidden = false;
        luna.hidden = true;
    } else {
        sol.hidden = true;
        luna.hidden = false;
    }

    const nuevoValor = esNoche == 'true' ? 'false' : 'true';
    console.log(nuevoValor)
    localStorage.setItem("darkmode", nuevoValor)
}

if (localStorage.getItem("darkmode") == 'true') {
    toggle('false');
}

btnModo.addEventListener("click", function() {
    toggle(localStorage.getItem("darkmode"));
    console.log(localStorage.getItem("darkmode"))
})