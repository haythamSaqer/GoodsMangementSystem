var match = document.getElementById("match");
var myInput = document.getElementById("pass");
var confirmInput = document.getElementById("c-pass");

var confirmInput = document.getElementById("c-pass");
confirmInput.onfocus = function () {
  document.getElementById("confirm-message").style.display = "block";
};
confirmInput.onblur = function () {
  document.getElementById("confirm-message").style.display = "none";
};

confirmInput.onkeyup = function () {
  // match password
  if (myInput.value === confirmInput.value) {
    match.classList.remove("invalid");
    match.classList.add("valid");
    match.innerHTML = "Passwords Match";
  } else {
    match.classList.remove("valid");
    match.classList.add("invalid");
  }
};


