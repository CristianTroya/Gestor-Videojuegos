const borrarBotones = document.querySelectorAll('.borrar');
const dialogBorrar = document.getElementById('dialog-borrar');

const borrarSi = document.getElementById('borrar-si');
const borrarNo = document.getElementById('borrar-no');

let ultimoBoton = null;
borrarBotones.forEach(function(boton) {
  boton.addEventListener('click', function() {
        dialogBorrar.showModal();
        // guardamos el último botón de cerrar presionado
        ultimoBoton = boton;
    });
});

// borramos el article del último botón presionado
borrarSi.addEventListener('click', function () {
  // efecto
  ultimoBoton.parentElement.style.transform = "scale(0.0001)";
  
  // esperamos 300ms antes de borrar
  // así le damos tiempo a la transición
  setTimeout(function() {
    ultimoBoton.parentElement.remove();
  }, 300);
  
  dialogBorrar.close();
});

borrarNo.addEventListener('click', function () {
  dialogBorrar.close();
});
