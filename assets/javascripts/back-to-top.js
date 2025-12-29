/**
 * Localized "Back to Top" FAB for MkDocs Material
 * Supports EN/DE with accessibility and smooth scroll
 */
(function () {
  "use strict";

  // Detect language from <html lang="...">
  const root = document.documentElement;
  const lang = (root.getAttribute("lang") || "en").toLowerCase();

  // Localized labels
  const labels = {
    en: "Back to top",
    de: "Nach oben",
  };
  const label = lang.startsWith("de") ? labels.de : labels.en;

  // Create button element
  const btn = document.createElement("button");
  btn.className = "btp-fab";
  btn.type = "button";
  btn.setAttribute("aria-label", label);
  btn.setAttribute("title", label);
  btn.setAttribute("tabindex", "0");
  btn.innerHTML = "↑";

  // Visibility state
  let visible = false;

  // Toggle visibility based on scroll position
  function toggleVisibility() {
    const shouldShow = window.scrollY > 400;
    if (shouldShow !== visible) {
      visible = shouldShow;
      btn.classList.toggle("btp-visible", shouldShow);
    }
  }

  // Scroll to top with smooth behavior
  function scrollToTop() {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  }

  // Event handlers
  btn.addEventListener("click", scrollToTop);
  btn.addEventListener("keydown", function (e) {
    if (e.key === "Enter" || e.key === " ") {
      e.preventDefault();
      scrollToTop();
    }
  });

  // Initialize on DOM ready
  document.addEventListener("DOMContentLoaded", function () {
    document.body.appendChild(btn);
    toggleVisibility();
  });

  // Update on scroll (passive for performance)
  window.addEventListener("scroll", toggleVisibility, { passive: true });
})();
