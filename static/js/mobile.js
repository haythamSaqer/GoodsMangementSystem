var input = document.querySelector("#mobile");
window.intlTelInput(input, {
  separateDialCode: true,
  excludeCountries: ["in", "il"],
  preferredCountries: ["sa", "jp", "pk", "no"],
});
