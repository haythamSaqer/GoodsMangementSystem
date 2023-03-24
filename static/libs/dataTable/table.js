jQuery(document).ready(function () {
  $("table").DataTable({
    responsive: true,
    language: {
      search: "",
      searchPlaceholder: "Search ..",
      paginate: {
        first: "Premier",
        last: "Précédent",
        next: ">>",
        previous: "<<",
      },
    },
  });
});
