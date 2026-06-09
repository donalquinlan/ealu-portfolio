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

  var caseHashes = {
    "case-ppp": "ppp",
    "case-fiserv": "deploy",
    "case-vineti": "stability",
    "case-ealu": "intake"
  };

  var openModal = null;
  var lastFocused = null;

  function getModal(id) {
    return document.getElementById("case-modal-" + id);
  }

  function caseIdFromHash(hash) {
    var key = (hash || "").replace(/^#/, "");
    return caseHashes[key] || null;
  }

  function hashFromCaseId(id) {
    var entry = Object.keys(caseHashes).find(function (hash) {
      return caseHashes[hash] === id;
    });
    return entry ? "#" + entry : null;
  }

  function setCaseHash(id) {
    var hash = hashFromCaseId(id);
    if (hash && window.location.hash !== hash) {
      history.pushState(null, "", hash);
    }
  }

  function clearCaseHash() {
    if (caseIdFromHash(window.location.hash)) {
      history.pushState(null, "", window.location.pathname + window.location.search + "#case-studies");
    }
  }

  function openCaseModal(id, updateHash) {
    var modal = getModal(id);
    if (!modal) {
      return;
    }

    if (openModal && openModal !== modal) {
      openModal.hidden = true;
    }

    lastFocused = document.activeElement;
    openModal = modal;
    modal.hidden = false;
    document.body.classList.add("case-modal-open");

    if (updateHash !== false) {
      setCaseHash(id);
    }

    var closeButton = modal.querySelector(".case-modal-close");
    if (closeButton) {
      closeButton.focus();
    }
  }

  function closeCaseModal(clearHash) {
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

    if (clearHash !== false) {
      clearCaseHash();
    }
  }

  function handleCaseHash() {
    var caseId = caseIdFromHash(window.location.hash);
    if (caseId) {
      openCaseModal(caseId, false);
      return;
    }

    if (openModal) {
      closeCaseModal(false);
    }
  }

  document.querySelectorAll("[data-case-open]").forEach(function (button) {
    button.addEventListener("click", function () {
      openCaseModal(button.getAttribute("data-case-open"));
    });
  });

  document.querySelectorAll(".case-permalink a").forEach(function (link) {
    link.addEventListener("click", function (event) {
      event.preventDefault();
      var caseId = caseIdFromHash(link.getAttribute("href"));
      if (caseId) {
        openCaseModal(caseId);
      }
    });
  });

  document.querySelectorAll("[data-case-close]").forEach(function (element) {
    element.addEventListener("click", function () {
      closeCaseModal();
    });
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      closeCaseModal();
    }
  });

  window.addEventListener("hashchange", handleCaseHash);
  handleCaseHash();
})();
