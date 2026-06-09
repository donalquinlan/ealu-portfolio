(function () {
  var yearEl = document.getElementById("year");
  if (yearEl) {
    yearEl.textContent = String(new Date().getFullYear());
  }

  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var isOpen = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
      toggle.setAttribute("aria-label", isOpen ? "Close menu" : "Open menu");
    });

    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.setAttribute("aria-label", "Open menu");
      });
    });
  }

  var hashRedirects = {
    "#case-apple": "case-apple.html",
    "#case-ppp": "case-ppp.html",
    "#case-fiserv": "case-fiserv.html",
    "#case-vineti": "case-vineti.html",
    "#case-ealu": "case-ealu.html"
  };

  var redirect = hashRedirects[window.location.hash];
  if (redirect) {
    window.location.replace(redirect);
  }
})();
