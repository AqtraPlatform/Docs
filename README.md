<div align="center">
  <img src="assets/brand/logo-light.svg" alt="Aqtra" width="200"/>

# Aqtra Documentation

**The official knowledge hub for Aqtra—clear, searchable, and built for everyone.**

[![Visit Documentation](https://img.shields.io/badge/📖_Visit-Documentation-4F46E5?style=for-the-badge)](https://docs.aqtra.io)
[![Languages](https://img.shields.io/badge/🌍_Languages-5-blue?style=flat-square)](https://docs.aqtra.io)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

[**Read the Docs**](https://docs.aqtra.io) · [**Release Notes**](https://github.com/AqtraPlatform/Docs/releases) · [**Give Feedback**](https://github.com/AqtraPlatform/Docs/issues)

</div>

---

## What This Repository Is

This repository contains the **official MkDocs documentation source** for the Aqtra platform—a single source of truth for product information, guides, and resources. The documentation is built with MkDocs and published transparently on GitHub, hosted at **[docs.aqtra.io](https://docs.aqtra.io)**.

Aqtra Docs serves customers, partners, developers, and decision-makers with clear, actionable knowledge to evaluate, implement, and get the most from the platform. Every change is tracked, reviewed, and versioned, built with accessibility, discoverability, and multilingual support in mind.

---

## Highlights

- **🌍 Multilingual** — Available in English, German, French, Spanish, and Portuguese, with built-in language switcher
- **🔍 Fast & Searchable** — Instant search across all content with smart suggestions
- **📌 Versioned & Traceable** — Release notes, change history, and stable references
- **♿ Accessibility-Minded** — Designed with WCAG principles for inclusive UX
- **🚀 SEO-Ready** — Sitemaps, alternate links, and structured metadata for discoverability
- **🔓 Open & Transparent** — Published from GitHub with full change visibility
- **🤖 AI-Powered Translation** — Automated documentation translation using LLM with markdown-aware processing

---

## Who It's For

**🎯 Decision-Makers & Evaluators**  
Understand what Aqtra does, how it fits your use case, and what sets it apart—without wading through technical jargon.

**👨‍💻 Developers & Implementers**  
Find step-by-step guides, component references, workflows, and Python scripting documentation to build and deploy applications efficiently.

**🤝 Partners & Integrators**  
Access architectural overviews, integration patterns, and deployment scenarios to deliver solutions confidently.

**💬 Support & Success Teams**  
Quickly locate troubleshooting steps, UI walkthroughs, and user-facing guides to resolve issues and onboard customers smoothly.

**📰 Media & Analysts**  
Get accurate, current product information, release history, and positioning for coverage, reviews, and market analysis.

---

## Quick Links

| Resource                                                                | Description                                                                      |
| ----------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **[📖 Documentation Site](https://docs.aqtra.io)**                      | Browse the full documentation in English, German, French, Spanish, or Portuguese |
| **[🆕 Release Notes](https://github.com/AqtraPlatform/Docs/releases)**  | See what's new in each version                                                   |
| **[💬 Discussions](https://github.com/AqtraPlatform/Docs/discussions)** | Ask questions and share ideas                                                    |
| **[🐛 Report an Issue](https://github.com/AqtraPlatform/Docs/issues)**  | Found something wrong? Let us know                                               |
| **[🔐 Security](https://github.com/AqtraPlatform/Docs/security)**       | Responsible disclosure and security policies                                     |

---

## Contributing & Feedback

We welcome your input! If you spot a gap, error, or opportunity to improve the docs:

- **Open an issue** to report bugs, suggest enhancements, or request new content
- **Start a discussion** to ask questions or propose new sections
- **Submit a pull request** if you'd like to contribute directly

For technical setup, translation workflow, and contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).  
For release process and deployment instructions, see [RELEASE.md](RELEASE.md).

---

## Localization

Aqtra Docs is available in multiple languages:

- **English** (en) — Default language, source documentation in `docs/`
- **German** (Deutsch) — `docs/de/`
- **French** (Français) — `docs/fr/`
- **Spanish** (Español) — `docs/es/`
- **Portuguese** (Português) — `docs/pt/`

The documentation uses MkDocs with `mkdocs-static-i18n` plugin. Each language is located in `docs/{lang}/` directory, mirroring the structure of `docs/` (English source). Language switching is seamless—use the selector in the site header.

### Translation System

Translations are managed using an automated LLM-powered pipeline that preserves Markdown structure, code blocks, links, and cross-references while translating human-readable text. The translation system intelligently handles technical content, maintaining code snippets, URLs, and internal references intact. Internal links to `docs.aqtra.io` are automatically prefixed with language paths (e.g., `/de/`, `/fr/`) to maintain proper navigation across language versions.

In case of translation issues, the system preserves structural correctness, ensuring documentation remains valid and buildable even when translation quality varies.

**For detailed instructions on translation workflow, regenerating specific pages, and running quality checks, see [CONTRIBUTING.md](CONTRIBUTING.md).**

## License & Trademarks

This documentation is licensed under the [MIT License](LICENSE).

Aqtra and related marks are trademarks of their respective owners. All rights reserved.

---

<div align="center">
  
  **Built with ❤️ for clarity, accuracy, and accessibility**
  
  [docs.aqtra.io](https://docs.aqtra.io) · [GitHub](https://github.com/AqtraPlatform/Docs) · [Issues](https://github.com/AqtraPlatform/Docs/issues)
  
</div>
