document.querySelectorAll(".fa-circle-info").forEach((item) => {
  item.addEventListener("click", function name(params) {
    var items = document.querySelectorAll(".modal-body");
    items.forEach(function (el) {
      if (el.classList.contains(item.id)) {
        el.classList.remove('none-body');
      }else{
        el.classList.add('none-body');
      }
    });
  });
});