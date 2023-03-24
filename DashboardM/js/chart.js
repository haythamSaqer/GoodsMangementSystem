var KPI = [
  {
    value: 69,
    color: "#70AB46",
    highlight: "#70AB46AD",
    label: "today",
  },
  {
    value: 15,
    color: "#D5702C",
    highlight: "#D5702CAD",
    label: "a day late",
  },
  {
    value: 16,
    color: "#BF0000",
    highlight: "#bf0000ad",
    label: "more than a day late",
  },
];
var DHL = [
  {
    value: 64,
    color: "#70AB46",
    highlight: "#70AB46AD",
    label: "today",
  },
  {
    value: 25,
    color: "#D5702C",
    highlight: "#D5702CAD",
    label: "a day late",
  },
  {
    value: 11,
    color: "#BF0000",
    highlight: "#bf0000ad",
    label: "more than a day late",
  },
];
var FEDEX = [
  {
    value: 57,
    color: "#70AB46",
    highlight: "#70AB46AD",
    label: "today",
  },
  {
    value: 30,
    color: "#D5702C",
    highlight: "#D5702CAD",
    label: "a day late",
  },
  {
    value: 13,
    color: "#BF0000",
    highlight: "#bf0000ad",
    label: "more than a day late",
  },
];
var ARAMEX = [
  {
    value: 75,
    color: "#70AB46",
    highlight: "#70AB46AD",
    label: "today",
  },
  {
    value: 15,
    color: "#D5702C",
    highlight: "#D5702CAD",
    label: "a day late",
  },
  {
    value: 10,
    color: "#BF0000",
    highlight: "#bf0000ad",
    label: "more than a day late",
  },
];
var UPS = [
  {
    value: 91,
    color: "#70AB46",
    highlight: "#70AB46AD",
    label: "today",
  },
  {
    value: 9,
    color: "#D5702C",
    highlight: "#D5702CAD",
    label: "a day late",
  },
  {
    value: 0,
    color: "#BF0000",
    highlight: "#bf0000ad",
    label: "more than a day late",
  },
];
var SMSACHART = [
  {
    value: 83,
    color: "#70AB46",
    highlight: "#70AB46AD",
    label: "today",
  },
  {
    value: 9,
    color: "#D5702C",
    highlight: "#D5702CAD",
    label: "a day late",
  },
  {
    value: 8,
    color: "#BF0000",
    highlight: "#bf0000ad",
    label: "more than a day late",
  },
];
var charts = [
  {
    id: "pieChart",
    data: KPI
  },
  {
    id: "dhl",
    data: DHL
  },
  {
    id: "FEDEX",
    data: FEDEX
  },
  {
    id: "ARAMEX",
    data: ARAMEX
  },
  {
    id: "UPS",
    data: UPS
  },
  {
    id: "SMSACHART",
    data: SMSACHART
  }
];

window.addEventListener('load', function() {
  for (var i = 0; i < charts.length; i++) {
    var canvas = document.getElementById(charts[i].id).getContext("2d");
    window.myPie = new Chart(canvas).Pie(charts[i].data, {
      animation: true,
      responsive: true,
    });
  }
});

// window.addEventListener('load', function() {
//   var kpi = document.getElementById("pieChart").getContext("2d");
//   window.myPie = new Chart(kpi).Pie(KPI, {
//     animation: true,
//     responsive: true,
//   });
//   var dhl = document.getElementById("dhl").getContext("2d");
//   window.myPie = new Chart(dhl).Pie(DHL, {
//     animation: true,
//     responsive: true,
//   });
//   var fedex = document.getElementById("FEDEX").getContext("2d");
//   window.myPie = new Chart(fedex).Pie(FEDEX, {
//     animation: true,
//     responsive: true,
//   });
//   var aramex = document.getElementById("ARAMEX").getContext("2d");
//   window.myPie = new Chart(aramex).Pie(ARAMEX, {
//     animation: true,
//     responsive: true,
//   });
//   var ups = document.getElementById("UPS").getContext("2d");
//   window.myPie = new Chart(ups).Pie(UPS, {
//     animation: true,
//     responsive: true,
//   });
//   var smsa_chart = document.getElementById("SMSACHART").getContext("2d");
//   window.myPie = new Chart(smsa_chart).Pie(SMSACHART, {
//     animation: true,
//     responsive: true,
//   });
// })

