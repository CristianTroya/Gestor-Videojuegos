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