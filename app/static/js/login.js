function submitting() {
  // Exit the function if any field in the current tab is invalid:
  if (!validateForm()) return false;

  addSubmit();

}


function validateForm() {

  // This function deals with validation of the form fields
  var x = document.getElementsByTagName("input");
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
  if (notValid === 0) {
    return true;
  }
  return false;
}

function addSubmit(){
  var x = document.getElementById("form-login-button");
  x.setAttribute("name", "submit");
  x.setAttribute("value", "submit");
}