// Mermaid Theme Auto-Switcher for Aqtra Docs
(function () {
  function applyMermaidTheme() {
    const scheme = document.documentElement.getAttribute(
      "data-md-color-scheme"
    );
    const dark = scheme === "slate";

    if (window.mermaid) {
      window.mermaid.initialize({
        startOnLoad: true,
        theme: dark ? "dark" : "default",
        securityLevel: "strict",
        themeVariables: {
          // Кастомизация цветов под бренд
          primaryColor: dark ? "#6366f1" : "#4f46e5", // indigo
          primaryTextColor: dark ? "#f8fafc" : "#1e293b",
          primaryBorderColor: dark ? "#475569" : "#cbd5e1",
          lineColor: dark ? "#64748b" : "#94a3b8",
          secondaryColor: dark ? "#1e293b" : "#f1f5f9",
          tertiaryColor: dark ? "#0f172a" : "#ffffff",
          background: dark ? "#0f172a" : "#ffffff",
          mainBkg: dark ? "#1e293b" : "#f8fafc",
          secondBkg: dark ? "#334155" : "#f1f5f9",
          tertiaryBkg: dark ? "#475569" : "#e2e8f0",
        },
        flowchart: {
          htmlLabels: true,
          curve: "basis",
        },
        sequence: {
          diagramMarginX: 50,
          diagramMarginY: 10,
          actorMargin: 50,
          width: 150,
          height: 65,
          boxMargin: 10,
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
          barGap: 4,
          topPadding: 50,
          leftPadding: 75,
          gridLineStartPadding: 35,
          fontSize: 11,
          fontFamily: '"JetBrains Mono", monospace',
          sectionFontSize: 24,
          numberSectionStyles: 4,
        },
      });
    }
  }

  // Первичная инициализация
  document.addEventListener("DOMContentLoaded", function () {
    // Небольшая задержка для загрузки Mermaid
    setTimeout(applyMermaidTheme, 100);
  });

  // Слежение за переключением темы в Material
  const obs = new MutationObserver(function (mutations) {
    mutations.forEach(function (mutation) {
      if (
        mutation.type === "attributes" &&
        mutation.attributeName === "data-md-color-scheme"
      ) {
        setTimeout(applyMermaidTheme, 50);
      }
    });
  });

  obs.observe(document.documentElement, {
    attributes: true,
    attributeFilter: ["data-md-color-scheme"],
  });

  // Переинициализация при изменении размера окна
  window.addEventListener("resize", function () {
    if (window.mermaid) {
      setTimeout(applyMermaidTheme, 100);
    }
  });
})();
