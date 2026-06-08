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

  var openModal = null;
  var lastFocused = null;

  function getModal(id) {
    return document.getElementById("case-modal-" + id);
  }

  function openCaseModal(id) {
    var modal = getModal(id);
    if (!modal) {
      return;
    }

    closeCaseModal();

    lastFocused = document.activeElement;
    openModal = modal;
    modal.hidden = false;
    document.body.classList.add("case-modal-open");

    var closeButton = modal.querySelector(".case-modal-close");
    if (closeButton) {
      closeButton.focus();
    }
  }

  function closeCaseModal() {
    if (!openModal) {
      return;
    }

    openModal.hidden = true;
    document.body.classList.remove("case-modal-open");

    if (lastFocused && typeof lastFocused.focus === "function") {
      lastFocused.focus();
    }

    openModal = null;
    lastFocused = null;
  }

  document.querySelectorAll("[data-case-open]").forEach(function (button) {
    button.addEventListener("click", function () {
      openCaseModal(button.getAttribute("data-case-open"));
    });
  });

  document.querySelectorAll("[data-case-close]").forEach(function (element) {
    element.addEventListener("click", closeCaseModal);
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      closeCaseModal();
    }
  });
})();
