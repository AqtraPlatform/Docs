# Getting Started

> A structured entry point for newcomers to Aqtra. Technical tone. This page links documentation, tutorials, videos (with transcripts), and a runnable sample to form a progressive learning roadmap.

---

## What is Aqtra?

Aqtra is a **low‑code platform** for building business applications primarily through a visual UI, with optional **Python scripting** for advanced logic. This hybrid model speeds up delivery for beginners and lets developers extend and customize when needed.

**You will learn to:**

- Install and run Aqtra (cloud or local via Docker).
- Build a first feature end‑to‑end (data model → UI component → data flow → publish).
- Use Python scripts where appropriate.
- Integrate with external services and APIs.

> **Target audience:** citizen developers, junior front‑/back‑end developers, analysts, architects, team leads.

**Primary CTAs:**

- **Start in 60 minutes →** First feature walkthrough (see [4) First win](#4-first-win-in-60-minutes))
- **Documentation →** [https://docs.aqtra.io/en/](https://docs.aqtra.io/en/)
- **Video track →** [https://www.youtube.com/@Aqtra.Academy](https://www.youtube.com/@Aqtra.Academy)

**Quick links (cards):**

- **Install** → [5) Install & Access](#5-install--access) (Cloud / Docker)
- **Build your first screen (Invoice)** → [4) First win](#4-first-win-in-60-minutes)
- **DataFlow basics** → [2) Step‑by‑step learning path](#2-stepbystep-learning-path-single-track)
- **Publish to web** → [2) Step‑by‑step learning path](#2-stepbystep-learning-path-single-track)

**On this page**

- [1) Methodology — how to use this guide](#1-methodology--how-to-use-this-guide)
- [2) Step‑by‑step learning path](#2-stepbystep-learning-path-single-track)
- [3) Tutorials & Documentation Cross-Links](#tutorials-documentation-cross-links)
- [4) First win in ~60 minutes](#4-first-win-in-60-minutes)
- [5) Install & Access](#5-install--access)
- [6) Core Concepts (Aqtra Glossary)](#6-core-concepts-aqtra-glossary)
- [7) Video Track](#7-video-track-with-transcripts--timecodes)
- [8) DataFlow Step Library](#8-dataflow-step-library-quick-reference)
- [9) FAQ](#9-faq-short-practical)

---

## 1) Methodology — how to use this guide {: #1-methodology--how-to-use-this-guide }

- **Single-track progression**: one unified path for all roles, minimal new concepts per step.
- **First‑mention linking**: each concept/UI element is linked once at first appearance; later steps assume it.
- **Just‑in‑time depth**: each step references focused docs and a short video with clickable timestamps.
- **Visible outcomes**: every step ends in a concrete, testable result in Workplace.
- **Error‑first mindset**: Step 10 teaches systematic debugging/log analysis.
- **Assessment**: the **Capstone** (Step 11) validates CRUD, integration, templating, navigation, and roles/permissions.

### Scope & prerequisites

- Access to **Aqtra Studio/Workplace** (cloud tenant) _or_ a local **Docker** setup (≥ 4 vCPU / 8 GB RAM).
- Modern browser and the ability to view devtools **Network** tab.
- (Optional) Basic familiarity with JSON and HTTP APIs for Step 6.

### Learning outcomes (per step)

- **Step 1**: you can access Studio/Workplace.
- **Step 2**: you can model an entity (Invoice) and surface it in a Component visible in Workplace.
- **Step 3**: you can build a DataFlow and bind it to a Button.
- **Step 4**: you can complete CRUD and basic validation.
- **Step 5**: you can add Python logic in a flow.
- **Step 6**: you can call an external HTTP API and map results.
- **Step 7**: you can compose a MultiComponent page with data context.
- **Step 8**: you can navigate between pages with action parameters.
- **Step 9**: you can render and download a document from a template.
- **Step 10**: you can diagnose errors using logs/devtools and republish.
- **Step 11**: you can deliver a small feature with roles/permissions and one integration.

### Feedback loop

- After **First win** and **Capstone**, capture feedback: what was unclear, where errors appeared, and which links/videos helped most; feed this back into docs.

### Assessment rubric (Capstone)

- [ ] CRUD works with validation and clear user messages.
- [ ] External API call mapped; failures handled (timeouts/4xx/5xx).
- [ ] Document template rendered; file is downloadable.
- [ ] Navigation via action parameters opens the right record/page.
- [ ] At least **2 roles** configured with different access.
- [ ] All components **Published** with no blocking warnings.

---

## 2) Step‑by‑step learning path (single track)

A unified path for all roles. Follow the steps in order; each step links to docs and (optionally) a short video.

**Step 1 — Access Aqtra (cloud or Docker)**
Get a running instance (see Section 4). Verify you can open **Studio** and **Workplace**.

**Step 2 — First application skeleton**
Create a minimal **DataModel** (e.g., `Invoice(number, title, totalAmount, dueDate)`) and a **Component** to display/edit it. Publish and add to navigation so it appears in Workplace.

**Docs**: Component → [https://docs.aqtra.io/en/app-develop/component.html](https://docs.aqtra.io/en/app-develop/component.html) ; UI catalog → [https://docs.aqtra.io/en/app-develop/ui-components/index.html](https://docs.aqtra.io/en/app-develop/ui-components/index.html)
**Video**: Tutorial #1 → [https://youtu.be/GaUr5ET4dfQ](https://youtu.be/GaUr5ET4dfQ) ; Tutorial #2 → [https://youtu.be/UEG2pmct74s](https://youtu.be/UEG2pmct74s)

**Step 3 — DataFlow basics**
Add a **DataFlow** with stages/steps: `Get Action Model → Update Entry → Write Response`. Bind it to a **Button** and test create/update.

**Docs**: Dataflow overview → [https://docs.aqtra.io/en/app-develop/data-flow-components/index.html](https://docs.aqtra.io/en/app-develop/data-flow-components/index.html) ; Update entry → [https://docs.aqtra.io/en/app-develop/data-flow-components/update-entry.html](https://docs.aqtra.io/en/app-develop/data-flow-components/update-entry.html) ; Execute dataflow → [https://docs.aqtra.io/en/app-develop/data-flow-components/execute-dataflow.html](https://docs.aqtra.io/en/app-develop/data-flow-components/execute-dataflow.html)
**Video**: Tutorial #3 — ([05:16](https://youtu.be/UEG2pmct74s?t=316)–[07:30](https://youtu.be/UEG2pmct74s?t=450))

**Step 4 — CRUD completion**
Add list/detail views, finish create/update/delete flows, and validations.

**Docs**: Data Grid → [https://docs.aqtra.io/en/app-develop/ui-components/data-grid.html](https://docs.aqtra.io/en/app-develop/ui-components/data-grid.html)
**Video**: Tutorial #4 — delete via Update Entry ([05:18](https://youtu.be/oLoYMSAlLVo?t=318)–[06:20](https://youtu.be/oLoYMSAlLVo?t=380)); Tutorial #5 — dynamic filters ([00:13](https://youtu.be/YuU_YomoNaw?t=13)–[03:00](https://youtu.be/YuU_YomoNaw?t=180))

**Step 5 — Python scripting for business logic**
Insert a **Python Script** step to compute derived fields and validate inputs.

**Docs**: Execute script → [https://docs.aqtra.io/en/app-develop/data-flow-components/execute-script.html](https://docs.aqtra.io/en/app-develop/data-flow-components/execute-script.html)
**Video**: Tutorial #6 — Execute Script ([04:10](https://youtu.be/bOR2nOk_S0c?t=250)–[06:10](https://youtu.be/bOR2nOk_S0c?t=370))

**Step 6 — External integrations**
Call an external HTTP API from a Python script; map the response to your DataModel.

**Docs**: Execute API call → [https://docs.aqtra.io/en/app-develop/data-flow-components/execute-api-call.html](https://docs.aqtra.io/en/app-develop/data-flow-components/execute-api-call.html)
**Video**: (Optional) Tutorial #10 — diagnosing payload/type mismatches ([01:46](https://youtu.be/qJcpIQQEqbo?t=106)–[05:00](https://youtu.be/qJcpIQQEqbo?t=300))

!!! tip "Troubleshooting"
_ **Timeout/5xx**: verify URL/method/headers; add retry/backoff; log response body.
_ **401/403**: supply/refresh auth token (store secrets securely).
_ **406/422 (type mismatch)**: fix field mapping and types; transform in **Execute Script** (e.g., string → number/date) before `Update Entry`.
_ Use `context.Logger` to log correlation IDs and payload snippets.

**Step 7 — MultiComponent pages**
Compose a page from several components (filters + grid + form). Configure **data context** and wiring.

**Docs**: List View → [https://docs.aqtra.io/en/app-develop/ui-components/list-view.html](https://docs.aqtra.io/en/app-develop/ui-components/list-view.html) ; Tab Control → [https://docs.aqtra.io/en/app-develop/ui-components/tab-control.html](https://docs.aqtra.io/en/app-develop/ui-components/tab-control.html) ; Charts → [https://docs.aqtra.io/en/app-develop/ui-components/charts.html](https://docs.aqtra.io/en/app-develop/ui-components/charts.html)
**Video**: Tutorial #6 — modal dialog + auto‑refresh grid ([10:45](https://youtu.be/bOR2nOk_S0c?t=645)–[17:00](https://youtu.be/bOR2nOk_S0c?t=1020)); Tutorial #7 — List View ([00:59](https://youtu.be/PtAJwn07sWI?t=59)–[03:00](https://youtu.be/PtAJwn07sWI?t=180))

> **Design tip (optional)**: group related inputs into panels, keep vertical rhythm consistent (8–12px multiples), avoid overusing charts—add them only when they clarify trends.

**Step 8 — Navigation & cross‑page wiring**
Add menu items and open pages with **action parameters** (pass record `id` from grid to form).

**Docs**: Button actions → [https://docs.aqtra.io/en/app-develop/ui-components/button.html](https://docs.aqtra.io/en/app-develop/ui-components/button.html)
**Video**: Tutorial #12 — open page + parameter mapping ([06:18](https://youtu.be/k36-qpZa9bU?t=378)–[07:00](https://youtu.be/k36-qpZa9bU?t=420)); Tutorial #5 — Open application from grid ([10:53](https://youtu.be/YuU_YomoNaw?t=653)–[11:20](https://youtu.be/YuU_YomoNaw?t=680))

**Step 9 — Templates & document generation (PDF)**
Render and download a document from a template via DataFlow.

**Docs**: Dataflow components (Render Template) → [https://docs.aqtra.io/en/app-develop/data-flow-components/index.html](https://docs.aqtra.io/en/app-develop/data-flow-components/index.html)
**Video**: Tutorial #12 — template render + download ([01:37](https://youtu.be/k36-qpZa9bU?t=97)–[02:45](https://youtu.be/k36-qpZa9bU?t=165); [05:20](https://youtu.be/k36-qpZa9bU?t=320)–[07:00](https://youtu.be/k36-qpZa9bU?t=420))

**Step 10 — Error handling & debugging**
Use Network tab and Studio logs to diagnose 4xx/5xx; fix types; republish.

**Docs**: Publishing applications → [https://docs.aqtra.io/en/app-develop/publishing-applications.html](https://docs.aqtra.io/en/app-develop/publishing-applications.html)
**Video**: Tutorial #10 — finding and fixing errors ([01:46](https://youtu.be/qJcpIQQEqbo?t=106)–[05:00](https://youtu.be/qJcpIQQEqbo?t=300))

!!! tip "Troubleshooting"

- Follow the sequence: **Compile → Save → Ready to publish → Publish**; verify the component is listed as _Published_.
- Use browser devtools **Network** to compare request/response to expected schema; correct mapping/types.
  _ If behavior differs between pages, check that **all dependent components** were republished together.
  _ On Docker setups, inspect container logs for stack traces and port conflicts.

**Step 11 — Capstone**
Extend your app into a small feature (e.g., Mini‑CRM): roles/permissions, MultiComponent dashboard, one integration, one document template. Document acceptance criteria and make a short demo video.

[Back to top](#getting-started)

---

## 3) Tutorials & Documentation Cross-Links {: #tutorials-documentation-cross-links }

**Install / Platform**

- Basic settings, auth, logs, metrics → [https://docs.aqtra.io/en/install1/basic-settings.html](https://docs.aqtra.io/en/install1/basic-settings.html)

**Core build**

- Component (creating, basic settings) → [https://docs.aqtra.io/en/app-develop/component.html](https://docs.aqtra.io/en/app-develop/component.html)
- UI components catalog (first mention) → [https://docs.aqtra.io/en/app-develop/ui-components/index.html](https://docs.aqtra.io/en/app-develop/ui-components/index.html)
- Data Grid (first mention) → [https://docs.aqtra.io/en/app-develop/ui-components/data-grid.html](https://docs.aqtra.io/en/app-develop/ui-components/data-grid.html)
- List View / Tab Control / Charts (first mention) → [https://docs.aqtra.io/en/app-develop/ui-components/list-view.html](https://docs.aqtra.io/en/app-develop/ui-components/list-view.html), [https://docs.aqtra.io/en/app-develop/ui-components/tab-control.html](https://docs.aqtra.io/en/app-develop/ui-components/tab-control.html), [https://docs.aqtra.io/en/app-develop/ui-components/charts.html](https://docs.aqtra.io/en/app-develop/ui-components/charts.html)

**Flows / Logic**

- Dataflow overview → [https://docs.aqtra.io/en/app-develop/data-flow-components/index.html](https://docs.aqtra.io/en/app-develop/data-flow-components/index.html)
- Update Entry (CRUD) → [https://docs.aqtra.io/en/app-develop/data-flow-components/update-entry.html](https://docs.aqtra.io/en/app-develop/data-flow-components/update-entry.html)
- Execute dataflow → [https://docs.aqtra.io/en/app-develop/data-flow-components/execute-dataflow.html](https://docs.aqtra.io/en/app-develop/data-flow-components/execute-dataflow.html)
- Execute script (Python) → [https://docs.aqtra.io/en/app-develop/data-flow-components/execute-script.html](https://docs.aqtra.io/en/app-develop/data-flow-components/execute-script.html)
- Execute API call → [https://docs.aqtra.io/en/app-develop/data-flow-components/execute-api-call.html](https://docs.aqtra.io/en/app-develop/data-flow-components/execute-api-call.html)

**Publishing**

- Publishing applications → [https://docs.aqtra.io/en/app-develop/publishing-applications.html](https://docs.aqtra.io/en/app-develop/publishing-applications.html)

**Tutorials (docs)**

- Tutorial #1 → [https://docs.aqtra.io/en/tutorials/tutorial1.html](https://docs.aqtra.io/en/tutorials/tutorial1.html)
- Tutorial #2 → [https://docs.aqtra.io/en/tutorials/tutorial2.html](https://docs.aqtra.io/en/tutorials/tutorial2.html)
- Tutorial #3 → [https://docs.aqtra.io/en/tutorials/tutorial3.html](https://docs.aqtra.io/en/tutorials/tutorial3.html)

**Video index (clickable timestamps)**

- T#3 — DataFlow basics ([05:16](https://youtu.be/UEG2pmct74s?t=316)–[07:30](https://youtu.be/UEG2pmct74s?t=450)).
- T#4 — Delete via Update Entry ([05:18](https://youtu.be/oLoYMSAlLVo?t=318)–[06:20](https://youtu.be/oLoYMSAlLVo?t=380)).
- T#5 — Data Grid filters; Open application ([00:13](https://youtu.be/YuU_YomoNaw?t=13)–[03:00](https://youtu.be/YuU_YomoNaw?t=180)), ([10:53](https://youtu.be/YuU_YomoNaw?t=653)–[11:20](https://youtu.be/YuU_YomoNaw?t=680)).
- T#6 — Execute Script; modal dialog; auto‑refresh grid ([04:10](https://youtu.be/bOR2nOk_S0c?t=250)–[06:10](https://youtu.be/bOR2nOk_S0c?t=370)), ([10:45](https://youtu.be/bOR2nOk_S0c?t=645)–[17:00](https://youtu.be/bOR2nOk_S0c?t=1020)).
- T#10 — Debug 500→406; fix types; republish ([01:46](https://youtu.be/qJcpIQQEqbo?t=106)–[05:00](https://youtu.be/qJcpIQQEqbo?t=300)).
- T#12 — Render template; Download; Open page + mapping ([01:37](https://youtu.be/k36-qpZa9bU?t=97)–[02:45](https://youtu.be/k36-qpZa9bU?t=165)), ([06:18](https://youtu.be/k36-qpZa9bU?t=378)–[07:00](https://youtu.be/k36-qpZa9bU?t=420)).

---

## 4) First win in ~60 minutes

> Build the **Invoice Inventory** mini‑feature end‑to‑end.

1. **Access Aqtra** (cloud or Docker) and open **Studio**.
2. **Create DataModel** `Invoice(number, title, totalAmount, dueDate)`.
3. **Add a Component** to create/list invoices (first use of Data Grid).
4. **Wire a DataFlow** — `Get Action Model → Update Entry → Write Response` (optional **Execute Script** to validate totalAmount).
5. **Publish** and verify in **Workplace**: create two invoices, edit one.

**Docs**: Tutorials → Build your first app — [https://docs.aqtra.io/en/tutorials/index.html](https://docs.aqtra.io/en/tutorials/index.html)

---

## 5) Install & Access {: #5-install--access }

Choose one of the following. Keep credentials and license keys secure.

### Option 1 — Cloud (Hosted)

- Obtain access via a hosting partner or purchase directly.
- Pricing & procurement: [https://aqtra.io/#price](https://aqtra.io/#price).
- Receive an organization/tenant URL and credentials.
- Configure SSO (optional), users, and roles.

### Option 2 — Local (Docker)

**Prerequisites**: Docker Engine/Compose latest; Linux/Windows/macOS host with **4 vCPU / 8 GB RAM** minimum.

**Checklist**

- [ ] Install Docker/Compose and verify `docker ps` works.
- [ ] Prepare `docker-compose.yml` and `.env` with required secrets.
- [ ] Start DB → `docker compose up -d db` and wait for readiness.
- [ ] Start app → `docker compose up -d app`.
- [ ] Access **Workplace** at `http://<host>:8080/` and **Studio** at `http://<host>:8080/studio/`.

**Docs**: Basic settings (architecture, ports, auth, logs, metrics) → [https://docs.aqtra.io/en/install1/basic-settings.html](https://docs.aqtra.io/en/install1/basic-settings.html)

[Back to top](#getting-started)

---

## 6) Core Concepts (Aqtra Glossary)

Short, actionable definitions.

- **Component** — a UI building block that renders data and actions for users (form, list, detail, etc.). [https://docs.aqtra.io/en/app-develop/component.html](https://docs.aqtra.io/en/app-develop/component.html)
- **DataFlow** — a directed flow of operations (e.g., validate → transform → persist → notify) that executes on user or system events. Typical steps: **Get Action Model**, **Update Entry**, **Write Response**, **Execute Script**, **Execute API call**. [https://docs.aqtra.io/en/app-develop/data-flow-components/index.html](https://docs.aqtra.io/en/app-develop/data-flow-components/index.html)
- **DataModel** — the structured definition of entities/attributes that the application persists and manipulates.
- **MultiComponent** — a composite view assembling several Components (e.g., list + details + filters) into a cohesive page; elements use **data context** to bind to a source component.
- **Python Script** — custom logic step embedded in a flow to transform data, call services, or implement rules. [https://docs.aqtra.io/en/app-develop/data-flow-components/execute-script.html](https://docs.aqtra.io/en/app-develop/data-flow-components/execute-script.html)

---

## 7) Video Track (with transcripts & timecodes) {: #7-video-track-with-transcripts--timecodes }

Centralized video list with deep links and timestamps. Use these to jump directly to the relevant demo moments.

- **Tutorial #1** — [https://youtu.be/GaUr5ET4dfQ](https://youtu.be/GaUr5ET4dfQ)
- **Tutorial #2** — [https://youtu.be/UEG2pmct74s](https://youtu.be/UEG2pmct74s)
- **Tutorial #3** — DataFlow basics ([05:16](https://youtu.be/UEG2pmct74s?t=316)–[07:30](https://youtu.be/UEG2pmct74s?t=450))
- **Tutorial #4** — Delete via Update Entry ([05:18](https://youtu.be/oLoYMSAlLVo?t=318)–[06:20](https://youtu.be/oLoYMSAlLVo?t=380))
- **Tutorial #5** — Data Grid filters; Open application ([00:13](https://youtu.be/YuU_YomoNaw?t=13)–[03:00](https://youtu.be/YuU_YomoNaw?t=180)), ([10:53](https://youtu.be/YuU_YomoNaw?t=653)–[11:20](https://youtu.be/YuU_YomoNaw?t=680))
- **Tutorial #6** — Execute Script; modal dialog; auto‑refresh grid ([04:10](https://youtu.be/bOR2nOk_S0c?t=250)–[06:10](https://youtu.be/bOR2nOk_S0c?t=370)), ([10:45](https://youtu.be/bOR2nOk_S0c?t=645)–[17:00](https://youtu.be/bOR2nOk_S0c?t=1020))
- **Tutorial #7** — [https://youtu.be/PtAJwn07sWI](https://youtu.be/PtAJwn07sWI)
- **Tutorial #8** — [https://youtu.be/YfqfdJpDm-k](https://youtu.be/YfqfdJpDm-k)
- **Tutorial #9/10** — Debug & diagnostics ([01:46](https://youtu.be/qJcpIQQEqbo?t=106)–[05:00](https://youtu.be/qJcpIQQEqbo?t=300))
- **Tutorial #11** — [https://youtu.be/d-FD1ARn0h0](https://youtu.be/d-FD1ARn0h0)
- **Tutorial #12** — Render template; Download; Open page + mapping ([01:37](https://youtu.be/k36-qpZa9bU?t=97)–[02:45](https://youtu.be/k36-qpZa9bU?t=165)), ([06:18](https://youtu.be/k36-qpZa9bU?t=378)–[07:00](https://youtu.be/k36-qpZa9bU?t=420))

!!! note "Stay updated"
Subscribe to **Aqtra Academy** on YouTube and check the docs root regularly for updates. New episodes will be linked here as they arrive.

[Back to top](#getting-started)

---

## 8) DataFlow Step Library (quick reference)

A few useful steps you'll likely use beyond CRUD:

- **Update Entry** — [https://docs.aqtra.io/en/app-develop/data-flow-components/update-entry.html](https://docs.aqtra.io/en/app-develop/data-flow-components/update-entry.html)
- **Execute dataflow** — call another dataflow and merge results.
  [https://docs.aqtra.io/en/app-develop/data-flow-components/execute-dataflow.html](https://docs.aqtra.io/en/app-develop/data-flow-components/execute-dataflow.html)
- **Execute API call** — configure and run HTTP request, bind results.
  [https://docs.aqtra.io/en/app-develop/data-flow-components/execute-api-call.html](https://docs.aqtra.io/en/app-develop/data-flow-components/execute-api-call.html)
- **Get entity by id** — fetch entity by identifier via catalog field.
  [https://docs.aqtra.io/en/app-develop/data-flow-components/get-entity-by-id.html](https://docs.aqtra.io/en/app-develop/data-flow-components/get-entity-by-id.html)
- **Update model field** — set/derive a single field within model.
  [https://docs.aqtra.io/en/workflow-components/update-model-field.html](https://docs.aqtra.io/en/workflow-components/update-model-field.html)
- **Simple math** — add/subtract/multiply and write to a target field.
  [https://docs.aqtra.io/en/app-develop/data-flow-components/simple-math.html](https://docs.aqtra.io/en/app-develop/data-flow-components/simple-math.html)
- **Store entry over bus** — create/store component instance asynchronously.
  [https://docs.aqtra.io/en/app-develop/data-flow-components/store-entry-over-bus.html](https://docs.aqtra.io/en/app-develop/data-flow-components/store-entry-over-bus.html)
- **Subscribe to connector** — e.g., RabbitMQ subscription → process → save.
  [https://docs.aqtra.io/en/app-develop/data-flow-components/subscribe-to-connector.html](https://docs.aqtra.io/en/app-develop/data-flow-components/subscribe-to-connector.html)

[Back to top](#getting-started)

---

## 9) FAQ (short, practical)

**Q: Cloud vs local?**
A: Cloud for fastest onboarding/team access; local Docker for offline/PoCs/restricted environments.

**Q: Docker fails to start or is slow.**
A: Ensure 4 vCPU/8 GB RAM+, free the target ports, and check container logs. Restart Docker and retry compose.

**Q: Where to put custom logic?**
A: Add a **Python Script** step inside a **DataFlow** to validate, transform, or call external APIs.

**Q: How to call external services?**
A: Use `http.client` from a Python script; map the response to your DataModel.

**Q: Main building blocks?**
A: **DataModel**, **Component**, **DataFlow**, **MultiComponent**, **Python Script**.

**Q: Errors and exceptions?**
A: Use network inspector and Studio logs; fix type mismatches, republish, and re‑test. See the video in Section 8.

**Q: How to purchase or get a trial?**
A: See pricing: [https://aqtra.io/#price](https://aqtra.io/#price). Purchase via vendor or directly; for hosted deployments, follow partner onboarding.

---

## 10) What's next

- Patterns & best practices (naming, versioning, testing flows).
- Advanced integrations (SSO, databases, message queues).
- Team workflows (code reviews for scripts, environment promotion).
- Community & support links (Slack/Telegram/Forum) — _add when available_.
