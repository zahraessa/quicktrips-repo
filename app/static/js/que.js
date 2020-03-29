var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab
toKeyword(document.getElementById("nextBtn").innerHTML, currentTab);

function toKeyword(n,m){
  var x = document.getElementsByClassName("tab");
  if (n == "Final Question!" && m == x.length) {
    x.onclick = addSubmit(x);
  }

}

function addSubmit(x) {
  x.setAttribute("name", "submit");
  x.setAttribute("value", "submit");
}

function showTab(n) {
  // This function will display the specified tab of the form ...
  var x = document.getElementsByClassName("tab");
  x[n].style.display = "block";
  // ... and fix the Previous/Next buttons:
  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
  if (n == (x.length - 1)) {
    document.getElementById("nextBtn").innerHTML = "Final Question!";
  } else {
    document.getElementById("nextBtn").innerHTML = "Next";
  }
  // ... and run a function that displays the correct step indicator:
  fixStepIndicator(n)
}

function nextPrev(n) {
  // This function will figure out which tab to display
  var x = document.getElementsByClassName("tab");
  // Exit the function if any field in the current tab is invalid:
  if (n == 1 && !validateForm()) return false;
  // Hide the current tab:
  x[currentTab].style.display = "none";
  // Increase or decrease the current tab by 1:
  currentTab = currentTab + n;
  // if you have reached the end of the form... :
  if (currentTab >= x.length) {
    //...the form gets submitted:
    document.getElementById("queForm").submit();
    return false;
  }
  // Otherwise, display the correct tab:
  showTab(currentTab);
}

function validateForm() {
  // This function deals with validation of the form fields
  var x, y, z, i, valid = true;
  x = document.getElementsByClassName("tab");
  y = x[currentTab].getElementsByTagName("input");
  z = x[currentTab].getElementsByTagName("select");

  // A loop that checks every input field in the current tab:
  for (i = 0; i < y.length; i++) {
    // If a field is empty...
    if (y[i].value === "") {
      // add an "invalid" class to the field:
      y[i].className += " invalid";
      // and set the current valid status to false:
      valid = false;
    }
  }

  // A loop that checks every select field in the current tab:
  for (i = 0; i < z.length; i++) {
    // If a field is empty...
    if (z[i].value === "") {
      // add an "invalid" class to the field:
      z[i].className += " invalid";
      // and set the current valid status to false:
      valid = false;
    }
  }

  // If min is greater than max, then add is-invalid class
  if (currentTab == 0) {
    if (parseInt(z[0].value)  > parseInt(z[1].value)){
      // add an "is-invalid" class to the field:
      z[0].className += " is-invalid";
      z[1].className += " is-invalid";
      valid = false;
    }
  }

  // If 0 person is selected, then add is-invalid class
  if (currentTab == 1) {
    if (z[0].value == "0"  && z[1].value == "0" && z[2].value == "0" && z[3].value == "0"){
      // add an "is-invalid" class to the field:
      z[0].className += " is-invalid";
      z[1].className += " is-invalid";
      z[2].className += " is-invalid";
      z[3].className += " is-invalid";
      z[4].className += " is-invalid";
      valid = false;
    }
  }

  if (currentTab == 2) {
    var startDate = y[0].value.split("/");
    var endDate = y[1].value.split("/");

    // If start date is earlier than end date, then add is-invalid class
    if((startDate[0] > endDate[0]) || ((startDate[0] === endDate[0]) && (startDate[1] > endDate[1])) || ((startDate[0] === endDate[0]) && (startDate[1] === endDate[1]) && (startDate[2] > endDate[2]))){
      // add an "is-invalid" class to the field:
      y[0].className += " is-invalid";
      y[1].className += " is-invalid";
      valid = false;
    }

  }


  // If the valid status is true, mark the step as finished and valid:
  if (valid) {
    document.getElementsByClassName("step")[currentTab].className += " finish";
  }
  return valid; // return the valid status
}

function checkValid(currentTab) {
  // If select is valid, then remove invalid class
  var x = document.getElementsByClassName("tab");
  var z = x[currentTab].getElementsByTagName("select");

  for (i = 0; i < z.length; i++) {
    if (z[i].value !== "") {
      // remove an "invalid" class to the field:
      var classVal = z[i].getAttribute("class");
      classVal = classVal.replace("invalid", "").replace("is-invalid", "")
      z[i].setAttribute("class", classVal);
    }
  }
}

function fixStepIndicator(n) {
  // This function removes the "active" class of all steps...
  var i, x = document.getElementsByClassName("step");
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active", "");
  }
  //... and adds the "active" class to the current step:
  x[n].className += " active";
}
