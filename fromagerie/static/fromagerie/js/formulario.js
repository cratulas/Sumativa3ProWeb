$(document).ready(function() {
    $('#limpiarFormulario').click(function() {
        $('form')[0].reset(); // Limpia todos los campos del formulario
    });

    $("form").submit(function(event) {
        event.preventDefault(); // Evita que el formulario se envíe automáticamente
        
        var nombre = $("#nombre").val();
        var email = $("#email").val();
        var asunto = $("#assunto").val(); 
        var mensaje = $("#mensaje").val();
        
        // Validación de campos obligatorios
        if (nombre === "" || email === "" || asunto === "" || mensaje === "") {
            alert("Todos los campos obligatorios deben ser completados.");
        } else if (!isValidEmail(email)) {
            alert("Por favor, ingresa un email válido.");
        } else {
            alert("¡Formulario enviado con éxito!");
            $("form")[0].reset(); // Limpia el formulario
        }
    });
});

function isValidEmail(email) {
    var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    return emailPattern.test(email);
}
