$(document).ready(function () {
    $("button.btn-login").click(function () {
      var username = $("#form2Example11").val();
      var password = $("#form2Example22").val();
  
      if (!isValidEmail(username)) {
        alert("Por favor, ingrese un correo electrónico válido.");
        return;
      }
  
      if (password === "") {
        alert("Por favor, ingrese una contraseña.");
        return;
      }
  
      alert("¡Inicio de sesión exitoso!");
      window.location.href = "index.html";
    });
  
    function isValidEmail(email) {
      var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailRegex.test(email);
    }
  });
  