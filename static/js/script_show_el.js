document.querySelector(".btn-select").addEventListener("click", function () {
  this.parentNode.classList.add("btn-select-hide");
  this.parentNode.nextElementSibling.classList.remove("choose-select-none");
});
document.querySelector(".accept").addEventListener("click", function () {
  this.parentNode.classList.add("btn-select-hide");
  document.querySelector('.done').classList.remove("d-none-done");
});
document.querySelector(".notes").addEventListener("click", function () {
  this.parentNode.classList.add("btn-select-hide");
  document.querySelector('.box-notes').classList.remove("d-none-notes");
});
