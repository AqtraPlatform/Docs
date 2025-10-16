/**
 * Locale Link Normalizer
 * Fixes language switching and ensures correct locale prefixes
 * Works with any number of languages configured in mkdocs-static-i18n
 */
(function () {
  // Determine current locale from path: '/en/...' → 'en'
  function currentLocale() {
    var m = (location.pathname || "/").match(/^\/([^/]+)\//);
    return m ? m[1] : "";
  }

  // Extract available locales from <link rel="alternate" hreflang="xx">
  function knownLocales() {
    var set = new Set();
    document
      .querySelectorAll('link[rel="alternate"][hreflang]')
      .forEach(function (l) {
        var lang = (l.getAttribute("hreflang") || "").trim();
        if (lang && lang !== "x-default") set.add(lang);
      });
    // Fallback to EN/DE if alternates not available
    if (set.size === 0)
      ["en", "de"].forEach(function (x) {
        set.add(x);
      });
    return Array.from(set);
  }

  // Normalize href: absolute /xx/...; relative → add current locale prefix
  function normalizeHref(href, locales) {
    try {
      if (
        !href ||
        href.startsWith("#") ||
        href.startsWith("mailto:") ||
        href.startsWith("tel:")
      )
        return href;
      // External absolute URL — ignore
      if (/^[a-z]+:\/\//i.test(href)) return href;

      // Absolute site path
      if (href.startsWith("/")) {
        // If /de/... or /en/... — OK
        var m = href.match(/^\/([^/]+)\//);
        if (m && locales.indexOf(m[1]) >= 0) return href;
        // If /de (without slash) → /de/
        if (locales.indexOf(href.slice(1)) >= 0)
          return "/" + href.slice(1) + "/";
        return href; // Leave as-is (/assets/..., /img/...)
      }

      // Relative path (problematic case)
      var loc = currentLocale();
      if (loc) {
        // If relative starts with another locale: 'de/...' on EN page → make absolute '/de/...'
        for (var i = 0; i < locales.length; i++) {
          var L = locales[i];
          if (href.startsWith(L + "/")) return "/" + href;
        }
        // Normal relative → add current locale: 'tutorials/...' → '/en/tutorials/...'
        return "/" + loc + "/" + href.replace(/^\.?\//, "");
      }
      return href;
    } catch (e) {
      return href;
    }
  }

  function applyFix() {
    var locales = knownLocales();

    // Normalize links in language menu, navigation and main content
    document.querySelectorAll("a[href]").forEach(function (a) {
      var orig = a.getAttribute("href");
      var fixed = normalizeHref(orig, locales);
      if (fixed !== orig) {
        a.setAttribute("href", fixed);
      }
    });

    // If Material has language <select> — normalize options
    document
      .querySelectorAll(
        'select[aria-label*="language" i] option,[data-md-component="language"] option'
      )
      .forEach(function (opt) {
        var v = opt.getAttribute("value");
        if (v) {
          var fixed = normalizeHref(v, locales);
          if (fixed !== v) opt.setAttribute("value", fixed);
        }
      });
  }

  // Run after render
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", applyFix);
  } else {
    applyFix();
  }

  // On Material SPA navigation (instant loading) catch changes
  document.addEventListener("navigation", applyFix, { passive: true });
})();
