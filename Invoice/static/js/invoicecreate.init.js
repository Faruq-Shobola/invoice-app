var paymentSign = "$";
function otherPayment() {
  var e = document.getElementById("choices-payment-currency").value;
  (paymentSign = e),
    Array.from(document.getElementsByClassName("product-line-price")).forEach(
      function (e) {
        (isUpdate = e.value.slice(1)), (e.value = paymentSign + isUpdate);
      }
    ),
    recalculateCart();
}
Array.from(document.getElementsByClassName("product-line-price")).forEach(
  function (e) {
    e.value = paymentSign + "0.00";
  }
);
var isPaymentEl = document.getElementById("choices-payment-currency"),
  choices = new Choices(isPaymentEl, { searchEnabled: !1 });
function isData() {
  var e = document.getElementsByClassName("plus"),
    t = document.getElementsByClassName("minus");
  e &&
    Array.from(e).forEach(function (n) {
      n.onclick = function (e) {
        var t;
        parseInt(n.previousElementSibling.value) < 100 &&
          (e.target.previousElementSibling.value++,
          (e =
            n.parentElement.parentElement.previousElementSibling.querySelector(
              ".product-price"
            ).value),
          (t = n.parentElement.parentElement.nextElementSibling.querySelector(
            ".product-line-price"
          )),
          updateQuantity(
            n.parentElement.querySelector(".product-quantity").value,
            e,
            t
          ));
      };
    }),
    t &&
      Array.from(t).forEach(function (n) {
        n.onclick = function (e) {
          var t;
          1 < parseInt(n.nextElementSibling.value) &&
            (e.target.nextElementSibling.value--,
            (e =
              n.parentElement.parentElement.previousElementSibling.querySelector(
                ".product-price"
              ).value),
            (t = n.parentElement.parentElement.nextElementSibling.querySelector(
              ".product-line-price"
            )),
            updateQuantity(
              n.parentElement.querySelector(".product-quantity").value,
              e,
              t
            ));
        };
      });
}
document
  .querySelector("#profile-img-file-input")
  .addEventListener("change", function () {
    var e = document.querySelector(".user-profile-image"),
      t = document.querySelector(".profile-img-file-input").files[0],
      n = new FileReader();
    n.addEventListener(
      "load",
      function () {
        e.src = n.result;
      },
      !1
    ),
      t && n.readAsDataURL(t);
  }),
  flatpickr("#date-field", { enableTime: !0, dateFormat: "d M, Y, h:i K" }),
  isData();

function new_link() {
  //   itemCount++;
  var newRow = document.querySelector("#newForm").cloneNode(true);
  var addItemBtn = document.querySelector("#add-item");

  //   newRow.id = itemCount;
  //   newRow.querySelector(".product-id").textContent = itemCount;

  newRow.querySelectorAll("input, textarea").forEach((input) => {
    input.value = "";
    input.classList.remove("is-invalid");
  });

  document
    .getElementById("newlink")
    .insertBefore(newRow, addItemBtn.parentNode.parentNode);

  isData();
  remove();
  amountKeyup();
  resetRow();
}
remove();

function remove() {
  Array.from(document.querySelectorAll(".product-removal a")).forEach(function (
    e
  ) {
    e.addEventListener("click", function (e) {
      removeItem(e), resetRow();
    });
  });
}
function resetRow() {
  Array.from(document.getElementById("newlink").querySelectorAll("tr")).forEach(
    function (e, t) {
      t += 1;
      e.querySelector(".product-id").innerHTML = t;
    }
  );
}
function recalculateCart() {
  var subtotal = 0;
  var total = 0;

  // Loop through each product row and sum up the product line prices
  Array.from(document.querySelectorAll(".product")).forEach(function (
    productRow
  ) {
    var productLinePrice = productRow.querySelector(
      ".product-line-price"
    ).value;
    var productLineAmount = parseFloat(productLinePrice.slice(1));
    subtotal += productLineAmount;
  });
  total = subtotal;

  // Update the corresponding input field
  document.getElementById("cart-subtotal").value =
    paymentSign + subtotal.toFixed(2);
  document.getElementById("cart-total").value = total.toFixed(2);
  updateTotal();
}

// Function to calculate the Total based on Subtotal and Labour
function updateTotal() {
  console.log("updateTotal function is triggered!");
  var subtotal = parseFloat(
    document.getElementById("cart-subtotal").value.slice(1)
  );
  console.log(subtotal);
  var labour = parseFloat(document.getElementById("cart-labour").value);
  console.log(labour);

  var total = subtotal + labour;
  console.log(total);

  document.getElementById("cart-total").value = "$" + total.toFixed(2);
}



function amountKeyup() {
  Array.from(document.getElementsByClassName("product-price")).forEach(
    function (n) {
      n.addEventListener("keyup", function (e) {
        var t =
          n.parentElement.nextElementSibling.nextElementSibling.querySelector(
            ".product-line-price"
          );
        updateQuantity(
          e.target.value,
          n.parentElement.nextElementSibling.querySelector(".product-quantity")
            .value,
          t
        );
      });
    }
  );
}

function updateQuantity(e, t, n) {
  e = (e = e * t).toFixed(2);
  (n.value = paymentSign + e), recalculateCart();
}
function removeItem(e) {
  e.target.closest("tr").remove(), recalculateCart();
}

amountKeyup();
var genericExamples = document.querySelectorAll("[data-trigger]");
function billingFunction() {
  document.getElementById("same").checked
    ? ((document.getElementById("shippingName").value =
        document.getElementById("billingName").value),
      (document.getElementById("shippingAddress").value =
        document.getElementById("billingAddress").value),
      (document.getElementById("shippingPhoneno").value =
        document.getElementById("billingPhoneno").value),
      (document.getElementById("shippingTaxno").value =
        document.getElementById("billingTaxno").value))
    : ((document.getElementById("shippingName").value = ""),
      (document.getElementById("shippingAddress").value = ""),
      (document.getElementById("shippingPhoneno").value = ""),
      (document.getElementById("shippingTaxno").value = ""));
}
Array.from(genericExamples).forEach(function (e) {
  new Choices(e, {
    placeholderValue: "This is a placeholder set in the config",
    searchPlaceholderValue: "This is a search placeholder",
  });
});
var cleaveBlocks = new Cleave("#cardNumber", {
    blocks: [4, 4, 4, 4],
    uppercase: !0,
  }),
  genericExamples = document.querySelectorAll('[data-plugin="cleave-phone"]');
Array.from(genericExamples).forEach(function (e) {
  new Cleave(e, { delimiters: ["(", ")", "-"], blocks: [0, 3, 3, 4] });
});
let viewobj;
var value,
  invoices_list = localStorage.getItem("invoices-list"),
  options = localStorage.getItem("option"),
  invoice_no = localStorage.getItem("invoice_no"),
  invoices = JSON.parse(invoices_list);
if (
  (null === localStorage.getItem("invoice_no") &&
  null === localStorage.getItem("option")
    ? ((viewobj = ""),
      (value = "#VL" + Math.floor(11111111 + 99999999 * Math.random())),
      (document.getElementById("invoicenoInput").value = value))
    : (viewobj = invoices.find((e) => e.invoice_no === invoice_no)),
  "" != viewobj && "edit-invoice" == options)
) {
  (document.getElementById("registrationNumber").value =
    viewobj.company_details.legal_registration_no),
    (document.getElementById("companyEmail").value =
      viewobj.company_details.email),
    (document.getElementById("companyWebsite").value =
      viewobj.company_details.website),
    new Cleave("#compnayContactno", {
      prefix: viewobj.company_details.contact_no,
      delimiters: ["(", ")", "-"],
      blocks: [0, 3, 3, 4],
    }),
    (document.getElementById("companyAddress").value =
      viewobj.company_details.address),
    (document.getElementById("companyaddpostalcode").value =
      viewobj.company_details.zip_code);
  for (
    var preview = document.querySelectorAll(".user-profile-image"),
      paroducts_list =
        ("" !== viewobj.img && (preview.src = viewobj.img),
        (document.getElementById("invoicenoInput").value =
          "#VAL" + viewobj.invoice_no),
        document.getElementById("invoicenoInput").setAttribute("readonly", !0),
        (document.getElementById("date-field").value = viewobj.date),
        (document.getElementById("choices-payment-status").value =
          viewobj.status),
        (document.getElementById("totalamountInput").value =
          "$" + viewobj.order_summary.total_amount),
        (document.getElementById("billingName").value =
          viewobj.billing_address.full_name),
        (document.getElementById("billingAddress").value =
          viewobj.billing_address.address),
        new Cleave("#billingPhoneno", {
          prefix: viewobj.company_details.contact_no,
          delimiters: ["(", ")", "-"],
          blocks: [0, 3, 3, 4],
        }),
        (document.getElementById("billingTaxno").value =
          viewobj.billing_address.tax),
        (document.getElementById("shippingName").value =
          viewobj.shipping_address.full_name),
        (document.getElementById("shippingAddress").value =
          viewobj.shipping_address.address),
        new Cleave("#shippingPhoneno", {
          prefix: viewobj.company_details.contact_no,
          delimiters: ["(", ")", "-"],
          blocks: [0, 3, 3, 4],
        }),
        (document.getElementById("shippingTaxno").value =
          viewobj.billing_address.tax),
        viewobj.prducts),
      counter = 1;
    counter++,
      1 < paroducts_list.length && document.getElementById("add-item").click(),
      paroducts_list.length - 1 >= counter;

  );
  var counter_1 = 1,
    cleave =
      (setTimeout(() => {
        Array.from(paroducts_list).forEach(function (e) {
          (document.getElementById("productName-" + counter_1).value =
            e.product_name),
            (document.getElementById("productDetails-" + counter_1).value =
              e.product_details),
            (document.getElementById("productRate-" + counter_1).value =
              e.rates),
            (document.getElementById("product-qty-" + counter_1).value =
              e.quantity),
            (document.getElementById("productPrice-" + counter_1).value =
              "$" + e.rates * e.quantity),
            counter_1++;
        });
      }, 300),
      (document.getElementById("cart-subtotal").value =
        "$" + viewobj.order_summary.sub_total),
      (document.getElementById("cart-tax").value =
        "$" + viewobj.order_summary.estimated_tex),
      (document.getElementById("cart-discount").value =
        "$" + viewobj.order_summary.discount),
      (document.getElementById("cart-shipping").value =
        "$" + viewobj.order_summary.shipping_charge),
      (document.getElementById("cart-total").value =
        "$" + viewobj.order_summary.total_amount),
      (document.getElementById("choices-payment-type").value =
        viewobj.payment_details.payment_method),
      (document.getElementById("cardholderName").value =
        viewobj.payment_details.card_holder_name),
      new Cleave("#cardNumber", {
        prefix: viewobj.payment_details.card_number,
        delimiter: " ",
        blocks: [4, 4, 4, 4],
        uppercase: !0,
      }));
  (document.getElementById("amountTotalPay").value =
    "$" + viewobj.order_summary.total_amount),
    (document.getElementById("exampleFormControlTextarea1").value =
      viewobj.notes);
}
document.addEventListener("DOMContentLoaded", function () {
  var T = document.getElementById("invoice_form");
  document.getElementsByClassName("needs-validation");
  T.addEventListener("submit", function (e) {
    e.preventDefault();
    var t = document.getElementById("invoicenoInput").value.slice(4),
      e = document.getElementById("companyEmail").value,
      n = document.getElementById("date-field").value,
      o = document.getElementById("totalamountInput").value.slice(1),
      a = document.getElementById("choices-payment-status").value,
      l = document.getElementById("billingName").value,
      i = document.getElementById("billingAddress").value,
      c = document
        .getElementById("billingPhoneno")
        .value.replace(/[^0-9]/g, ""),
      d = document.getElementById("billingTaxno").value,
      r = document.getElementById("shippingName").value,
      u = document.getElementById("shippingAddress").value,
      m = document
        .getElementById("shippingPhoneno")
        .value.replace(/[^0-9]/g, ""),
      s = document.getElementById("shippingTaxno").value,
      p = document.getElementById("choices-payment-type").value,
      v = document.getElementById("cardholderName").value,
      g = document.getElementById("cardNumber").value.replace(/[^0-9]/g, ""),
      y = document.getElementById("amountTotalPay").value.slice(1),
      E = document
        .getElementById("registrationNumber")
        .value.replace(/[^0-9]/g, ""),
      b = document.getElementById("companyEmail").value,
      I = document.getElementById("companyWebsite").value,
      h = document
        .getElementById("compnayContactno")
        .value.replace(/[^0-9]/g, ""),
      _ = document.getElementById("companyAddress").value,
      B = document.getElementById("companyaddpostalcode").value,
      f = document.getElementById("cart-subtotal").value.slice(1),
      x = document.getElementById("cart-tax").value.slice(1),
      w = document.getElementById("cart-discount").value.slice(1),
      S = document.getElementById("cart-shipping").value.slice(1),
      j = document.getElementById("cart-total").value.slice(1),
      q = document.getElementById("exampleFormControlTextarea1").value,
      A = document.getElementsByClassName("product"),
      N = 1,
      C = [];
    Array.from(A).forEach((e) => {
      var t = e.querySelector("#productName-" + N).value,
        n = e.querySelector("#productDetails-" + N).value,
        o = parseInt(e.querySelector("#productRate-" + N).value),
        a = parseInt(e.querySelector("#product-qty-" + N).value),
        e = e.querySelector("#productPrice-" + N).value.split("$"),
        t = {
          product_name: t,
          product_details: n,
          rates: o,
          quantity: a,
          amount: parseInt(e[1]),
        };
      C.push(t), N++;
    }),
      !1 === T.checkValidity()
        ? T.classList.add("was-validated")
        : ("edit-invoice" == options && invoice_no == t
            ? ((objIndex = invoices.findIndex((e) => e.invoice_no == t)),
              (invoices[objIndex].invoice_no = t),
              (invoices[objIndex].customer = l),
              (invoices[objIndex].img = ""),
              (invoices[objIndex].email = e),
              (invoices[objIndex].date = n),
              (invoices[objIndex].invoice_amount = o),
              (invoices[objIndex].status = a),
              (invoices[objIndex].billing_address = {
                full_name: l,
                address: i,
                phone: c,
                tax: d,
              }),
              (invoices[objIndex].shipping_address = {
                full_name: r,
                address: u,
                phone: m,
                tax: s,
              }),
              (invoices[objIndex].payment_details = {
                payment_method: p,
                card_holder_name: v,
                card_number: g,
                total_amount: y,
              }),
              (invoices[objIndex].company_details = {
                legal_registration_no: E,
                email: b,
                website: I,
                contact_no: h,
                address: _,
                zip_code: B,
              }),
              (invoices[objIndex].order_summary = {
                sub_total: f,
                estimated_tex: x,
                discount: w,
                shipping_charge: S,
                total_amount: j,
              }),
              (invoices[objIndex].prducts = C),
              (invoices[objIndex].notes = q),
              localStorage.removeItem("invoices-list"),
              localStorage.removeItem("option"),
              localStorage.removeItem("invoice_no"),
              localStorage.setItem("invoices-list", JSON.stringify(invoices)))
            : localStorage.setItem(
                "new_data_object",
                JSON.stringify({
                  invoice_no: t,
                  customer: l,
                  img: "",
                  email: e,
                  date: n,
                  invoice_amount: o,
                  status: a,
                  billing_address: {
                    full_name: l,
                    address: i,
                    phone: c,
                    tax: d,
                  },
                  shipping_address: {
                    full_name: r,
                    address: u,
                    phone: m,
                    tax: s,
                  },
                  payment_details: {
                    payment_method: p,
                    card_holder_name: v,
                    card_number: g,
                    total_amount: y,
                  },
                  company_details: {
                    legal_registration_no: E,
                    email: b,
                    website: I,
                    contact_no: h,
                    address: _,
                    zip_code: B,
                  },
                  order_summary: {
                    sub_total: f,
                    estimated_tex: x,
                    discount: w,
                    shipping_charge: S,
                    total_amount: j,
                  },
                  prducts: C,
                  notes: q,
                })
              ),
          (window.location.href = "apps-invoices-list.html"));
  });
});
