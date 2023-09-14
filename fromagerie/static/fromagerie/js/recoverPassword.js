$(document).ready(function() {
    // Select the recover password button by its class
    $('.btn-login').click(function() {
      // Get the value from the input
      var usernameOrEmail = $('#form2Example11').val();
  
      // Check if the field is empty
      if (usernameOrEmail === '') {
        // Display an alert indicating that the field is empty
        alert('Please enter your username or email.');
      } else {
        // Display an alert with the recovery message
        alert('If the username or email match our records, we will send you a message with the steps to follow to recover your password.');
      }
    });
  });
  