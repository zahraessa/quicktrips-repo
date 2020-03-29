function submitting() {
  // Exit the function if any field in the current tab is invalid:
  if (!validateForm()) return false;
  // Add submit keyword in value and name so that flask get the form
  addSubmit();
}


function validateForm() {

  // This function deals with validation of the form fields
  var x = document.getElementsByTagName("input");
  var y = document.getElementsByTagName("select");
  var notValid = 0;

  // A loop that checks every input field in the current tab:
  for (i = 0; i < x.length; i++) {
    // If a field is empty...
    if (x[i].value === "") {
      // add an "invalid" class to the field:
      x[i].className += " invalid";
      notValid = notValid + 1;
    }
  }

   // A loop that checks every select field in the current tab:
  for (i = 0; i < y.length; i++) {
    // If a field is empty...
    if (y[i].value === "") {
      // add an "invalid" class to the field:
      y[i].className += " invalid";
      notValid = notValid + 1;
    }
  }
  if (notValid === 0) {
    return true;
  }
  return false;
}

function addSubmit(){
  var x = document.getElementById("form-register-button");

  x.setAttribute("name", "submit");
  x.setAttribute("value", "submit");
}