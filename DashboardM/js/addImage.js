// $("#upload-first").change(function (event) {
//   $(this).next("label").clone();
//   var file = $("#upload-first")[0].files[0].name;
//   $(this).next("label").text(file);
//   $(".logo.container-edit-img").css("display", "flex");
//   var image = $("#output_logo");
//   image.attr("src", URL.createObjectURL(event.target.files[0]));
// });

// $(".reset-logo").click(function () {
//   $("#upload-logo-media").val("");
//   $("#upload-logo-media").next("label").text("");
//   $("#upload-logo-media").next("label").append(`
//                 <i class="fa-solid fa-images"></i>
//                 <span class="mx-2">تحميل الصورة </span>
//                 <i class="fa-solid fa-cloud-arrow-up"></i>`);
//   $(".logo.container-edit-img").css("display", "none");
// });
// document
//   .querySelector(".upload-img")
//   .addEventListener("change", function (event) {
//     this.nextElementSibling.cloneNode();
//     var file = this.files[0].name;
//     this.nextElementSibling.textContent = file;
//     document.querySelector(".logo.container-edit-img").style.display = "flex";
//     var image = document.querySelector("#output_logo");
//     image.setAttribute("src", URL.createObjectURL(event.target.files[0]));
//   });

var container = document.getElementById("container-files");
var arr = ["firstComponent", "secondComponent"];
var components = arr.map(function (element, index) {
  return `
  <div class="container-add-img position-relative" id="${element}">
    <div class="p-3 d-flex justify-content-center align-items-center text-capitalize box-text">
      <i class="fa-solid fa-circle-check fa-circle-check-none me-2"></i>
      <h5 class="fw-bold mb-0">Photo No. ${index + 1}</h5>
    </div>
    <div class="p-3 p-md-4">
      <div class="img-change">
        <input class="d-none upload-img" type="file" id="upload-${element}" >
        <label for="upload-${element}" class="upload-image fw-bold px-4 py-2 gray-text font-14">
          <i class="fa-solid fa-images"></i>
          <span class="mx-2"> Click Here</span>
          <i class="fa-solid fa-cloud-arrow-up"></i>
        </label>
      </div>
      <div class="container-edit-img">
        <i class="fa-solid fa-circle-xmark position-absolute top-0 end-0 p-2 reset-logo reset-logo-none" onclick="reset('${element}')"></i>
        <div class="inner default">
          <img src="../images/default.png" alt="not found">
        </div>
      </div>
    </div>
  </div>`;
});

container.innerHTML = components.join("");

var fileInputs = document.querySelectorAll("input[type=file]");
for (var i = 0; i < fileInputs.length; i++) {
  fileInputs[i].addEventListener("change", function (event) {
    var file = this.files[0].name;
    var label = this.nextElementSibling;
    label.textContent = file;
    var container = this.closest(".container-add-img");
    container.querySelector(".reset-logo").classList.remove("reset-logo-none");
    container
      .querySelector(".fa-circle-check")
      .classList.remove("fa-circle-check-none");
    var image = container.querySelector("img");
    image.setAttribute("src", URL.createObjectURL(event.target.files[0]));
  });
}

function reset(id) {
  document.getElementById(`upload-${id}`).value = "";
  document.getElementById(`upload-${id}`).nextElementSibling.innerHTML = "";
  document.getElementById(`upload-${id}`).nextElementSibling.innerHTML = `
                <i class="fa-solid fa-images"></i>
                <span class="mx-2"> Click Here </span>
                <i class="fa-solid fa-cloud-arrow-up"></i>`;
  document
    .querySelector(`#${id} img`)
    .setAttribute("src", "../images/default.png");
  document
    .querySelector(`#${id} .fa-circle-check`)
    .classList.add("fa-circle-check-none");
}
