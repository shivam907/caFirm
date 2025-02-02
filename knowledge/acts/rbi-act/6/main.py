import os
import requests
from bs4 import BeautifulSoup

# Step 1: Define your custom header and footer
custom_header = """
<!DOCTYPE html>
<html lang="zxx">
  <head>
    <!-- meta tag -->
    <meta charset="utf-8" />
    <title>Kedia Dhandharia & Co</title>
    <meta name="description" content="" />
    <!-- responsive tag -->
    <meta http-equiv="x-ua-compatible" content="ie=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <!-- favicon -->
    <link rel="apple-touch-icon" href="apple-touch-icon.html" />
    <link
      rel="shortcut icon"
      type="image/x-icon"
      href="../../../../../../assets/images/favicon.ico"
    />
    <!-- Bootstrap v5.0.2 css -->
    <link
      rel="stylesheet"
      type="text/css"
      href="../../../../../../assets/css/bootstrap.min.css"
    />
    <!-- font-awesome css -->
    <link
      rel="stylesheet"
      type="text/css"
      href="../../../../../../assets/fonts/font/font-awesome.min.css"
    />
    <!-- Uicons Regular Rounded css -->
    <link
      rel="stylesheet"
      type="text/css"
      href="../../../../../../assets/css/uicons-regular-rounded.css"
    />
    <!-- flaticon css -->
    <link
      rel="stylesheet"
      type="text/css"
      href="../../../../../../assets/fonts/flaticon.css"
    />
    <!-- animate css -->
    <link
      rel="stylesheet"
      type="text/css"
      href="../../../../../../assets/css/animate.css"
    />
    <!-- owl.carousel css -->
    <link
      rel="stylesheet"
      type="text/css"
      href="../../../../../../assets/css/owl.carousel.css"
    />
    <!-- slick slider css -->
    <link
      rel="stylesheet"
      type="text/css"
      href="../../../../../../assets/css/slick.css"
    />
    <!-- odometer css -->
    <link
      rel="stylesheet"
      type="text/css"
      href="../../../../../../assets/css/odometer.min.css"
    />
    <!-- off canvas css -->
    <link
      rel="stylesheet"
      type="text/css"
      href="../../../../../../assets/css/off-canvas.css"
    />
    <!-- magnific popup css -->
    <link
      rel="stylesheet"
      type="text/css"
      href="../../../../../../assets/css/magnific-popup.css"
    />
    <!-- Main Menu css -->
    <link
      rel="stylesheet"
      type="text/css"
      href="../../../../../../assets/css/rsmenu-main.css"
    />
    <!-- spacing css -->
    <link
      rel="stylesheet"
      type="text/css"
      href="../../../../../../assets/css/rs-spacing.css"
    />
    <!-- style css -->
    <link rel="stylesheet" type="text/css" href="../../../../../../style.css" />
    <!-- This stylesheet dynamically changed from style.less -->
    <!-- responsive css -->
    <link
      rel="stylesheet"
      type="text/css"
      href="../../../../../../assets/css/responsive.css"
    />
<link rel="stylesheet" href="https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
 <style>
  table{
    width: 100%
  }
 </style>
<script src="script.js"></script>
  </head>
  <body class="defult-home">
    <div class="offwrap"></div>

    <!--Preloader start here-->

    <!--Preloader area end here-->

    <!-- Main content Start -->
    <div class="main-content">
      <!--Full width header Start-->
    <div class="full-width-header">
      <!--Header Start-->
      <header id="rs-header" class="rs-header header-style1 header-modify1">
        <!-- Toolbar Area Start -->
        <div class="toolbar-area topbar-style1 hidden-md">
          <div class="container">
            <div class="row rs-vertical-middle">
              <div class="col-lg-8">
                <div class="toolbar-contact">
                  <ul class="rs-contact-info">
                    <li>
                      <i class="fi fi-rr-envelope-plus"></i>
                      <a href="mailto:info@kediadhandharia.in">info@kediadhandharia.in</a>
                    </li>
                    <li>
                      <i class="fi fi-rr-phone-call"></i>
                      <a href="tel:033-2359-5641"> 033-2359-5641 / 42</a>
                    </li>
                    
                  </ul>
                </div>
              </div>
              
            </div>
          </div>
        </div>
        <!-- Toolbar Area End -->

        <!-- Menu Start -->
        <div class="menu-area menu-sticky">
          <div class="container">
            <div class="row-table">
              <div class="col-cell header-logo">
                <div class="logo-area">
                  <a href="index.html">
                    <img
                      class="normal-logo"
                      src="../../../../../assets/images/logo.svg"
                      alt="logo"
                    />
                    <img
                      class="sticky-logo"
                      src="../../../../../assets/images/logo.svg"
                      alt="logo"
                    />
                  </a>
                </div>
              </div>
              <div class="col-cell">
                <div class="rs-menu-area">
                  <div class="main-menu">
                    <nav class="rs-menu hidden-md">
                      <ul class="nav-menu">
                        <li class="current-menu-item">
                          <!-- <a href="/">Home</a> -->
                        </li>
                        <li class="current-menu-item">
                          <a href="/">Home</a>
                        </li>
                        <li class="menu-item-has-children">
                          <a href="#">About Us</a>
                         <ul class="sub-menu">
                              <li>
                                <a href="/about/about-company/">About Company</a>
                              </li>
                              <li>
                                <a href="/about/our-clients/">Our Clients</a>
                              </li>
                              <li>
                                <a href="/about/our-team/">Our Team</a>
                              </li>

                            </ul>
                        </li>
                        <li class="menu-item-has-children">
                          <a href="#">Resources</a>
                          <ul class="sub-menu">
                            <li class="menu-item-has-children">
                              <a href="#">Calculators</a>
                              <ul class="sub-menu">
                                <li>
                                  <a
                                    href="/knowledge/calculators/gst-calculator"
                                    >GST Calculator</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/calculators/tax-calculator"
                                    >Tax Calculator</a
                                  >
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">RERA Calculator</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a
                                        href="/knowledge/calculators/rera-calculator/developers-calculator"
                                        >Developers Calculator</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/calculators/rera-calculator/home-buyer-delay-interest"
                                        >Home Buyer Delay Interest</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/calculators/rera-calculator/home-buyer-refund"
                                        >Home Buyer Refund</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/calculators/tds-calculator"
                                    >TDS Calculator</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/calculators/calculate-net-profit"
                                    >Calculate Net Profit</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/calculators/calculate-net-worth"
                                    >Calculate Net Worth</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/calculators/effective-capital"
                                    >Effective Capital</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/calculators/hra">HRA</a>
                                </li>
                                <li>
                                  <a href="/knowledge/calculators/nsc">NSC</a>
                                </li>
                                <li>
                                  <a href="/knowledge/calculators/emi">EMI</a>
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/calculators/auto-loan-calculator"
                                    >Auto Loan Calculator</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/calculators/home-loan-calculator"
                                    >Home Loan Calculator</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/calculators/get-no-of-installment"
                                    >Get No. Of Installment</a
                                  >
                                </li>
                              </ul>
                            </li>
                            <li class="menu-item-has-children">
                              <a href="#">Bulletins</a>
                              <ul class="sub-menu">
                                <li>
                                  <a href="/knowledge/bulletins/rbi-sebi"
                                    >RBI SEBI</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/notification"
                                    >Notification</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/circular"
                                    >Circular</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/income-tax"
                                    >Income Tax</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/service-tax"
                                    >Service Tax</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/bulletins/central-sales-tax"
                                    >Central Sales Tax</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/excise-matters"
                                    >Excise Matters</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/customs"
                                    >Customs</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/company-law"
                                    >Company Law</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/labour-laws"
                                    >Labour Laws</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/fema">FEMA</a>
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/llp-act"
                                    >The LLP Act 2008</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/bulletins/accounting-standards"
                                    >Accounting Standard (INDAS)</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/others"
                                    >Others</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/gst">GST</a>
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">VAT</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a href="/knowledge/bulletins/delhi-vat"
                                        >Delhi VAT</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/bulletins/mumbai-vat"
                                        >Maharashtra VAT</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/bulletins/gujarat-vat"
                                        >Gujarat VAT</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/bulletins/telangana-vat"
                                        >Telangana VAT</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/bulletins/tamilnadu-vat"
                                        >Tamil Nadu VAT</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/igst">IGST</a>
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/utgst">UTGST</a>
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/bulletins/compensation-cess"
                                    >Compensation Cess</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/ibc-regulation"
                                    >IBC Regulation</a
                                  >
                                </li>
                              </ul>
                            </li>
                            <li class="menu-item-has-children">
                              <a href="#">Utilities</a>
                              <ul class="sub-menu">
                                <li>
                                  <a href="/knowledge/utilities/rates-of-tds"
                                    >Rates of TDS</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/utilities/tds-rates-for-nri"
                                    >TDS Rates for NRI us 195</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/utilities/rates-of-income-tax"
                                    >Rates of Income Tax</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/utilities/depreciation-rates-companies-act"
                                    >Depreciation Rates Companies Act</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/utilities/depreciation-rates-income-tax-act"
                                    >Depreciation Rates Income Tax Act</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/utilities/roc-filing-fees"
                                    >ROC Filing Fees (Cos Act, 2013)</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/utilities/roc-fee-structure"
                                    >ROC Fee Structure (Cos Act, 2013)</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/utilities/cost-inflation-index"
                                    >Cost Inflation Index</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/utilities/ifsc-codes"
                                    >IFSC Codes</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/utilities/micr-codes"
                                    >MICR Codes</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/utilities/rates-of-nsc-interest"
                                    >Rates of NSC Interest</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/utilities/gold-silver-rates"
                                    >Gold and Silver Rates</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/utilities/rates-of-stamp-duty"
                                    >Rates of Stamp Duty</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/utilities/llp-fees"
                                    >LLP Fees</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/utilities/national-industries-classification"
                                    >National Industries Classification</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/utilities/hsn-rate-list"
                                    >HSN Rate List</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/utilities/deduction-us-80tta-vs-80ttb"
                                    >Deduction u/s 80TTA Vs 80TTB</a
                                  >
                                </li>
                              </ul>
                            </li>

                            <li class="menu-item-has-children">
                              <a href="#">Forms</a>
                              <ul class="sub-menu">
                                <li>
                                  <a href="/knowledge/forms/income-tax-forms"
                                    >Income Tax Forms</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/forms/roc-forms-2013"
                                    >ROC Forms (Cos Act, 2013)</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/forms/roc-forms-1956"
                                    >ROC Forms (Cos Act, 1956)</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/forms/income-declaration-forms"
                                    >Income Declaration Forms</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/forms/wealth-tax-forms"
                                    >Wealth Tax Forms</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/forms/service-tax-forms"
                                    >Service Tax Forms</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/forms/unpaid-dividend-forms"
                                    >Companies Unpaid Dividend Forms</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/forms/nbfc-forms"
                                    >NBFC Forms</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/forms/llp-winding-up"
                                    >LLP Winding Up</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/forms/fema-forms"
                                    >FEMA Forms</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/forms/llp-forms"
                                    >LLP Forms</a
                                  >
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">CGST Forms</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/gst-forms"
                                        >GST Forms</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/accounts-and-records"
                                        >Accounts and Records</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/advance-ruling"
                                        >Advance Ruling</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/appeals-and-revision"
                                        >Appeals and Revision</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/assessment-and-audit"
                                        >Assessment and Audit</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/composition"
                                        >Composition</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/demands-and-recovery"
                                        >Demands and Recovery</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/input-tax-credit"
                                        >Input Tax Credit</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/inspection-search-and-seizure"
                                        >Inspection, Search and Seizure</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/offences-and-penalties"
                                        >Offences and Penalties</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/payment-of-tax"
                                        >Payment of Tax</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/refund"
                                        >Refund</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/registration"
                                        >Registration</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/returns"
                                        >Returns</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/transitional-provisions"
                                        >Transitional Provisions</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/value-of-supply"
                                        >Value of Supply</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                              </ul>
                            </li>
                            <li class="menu-item-has-children">
                              <a href="#">Links</a>
                              <ul class="sub-menu">
                                <li>
                                  <a href="/knowledge/links/quick-links"
                                    >Quick Links</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/links/important-links"
                                    >Important Links</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/links/gst-vat-links"
                                    >GST/VAT Links</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/links/ease-of-doing-business"
                                    >Ease Of Doing Business</a
                                  >
                                </li>
                              </ul>
                            </li>
                            <li class="menu-item-has-children">
                              <a href="#">Acts</a>
                              <ul class="sub-menu">
                                <li class="menu-item-has-children">
                                  <a href="#">Direct Tax</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a href="/knowledge/acts/income-tax-act"
                                        >Income Tax Act</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/wealth-tax-act"
                                        >Wealth Tax Act</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/income-declaration-scheme"
                                        >Income Declaration Scheme 2016</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">Indirect Tax</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a href="/knowledge/acts/service-tax-act"
                                        >Service Tax (Finance Act, 1994)</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/central-sales-tax-act"
                                        >Central Sales Tax Act, 1956</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/central-excise-act"
                                        >The Central Excise Act, 1944</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/customs-act"
                                        >Customs Act, 1962</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/entry-tax-act"
                                        >Entry Tax Act</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">Corporate Laws</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a
                                        href="/knowledge/acts/companies-act-2013"
                                        >Companies Act, 2013</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/companies-act-1956"
                                        >Companies Act, 1956</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/llp-act"
                                        >LLP Act</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/sebi-act"
                                        >SEBI Act, 1992</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">VAT Laws</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a href="/knowledge/acts/delhi-vat-act"
                                        >Delhi VAT Act, 2004</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/maharashtra-vat-act"
                                        >MVAT Act, 2002</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/west-bengal-vat-act"
                                        >West Bengal VAT Act, 2003</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/tamilnadu-vat-act"
                                        >Tamil Nadu VAT Act, 2006</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/karnataka-vat-act"
                                        >Karnataka VAT Act, 2003</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/gujarat-vat-act"
                                        >Gujarat VAT Act, 2003</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/up-vat-act"
                                        >UP VAT Act, 2008</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/rajasthan-vat-act"
                                        >Rajasthan VAT Act, 2003</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/punjab-vat-act"
                                        >Punjab VAT Act</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/haryana-vat-act"
                                        >Haryana VAT Act</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/telangana-vat-act"
                                        >Telangana VAT Act, 2005</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/andhra-pradesh-vat-act"
                                        >Andhra Pradesh VAT Act, 2005</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/bihar-vat-act"
                                        >Bihar VAT Act, 2005</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">Other Statutes</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a href="/knowledge/acts/esi-act"
                                        >ESI Act, 1948</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/pf-act"
                                        >PF Act, 1952</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/profession-tax-act"
                                        >Profession Tax Act</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/indian-partnership-act"
                                        >The Indian Partnership Act, 1932</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/societies-registration-act"
                                        >Societies Registration Act, 1860</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/competition-act"
                                        >Competition Act, 2002</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/rbi-act"
                                        >Reserve Bank of India Act, 1934</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/mrtp-act"
                                        >MRTP Act, 1969</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/equalisation-levy-act"
                                        >Equalisation Levy Act, 2016</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/rti-act"
                                        >Right To Information Act, 2005</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/fema-act"
                                        >FEMA, 1999</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/maharashtra-rera"
                                        >Maharashtra RERA</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/rera-act"
                                        >RERA, 2016</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/ibc-act"
                                        >Insolvency & Bankruptcy Code, 2016</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/benami-property-act"
                                        >Benami Property Act, 1988</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">GST Laws</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a href="/knowledge/acts/igst-act"
                                        >IGST Act, 2017</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/cgst-act"
                                        >CGST Tax Act, 2017</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/utgst-act"
                                        >UTGST Act, 2017</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/gst-compensation-act"
                                        >GST (Compensation to States) Act</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                              </ul>
                            </li>
                            <li class="menu-item-has-children">
                              <a href="#">Rules</a>
                              <ul class="sub-menu">
                                <li class="menu-item-has-children">
                                  <a href="#">Direct Tax Rules</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a
                                        href="/knowledge/rules/income-tax-rules"
                                        >Income Tax Rules</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/wealth-tax-rules"
                                        >Wealth Tax Rules, 1957</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/income-declaration-scheme-rules"
                                        >Income Declaration Scheme Rules,
                                        2016</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">Indirect Tax Rules</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a
                                        href="/knowledge/rules/gst-valuation-rules"
                                        >GST Valuation Rules, 2016</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/service-tax-rules"
                                        >Service Tax Rules</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/rules/cst-delhi-rules"
                                        >CST (Delhi) Rules, 2005</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/cst-maharashtra-rules"
                                        >CST (Maharashtra) Rules</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/customs-valuation-rules"
                                        >Customs Valuation Rules</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/cenvat-credit-rules"
                                        >Cenvat Credit Rules, 2017</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/rules/entry-tax-rules"
                                        >Entry Tax Rules</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">Corporate Laws Rules</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a href="/knowledge/rules/companies-rules"
                                        >Companies Rules, 2014</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/rules/llp-rules"
                                        >LLP Rules, 2009</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/llp-winding-up-rules"
                                        >LLP Winding up Rules, 2012</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/unpaid-dividend-rules"
                                        >Unpaid Dividend Rules, 1978</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">VAT Laws Rules</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a href="/knowledge/rules/delhi-vat-rules"
                                        >Delhi VAT Rules, 2005</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/maharashtra-vat-rules"
                                        >Maharashtra VAT Rules, 2005</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/west-bengal-vat-rules"
                                        >West Bengal VAT Rules, 2005</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/tamilnadu-vat-rules"
                                        >Tamil Nadu VAT Rules, 2007</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/karnataka-vat-rules"
                                        >Karnataka VAT Rules, 2005</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/gujarat-vat-rules"
                                        >Gujarat VAT Rules, 2006</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/rules/up-vat-rules"
                                        >Uttar Pradesh VAT Rules, 2008</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/rajasthan-vat-rules"
                                        >Rajasthan VAT Rules, 2006</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/punjab-vat-rules"
                                        >Punjab VAT Rules</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/haryana-vat-rules"
                                        >Haryana VAT Rules, 2003</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/telangana-vat-rules"
                                        >Telangana VAT Rules, 2005</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/andhra-pradesh-vat-rules"
                                        >Andhra Pradesh VAT Rules, 2005</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/rules/bihar-vat-rules"
                                        >Bihar VAT Rules, 2005</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">Other Statutes</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a
                                        href="/knowledge/rules/profession-tax-rules"
                                        >Profession Tax Rules</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/nbfc-deposits-directions"
                                        >NBFC Deposits Directions, 1998</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/nbfc-advertisement-rules"
                                        >NBFC & Misc NBC (Advt) Rules, 1977</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/nbfc-auditor-report"
                                        >NBFC Auditor Report Directions, 2008</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/delhi-labour-welfare-fund-rules"
                                        >Delhi Labour Welfare Fund Rules,
                                        1997</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/cost-records-and-audit-rules"
                                        >Cost Records and Audit Rules, 2014</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/rules/baggage-rules"
                                        >Baggage Rules, 2016</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/equalisation-levy-rules"
                                        >Equalisation Levy Rules, 2016</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/nclt-nclat-rules"
                                        >NCLT And NCLAT Rules</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/insolvency-rules"
                                        >Insolvency & Bankruptcy Rules</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/benami-property-rules"
                                        >Benami Property Rules, 2016</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">GST Rules</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a href="/knowledge/rules/cgst-rules"
                                        >CGST Rules, 2017</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/rules/igst-rules"
                                        >IGST Rules, 2017</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                              </ul>
                            </li>
                          </ul>
                        </li>
                        <li class="menu-item-has-children">
                          <a href="#">Services</a>
                          <ul class="sub-menu">
                            <li>
                              <a href="/services/finance-and-accounting/"
                                >Finance & Accounting</a
                              >
                            </li>
                            <li>
                              <a href="/services/indirect-taxes/"
                                >Indirect Taxes</a
                              >
                            </li>
                            <li>
                              <a href="/services/audit-and-insurance/"
                                >Audit </a
                              >
                            </li>
                            <li>
                              <a href="/services/direct-taxes/">Direct Taxes</a>
                            </li>
                            <li>
                              <a href="/services/corporate-law/"
                                >Corporate Law & Compliances</a
                              >
                            </li>
                          </ul>
                        </li>
                        <li><a href="/blogs/">Blog</a></li>
                        <li><a href="/careers/">Careers</a></li>
                        <li><a href="/contact/">Contact Us</a></li>
                      </ul>
                    </nav>
                  </div>
                  <!-- //.main-menu -->
                </div>
              </div>
              <div class="col-cell">
                <div class="expand-btn-inner">
                  <ul>
                    <li class="btn-quote">
                      <a class="readon slide-started" href="tel:033-2359-5641"
                        >Call Us Now</a
                      >
                    </li>
                    <li class="humburger">
                      <a id="nav-expander" class="nav-expander bar" href="#">
                        <div class="bar">
                          <span class="dot1"></span>
                          <span class="dot2"></span>
                          <span class="dot3"></span>
                          <span class="dot4"></span>
                          <span class="dot5"></span>
                          <span class="dot6"></span>
                          <span class="dot7"></span>
                          <span class="dot8"></span>
                          <span class="dot9"></span>
                        </div>
                      </a>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Menu End -->

        <!-- Canvas Menu start -->
        <nav class="right_menu_togle mobile-navbar-menu" id="mobile-navbar-menu">
  <div class="close-btn">
    <a id="nav-close2" class="nav-close">
      <div class="line">
        <span class="line1"></span>
        <span class="line2"></span>
      </div>
    </a>
  </div>
  <ul class="nav-menu">
    <li class="current-menu-item">
      <a href="/">Home</a>
    </li>
    <li class="menu-item-has-children">
      <a href="#">About Us</a>
      <ul class="sub-menu">
                              <li>
                                <a href="/about/about-company/">About Company</a>
                              </li>
                              <li>
                                <a href="/about/our-clients/">Our Clients</a>
                              </li>
                              <li>
                                <a href="/about/our-team/">Our Team</a>
                              </li>

                            </ul>
    </li>
    <li class="menu-item-has-children">
      <a href="#">Services</a>
      <ul class="sub-menu">
        <li><a href="/services/finance-and-accounting/">Finance & Accounting</a></li>
        <li><a href="/services/indirect-taxes/">Indirect Taxes</a></li>
        <li><a href="/services/audit-and-insurance/">Audit </a></li>
        <li><a href="/services/direct-taxes/">Direct Taxes</a></li>
        <li><a href="/services/corporate-law/">Corporate Law & Compliances</a></li>
      </ul>
    </li>
 <li class="menu-item-has-children">
                          <a href="#">Resources</a>
                          <ul class="sub-menu">
                            <li class="menu-item-has-children">
                              <a href="#">Calculators</a>
                              <ul class="sub-menu">
                                <li>
                                  <a
                                    href="/knowledge/calculators/gst-calculator"
                                    >GST Calculator</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/calculators/tax-calculator"
                                    >Tax Calculator</a
                                  >
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">RERA Calculator</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a
                                        href="/knowledge/calculators/rera-calculator/developers-calculator"
                                        >Developers Calculator</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/calculators/rera-calculator/home-buyer-delay-interest"
                                        >Home Buyer Delay Interest</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/calculators/rera-calculator/home-buyer-refund"
                                        >Home Buyer Refund</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/calculators/tds-calculator"
                                    >TDS Calculator</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/calculators/calculate-net-profit"
                                    >Calculate Net Profit</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/calculators/calculate-net-worth"
                                    >Calculate Net Worth</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/calculators/effective-capital"
                                    >Effective Capital</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/calculators/hra">HRA</a>
                                </li>
                                <li>
                                  <a href="/knowledge/calculators/nsc">NSC</a>
                                </li>
                                <li>
                                  <a href="/knowledge/calculators/emi">EMI</a>
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/calculators/auto-loan-calculator"
                                    >Auto Loan Calculator</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/calculators/home-loan-calculator"
                                    >Home Loan Calculator</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/calculators/get-no-of-installment"
                                    >Get No. Of Installment</a
                                  >
                                </li>
                              </ul>
                            </li>
                            <li class="menu-item-has-children">
                              <a href="#">Bulletins</a>
                              <ul class="sub-menu">
                                <li>
                                  <a href="/knowledge/bulletins/rbi-sebi"
                                    >RBI SEBI</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/notification"
                                    >Notification</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/circular"
                                    >Circular</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/income-tax"
                                    >Income Tax</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/service-tax"
                                    >Service Tax</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/bulletins/central-sales-tax"
                                    >Central Sales Tax</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/excise-matters"
                                    >Excise Matters</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/customs"
                                    >Customs</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/company-law"
                                    >Company Law</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/labour-laws"
                                    >Labour Laws</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/fema">FEMA</a>
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/llp-act"
                                    >The LLP Act 2008</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/bulletins/accounting-standards"
                                    >Accounting Standard (INDAS)</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/others"
                                    >Others</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/gst">GST</a>
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">VAT</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a href="/knowledge/bulletins/delhi-vat"
                                        >Delhi VAT</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/bulletins/mumbai-vat"
                                        >Maharashtra VAT</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/bulletins/gujarat-vat"
                                        >Gujarat VAT</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/bulletins/telangana-vat"
                                        >Telangana VAT</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/bulletins/tamilnadu-vat"
                                        >Tamil Nadu VAT</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/igst">IGST</a>
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/utgst">UTGST</a>
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/bulletins/compensation-cess"
                                    >Compensation Cess</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/bulletins/ibc-regulation"
                                    >IBC Regulation</a
                                  >
                                </li>
                              </ul>
                            </li>
                            <li class="menu-item-has-children">
                              <a href="#">Utilities</a>
                              <ul class="sub-menu">
                                <li>
                                  <a href="/knowledge/utilities/rates-of-tds"
                                    >Rates of TDS</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/utilities/tds-rates-for-nri"
                                    >TDS Rates for NRI us 195</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/utilities/rates-of-income-tax"
                                    >Rates of Income Tax</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/utilities/depreciation-rates-companies-act"
                                    >Depreciation Rates Companies Act</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/utilities/depreciation-rates-income-tax-act"
                                    >Depreciation Rates Income Tax Act</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/utilities/roc-filing-fees"
                                    >ROC Filing Fees (Cos Act, 2013)</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/utilities/roc-fee-structure"
                                    >ROC Fee Structure (Cos Act, 2013)</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/utilities/cost-inflation-index"
                                    >Cost Inflation Index</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/utilities/ifsc-codes"
                                    >IFSC Codes</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/utilities/micr-codes"
                                    >MICR Codes</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/utilities/rates-of-nsc-interest"
                                    >Rates of NSC Interest</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/utilities/gold-silver-rates"
                                    >Gold and Silver Rates</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/utilities/rates-of-stamp-duty"
                                    >Rates of Stamp Duty</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/utilities/llp-fees"
                                    >LLP Fees</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/utilities/national-industries-classification"
                                    >National Industries Classification</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/utilities/hsn-rate-list"
                                    >HSN Rate List</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/utilities/deduction-us-80tta-vs-80ttb"
                                    >Deduction u/s 80TTA Vs 80TTB</a
                                  >
                                </li>
                              </ul>
                            </li>

                            <li class="menu-item-has-children">
                              <a href="#">Forms</a>
                              <ul class="sub-menu">
                                <li>
                                  <a href="/knowledge/forms/income-tax-forms"
                                    >Income Tax Forms</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/forms/roc-forms-2013"
                                    >ROC Forms (Cos Act, 2013)</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/forms/roc-forms-1956"
                                    >ROC Forms (Cos Act, 1956)</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/forms/income-declaration-forms"
                                    >Income Declaration Forms</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/forms/wealth-tax-forms"
                                    >Wealth Tax Forms</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/forms/service-tax-forms"
                                    >Service Tax Forms</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/forms/unpaid-dividend-forms"
                                    >Companies Unpaid Dividend Forms</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/forms/nbfc-forms"
                                    >NBFC Forms</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/forms/llp-winding-up"
                                    >LLP Winding Up</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/forms/fema-forms"
                                    >FEMA Forms</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/forms/llp-forms"
                                    >LLP Forms</a
                                  >
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">CGST Forms</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/gst-forms"
                                        >GST Forms</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/accounts-and-records"
                                        >Accounts and Records</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/advance-ruling"
                                        >Advance Ruling</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/appeals-and-revision"
                                        >Appeals and Revision</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/assessment-and-audit"
                                        >Assessment and Audit</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/composition"
                                        >Composition</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/demands-and-recovery"
                                        >Demands and Recovery</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/input-tax-credit"
                                        >Input Tax Credit</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/inspection-search-and-seizure"
                                        >Inspection, Search and Seizure</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/offences-and-penalties"
                                        >Offences and Penalties</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/payment-of-tax"
                                        >Payment of Tax</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/refund"
                                        >Refund</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/registration"
                                        >Registration</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/returns"
                                        >Returns</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/transitional-provisions"
                                        >Transitional Provisions</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/forms/cgst-forms/value-of-supply"
                                        >Value of Supply</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                              </ul>
                            </li>
                            <li class="menu-item-has-children">
                              <a href="#">Links</a>
                              <ul class="sub-menu">
                                <li>
                                  <a href="/knowledge/links/quick-links"
                                    >Quick Links</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/links/important-links"
                                    >Important Links</a
                                  >
                                </li>
                                <li>
                                  <a href="/knowledge/links/gst-vat-links"
                                    >GST/VAT Links</a
                                  >
                                </li>
                                <li>
                                  <a
                                    href="/knowledge/links/ease-of-doing-business"
                                    >Ease Of Doing Business</a
                                  >
                                </li>
                              </ul>
                            </li>
                            <li class="menu-item-has-children">
                              <a href="#">Acts</a>
                              <ul class="sub-menu">
                                <li class="menu-item-has-children">
                                  <a href="#">Direct Tax</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a href="/knowledge/acts/income-tax-act"
                                        >Income Tax Act</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/wealth-tax-act"
                                        >Wealth Tax Act</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/income-declaration-scheme"
                                        >Income Declaration Scheme 2016</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">Indirect Tax</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a href="/knowledge/acts/service-tax-act"
                                        >Service Tax (Finance Act, 1994)</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/central-sales-tax-act"
                                        >Central Sales Tax Act, 1956</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/central-excise-act"
                                        >The Central Excise Act, 1944</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/customs-act"
                                        >Customs Act, 1962</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/entry-tax-act"
                                        >Entry Tax Act</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">Corporate Laws</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a
                                        href="/knowledge/acts/companies-act-2013"
                                        >Companies Act, 2013</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/companies-act-1956"
                                        >Companies Act, 1956</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/llp-act"
                                        >LLP Act</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/sebi-act"
                                        >SEBI Act, 1992</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">VAT Laws</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a href="/knowledge/acts/delhi-vat-act"
                                        >Delhi VAT Act, 2004</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/maharashtra-vat-act"
                                        >MVAT Act, 2002</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/west-bengal-vat-act"
                                        >West Bengal VAT Act, 2003</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/tamilnadu-vat-act"
                                        >Tamil Nadu VAT Act, 2006</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/karnataka-vat-act"
                                        >Karnataka VAT Act, 2003</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/gujarat-vat-act"
                                        >Gujarat VAT Act, 2003</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/up-vat-act"
                                        >UP VAT Act, 2008</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/rajasthan-vat-act"
                                        >Rajasthan VAT Act, 2003</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/punjab-vat-act"
                                        >Punjab VAT Act</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/haryana-vat-act"
                                        >Haryana VAT Act</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/telangana-vat-act"
                                        >Telangana VAT Act, 2005</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/andhra-pradesh-vat-act"
                                        >Andhra Pradesh VAT Act, 2005</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/bihar-vat-act"
                                        >Bihar VAT Act, 2005</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">Other Statutes</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a href="/knowledge/acts/esi-act"
                                        >ESI Act, 1948</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/pf-act"
                                        >PF Act, 1952</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/profession-tax-act"
                                        >Profession Tax Act</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/indian-partnership-act"
                                        >The Indian Partnership Act, 1932</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/societies-registration-act"
                                        >Societies Registration Act, 1860</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/competition-act"
                                        >Competition Act, 2002</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/rbi-act"
                                        >Reserve Bank of India Act, 1934</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/mrtp-act"
                                        >MRTP Act, 1969</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/equalisation-levy-act"
                                        >Equalisation Levy Act, 2016</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/rti-act"
                                        >Right To Information Act, 2005</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/fema-act"
                                        >FEMA, 1999</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/maharashtra-rera"
                                        >Maharashtra RERA</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/rera-act"
                                        >RERA, 2016</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/ibc-act"
                                        >Insolvency & Bankruptcy Code, 2016</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/benami-property-act"
                                        >Benami Property Act, 1988</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">GST Laws</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a href="/knowledge/acts/igst-act"
                                        >IGST Act, 2017</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/cgst-act"
                                        >CGST Tax Act, 2017</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/acts/utgst-act"
                                        >UTGST Act, 2017</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/acts/gst-compensation-act"
                                        >GST (Compensation to States) Act</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                              </ul>
                            </li>
                            <li class="menu-item-has-children">
                              <a href="#">Rules</a>
                              <ul class="sub-menu">
                                <li class="menu-item-has-children">
                                  <a href="#">Direct Tax Rules</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a
                                        href="/knowledge/rules/income-tax-rules"
                                        >Income Tax Rules</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/wealth-tax-rules"
                                        >Wealth Tax Rules, 1957</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/income-declaration-scheme-rules"
                                        >Income Declaration Scheme Rules,
                                        2016</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">Indirect Tax Rules</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a
                                        href="/knowledge/rules/gst-valuation-rules"
                                        >GST Valuation Rules, 2016</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/service-tax-rules"
                                        >Service Tax Rules</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/rules/cst-delhi-rules"
                                        >CST (Delhi) Rules, 2005</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/cst-maharashtra-rules"
                                        >CST (Maharashtra) Rules</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/customs-valuation-rules"
                                        >Customs Valuation Rules</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/cenvat-credit-rules"
                                        >Cenvat Credit Rules, 2017</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/rules/entry-tax-rules"
                                        >Entry Tax Rules</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">Corporate Laws Rules</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a href="/knowledge/rules/companies-rules"
                                        >Companies Rules, 2014</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/rules/llp-rules"
                                        >LLP Rules, 2009</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/llp-winding-up-rules"
                                        >LLP Winding up Rules, 2012</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/unpaid-dividend-rules"
                                        >Unpaid Dividend Rules, 1978</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">VAT Laws Rules</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a href="/knowledge/rules/delhi-vat-rules"
                                        >Delhi VAT Rules, 2005</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/maharashtra-vat-rules"
                                        >Maharashtra VAT Rules, 2005</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/west-bengal-vat-rules"
                                        >West Bengal VAT Rules, 2005</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/tamilnadu-vat-rules"
                                        >Tamil Nadu VAT Rules, 2007</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/karnataka-vat-rules"
                                        >Karnataka VAT Rules, 2005</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/gujarat-vat-rules"
                                        >Gujarat VAT Rules, 2006</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/rules/up-vat-rules"
                                        >Uttar Pradesh VAT Rules, 2008</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/rajasthan-vat-rules"
                                        >Rajasthan VAT Rules, 2006</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/punjab-vat-rules"
                                        >Punjab VAT Rules</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/haryana-vat-rules"
                                        >Haryana VAT Rules, 2003</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/telangana-vat-rules"
                                        >Telangana VAT Rules, 2005</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/andhra-pradesh-vat-rules"
                                        >Andhra Pradesh VAT Rules, 2005</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/rules/bihar-vat-rules"
                                        >Bihar VAT Rules, 2005</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">Other Statutes</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a
                                        href="/knowledge/rules/profession-tax-rules"
                                        >Profession Tax Rules</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/nbfc-deposits-directions"
                                        >NBFC Deposits Directions, 1998</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/nbfc-advertisement-rules"
                                        >NBFC & Misc NBC (Advt) Rules, 1977</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/nbfc-auditor-report"
                                        >NBFC Auditor Report Directions, 2008</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/delhi-labour-welfare-fund-rules"
                                        >Delhi Labour Welfare Fund Rules,
                                        1997</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/cost-records-and-audit-rules"
                                        >Cost Records and Audit Rules, 2014</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/rules/baggage-rules"
                                        >Baggage Rules, 2016</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/equalisation-levy-rules"
                                        >Equalisation Levy Rules, 2016</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/nclt-nclat-rules"
                                        >NCLT And NCLAT Rules</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/insolvency-rules"
                                        >Insolvency & Bankruptcy Rules</a
                                      >
                                    </li>
                                    <li>
                                      <a
                                        href="/knowledge/rules/benami-property-rules"
                                        >Benami Property Rules, 2016</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                                <li class="menu-item-has-children">
                                  <a href="#">GST Rules</a>
                                  <ul class="sub-menu">
                                    <li>
                                      <a href="/knowledge/rules/cgst-rules"
                                        >CGST Rules, 2017</a
                                      >
                                    </li>
                                    <li>
                                      <a href="/knowledge/rules/igst-rules"
                                        >IGST Rules, 2017</a
                                      >
                                    </li>
                                  </ul>
                                </li>
                              </ul>
                            </li>
                          </ul>
                        </li>
    <li>
      <a href="/careers/">Careers</a>
    </li>
    <li>
      <a href="/contact/">Contact Us</a>
    </li>
  </ul>
  <!-- //.nav-menu -->
  <div class="canvas-contact">
    <div class="address-area">
      <div class="address-list">
        <div class="info-icon">
          <i class="flaticon-location"></i>
        </div>
        <div class="info-content">
          <h4 class="title">Address</h4>
          <em>BC - 266, Sector 1, Salt Lake City, Kolkata, West Bengal 700064</em>
        </div>
      </div>
      <div class="address-list">
        <div class="info-icon">
          <i class="flaticon-email"></i>
        </div>
        <div class="info-content">
          <h4 class="title">Email</h4>
          <em><a href="mailto:info@kediadhandharia.in">info@kediadhandharia.in</a></em>
        </div>
      </div>
      <div class="address-list">
        <div class="info-icon">
          <i class="flaticon-call"></i>
        </div>
        <div class="info-content">
          <h4 class="title">Phone</h4>
          <em><a href="tel:033-2359-5641">033-2359-5641 / 42</a></em>
        </div>
      </div>
    </div>
  </div>
</nav>
        <!-- Canvas Menu end -->
      </header>
      <!--Header End-->
    </div>
        <script src="../../../../../assets/js/jquery.min.js"></script>
    <script src="../../../../../assets/js/jquery.nav.js"></script>
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    <script src="../../../../../assets/js/slick.min.js"></script>
    <script src="../../../../../assets/js/wow.min.js"></script>
    <script src="../../../../../assets/js/jquery.appear.min.js"></script>
    <script src="../../../../../assets/js/jquery.easypiechart.min.js"></script>
    <script src="../../../../../assets/js/jquery.magnific-popup.min.js"></script>
    <script src="../../../../../assets/js/main.js"></script>
    <div style="-moz-border-radius:10px; -webkit-border-radius:10px; -khtml-border-radius:10px;border-radius:5px;
border-radius:10px; box-shadow: 0 0 10px rgba(0,0,0,.5); border: 3px groove threedface; background-color:#EEEEEE;
 margin-bottom:10px;min-height:450px;height:auto;" align="center">
"""

custom_footer = """
</div>
<link rel="stylesheet" href="https://ip.webtel.in/hra/css/calc_style.css">
<script src="https://ip.webtel.in/hra/js/jquery-ui.js"></script>
<script src="https://www.gstatic.com/charts/loader.js"></script>
<script>
    // JavaScript for initializing sliders and other interactive components
</script>

<style>

</style>


      <br>
      <br>
      <br>


    <!-- Main content End -->

    <!-- Footer Start -->
    <footer id="rs-footer" class="rs-footer footer-main-home">
      <div class="footer-top">
        <div class="container">
          <div class="row">
            <div class="col-lg-3 md-mb-20">
              <h3 class="footer-title">About Company</h3>
              <div class="textwidget mb-33" style="text-align: justify">
                Kedia Dhandharia & Co established in 1988, offers comprehensive
                accounting, assurance, tax advisory, and consultancy services,
                prioritizing integrity, transparency, and client success.
              </div>
              <ul class="footer-social md-mb-30">
                <li>
                  <a href="#"><i class="fab fa-facebook-f"></i></a>
                </li>
                <li>
                  <a href="#"><i class="fa-brands fa-x-twitter"></i></a>
                </li>
                <!-- <li><a href="#"><i class="fab fa-linkedin-in"></i></a></li>  -->
                <li>
                  <a href="#"><i class="fab fa-instagram"></i></a>
                </li>
              </ul>
            </div>
            <div class="col-lg-3 pl-76 md-pl-15 md-mb-10">
              <h3 class="footer-title">Contact Info</h3>
              <ul class="address-widget">
                <li>
                  <i class="fi fi-rr-map-marker-home"></i>
                  <div class="desc">
                    Reference<br />
                    Address
                  </div>
                </li>
                <li>
                  <i class="fi fi-rr-phone-call"></i>
                  <div class="desc">
                    <a href="tel:+910000000000">+91 0000000000</a>
                  </div>
                </li>
                <li>
                  <i class="fi fi-rr-envelope-plus"></i>
                  <div class="desc">
                    <a href="mailto:info@example.in">info@example.in</a>
                  </div>
                </li>
              </ul>
            </div>
            <div class="col-lg-3 pl-75 md-pl-15 md-mb-10">
              <h3 class="footer-title">Our Services</h3>
              <ul class="site-map">
                <li>
                  <a href="finance-and-accounting.html">Finance & Accounting</a>
                </li>
                <li><a href="indirect-taxes.html">Indirect Taxes</a></li>
                <li>
                  <a href="audit-and-insurance.html">Audit & Insurance</a>
                </li>
                <li><a href="direct-taxes.html">Direct Taxes</a></li>
                <li>
                  <a href="corporate-law.html">Corporate Law & Compliances</a>
                </li>
              </ul>
            </div>
            <div class="col-lg-3">
              <h3 class="footer-title">Our Resources</h3>
              <ul class="site-map">
                <li><a href="about.html">About Company</a></li>
                <li><a href="clients.html">Our Clients</a></li>
                <li><a href="careers.html">Careers</a></li>
                <li><a href="#">Example 1</a></li>
                <li><a href="#">Example 2</a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <div class="container">
          <div class="row y-middle">
            <div class="col-lg-6 md-mb-10 text-lg-end text-center order-last">
              <ul class="copy-right-menu">
                <li><a href="index.html">Home</a></li>
                <li><a href="about.html">About Us</a></li>
                <!-- <li><a href="#">Services</a></li> -->
                <!-- <li><a href="blog.html">Blog</a></li> -->
                <li><a href="contact.html">Contact</a></li>
              </ul>
            </div>
            <div class="col-lg-6">
              <div class="copyright text-lg-start text-center">
                <p>
                  © 2024 Kedia Dhandharia & Co Designed By
                  <a href="https://www.switchhigh.com/" target="blank"
                    >SwitchHigh</a
                  >
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </footer>
    <!-- Footer End -->

    <!-- start scrollUp  -->
    <div id="scrollUp">
      <i class="fa fa-angle-up"></i>
    </div>
    <!-- End scrollUp  -->

    <!-- Search Modal Start -->
    <div class="modal fade search-modal" id="searchModal" tabindex="-1">
      <button type="button" class="close" data-bs-dismiss="modal">
        <i class="fi fi-rr-cross-small"></i>
      </button>
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="search-block clearfix">
            <form>
              <div class="form-group">
                <input
                  class="form-control"
                  placeholder="Searching..."
                  type="text"
                />
                <button type="submit" value="Search">
                  <i class="fi fi-rr-search"></i>
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <!-- Search Modal End -->
  <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
 
<script src="script.js"></script>
    <!-- modernizr js -->
  </body>
</html>

"""

# Step 2: Get the main page content
main_url = "https://arksandassociates.com/laws/8199/Reserve_Bank_of_India_Act_1934.aspx"
response = requests.get(main_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Find all <a> tags in the table
table = soup.find('tbody')
rows = table.find_all('tr')

# Step 4: Loop through each row and fetch the link, download the page, extract the first <table>, and save it in a folder
for idx, row in enumerate(rows, start=1):
    a_tag = row.find('a')
    if a_tag and 'href' in a_tag.attrs:
        page_url = a_tag['href']
        if not page_url.startswith('http'):
            page_url = f"https://arksandassociates.com{page_url}"
        
        # Fetch the content of the linked page
        page_response = requests.get(page_url)
        page_soup = BeautifulSoup(page_response.content, 'html.parser')
        
        # Extract only the first <table> tag from the page
        first_table = page_soup.find('table')
        if first_table:
            # Create a folder for each page
            folder_name = f"{idx}"
            os.makedirs(folder_name, exist_ok=True)
            
            # Prepare the custom HTML with the header, first table, and footer
            final_content = custom_header + str(first_table) + custom_footer
            
            # Save the content as index.html inside the folder
            with open(os.path.join(folder_name, "index.html"), "w", encoding="utf-8") as file:
                file.write(final_content)
            
            print(f"Downloaded and saved: {folder_name}/index.html with custom header and footer")

print("All pages downloaded and customized.")
