/**
 * Legacy URL redirects for Aqtra Docs
 * Handles old URL patterns and redirects to new structure
 */
(function () {
  try {
    var p = window.location.pathname;
    var search = window.location.search;
    var hash = window.location.hash;

    // Global redirect: /en/app-develop/* → /en/app-development/*
    if (p.indexOf("/en/app-develop/") === 0) {
      var target = p.replace("/en/app-develop/", "/en/app-development/");
      var url = target + search + hash;
      window.location.replace(url);
      return;
    }

    // Specific redirects for renamed paths
    var redirectMap = {
      "/en/overview1/first-entry.html":
        "/en/overview/getting-started.html#first",
    };

    if (redirectMap[p]) {
      window.location.replace(redirectMap[p] + search);
      return;
    }
  } catch (e) {
    // Silently fail - don't break the page
    console.error("Redirect script error:", e);
  }
})();
