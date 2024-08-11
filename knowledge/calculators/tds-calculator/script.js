$(function () {
  $("#drp_Section_description").change(function () {
    var selectedOption = $(this).val();
    var rate = selectedOption.split(" ")[0]; // Extract the rate from the selected option
    var minAmount = selectedOption.split(" ")[1]; // Extract the minimum amount from the selected option

    if ($("#panquote").val() === "1") {
      // If PAN is not quoted
      rate *= 2; // Double the rate if PAN is not quoted
    }

    $("#plus_1").val(rate + "%");
    if (minAmount) {
      $("#ExceedAmount").text(minAmount);
      $("#tr_payexceeding").show();
    } else {
      $("#tr_payexceeding").hide();
    }

    calculateTax();
  });

  $("#panquote").change(function () {
    var selectedOption = $("#drp_Section_description").val();
    var rate = selectedOption.split(" ")[0];

    if ($(this).val() === "1") {
      // If PAN is not quoted
      rate *= 2; // Double the rate if PAN is not quoted
    }

    $("#plus_1").val(rate + "%");

    calculateTax();
  });

  $("#plus_2").on("input", function () {
    calculateTax();
  });

  function calculateTax() {
    var rate = parseFloat($("#plus_1").val()) || 0;
    var amount = parseFloat($("#plus_2").val()) || 0;
    var tax = (rate / 100) * amount;
    $("#min_1").val(tax.toFixed(2));
  }
  // Rate Slider
  $("#rate_slider").slider({
    range: "min",
    value: 20,
    min: 0,
    max: 100,
    slide: function (event, ui) {
      $("#plus_1").val(ui.value + "%");
    },
  });
  $("#plus_1").val($("#rate_slider").slider("value") + "%");

  // Amount Slider
  $("#amount_slider").slider({
    range: "min",
    value: 1000,
    min: 0,
    max: 1000000,
    slide: function (event, ui) {
      $("#plus_2").val(ui.value);
    },
  });
  $("#plus_2").val($("#amount_slider").slider("value"));

  $("#rate_slider, #amount_slider").on("slidechange", function () {
    calculateTax();
  });
  calculateTax();
});
