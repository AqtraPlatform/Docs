// Mermaid theme synchronization for MkDocs Material
(function () {
  "use strict";

  // Wait for DOM to be ready
  document.addEventListener("DOMContentLoaded", function () {
    // Initialize Mermaid with theme synchronization
    if (typeof mermaid !== "undefined") {
      // Configure Mermaid
      mermaid.initialize({
        theme: "default",
        themeVariables: {
          primaryColor: "#1976d2",
          primaryTextColor: "#ffffff",
          primaryBorderColor: "#1565c0",
          lineColor: "#424242",
          secondaryColor: "#f5f5f5",
          tertiaryColor: "#ffffff",
        },
        flowchart: {
          htmlLabels: true,
          curve: "basis",
        },
        sequence: {
          diagramMarginX: 50,
          diagramMarginY: 10,
          boxTextMargin: 5,
          noteMargin: 10,
          messageMargin: 35,
          mirrorActors: true,
          bottomMarginAdj: 1,
          useMaxWidth: true,
          rightAngles: false,
          showSequenceNumbers: false,
        },
        gantt: {
          titleTopMargin: 25,
          barHeight: 20,
          fontFamily: "Arial, sans-serif",
          fontSize: 11,
          gridLineStartPadding: 35,
          bottomPadding: 25,
          leftPadding: 75,
          rightPadding: 75,
          numberSectionStyles: 4,
        },
      });

      // Theme synchronization function
      function syncMermaidTheme() {
        const isDark =
          document.documentElement.getAttribute("data-md-color-scheme") ===
          "slate";

        if (isDark) {
          mermaid.initialize({
            theme: "dark",
            themeVariables: {
              primaryColor: "#42a5f5",
              primaryTextColor: "#ffffff",
              primaryBorderColor: "#1976d2",
              lineColor: "#757575",
              secondaryColor: "#424242",
              tertiaryColor: "#616161",
            },
          });
        } else {
          mermaid.initialize({
            theme: "default",
            themeVariables: {
              primaryColor: "#1976d2",
              primaryTextColor: "#ffffff",
              primaryBorderColor: "#1565c0",
              lineColor: "#424242",
              secondaryColor: "#f5f5f5",
              tertiaryColor: "#ffffff",
            },
          });
        }

        // Re-render all Mermaid diagrams
        const mermaidElements = document.querySelectorAll(".mermaid");
        mermaidElements.forEach((element) => {
          const id = element.id;
          if (id) {
            mermaid.init(undefined, element);
          }
        });
      }

      // Listen for theme changes
      const observer = new MutationObserver(function (mutations) {
        mutations.forEach(function (mutation) {
          if (
            mutation.type === "attributes" &&
            mutation.attributeName === "data-md-color-scheme"
          ) {
            syncMermaidTheme();
          }
        });
      });

      // Start observing
      observer.observe(document.documentElement, {
        attributes: true,
        attributeFilter: ["data-md-color-scheme"],
      });

      // Initial theme sync
      syncMermaidTheme();
    }
  });
})();
