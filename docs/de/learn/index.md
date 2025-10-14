# Erste Schritte {: #getting-started }

> Ein strukturierter Einstiegspunkt für Neueinsteiger in Aqtra. Technischer Ton. Diese Seite verlinkt Dokumentation, Tutorials, Videos (mit Transkripten) und ein ausführbares Beispiel, um eine progressive Lernkarte zu bilden.

---

## Was ist Aqtra?

Aqtra ist eine **Low-Code-Plattform** zum Erstellen von Geschäftsanwendungen hauptsächlich über eine visuelle Benutzeroberfläche, mit optionalem **Python-Skripting** für erweiterte Logik. Dieses Hybridmodell beschleunigt die Bereitstellung für Anfänger und ermöglicht es Entwicklern, bei Bedarf zu erweitern und anzupassen.

**Sie werden lernen:**

- Aqtra zu installieren und auszuführen (Cloud oder lokal über Docker).
- Eine erste Funktion von Ende zu Ende zu erstellen (Datenmodell → UI-Komponente → Datenfluss → veröffentlichen).
- Python-Skripte zu verwenden, wo dies angemessen ist.
- Mit externen Diensten und APIs zu integrieren.

> **Zielgruppe:** Citizen Developers, Junior Front-/Back-End-Entwickler, Analysten, Architekten, Teamleiter.

**Primäre CTAs:**

- **Start in 60 Minuten →** Erste Feature-Walkthrough (siehe [4) Erster Erfolg](#4-first-win-in-60-minutes))
- **Dokumentation →** [https://docs.aqtra.io/en/](https://docs.aqtra.io/en/)
- **Video-Track →** [https://www.youtube.com/@Aqtra.Academy](https://www.youtube.com/@Aqtra.Academy)

**Schnelllinks (Karten):**

- **Installation** → [5) Install & Access](#5-install--access) (Cloud / Docker)
- **Erstellen Sie Ihren ersten Bildschirm (Invoice)** → [4) Erster Erfolg](#4-first-win-in-60-minutes)
- **DataFlow-Grundlagen** → [2) Schritt-für-Schritt-Lernpfad](#2-stepbystep-learning-path-single-track)
- **Im Web veröffentlichen** → [2) Schritt-für-Schritt-Lernpfad](#2-stepbystep-learning-path-single-track)

**Auf dieser Seite**

- [1) Methodik — wie man diesen Leitfaden verwendet](#1-methodology--how-to-use-this-guide)
- [2) Schritt-für-Schritt-Lernpfad](#2-stepbystep-learning-path-single-track)
- [3) Tutorials & Dokumentations-Cross-Links](#3-tutorials-documentation-cross-links)
- [4) Erster Erfolg in ~60 Minuten](#4-first-win-in-60-minutes)
- [5) Installation & Zugang](#5-install--access)
- [6) Kernkonzepte (Aqtra-Glossar)](#6-core-concepts-aqtra-glossary)
- [7) Video-Track](#7-video-track-with-transcripts--timecodes)
- [8) DataFlow Step Library](#8-dataflow-step-library-quick-reference)
- [9) FAQ](#9-faq-short-practical)

---

## 1) Methodik — wie man diesen Leitfaden verwendet {: #1-methodology--how-to-use-this-guide }

- **Single-Track-Progression**: ein einheitlicher Pfad für alle Rollen, minimale neue Konzepte pro Schritt.
- **First-Mention-Linking**: jedes Konzept/UI-Element wird beim ersten Auftreten einmal verlinkt; spätere Schritte setzen es voraus.
- **Just-in-Time-Tiefe**: jeder Schritt verweist auf fokussierte Dokumente und ein kurzes Video mit anklickbaren Zeitstempeln.
- **Sichtbare Ergebnisse**: jeder Schritt endet mit einem konkreten, testbaren Ergebnis im Workplace.
- **Error-First-Mindset**: Schritt 10 lehrt systematisches Debugging/Log-Analyse.
- **Bewertung**: das **Capstone** (Schritt 11) validiert CRUD, Integration, Templating, Navigation und Rollen/Berechtigungen.

### Umfang & Voraussetzungen

- Zugriff auf **Aqtra Studio/Workplace** (Cloud-Tenant) _oder_ ein lokales **Docker**-Setup (≥ 4 vCPU / 8 GB RAM).
- Moderner Browser und die Fähigkeit, Devtools **Network**-Tab anzuzeigen.
- (Optional) Grundkenntnisse mit JSON und HTTP-APIs für Schritt 6.

### Lernergebnisse (pro Schritt)

- **Schritt 1**: Sie können auf Studio/Workplace zugreifen.
- **Schritt 2**: Sie können eine Entität (Invoice) modellieren und in einer Komponente sichtbar im Workplace darstellen.
- **Schritt 3**: Sie können einen DataFlow erstellen und ihn an einen Button binden.
- **Schritt 4**: Sie können CRUD und grundlegende Validierung abschließen.
- **Schritt 5**: Sie können Python-Logik in einen Flow hinzufügen.
- **Schritt 6**: Sie können eine externe HTTP-API aufrufen und Ergebnisse zuordnen.
- **Schritt 7**: Sie können eine MultiComponent-Seite mit Datenkontext erstellen.
- **Schritt 8**: Sie können zwischen Seiten mit Aktionsparametern navigieren.
- **Schritt 9**: Sie können ein Dokument aus einer Vorlage rendern und herunterladen.
- **Schritt 10**: Sie können Fehler mit Logs/Devtools diagnostizieren und neu veröffentlichen.
- **Schritt 11**: Sie können eine kleine Funktion mit Rollen/Berechtigungen und einer Integration bereitstellen.

### Feedback-Schleife

- Nach **Erstem Erfolg** und **Capstone**, sammeln Sie Feedback: was unklar war, wo Fehler auftraten und welche Links/Videos am meisten geholfen haben; speisen Sie dies zurück in die Dokumentation.

### Bewertungsrubrik (Capstone)

- [ ] CRUD funktioniert mit Validierung und klaren Benutzernachrichten.
- [ ] Externer API-Aufruf zugeordnet; Fehler behandelt (Timeouts/4xx/5xx).
- [ ] Dokumentenvorlage gerendert; Datei ist herunterladbar.
- [ ] Navigation über Aktionsparameter öffnet den richtigen Datensatz/die richtige Seite.
- [ ] Mindestens **2 Rollen** konfiguriert mit unterschiedlichem Zugriff.
- [ ] Alle Komponenten **veröffentlicht** ohne blockierende Warnungen.

---

## 2) Schritt-für-Schritt-Lernpfad (Single Track) {: #2-stepbystep-learning-path-single-track }

Ein einheitlicher Pfad für alle Rollen. Folgen Sie den Schritten in der Reihenfolge; jeder Schritt verlinkt auf Dokumente und (optional) ein kurzes Video.

**Schritt 1 — Zugriff auf Aqtra (Cloud oder Docker)**
Erhalten Sie eine laufende Instanz (siehe Abschnitt 4). Überprüfen Sie, ob Sie **Studio** und **Workplace** öffnen können.

**Schritt 2 — Erstes Anwendungsskelett**
Erstellen Sie ein minimales **DataModel** (z.B. `Invoice(number, title, totalAmount, dueDate)`) und eine **Komponente** zum Anzeigen/Bearbeiten. Veröffentlichen und zur Navigation hinzufügen, damit es im Workplace erscheint.

**Docs**: Component → [https://docs.aqtra.io/en/app-develop/component.html](https://docs.aqtra.io/en/app-develop/component.html) ; UI catalog → [https://docs.aqtra.io/en/app-develop/ui-components/index.html](https://docs.aqtra.io/en/app-develop/ui-components/index.html)
**Video**: Tutorial #1 → [https://youtu.be/GaUr5ET4dfQ](https://youtu.be/GaUr5ET4dfQ) ; Tutorial #2 → [https://youtu.be/UEG2pmct74s](https://youtu.be/UEG2pmct74s)

**Schritt 3 — DataFlow-Grundlagen**
Fügen Sie einen **DataFlow** mit Phasen/Schritten hinzu: `Get Action Model → Update Entry → Write Response`. Binden Sie ihn an einen **Button** und testen Sie create/update.

**Docs**: Dataflow overview → [https://docs.aqtra.io/en/app-develop/data-flow-components/index.html](https://docs.aqtra.io/en/app-develop/data-flow-components/index.html) ; Update entry → [https://docs.aqtra.io/en/app-develop/data-flow-components/update-entry.html](https://docs.aqtra.io/en/app-develop/data-flow-components/update-entry.html) ; Execute dataflow → [https://docs.aqtra.io/en/app-develop/data-flow-components/execute-dataflow.html](https://docs.aqtra.io/en/app-develop/data-flow-components/execute-dataflow.html)
**Video**: Tutorial #3 — ([05:16](https://youtu.be/UEG2pmct74s?t=316)–[07:30](https://youtu.be/UEG2pmct74s?t=450))

**Schritt 4 — CRUD-Vervollständigung**
Fügen Sie Listen-/Detailansichten hinzu, schließen Sie Create/Update/Delete-Flows und Validierungen ab.

**Docs**: Data Grid → [https://docs.aqtra.io/en/app-develop/ui-components/data-grid.html](https://docs.aqtra.io/en/app-develop/ui-components/data-grid.html)
**Video**: Tutorial #4 — delete via Update Entry ([05:18](https://youtu.be/oLoYMSAlLVo?t=318)–[06:20](https://youtu.be/oLoYMSAlLVo?t=380)); Tutorial #5 — dynamic filters ([00:13](https://youtu.be/YuU_YomoNaw?t=13)–[03:00](https://youtu.be/YuU_YomoNaw?t=180))

**Schritt 5 — Python-Skripting für Geschäftslogik**
Fügen Sie einen **Python Script**-Schritt ein, um abgeleitete Felder zu berechnen und Eingaben zu validieren.

**Docs**: Execute script → [https://docs.aqtra.io/en/app-develop/data-flow-components/execute-script.html](https://docs.aqtra.io/en/app-develop/data-flow-components/execute-script.html)
**Video**: Tutorial #6 — Execute Script ([04:10](https://youtu.be/bOR2nOk_S0c?t=250)–[06:10](https://youtu.be/bOR2nOk_S0c?t=370))

**Schritt 6 — Externe Integrationen**
Rufen Sie eine externe HTTP-API von einem Python-Skript aus auf; ordnen Sie die Antwort Ihrem DataModel zu.

**Docs**: Execute API call → [https://docs.aqtra.io/en/app-develop/data-flow-components/execute-api-call.html](https://docs.aqtra.io/en/app-develop/data-flow-components/execute-api-call.html)
**Video**: (Optional) Tutorial #10 — diagnosing payload/type mismatches ([01:46](https://youtu.be/qJcpIQQEqbo?t=106)–[05:00](https://youtu.be/qJcpIQQEqbo?t=300))

!!! tip "Fehlerbehebung"
    - **Timeout/5xx**: URL/Methode/Header überprüfen; Wiederholung/Backoff hinzufügen; Antwortkörper protokollieren.
    - **401/403**: Auth-Token bereitstellen/aktualisieren (Secrets sicher speichern).
    - **406/422 (Typ-Mismatch)**: Feldzuordnung und Typen korrigieren; in **Execute Script** transformieren (z.B. string → number/date) vor `Update Entry`.
    - Verwenden Sie `context.Logger`, um Korrelations-IDs und Payload-Snippets zu protokollieren.

**Schritt 7 — MultiComponent-Seiten**
Erstellen Sie eine Seite aus mehreren Komponenten (Filter + Grid + Formular). Konfigurieren Sie **Datenkontext** und Verdrahtung.

**Docs**: List View → [https://docs.aqtra.io/en/app-develop/ui-components/list-view.html](https://docs.aqtra.io/en/app-develop/ui-components/list-view.html) ; Tab Control → [https://docs.aqtra.io/en/app-develop/ui-components/tab-control.html](https://docs.aqtra.io/en/app-develop/ui-components/tab-control.html) ; Charts → [https://docs.aqtra.io/en/app-develop/ui-components/charts.html](https://docs.aqtra.io/en/app-develop/ui-components/charts.html)
**Video**: Tutorial #6 — modal dialog + auto‑refresh grid ([10:45](https://youtu.be/bOR2nOk_S0c?t=645)–[17:00](https://youtu.be/bOR2nOk_S0c?t=1020)); Tutorial #7 — List View ([00:59](https://youtu.be/PtAJwn07sWI?t=59)–[03:00](https://youtu.be/PtAJwn07sWI?t=180))

> **Design-Tipp (optional)**: Gruppieren Sie zusammenhängende Eingaben in Panels, halten Sie den vertikalen Rhythmus konsistent (8–12px Vielfache), vermeiden Sie übermäßige Verwendung von Diagrammen—fügen Sie sie nur hinzu, wenn sie Trends verdeutlichen.

**Schritt 8 — Navigation & seitenübergreifende Verdrahtung**
Fügen Sie Menüpunkte hinzu und öffnen Sie Seiten mit **Aktionsparametern** (übergeben Sie Datensatz `id` vom Grid zum Formular).

**Docs**: Button actions → [https://docs.aqtra.io/en/app-develop/ui-components/button.html](https://docs.aqtra.io/en/app-develop/ui-components/button.html)
**Video**: Tutorial #12 — open page + parameter mapping ([06:18](https://youtu.be/k36-qpZa9bU?t=378)–[07:00](https://youtu.be/k36-qpZa9bU?t=420)); Tutorial #5 — Open application from grid ([10:53](https://youtu.be/YuU_YomoNaw?t=653)–[11:20](https://youtu.be/YuU_YomoNaw?t=680))

**Schritt 9 — Vorlagen & Dokumentengenerierung (PDF)**
Rendern und laden Sie ein Dokument aus einer Vorlage über DataFlow herunter.

**Docs**: Dataflow components (Render Template) → [https://docs.aqtra.io/en/app-develop/data-flow-components/index.html](https://docs.aqtra.io/en/app-develop/data-flow-components/index.html)
**Video**: Tutorial #12 — template render + download ([01:37](https://youtu.be/k36-qpZa9bU?t=97)–[02:45](https://youtu.be/k36-qpZa9bU?t=165); [05:20](https://youtu.be/k36-qpZa9bU?t=320)–[07:00](https://youtu.be/k36-qpZa9bU?t=420))

**Schritt 10 — Fehlerbehandlung & Debugging**
Verwenden Sie den Network-Tab und Studio-Logs, um 4xx/5xx zu diagnostizieren; Typen korrigieren; neu veröffentlichen.

**Docs**: Publishing applications → [https://docs.aqtra.io/en/app-develop/publishing-applications.html](https://docs.aqtra.io/en/app-develop/publishing-applications.html)
**Video**: Tutorial #10 — finding and fixing errors ([01:46](https://youtu.be/qJcpIQQEqbo?t=106)–[05:00](https://youtu.be/qJcpIQQEqbo?t=300))

!!! tip "Fehlerbehebung"

    - Folgen Sie der Reihenfolge: **Compile → Save → Ready to publish → Publish**; überprüfen Sie, ob die Komponente als _Published_ aufgeführt ist.
    - Verwenden Sie Browser-Devtools **Network**, um Request/Response mit erwartetem Schema zu vergleichen; Zuordnung/Typen korrigieren.
    - Wenn das Verhalten zwischen Seiten unterschiedlich ist, überprüfen Sie, ob **alle abhängigen Komponenten** zusammen neu veröffentlicht wurden.
    - Bei Docker-Setups inspizieren Sie Container-Logs auf Stack-Traces und Port-Konflikte.

**Schritt 11 — Capstone**
Erweitern Sie Ihre App zu einer kleinen Funktion (z.B. Mini-CRM): Rollen/Berechtigungen, MultiComponent-Dashboard, eine Integration, eine Dokumentenvorlage. Dokumentieren Sie Akzeptanzkriterien und erstellen Sie ein kurzes Demo-Video.

[Zurück nach oben](#getting-started)

---

## 3) Tutorials & Dokumentations-Cross-Links {: #3-tutorials-documentation-cross-links }

**Installation / Plattform**

- Grundeinstellungen, Auth, Logs, Metriken → [https://docs.aqtra.io/en/install1/basic-settings.html](https://docs.aqtra.io/en/install1/basic-settings.html)

**Kern-Build**

- Component (Erstellen, Grundeinstellungen) → [https://docs.aqtra.io/en/app-develop/component.html](https://docs.aqtra.io/en/app-develop/component.html)
- UI-Komponentenkatalog (erste Erwähnung) → [https://docs.aqtra.io/en/app-develop/ui-components/index.html](https://docs.aqtra.io/en/app-develop/ui-components/index.html)
- Data Grid (erste Erwähnung) → [https://docs.aqtra.io/en/app-develop/ui-components/data-grid.html](https://docs.aqtra.io/en/app-develop/ui-components/data-grid.html)
- List View / Tab Control / Charts (erste Erwähnung) → [https://docs.aqtra.io/en/app-develop/ui-components/list-view.html](https://docs.aqtra.io/en/app-develop/ui-components/list-view.html), [https://docs.aqtra.io/en/app-develop/ui-components/tab-control.html](https://docs.aqtra.io/en/app-develop/ui-components/tab-control.html), [https://docs.aqtra.io/en/app-develop/ui-components/charts.html](https://docs.aqtra.io/en/app-develop/ui-components/charts.html)

**Flows / Logik**

- Dataflow overview → [https://docs.aqtra.io/en/app-develop/data-flow-components/index.html](https://docs.aqtra.io/en/app-develop/data-flow-components/index.html)
- Update Entry (CRUD) → [https://docs.aqtra.io/en/app-develop/data-flow-components/update-entry.html](https://docs.aqtra.io/en/app-develop/data-flow-components/update-entry.html)
- Execute dataflow → [https://docs.aqtra.io/en/app-develop/data-flow-components/execute-dataflow.html](https://docs.aqtra.io/en/app-develop/data-flow-components/execute-dataflow.html)
- Execute script (Python) → [https://docs.aqtra.io/en/app-develop/data-flow-components/execute-script.html](https://docs.aqtra.io/en/app-develop/data-flow-components/execute-script.html)
- Execute API call → [https://docs.aqtra.io/en/app-develop/data-flow-components/execute-api-call.html](https://docs.aqtra.io/en/app-develop/data-flow-components/execute-api-call.html)

**Veröffentlichung**

- Publishing applications → [https://docs.aqtra.io/en/app-develop/publishing-applications.html](https://docs.aqtra.io/en/app-develop/publishing-applications.html)

**Tutorials (Dokumente)**

- Tutorial #1 → [https://docs.aqtra.io/en/tutorials/tutorial1.html](https://docs.aqtra.io/en/tutorials/tutorial1.html)
- Tutorial #2 → [https://docs.aqtra.io/en/tutorials/tutorial2.html](https://docs.aqtra.io/en/tutorials/tutorial2.html)
- Tutorial #3 → [https://docs.aqtra.io/en/tutorials/tutorial3.html](https://docs.aqtra.io/en/tutorials/tutorial3.html)

**Video-Index (anklickbare Zeitstempel)**

- T#3 — DataFlow-Grundlagen ([05:16](https://youtu.be/UEG2pmct74s?t=316)–[07:30](https://youtu.be/UEG2pmct74s?t=450)).
- T#4 — Löschen über Update Entry ([05:18](https://youtu.be/oLoYMSAlLVo?t=318)–[06:20](https://youtu.be/oLoYMSAlLVo?t=380)).
- T#5 — Data Grid-Filter; Anwendung öffnen ([00:13](https://youtu.be/YuU_YomoNaw?t=13)–[03:00](https://youtu.be/YuU_YomoNaw?t=180)), ([10:53](https://youtu.be/YuU_YomoNaw?t=653)–[11:20](https://youtu.be/YuU_YomoNaw?t=680)).
- T#6 — Execute Script; modaler Dialog; Auto-Refresh-Grid ([04:10](https://youtu.be/bOR2nOk_S0c?t=250)–[06:10](https://youtu.be/bOR2nOk_S0c?t=370)), ([10:45](https://youtu.be/bOR2nOk_S0c?t=645)–[17:00](https://youtu.be/bOR2nOk_S0c?t=1020)).
- T#10 — Debug 500→406; Typen korrigieren; neu veröffentlichen ([01:46](https://youtu.be/qJcpIQQEqbo?t=106)–[05:00](https://youtu.be/qJcpIQQEqbo?t=300)).
- T#12 — Vorlage rendern; Herunterladen; Seite öffnen + Mapping ([01:37](https://youtu.be/k36-qpZa9bU?t=97)–[02:45](https://youtu.be/k36-qpZa9bU?t=165)), ([06:18](https://youtu.be/k36-qpZa9bU?t=378)–[07:00](https://youtu.be/k36-qpZa9bU?t=420)).

---

## 4) Erster Erfolg in ~60 Minuten {: #4-first-win-in-60-minutes }

> Erstellen Sie die **Invoice Inventory** Mini-Funktion von Ende zu Ende.

1. **Zugriff auf Aqtra** (Cloud oder Docker) und **Studio** öffnen.
2. **DataModel erstellen** `Invoice(number, title, totalAmount, dueDate)`.
3. **Komponente hinzufügen** zum Erstellen/Auflisten von Rechnungen (erste Verwendung von Data Grid).
4. **DataFlow verdrahten** — `Get Action Model → Update Entry → Write Response` (optional **Execute Script** zur Validierung von totalAmount).
5. **Veröffentlichen** und im **Workplace** überprüfen: zwei Rechnungen erstellen, eine bearbeiten.

**Docs**: Tutorials → Build your first app — [https://docs.aqtra.io/en/tutorials/index.html](https://docs.aqtra.io/en/tutorials/index.html)

---

## 5) Installation & Zugang {: #5-install--access }

Wählen Sie eine der folgenden Optionen. Bewahren Sie Anmeldedaten und Lizenzschlüssel sicher auf.

### Option 1 — Cloud (Hosted)

- Erhalten Sie Zugang über einen Hosting-Partner oder kaufen Sie direkt.
- Preise & Beschaffung: [https://aqtra.io/#price](https://aqtra.io/#price).
- Erhalten Sie eine Organisations-/Tenant-URL und Anmeldedaten.
- Konfigurieren Sie SSO (optional), Benutzer und Rollen.

### Option 2 — Lokal (Docker)

**Voraussetzungen**: Docker Engine/Compose neueste Version; Linux/Windows/macOS-Host mit **4 vCPU / 8 GB RAM** minimum.

**Checkliste**

- [ ] Docker/Compose installieren und `docker ps` funktioniert überprüfen.
- [ ] `docker-compose.yml` und `.env` mit erforderlichen Secrets vorbereiten.
- [ ] DB starten → `docker compose up -d db` und auf Bereitschaft warten.
- [ ] App starten → `docker compose up -d app`.
- [ ] **Workplace** unter `http://<host>:8080/` und **Studio** unter `http://<host>:8080/studio/` aufrufen.

**Docs**: Grundeinstellungen (Architektur, Ports, Auth, Logs, Metriken) → [https://docs.aqtra.io/en/install1/basic-settings.html](https://docs.aqtra.io/en/install1/basic-settings.html)

[Zurück nach oben](#getting-started)

---

## 6) Kernkonzepte (Aqtra-Glossar) {: #6-core-concepts-aqtra-glossary }

Kurze, umsetzbare Definitionen.

- **Component** — ein UI-Baustein, der Daten und Aktionen für Benutzer rendert (Formular, Liste, Detail usw.). [https://docs.aqtra.io/en/app-develop/component.html](https://docs.aqtra.io/en/app-develop/component.html)
- **DataFlow** — ein gerichteter Fluss von Operationen (z.B. validieren → transformieren → persistieren → benachrichtigen), der bei Benutzer- oder Systemereignissen ausgeführt wird. Typische Schritte: **Get Action Model**, **Update Entry**, **Write Response**, **Execute Script**, **Execute API call**. [https://docs.aqtra.io/en/app-develop/data-flow-components/index.html](https://docs.aqtra.io/en/app-develop/data-flow-components/index.html)
- **DataModel** — die strukturierte Definition von Entitäten/Attributen, die die Anwendung persistiert und manipuliert.
- **MultiComponent** — eine zusammengesetzte Ansicht, die mehrere Komponenten (z.B. Liste + Details + Filter) zu einer kohärenten Seite zusammenfügt; Elemente verwenden **Datenkontext**, um an eine Quellkomponente zu binden.
- **Python Script** — benutzerdefinierter Logikschritt, der in einen Flow eingebettet ist, um Daten zu transformieren, Dienste aufzurufen oder Regeln zu implementieren. [https://docs.aqtra.io/en/app-develop/data-flow-components/execute-script.html](https://docs.aqtra.io/en/app-develop/data-flow-components/execute-script.html)

---

## 7) Video-Track (mit Transkripten & Zeitcodes) {: #7-video-track-with-transcripts--timecodes }

Zentralisierte Videoliste mit Deep-Links und Zeitstempeln. Verwenden Sie diese, um direkt zu den relevanten Demo-Momenten zu springen.

- **Tutorial #1** — [https://youtu.be/GaUr5ET4dfQ](https://youtu.be/GaUr5ET4dfQ)
- **Tutorial #2** — [https://youtu.be/UEG2pmct74s](https://youtu.be/UEG2pmct74s)
- **Tutorial #3** — DataFlow-Grundlagen ([05:16](https://youtu.be/UEG2pmct74s?t=316)–[07:30](https://youtu.be/UEG2pmct74s?t=450))
- **Tutorial #4** — Löschen über Update Entry ([05:18](https://youtu.be/oLoYMSAlLVo?t=318)–[06:20](https://youtu.be/oLoYMSAlLVo?t=380))
- **Tutorial #5** — Data Grid-Filter; Anwendung öffnen ([00:13](https://youtu.be/YuU_YomoNaw?t=13)–[03:00](https://youtu.be/YuU_YomoNaw?t=180)), ([10:53](https://youtu.be/YuU_YomoNaw?t=653)–[11:20](https://youtu.be/YuU_YomoNaw?t=680))
- **Tutorial #6** — Execute Script; modaler Dialog; Auto-Refresh-Grid ([04:10](https://youtu.be/bOR2nOk_S0c?t=250)–[06:10](https://youtu.be/bOR2nOk_S0c?t=370)), ([10:45](https://youtu.be/bOR2nOk_S0c?t=645)–[17:00](https://youtu.be/bOR2nOk_S0c?t=1020))
- **Tutorial #7** — [https://youtu.be/PtAJwn07sWI](https://youtu.be/PtAJwn07sWI)
- **Tutorial #8** — [https://youtu.be/YfqfdJpDm-k](https://youtu.be/YfqfdJpDm-k)
- **Tutorial #9/10** — Debug & Diagnostics ([01:46](https://youtu.be/qJcpIQQEqbo?t=106)–[05:00](https://youtu.be/qJcpIQQEqbo?t=300))
- **Tutorial #11** — [https://youtu.be/d-FD1ARn0h0](https://youtu.be/d-FD1ARn0h0)
- **Tutorial #12** — Vorlage rendern; Herunterladen; Seite öffnen + Mapping ([01:37](https://youtu.be/k36-qpZa9bU?t=97)–[02:45](https://youtu.be/k36-qpZa9bU?t=165)), ([06:18](https://youtu.be/k36-qpZa9bU?t=378)–[07:00](https://youtu.be/k36-qpZa9bU?t=420))

!!! note "Auf dem Laufenden bleiben"
Abonnieren Sie **Aqtra Academy** auf YouTube und überprüfen Sie regelmäßig das Dokumentationsstammverzeichnis auf Updates. Neue Episoden werden hier verlinkt, sobald sie verfügbar sind.

[Zurück nach oben](#getting-started)

---

## 8) DataFlow Step Library (Kurzreferenz) {: #8-dataflow-step-library-quick-reference }

Ein paar nützliche Schritte, die Sie wahrscheinlich über CRUD hinaus verwenden werden:

- **Update Entry** — [https://docs.aqtra.io/en/app-develop/data-flow-components/update-entry.html](https://docs.aqtra.io/en/app-develop/data-flow-components/update-entry.html)
- **Execute dataflow** — rufen Sie einen anderen Dataflow auf und führen Sie Ergebnisse zusammen.
  [https://docs.aqtra.io/en/app-develop/data-flow-components/execute-dataflow.html](https://docs.aqtra.io/en/app-develop/data-flow-components/execute-dataflow.html)
- **Execute API call** — konfigurieren und führen Sie HTTP-Anfrage aus, binden Sie Ergebnisse.
  [https://docs.aqtra.io/en/app-develop/data-flow-components/execute-api-call.html](https://docs.aqtra.io/en/app-develop/data-flow-components/execute-api-call.html)
- **Get entity by id** — holen Sie Entität nach Kennung über Katalogfeld.
  [https://docs.aqtra.io/en/app-develop/data-flow-components/get-entity-by-id.html](https://docs.aqtra.io/en/app-develop/data-flow-components/get-entity-by-id.html)
- **Update model field** — setzen/leiten Sie ein einzelnes Feld innerhalb des Modells ab.
  [https://docs.aqtra.io/en/workflow-components/update-model-field.html](https://docs.aqtra.io/en/workflow-components/update-model-field.html)
- **Simple math** — addieren/subtrahieren/multiplizieren und in ein Zielfeld schreiben.
  [https://docs.aqtra.io/en/app-develop/data-flow-components/simple-math.html](https://docs.aqtra.io/en/app-develop/data-flow-components/simple-math.html)
- **Store entry over bus** — erstellen/speichern Sie Komponenteninstanz asynchron.
  [https://docs.aqtra.io/en/app-develop/data-flow-components/store-entry-over-bus.html](https://docs.aqtra.io/en/app-develop/data-flow-components/store-entry-over-bus.html)
- **Subscribe to connector** — z.B. RabbitMQ-Abonnement → verarbeiten → speichern.
  [https://docs.aqtra.io/en/app-develop/data-flow-components/subscribe-to-connector.html](https://docs.aqtra.io/en/app-develop/data-flow-components/subscribe-to-connector.html)

[Zurück nach oben](#getting-started)

---

## 9) FAQ (kurz, praktisch) {: #9-faq-short-practical }

**F: Cloud vs. lokal?**
A: Cloud für schnellstes Onboarding/Teamzugang; lokales Docker für Offline/PoCs/eingeschränkte Umgebungen.

**F: Docker startet nicht oder ist langsam.**
A: Stellen Sie 4 vCPU/8 GB RAM+ sicher, geben Sie die Zielports frei und überprüfen Sie Container-Logs. Docker neu starten und Compose wiederholen.

**F: Wo benutzerdefinierte Logik platzieren?**
A: Fügen Sie einen **Python Script**-Schritt innerhalb eines **DataFlow** hinzu, um zu validieren, zu transformieren oder externe APIs aufzurufen.

**F: Wie externe Dienste aufrufen?**
A: Verwenden Sie `http.client` aus einem Python-Skript; ordnen Sie die Antwort Ihrem DataModel zu.

**F: Hauptbausteine?**
A: **DataModel**, **Component**, **DataFlow**, **MultiComponent**, **Python Script**.

**F: Fehler und Ausnahmen?**
A: Verwenden Sie Network Inspector und Studio-Logs; Typ-Mismatches korrigieren, neu veröffentlichen und erneut testen. Siehe Video in Abschnitt 8.

**F: Wie kaufen oder Testversion erhalten?**
A: Siehe Preise: [https://aqtra.io/#price](https://aqtra.io/#price). Kauf über Anbieter oder direkt; für gehostete Bereitstellungen folgen Sie Partner-Onboarding.

---

## 10) Was kommt als Nächstes

- Muster & Best Practices (Benennung, Versionierung, Testen von Flows).
- Erweiterte Integrationen (SSO, Datenbanken, Nachrichtenwarteschlangen).
- Team-Workflows (Code-Reviews für Skripte, Umgebungsförderung).
- Community- & Support-Links (Slack/Telegram/Forum) — _hinzufügen, wenn verfügbar_.
