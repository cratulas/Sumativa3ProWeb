$(document).ready(function () {
    $("form").submit(function (event) {
      event.preventDefault(); // Evita el envío del formulario por defecto
      
      // Obtener los valores de los campos
      var username = $("input[name='username']").val();
      var email = $("input[name='email']").val();
      var password = $("input[name='password']").val();
      var confirmPassword = $("input[name='confirm_password']").val();
      var termsCheckbox = $("input[type='checkbox']").is(":checked");
      
      // Validar campos vacíos
      if (username === "" || email === "" || password === "" || confirmPassword === "") {
        alert("Por favor, completa todos los campos.");
        return;
      }
      
      // Validar longitud del username
      if (username.length <= 6) {
        alert("El nombre de usuario debe tener al menos 7 caracteres.");
        return;
      }
      
      // Validar formato de email
      var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email)) {
        alert("Por favor, ingresa un correo electrónico válido.");
        return;
      }
      
      // Validar coincidencia de contraseñas
      if (password !== confirmPassword) {
        alert("Las contraseñas no coinciden.");
        return;
      }
      
      // Validar formato y complejidad de la contraseña
      var passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/;
      if (!passwordRegex.test(password)) {
        alert("La contraseña debe tener al menos 8 caracteres y contener al menos una letra mayúscula, una letra minúscula y un número.");
        return;
      }
      
      // Validar aceptación de términos
      if (!termsCheckbox) {
        alert("Debes aceptar los términos y condiciones.");
        return;
      }
      
      // Mostrar mensaje de éxito y redirigir
      alert("Registro exitoso. ¡Bienvenido a Fromagerie!");
      window.location.href = "index.html"; // Cambia "index.html" por la URL deseada
    });
  });