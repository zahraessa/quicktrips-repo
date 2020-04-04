function submitting() {
  // Exit the function if any field in the current tab is invalid:
  // if (!validateForm()) return false;
  if (!validated()) return false;
  addSubmit();

}


// function validateForm() {
//
//   // This function deals with validation of the form fields
//   var x = document.getElementsByTagName("input");
//   var valid = true;
//
//   // A loop that checks every input field in the current tab:
//   for (i = 0; i < x.length; i++) {
//     // If a field is empty...
//     if (x[i].value === "") {
//       // add an "invalid" class to the field:
//       x[i].className += " invalid";
//       valid = false;
//     }
//   }
//   return valid;
// }


function validated() {
  var a = document.getElementsByTagName("input")[1].value;
  var b = document.getElementsByTagName("input")[2].value;
  if (a === "" || b === "") {
    window.alert("Username or password is empty... Please check and click Login again.");
    return false;
  }
  return true;
}

function addSubmit(){
  var x = document.getElementById("form-login-button");
  x.setAttribute("name", "submit");
  x.setAttribute("value", "submit");
}