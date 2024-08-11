function setlabel80tta() {
  var tr80tta = document.getElementById("tr_88ta");
  if (document.getElementById("Select3").value == "No") {
    tr80tta.cells[0].innerText = "Deduction u/s 80TTA";
    document.getElementById("txt_80tta").value = 0;
  } else {
    tr80tta.cells[0].innerText = "Deduction u/s 80TTB";
    document.getElementById("txt_80tta").value = 0;
  }
}

function changelable(fla) {
  // Your existing function for changing labels based on the regime
}

function ckeck_PER() {
  var index = document.getElementById("Select1").value;
  $("#Select1 option[value=" + index + "]").attr("selected", "selected");
  if (index == 2007) {
    document.getElementById("newtd").innerHTML = "STT @10%";
  } else {
    document.getElementById("newtd").innerHTML = "STT @15%";
  }
  if (index > 2017 && index < 2019) {
    document.getElementById("lbl_sal").innerHTML =
      "Salary (Enter taxable salary after standard deduction of Rs.40000)";
    document.getElementById("ECess").innerHTML = "Health & Education Cess";
  } else {
    if (index > 2018) {
      document.getElementById("lbl_sal").innerHTML =
        "Salary (Enter taxable salary after standard deduction of Rs.50000)";
      document.getElementById("ECess").innerHTML = "Health & Education Cess";
    } else {
      document.getElementById("lbl_sal").innerHTML = "Salary";
      document.getElementById("ECess").innerHTML = "Education Cess";
    }
  }
  hideshow();
  if (index <= 2019) {
    document.getElementById("typeTO3").style.display = "none";
  }
  showcompanynewregime();
}

function showcompanynewregime() {
  if (document.getElementById("Select1").value >= 2020) {
    document.getElementById("lbl_TO").innerHTML = "";
    document.getElementById("SelectTO1").style.display = "none";
  }
}

function hideshow() {
  var ut = document.getElementById("Select2").value;
  var index = document.getElementById("Select1").value;
  document.getElementById("typeTO").style.display = "none";
  document.getElementById("typeTO1").style.display = "none";
  document.getElementById("lbl_TO").innerHTML = "";
  document.getElementById("SelectTO").value = "-1";
  document.getElementById("SelectTO1").value = "-1";
  if (ut == "Individual") {
    document.getElementById("genderl").style.display = "block";
    document.getElementById("seniorcitizenl").style.display = "block";
    document.getElementById("typel").style.display = "none";
    document.getElementById("genderc").style.display = "block";
    document.getElementById("seniorcitizenc").style.display = "block";
    document.getElementById("typec").style.display = "none";
    document.getElementById("lbl_sal").style.display = "block";
    document.getElementById("txtSalary").style.display = "block";
    document.getElementById("deduction1").style.display = "";
    document.getElementById("deduction2").style.display = "";
    document.getElementById("otherdeduction").innerHTML = "Other deduction";
  } else if (ut == "HUF") {
    document.getElementById("genderl").style.display = "none";
    document.getElementById("seniorcitizenl").style.display = "none";
    document.getElementById("typel").style.display = "none";
    document.getElementById("genderc").style.display = "none";
    document.getElementById("seniorcitizenc").style.display = "none";
    document.getElementById("typec").style.display = "none";
    document.getElementById("lbl_sal").style.display = "none";
    document.getElementById("txtSalary").style.display = "none";
    document.getElementById("deduction1").style.display = "";
    document.getElementById("deduction2").style.display = "";
    document.getElementById("otherdeduction").innerHTML = "Other deduction";
  } else if (ut == "Firm") {
    document.getElementById("genderl").style.display = "none";
    document.getElementById("seniorcitizenl").style.display = "none";
    document.getElementById("typel").style.display = "none";
    document.getElementById("genderc").style.display = "none";
    document.getElementById("seniorcitizenc").style.display = "none";
    document.getElementById("typec").style.display = "none";
    document.getElementById("lbl_sal").style.display = "none";
    document.getElementById("txtSalary").style.display = "none";
    document.getElementById("deduction1").style.display = "none";
    document.getElementById("deduction2").style.display = "none";
    document.getElementById("otherdeduction").innerHTML = "Deduction";
  } else if (ut == "Company") {
    document.getElementById("genderl").style.display = "none";
    document.getElementById("seniorcitizenl").style.display = "none";
    document.getElementById("typel").style.display = "block";
    document.getElementById("genderc").style.display = "none";
    document.getElementById("seniorcitizenc").style.display = "none";
    document.getElementById("typec").style.display = "block";
    document.getElementById("lbl_sal").style.display = "none";
    document.getElementById("txtSalary").style.display = "none";
    document.getElementById("deduction1").style.display = "none";
    document.getElementById("deduction2").style.display = "none";
    document.getElementById("otherdeduction").innerHTML = "Deduction";
    if (document.getElementById("Select5").value == "Domestic") {
      if (index > 2019) {
        document.getElementById("typeTO2").style.display = "block";
        document.getElementById("typeTO1").style.display = "none";
        document.getElementById("typeTO3").style.display = "none";
        if (rdnew.checked) {
          document.getElementById("typeTO2").style.display = "none";
          document.getElementById("typeTO1").style.display = "none";
          document.getElementById("typeTO3").style.display = "block";
          document.getElementById("lbl_TO").innerHTML =
            "Section under which tax is calculated in new regime";
        } else {
          document.getElementById("typeTO3").style.display = "none";
          document.getElementById("lbl_TO").innerHTML =
            "Turnover in Financial Year 2018-19";
        }
      } else if (index > 2018) {
        document.getElementById("typeTO2").style.display = "block";
        document.getElementById("typeTO1").style.display = "none";
        document.getElementById("typeTO").style.display = "none";
        document.getElementById("lbl_TO").innerHTML =
          "Turnover in Financial Year 2017-18";
      } else if (index == 2018) {
        document.getElementById("typeTO2").style.display = "none";
        document.getElementById("typeTO1").style.display = "block";
        document.getElementById("typeTO").style.display = "none";
        document.getElementById("lbl_TO").innerHTML =
          "Turnover in Financial Year 2016-17";
      } else if (index == 2017) {
        document.getElementById("typeTO2").style.display = "none";
        document.getElementById("typeTO").style.display = "block";
        document.getElementById("typeTO1").style.display = "none";
        document.getElementById("lbl_TO").innerHTML =
          "Turnover in Financial Year 2015-16";
      } else {
        document.getElementById("typeTO2").style.display = "none";
        document.getElementById("typeTO").style.display = "none";
        document.getElementById("typeTO1").style.display = "none";
        document.getElementById("lbl_TO").innerHTML = "";
        document.getElementById("SelectTO").value = "-1";
        document.getElementById("SelectTO1").value = "-1";
      }
    } else {
      document.getElementById("SelectTO").value = "-1";
      document.getElementById("SelectTO1").value = "-1";
      document.getElementById("typeTO").style.display = "none";
      document.getElementById("typeTO1").style.display = "none";
      document.getElementById("typeTO2").style.display = "none";
      document.getElementById("lbl_TO").innerHTML = "";
    }
  }
}

function calculateTax() {
  // Get input values
  var salary = parseFloat(document.getElementById("txtSalary").value) || 0;
  var ifhProperty =
    parseFloat(document.getElementById("txtIFHProperty").value) || 0;
  var bIncome = parseFloat(document.getElementById("txtBIncome").value) || 0;
  var otherIncome =
    parseFloat(document.getElementById("txtOtherIncome").value) || 0;
  var stcg = parseFloat(document.getElementById("txtSTCG").value) || 0;
  var ltcg = parseFloat(document.getElementById("txtLTCG").value) || 0;
  var chVIDeduction = parseFloat(document.getElementById("txtChVI").value) || 0;
  var sec10Deduction =
    parseFloat(document.getElementById("txtSec10").value) || 0;
  var ttaDeduction =
    parseFloat(document.getElementById("txt_80tta").value) || 0;

  // Calculate gross total income
  var grossTotalIncome =
    salary + ifhProperty + bIncome + otherIncome + stcg + ltcg;
  document.getElementById("txtGTI").value = grossTotalIncome.toFixed(2);

  // Calculate net taxable income
  var netTaxableIncome =
    grossTotalIncome - (chVIDeduction + sec10Deduction + ttaDeduction);
  document.getElementById("txtNTI").value = netTaxableIncome.toFixed(2);

  // Calculate tax payable
  var taxPayable = 0;

  // Example tax calculation logic (you can replace this with the actual tax slabs)
  if (netTaxableIncome <= 250000) {
    taxPayable = 0;
  } else if (netTaxableIncome <= 500000) {
    taxPayable = (netTaxableIncome - 250000) * 0.05;
  } else if (netTaxableIncome <= 1000000) {
    taxPayable = (netTaxableIncome - 500000) * 0.2 + 12500;
  } else {
    taxPayable = (netTaxableIncome - 1000000) * 0.3 + 112500;
  }

  // Update tax payable field
  document.getElementById("txtTaxPay").value = taxPayable.toFixed(2);
}

function goback() {
  history.back(1);
}

function Callprint(printArea) {
  try {
    var index = document.getElementById("Select2").value;
    $("#Select2 option[value=" + index + "]").attr("selected", "selected");
    var index2 = document.getElementById("Select4").value;
    $("#Select4 option[value=" + index2 + "]").attr("selected", "selected");
    var index3 = document.getElementById("Select3").value;
    $("#Select3 option[value=" + index3 + "]").attr("selected", "selected");
    var oIframe = document.getElementById("ifrmPrint");
    var oContent = document.getElementById(printArea).innerHTML;
    var oDoc = oIframe.contentWindow || oIframe.contentDocument;
    if (oDoc.document) oDoc = oDoc.document;
    oDoc.write(
      "<body style='vertical-align:top;' onload='this.focus(); this.print();'>"
    );
    oDoc.write(oContent + "</body>");
    oDoc.close();
  } catch (e) {
    self.print();
  }
}
