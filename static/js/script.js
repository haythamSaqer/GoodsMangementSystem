function changeClassOpenNav() {
  document.getElementById("mySidebar").classList.add("w-300");
  document.querySelector("main").classList.add("m-300");
  document.querySelector(".openbtn").classList.add("show-btn");
  document.querySelector("nav .logo").classList.remove("m-65");
  document.querySelectorAll(".client-page .w-card").forEach(function (item) {
    item.classList.remove("w-close");
  });
  document
    .querySelectorAll(".box-charts .box-chart-5")
    .forEach(function (item) {
      item.classList.remove("w-280");
    });
}
function changeClassCloseNav() {
  document.getElementById("mySidebar").classList.remove("w-300");
  document.querySelector("main").classList.remove("m-300");
  document.querySelector(".openbtn").classList.remove("show-btn");
  document.querySelector("nav .logo").classList.add("m-65");
  document.querySelectorAll(".client-page .w-card").forEach(function (item) {
    item.classList.add("w-close");
  });
  document
    .querySelectorAll(".box-charts .box-chart-5")
    .forEach(function (item) {
      item.classList.add("w-280");
    });
}

function openNav() {
  changeClassOpenNav();
}

function closeNav() {
  changeClassCloseNav();
}

window.addEventListener("load", function () {
  var viewport_width = window.outerWidth;
  if (viewport_width < 576) {
    closeNav();
  }
  if (viewport_width < 768) {
    document.querySelectorAll(".client-page .w-card").forEach(function (item) {
      item.classList.remove("w-close");
    });
  }
});

window.addEventListener("resize", function () {
  var viewport_width = window.outerWidth;
  if (viewport_width < 576) {
    closeNav();
  } else {
    openNav();
  }
});

let aside = document.getElementById("mySidebar");
document.querySelector(".openbtn").addEventListener("click", function () {
  if (aside.classList.contains("w-300")) {
    document.querySelector("main").classList.add("oevrFlowH");
    document.querySelector("main .content-page").classList.add("w-500");
  }
});
document.querySelector(".closebtn").addEventListener("click", function () {
  if (!aside.classList.contains("w-300")) {
    document.querySelector("main").classList.remove("oevrFlowH");
    document.querySelector("main .content-page").classList.remove("w-500");
  }
});
document
  .querySelector(".new-request .btn-send")
  .addEventListener("click", function (e) {
    e.preventDefault();
    document
      .querySelector(".alert-success")
      .classList.remove("alert-success-send");
  });
