(function() {
  'use strict';
  window.addEventListener('load', function() {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    });
  }, false);
})();

// function submitting() {
//   // Exit the function if any field in the current tab is invalid:
//   if (!validateForm()) return false;
//   // Add submit keyword in value and name so that flask get the form
//   addSubmit();
// }
//
// function validated() {
//   var a = document.getElementsByTagName("input")[1].value;
//   var b = document.getElementsByTagName("input")[2].value;
//   if (a === "" || b === "") {
//     window.alert("Username or password is empty... Please check and click Login again.");
//     return false;
//   }
//   return true;
// }
//
// function validateForm() {
//
//   // This function deals with validation of the form fields
//   var x = document.getElementsByTagName("input");
//   var y = document.getElementsByTagName("select");
//   var valid = true;
//
//   // A loop that checks every input field in the current tab:
//   for (i = 0; i < x.length; i++) {
//     // If a field is empty...
//     if (x[i].value === "") {
//       window.alert("A");
//       valid = false;
//     }
//   }
//
//    // A loop that checks every select field in the current tab:
//   for (i = 0; i < y.length; i++) {
//     // If a field is empty...
//     if (y[i].value === "") {
//       // add an "invalid" class to the field:
//       y[i].className += " invalid";
//       valid = false;
//     }
//   }
//
//   return valid;
// }
//
// function addSubmit(){
//   var x = document.getElementById("form-register-button");
//
//   x.setAttribute("name", "submit");
//   x.setAttribute("value", "submit");
// }