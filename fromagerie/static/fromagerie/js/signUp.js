$(document).ready(function () {
  $("form").submit(function (event) {
      event.preventDefault(); 

      // Obtener los valores de los campos
      var username = $("input[name='username']").val();
      var email = $("input[name='email']").val();
      var password1 = $("input[name='password1']").val();
      var password2 = $("input[name='password2']").val();

      // Validar longitud del username
      if (username.length < 6) {
          alert("El nombre de usuario debe tener al menos 6 caracteres.");
          return;
      }

      // Validar formato de email
      var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email)) {
          alert("Por favor, ingresa un correo electrónico válido.");
          return;
      }

      // Validar coincidencia de contraseñas
      if (password1 !== password2) {
          alert("Las contraseñas no coinciden.");
          return;
      }

      // Validar formato y complejidad de la contraseña
      var passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/;
      if (!passwordRegex.test(password1)) {
          alert("La contraseña debe tener al menos 8 caracteres y contener al menos una letra mayúscula, una letra minúscula y un número.");
          return;
      }

      // Mostrar mensaje de éxito y redirigir
      alert("Registro exitoso. ¡Bienvenido a Fromagerie!");
      $("form").unbind('submit').submit();
  });
});
