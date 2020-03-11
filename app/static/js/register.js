function submit() {
  // Exit the function if any field in the current tab is invalid:
  if (!validateForm()) return false;
  document.getElementById("queForm").submit();
}


function validateForm() {

  // This function deals with validation of the form fields
  var x = document.getElementsByTagName("input");
  var y = document.getElementsByTagName("select");

  // A loop that checks every input field in the current tab:
  for (i = 0; i < x.length; i++) {
    // If a field is empty...
    if (x[i].value === "") {
      // add an "invalid" class to the field:
      x[i].className += " invalid";
    }
  }

   // A loop that checks every select field in the current tab:
  for (i = 0; i < y.length; i++) {
    // If a field is empty...
    if (y[i].value === "") {
      // add an "invalid" class to the field:
      y[i].className += " invalid";
    }
  }
}