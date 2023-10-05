document.addEventListener('DOMContentLoaded', function() {
  let messages = document.querySelectorAll('.messages div');
  messages.forEach(function(message) {
      if (message.classList.contains('success')) {
          alert('¡Exito! ' + message.innerText);
      } else if (message.classList.contains('error')) {
          alert('Error: ' + message.innerText);
      }
  });
});
