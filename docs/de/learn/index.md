# Erste Schritte

> Ein strukturierter Einstiegspunkt für Neulinge in Aqtra. Technischer Ton. Diese Seite verlinkt Dokumentation, Tutorials, Videos (mit Transkripten) und ein ausführbares Beispiel, um einen progressiven Lernpfad zu bilden.

---

## Was ist Aqtra?

Aqtra ist eine **Low-Code-Plattform** zum Erstellen von Geschäftsanwendungen, hauptsächlich über eine visuelle Benutzeroberfläche, mit optionalem **Python-Scripting** für erweiterte Logik. Dieses hybride Modell beschleunigt die Bereitstellung für Anfänger und ermöglicht es Entwicklern, bei Bedarf zu erweitern und anzupassen.

**Sie werden lernen:**

- Aqtra zu installieren und auszuführen (Cloud oder lokal über Docker).
- Eine erste Funktion von Anfang bis Ende zu erstellen (Datenmodell → UI-Komponente → Datenfluss → veröffentlichen).
- Python-Skripte dort zu verwenden, wo es angebracht ist.
- Mit externen Diensten und APIs zu integrieren.

> **Zielgruppe:** Citizen-Entwickler, Junior Front-/Back-End-Entwickler, Analysten, Architekten, Teamleiter.

**Primäre CTAs:**

- **In 60 Minuten starten →** Erste Funktion Schritt-für-Schritt (siehe [4) Erster Erfolg](#4-first-win-in-60-minutes))
- **Dokumentation →** [https://docs.aqtra.io/](https://docs.aqtra.io/de/)
- **Videokurs →** [https://www.youtube.com/@Aqtra.Academy](https://www.youtube.com/@Aqtra.Academy)

**Schnelllinks (Karten):**

- **Installieren** → [5) Installieren & Zugreifen](#5-install--access) (Cloud / Docker)
- **Erstellen Sie Ihren ersten Bildschirm (Rechnung)** → [4) Erster Erfolg](#4-first-win-in-60-minutes)
- **DataFlow-Grundlagen** → [2) Schritt-für-Schritt-Lernpfad](#2-stepbystep-learning-path-single-track)
- **Im Web veröffentlichen** → [2) Schritt-für-Schritt-Lernpfad](#2-stepbystep-learning-path-single-track)

**Auf dieser Seite**

- [1) Methodik — wie man diesen Leitfaden verwendet](#1-methodology--how-to-use-this-guide)
- [2) Schritt-für-Schritt-Lernpfad](#2-stepbystep-learning-path-single-track)
- [3) Tutorials & Dokumentationsverlinkungen](#tutorials-documentation-cross-links)
- [4) Erster Erfolg in ~60 Minuten](#4-first-win-in-60-minutes)
- [5) Installieren & Zugreifen](#5-install--access)
- [6) Kernkonzepte (Aqtra-Glossar)](#6-core-concepts-aqtra-glossary)
- [7) Videokurs](#7-video-track-with-transcripts--timecodes)
- [8) DataFlow Schrittbibliothek](#8-dataflow-step-library-quick-reference)
- [9) FAQ](#9-faq-short-practical)

---

## 1) Methodik — wie man diesen Leitfaden verwendet {: #1-methodology--how-to-use-this-guide }

- **Einzelner Fortschrittspfad**: ein einheitlicher Weg für alle Rollen, minimale neue Konzepte pro Schritt.
- **Erstnennung-Verlinkung**: jedes Konzept/UI-Element wird beim ersten Auftreten einmal verlinkt; spätere Schritte setzen dies voraus.
- **Just-in-Time-Tiefe**: jeder Schritt verweist auf fokussierte Dokumente und ein kurzes Video mit klickbaren Zeitstempeln.
- **Sichtbare Ergebnisse**: jeder Schritt endet mit einem konkreten, testbaren Ergebnis in Workplace.
- **Fehler-zuerst-Denkweise**: Schritt 10 lehrt systematisches Debugging/Protokollanalyse.
- **Bewertung**: das **Capstone** (Schritt 11) validiert CRUD, Integration, Vorlagen, Navigation und Rollen/Berechtigungen.

### Umfang & Voraussetzungen

- Zugang zu **Aqtra Studio/Workplace** (Cloud-Mieter) _oder_ einer lokalen **Docker**-Installation (≥ 4 vCPU / 8 GB RAM).
- Moderner Browser und die Fähigkeit, die Entwicklertools im **Netzwerk**-Tab anzuzeigen.
- (Optional) Grundkenntnisse in JSON und HTTP-APIs für Schritt 6.

### Lernziele (pro Schritt)

- **Schritt 1**: Sie können auf Studio/Workplace zugreifen.
- **Schritt 2**: Sie können eine Entität (Rechnung) modellieren und in einer Komponente sichtbar machen, die in Workplace angezeigt wird.
- **Schritt 3**: Sie können einen DataFlow erstellen und ihn an einen Button binden.
- **Schritt 4**: Sie können CRUD und grundlegende Validierung abschließen.
- **Schritt 5**: Sie können Python-Logik in einem Fluss hinzufügen.
- **Schritt 6**: Sie können eine externe HTTP-API aufrufen und Ergebnisse zuordnen.
- **Schritt 7**: Sie können eine MultiComponent-Seite mit Datenkontext erstellen.
- **Schritt 8**: Sie können zwischen Seiten mit Aktionsparametern navigieren.
- **Schritt 9**: Sie können ein Dokument aus einer Vorlage rendern und herunterladen.
- **Schritt 10**: Sie können Fehler mithilfe von Protokollen/Entwicklertools diagnostizieren und erneut veröffentlichen.
- **Schritt 11**: Sie können eine kleine Funktion mit Rollen/Berechtigungen und einer Integration bereitstellen.

### Feedback-Schleife

- Nach **Erster Erfolg** und **Capstone** Feedback einholen: Was war unklar, wo traten Fehler auf und welche Links/Videos haben am meisten geholfen; dies in die Dokumentation zurückspeisen.

### Bewertungsrubrik (Capstone)

- [ ] CRUD funktioniert mit Validierung und klaren Benutzerhinweisen.
- [ ] Externer API-Aufruf zugeordnet; Fehler behandelt (Zeitüberschreitungen/4xx/5xx).
- [ ] Dokumentvorlage gerendert; Datei ist herunterladbar.
- [ ] Navigation über Aktionsparameter öffnet den richtigen Datensatz/Seite.
- [ ] Mindestens **2 Rollen** mit unterschiedlichen Zugriffsrechten konfiguriert.
- [ ] Alle Komponenten **Veröffentlicht** ohne blockierende Warnungen.

---

## 2) Schritt-für-Schritt-Lernpfad (einzelner Track)

Ein einheitlicher Pfad für alle Rollen. Folgen Sie den Schritten in der Reihenfolge; jeder Schritt verlinkt zu Dokumentationen und (optional) einem kurzen Video.

**Schritt 1 — Zugriff auf Aqtra (Cloud oder Docker)**
Holen Sie sich eine laufende Instanz (siehe Abschnitt 4). Überprüfen Sie, ob Sie **Studio** und **Workplace** öffnen können.

**Schritt 2 — Erstes Anwendungsskelett**
Erstellen Sie ein minimales **DataModel** (z. B. `Invoice(number, title, totalAmount, dueDate)`) und eine **Komponente**, um es anzuzeigen/bearbeiten. Veröffentlichen Sie es und fügen Sie es zur Navigation hinzu, damit es im Workplace erscheint.

**Docs**: Komponente → [https://docs.aqtra.io/app-development/component.html](https://docs.aqtra.io/de/app-development/component.html) ; UI-Katalog → [https://docs.aqtra.io/app-development/ui-components/index.html](https://docs.aqtra.io/de/app-development/ui-components/index.html)
**Video**: Tutorial #1 → [https://youtu.be/GaUr5ET4dfQ](https://youtu.be/GaUr5ET4dfQ) ; Tutorial #2 → [https://youtu.be/UEG2pmct74s](https://youtu.be/UEG2pmct74s)

**Schritt 3 — Grundlagen des DataFlow**
Fügen Sie einen **DataFlow** mit Phasen/Schritten hinzu: `Get Action Model → Update Entry → Write Response`. Binden Sie ihn an einen **Button** und testen Sie das Erstellen/Aktualisieren.

**Docs**: Dataflow-Übersicht → [https://docs.aqtra.io/app-development/data-flow-components/index.html](https://docs.aqtra.io/de/app-development/data-flow-components/index.html) ; Eintrag aktualisieren → [https://docs.aqtra.io/app-development/data-flow-components/update-entry.html](https://docs.aqtra.io/de/app-development/data-flow-components/update-entry.html) ; Dataflow ausführen → [https://docs.aqtra.io/app-development/data-flow-components/execute-dataflow.html](https://docs.aqtra.io/de/app-development/data-flow-components/execute-dataflow.html)
**Video**: Tutorial #3 — ([05:16](https://youtu.be/UEG2pmct74s?t=316)–[07:30](https://youtu.be/UEG2pmct74s?t=450))

**Schritt 4 — CRUD-Abschluss**
Fügen Sie Listen-/Detailansichten hinzu, beenden Sie die Erstellungs-/Aktualisierungs-/Löschflüsse und Validierungen.

**Docs**: Datenraster → [https://docs.aqtra.io/app-development/ui-components/data-grid.html](https://docs.aqtra.io/de/app-development/ui-components/data-grid.html)
**Video**: Tutorial #4 — Löschen über Eintrag aktualisieren ([05:18](https://youtu.be/oLoYMSAlLVo?t=318)–[06:20](https://youtu.be/oLoYMSAlLVo?t=380)); Tutorial #5 — dynamische Filter ([00:13](https://youtu.be/YuU_YomoNaw?t=13)–[03:00](https://youtu.be/YuU_YomoNaw?t=180))

**Schritt 5 — Python-Skripting für Geschäftslogik**
Fügen Sie einen **Python Script**-Schritt hinzu, um abgeleitete Felder zu berechnen und Eingaben zu validieren.

**Docs**: Skript ausführen → [https://docs.aqtra.io/app-development/data-flow-components/execute-script.html](https://docs.aqtra.io/de/app-development/data-flow-components/execute-script.html)
**Video**: Tutorial #6 — Skript ausführen ([04:10](https://youtu.be/bOR2nOk_S0c?t=250)–[06:10](https://youtu.be/bOR2nOk_S0c?t=370))

**Schritt 6 — Externe Integrationen**
Rufen Sie eine externe HTTP-API von einem Python-Skript auf; mappen Sie die Antwort auf Ihr DataModel.

**Docs**: API-Aufruf ausführen → [https://docs.aqtra.io/app-development/data-flow-components/execute-api-call.html](https://docs.aqtra.io/de/app-development/data-flow-components/execute-api-call.html)
**Video**: (Optional) Tutorial #10 — Diagnostizieren von Payload-/Typeninkongruenzen ([01:46](https://youtu.be/qJcpIQQEqbo?t=106)–[05:00](https://youtu.be/qJcpIQQEqbo?t=300))

!!! tip "Fehlerbehebung"
_ **Timeout/5xx**: Überprüfen Sie URL/Methode/Headers; fügen Sie Wiederholungen/Backoff hinzu; protokollieren Sie den Antworttext.
_ **401/403**: Authentifizierungstoken bereitstellen/aktualisieren (Geheimnisse sicher speichern).
_ **406/422 (Typinkongruenz)**: Beheben Sie die Feldzuordnung und Typen; transformieren Sie in **Execute Script** (z. B. String → Zahl/Datum) vor `Update Entry`.
_ Verwenden Sie `context.Logger`, um Korrelations-IDs und Payload-Ausschnitte zu protokollieren.

**Schritt 7 — MultiComponent-Seiten**
Stellen Sie eine Seite aus mehreren Komponenten (Filter + Raster + Formular) zusammen. Konfigurieren Sie den **Datenkontext** und die Verkabelung.

**Docs**: Listenansicht → [https://docs.aqtra.io/app-development/ui-components/list-view.html](https://docs.aqtra.io/de/app-development/ui-components/list-view.html) ; Tab-Steuerung → [https://docs.aqtra.io/app-development/ui-components/tab-control.html](https://docs.aqtra.io/de/app-development/ui-components/tab-control.html) ; Diagramme → [https://docs.aqtra.io/app-development/ui-components/charts.html](https://docs.aqtra.io/de/app-development/ui-components/charts.html)
**Video**: Tutorial #6 — Modales Dialogfeld + automatisch aktualisiertes Raster ([10:45](https://youtu.be/bOR2nOk_S0c?t=645)–[17:00](https://youtu.be/bOR2nOk_S0c?t=1020)); Tutorial #7 — Listenansicht ([00:59](https://youtu.be/PtAJwn07sWI?t=59)–[03:00](https://youtu.be/PtAJwn07sWI?t=180))

> **Design-Tipp (optional)**: Gruppieren Sie verwandte Eingaben in Panels, halten Sie den vertikalen Rhythmus konsistent (8–12px Vielfache), vermeiden Sie übermäßigen Einsatz von Diagrammen—fügen Sie sie nur hinzu, wenn sie Trends verdeutlichen.

**Schritt 8 — Navigation & Verkabelung über Seiten hinweg**
Fügen Sie Menüelemente hinzu und öffnen Sie Seiten mit **Aktionsparametern** (übergeben Sie Datensatz `id` vom Raster zum Formular).
**Docs**: Schaltflächenaktionen → [https://docs.aqtra.io/app-development/ui-components/button.html](https://docs.aqtra.io/de/app-development/ui-components/button.html)  
**Video**: Tutorial #12 — Seite öffnen + Parameterzuordnung ([06:18](https://youtu.be/k36-qpZa9bU?t=378)–[07:00](https://youtu.be/k36-qpZa9bU?t=420)); Tutorial #5 — Anwendung aus dem Raster öffnen ([10:53](https://youtu.be/YuU_YomoNaw?t=653)–[11:20](https://youtu.be/YuU_YomoNaw?t=680))

**Schritt 9 — Vorlagen & Dokumentenerstellung (PDF)**  
Ein Dokument aus einer Vorlage über DataFlow rendern und herunterladen.

**Docs**: Dataflow-Komponenten (Vorlage rendern) → [https://docs.aqtra.io/app-development/data-flow-components/index.html](https://docs.aqtra.io/de/app-development/data-flow-components/index.html)  
**Video**: Tutorial #12 — Vorlage rendern + herunterladen ([01:37](https://youtu.be/k36-qpZa9bU?t=97)–[02:45](https://youtu.be/k36-qpZa9bU?t=165); [05:20](https://youtu.be/k36-qpZa9bU?t=320)–[07:00](https://youtu.be/k36-qpZa9bU?t=420))

**Schritt 10 — Fehlerbehandlung & Debugging**  
Verwenden Sie die Netzwerk-Registerkarte und die Studio-Protokolle, um 4xx/5xx zu diagnostizieren; Typen korrigieren; erneut veröffentlichen.

**Docs**: Anwendungen veröffentlichen → [https://docs.aqtra.io/app-development/publishing-applications.html](https://docs.aqtra.io/de/app-development/publishing-applications.html)  
**Video**: Tutorial #10 — Fehler finden und beheben ([01:46](https://youtu.be/qJcpIQQEqbo?t=106)–[05:00](https://youtu.be/qJcpIQQEqbo?t=300))

!!! tip "Fehlerbehebung"

- Folgen Sie der Reihenfolge: **Kompilieren → Speichern → Bereit zum Veröffentlichen → Veröffentlichen**; überprüfen Sie, ob die Komponente als _Veröffentlicht_ aufgeführt ist.  
- Verwenden Sie die Entwicklertools des Browsers **Netzwerk**, um Anfrage/Antwort mit dem erwarteten Schema zu vergleichen; Mapping/Typen korrigieren.  
  _ Wenn sich das Verhalten zwischen den Seiten unterscheidet, überprüfen Sie, ob **alle abhängigen Komponenten** zusammen erneut veröffentlicht wurden.  
  _ Bei Docker-Setups die Containerprotokolle auf Stack-Traces und Portkonflikte überprüfen.

**Schritt 11 — Abschluss**  
Erweitern Sie Ihre App um eine kleine Funktion (z. B. Mini‑CRM): Rollen/Berechtigungen, MultiComponent-Dashboard, eine Integration, eine Dokumentvorlage. Dokumentieren Sie die Akzeptanzkriterien und erstellen Sie ein kurzes Demovideo.

[Zurück nach oben](#getting-started)

---

## 3) Tutorials & Dokumentation Querverweise {: #tutorials-documentation-cross-links }

**Installation / Plattform**

- Grundeinstellungen, Authentifizierung, Protokolle, Metriken → [https://docs.aqtra.io/install1/basic-settings.html](https://docs.aqtra.io/de/install1/basic-settings.html)

**Kernaufbau**

- Komponente (erstellen, Grundeinstellungen) → [https://docs.aqtra.io/app-development/component.html](https://docs.aqtra.io/de/app-development/component.html)  
- Katalog der UI-Komponenten (erste Erwähnung) → [https://docs.aqtra.io/app-development/ui-components/index.html](https://docs.aqtra.io/de/app-development/ui-components/index.html)  
- Datenraster (erste Erwähnung) → [https://docs.aqtra.io/app-development/ui-components/data-grid.html](https://docs.aqtra.io/de/app-development/ui-components/data-grid.html)  
- Listenansicht / Tab-Steuerung / Diagramme (erste Erwähnung) → [https://docs.aqtra.io/app-development/ui-components/list-view.html](https://docs.aqtra.io/de/app-development/ui-components/list-view.html), [https://docs.aqtra.io/app-development/ui-components/tab-control.html](https://docs.aqtra.io/de/app-development/ui-components/tab-control.html), [https://docs.aqtra.io/app-development/ui-components/charts.html](https://docs.aqtra.io/de/app-development/ui-components/charts.html)

**Flows / Logik**

- Dataflow-Übersicht → [https://docs.aqtra.io/app-development/data-flow-components/index.html](https://docs.aqtra.io/de/app-development/data-flow-components/index.html)  
- Eintrag aktualisieren (CRUD) → [https://docs.aqtra.io/app-development/data-flow-components/update-entry.html](https://docs.aqtra.io/de/app-development/data-flow-components/update-entry.html)  
- Dataflow ausführen → [https://docs.aqtra.io/app-development/data-flow-components/execute-dataflow.html](https://docs.aqtra.io/de/app-development/data-flow-components/execute-dataflow.html)  
- Skript ausführen (Python) → [https://docs.aqtra.io/app-development/data-flow-components/execute-script.html](https://docs.aqtra.io/de/app-development/data-flow-components/execute-script.html)  
- API-Aufruf ausführen → [https://docs.aqtra.io/app-development/data-flow-components/execute-api-call.html](https://docs.aqtra.io/de/app-development/data-flow-components/execute-api-call.html)

**Veröffentlichung**

- Anwendungen veröffentlichen → [https://docs.aqtra.io/app-development/publishing-applications.html](https://docs.aqtra.io/de/app-development/publishing-applications.html)

**Tutorials (Dokumente)**

- Tutorial #1 → [https://docs.aqtra.io/tutorials/tutorial1.html](https://docs.aqtra.io/de/tutorials/tutorial1.html)  
- Tutorial #2 → [https://docs.aqtra.io/tutorials/tutorial2.html](https://docs.aqtra.io/de/tutorials/tutorial2.html)  
- Tutorial #3 → [https://docs.aqtra.io/tutorials/tutorial3.html](https://docs.aqtra.io/de/tutorials/tutorial3.html)

**Videoindex (klickbare Zeitstempel)**

- T#3 — DataFlow-Grundlagen ([05:16](https://youtu.be/UEG2pmct74s?t=316)–[07:30](https://youtu.be/UEG2pmct74s?t=450)).  
- T#4 — Löschen über Eintrag aktualisieren ([05:18](https://youtu.be/oLoYMSAlLVo?t=318)–[06:20](https://youtu.be/oLoYMSAlLVo?t=380)).  
- T#5 — Datenrasterfilter; Anwendung öffnen ([00:13](https://youtu.be/YuU_YomoNaw?t=13)–[03:00](https://youtu.be/YuU_YomoNaw?t=180)), ([10:53](https://youtu.be/YuU_YomoNaw?t=653)–[11:20](https://youtu.be/YuU_YomoNaw?t=680)).  
- T#6 — Skript ausführen; modales Dialogfeld; Raster automatisch aktualisieren ([04:10](https://youtu.be/bOR2nOk_S0c?t=250)–[06:10](https://youtu.be/bOR2nOk_S0c?t=370)), ([10:45](https://youtu.be/bOR2nOk_S0c?t=645)–[17:00](https://youtu.be/bOR2nOk_S0c?t=1020)).
- T#10 — Debug 500→406; Typen beheben; erneut veröffentlichen ([01:46](https://youtu.be/qJcpIQQEqbo?t=106)–[05:00](https://youtu.be/qJcpIQQEqbo?t=300)).
- T#12 — Vorlage rendern; Herunterladen; Seite öffnen + Zuordnung ([01:37](https://youtu.be/k36-qpZa9bU?t=97)–[02:45](https://youtu.be/k36-qpZa9bU?t=165)), ([06:18](https://youtu.be/k36-qpZa9bU?t=378)–[07:00](https://youtu.be/k36-qpZa9bU?t=420)).

---

## 4) Erster Erfolg in ~60 Minuten

> Erstellen Sie das **Rechnungsinventar** Mini-Feature von Anfang bis Ende.

1. **Zugriff auf Aqtra** (Cloud oder Docker) und öffnen Sie **Studio**.
2. **Datenmodell erstellen** `Invoice(number, title, totalAmount, dueDate)`.
3. **Komponente hinzufügen**, um Rechnungen zu erstellen/aufzulisten (erste Verwendung von Data Grid).
4. **Datenfluss verdrahten** — `Get Action Model → Update Entry → Write Response` (optionales **Skript ausführen**, um totalAmount zu validieren).
5. **Veröffentlichen** und im **Arbeitsplatz** überprüfen: zwei Rechnungen erstellen, eine bearbeiten.

**Docs**: Tutorials → Erstellen Sie Ihre erste App — [https://docs.aqtra.io/tutorials/index.html](https://docs.aqtra.io/de/tutorials/index.html)

---

## 5) Installieren & Zugreifen {: #5-install--access }

Wählen Sie eine der folgenden Optionen. Halten Sie Anmeldeinformationen und Lizenzschlüssel sicher.

### Option 1 — Cloud (Gehostet)

- Zugriff über einen Hosting-Partner erhalten oder direkt kaufen.
- Preise & Beschaffung: [https://aqtra.io/#price](https://aqtra.io/#price).
- Erhalten Sie eine Organisations-/Mandanten-URL und Anmeldeinformationen.
- SSO konfigurieren (optional), Benutzer und Rollen.

### Option 2 — Lokal (Docker)

**Voraussetzungen**: Docker Engine/Compose aktuell; Linux/Windows/macOS-Host mit **4 vCPU / 8 GB RAM** mindestens.

**Checkliste**

- [ ] Docker/Compose installieren und überprüfen, dass `docker ps` funktioniert.
- [ ] `docker-compose.yml` und `.env` mit erforderlichen Geheimnissen vorbereiten.
- [ ] DB starten → `docker compose up -d db` und auf Bereitschaft warten.
- [ ] App starten → `docker compose up -d app`.
- [ ] Zugriff auf **Arbeitsplatz** unter `http://<host>:8080/` und **Studio** unter `http://<host>:8080/studio/`.

**Docs**: Grundlegende Einstellungen (Architektur, Ports, Authentifizierung, Protokolle, Metriken) → [https://docs.aqtra.io/install1/basic-settings.html](https://docs.aqtra.io/de/install1/basic-settings.html)

[Zurück nach oben](#getting-started)

---

## 6) Kernkonzepte (Aqtra Glossar)

Kurze, umsetzbare Definitionen.

- **Komponente** — ein UI-Baustein, der Daten und Aktionen für Benutzer rendert (Formular, Liste, Detail usw.). [https://docs.aqtra.io/app-development/component.html](https://docs.aqtra.io/de/app-development/component.html)
- **Datenfluss** — ein gerichteter Fluss von Operationen (z. B. validieren → transformieren → persistieren → benachrichtigen), der bei Benutzer- oder Systemereignissen ausgeführt wird. Typische Schritte: **Aktion Modell abrufen**, **Eintrag aktualisieren**, **Antwort schreiben**, **Skript ausführen**, **API-Aufruf ausführen**. [https://docs.aqtra.io/app-development/data-flow-components/index.html](https://docs.aqtra.io/de/app-development/data-flow-components/index.html)
- **Datenmodell** — die strukturierte Definition von Entitäten/Attributen, die die Anwendung speichert und manipuliert.
- **MultiKomponente** — eine zusammengesetzte Ansicht, die mehrere Komponenten (z. B. Liste + Details + Filter) in eine kohärente Seite integriert; Elemente verwenden **Datenkontext**, um an eine Quellkomponente zu binden.
- **Python-Skript** — benutzerdefinierter Logikschritt, der in einen Fluss eingebettet ist, um Daten zu transformieren, Dienste aufzurufen oder Regeln zu implementieren. [https://docs.aqtra.io/app-development/data-flow-components/execute-script.html](https://docs.aqtra.io/de/app-development/data-flow-components/execute-script.html)

---

## 7) Video Track (mit Transkripten & Zeitcodes) {: #7-video-track-with-transcripts--timecodes }

Zentralisierte Videoliste mit Deep Links und Zeitstempeln. Verwenden Sie diese, um direkt zu den relevanten Demomomenten zu springen.

- **Tutorial #1** — [https://youtu.be/GaUr5ET4dfQ](https://youtu.be/GaUr5ET4dfQ)
- **Tutorial #2** — [https://youtu.be/UEG2pmct74s](https://youtu.be/UEG2pmct74s)
- **Tutorial #3** — Grundlagen des Datenflusses ([05:16](https://youtu.be/UEG2pmct74s?t=316)–[07:30](https://youtu.be/UEG2pmct74s?t=450))
- **Tutorial #4** — Löschen über Eintrag aktualisieren ([05:18](https://youtu.be/oLoYMSAlLVo?t=318)–[06:20](https://youtu.be/oLoYMSAlLVo?t=380))
- **Tutorial #5** — Data Grid-Filter; Anwendung öffnen ([00:13](https://youtu.be/YuU_YomoNaw?t=13)–[03:00](https://youtu.be/YuU_YomoNaw?t=180)), ([10:53](https://youtu.be/YuU_YomoNaw?t=653)–[11:20](https://youtu.be/YuU_YomoNaw?t=680))
- **Tutorial #6** — Skript ausführen; modales Dialogfeld; Grid automatisch aktualisieren ([04:10](https://youtu.be/bOR2nOk_S0c?t=250)–[06:10](https://youtu.be/bOR2nOk_S0c?t=370)), ([10:45](https://youtu.be/bOR2nOk_S0c?t=645)–[17:00](https://youtu.be/bOR2nOk_S0c?t=1020))
- **Tutorial #7** — [https://youtu.be/PtAJwn07sWI](https://youtu.be/PtAJwn07sWI)
- **Tutorial #8** — [https://youtu.be/YfqfdJpDm-k](https://youtu.be/YfqfdJpDm-k)
- **Tutorial #9/10** — Debugging & Diagnosen ([01:46](https://youtu.be/qJcpIQQEqbo?t=106)–[05:00](https://youtu.be/qJcpIQQEqbo?t=300))
- **Tutorial #11** — [https://youtu.be/d-FD1ARn0h0](https://youtu.be/d-FD1ARn0h0)
- **Tutorial #12** — Vorlage rendern; Herunterladen; Seite + Zuordnung öffnen ([01:37](https://youtu.be/k36-qpZa9bU?t=97)–[02:45](https://youtu.be/k36-qpZa9bU?t=165)), ([06:18](https://youtu.be/k36-qpZa9bU?t=378)–[07:00](https://youtu.be/k36-qpZa9bU?t=420))

!!! note "Bleiben Sie auf dem Laufenden"
Abonnieren Sie **Aqtra Academy** auf YouTube und überprüfen Sie regelmäßig das Dokumentenverzeichnis auf Updates. Neue Episoden werden hier verlinkt, sobald sie verfügbar sind.

[Zurück nach oben](#getting-started)

---

## 8) DataFlow Schrittbibliothek (schnelle Referenz)

Einige nützliche Schritte, die Sie wahrscheinlich über CRUD hinaus verwenden werden:

- **Eintrag aktualisieren** — [https://docs.aqtra.io/app-development/data-flow-components/update-entry.html](https://docs.aqtra.io/de/app-development/data-flow-components/update-entry.html)
- **Datenfluss ausführen** — einen anderen Datenfluss aufrufen und Ergebnisse zusammenführen.
  [https://docs.aqtra.io/app-development/data-flow-components/execute-dataflow.html](https://docs.aqtra.io/de/app-development/data-flow-components/execute-dataflow.html)
- **API-Aufruf ausführen** — HTTP-Anfrage konfigurieren und ausführen, Ergebnisse binden.
  [https://docs.aqtra.io/app-development/data-flow-components/execute-api-call.html](https://docs.aqtra.io/de/app-development/data-flow-components/execute-api-call.html)
- **Entität nach ID abrufen** — Entität über Identifikator über das Katalogfeld abrufen.
  [https://docs.aqtra.io/app-development/data-flow-components/get-entity-by-id.html](https://docs.aqtra.io/de/app-development/data-flow-components/get-entity-by-id.html)
- **Modellfeld aktualisieren** — ein einzelnes Feld innerhalb des Modells festlegen/ableiten.
  [https://docs.aqtra.io/workflow-components/update-model-field.html](https://docs.aqtra.io/de/workflow-components/update-model-field.html)
- **Einfache Mathematik** — addieren/subtrahieren/multiplizieren und in ein Ziel-Feld schreiben.
  [https://docs.aqtra.io/app-development/data-flow-components/simple-math.html](https://docs.aqtra.io/de/app-development/data-flow-components/simple-math.html)
- **Eintrag über Bus speichern** — Komponentinstanz asynchron erstellen/speichern.
  [https://docs.aqtra.io/app-development/data-flow-components/store-entry-over-bus.html](https://docs.aqtra.io/de/app-development/data-flow-components/store-entry-over-bus.html)
- **Auf Connector abonnieren** — z.B. RabbitMQ-Abonnement → verarbeiten → speichern.
  [https://docs.aqtra.io/app-development/data-flow-components/subscribe-to-connector.html](https://docs.aqtra.io/de/app-development/data-flow-components/subscribe-to-connector.html)

[Zurück nach oben](#getting-started)

---

## 9) FAQ (kurz, praktisch)

**F: Cloud vs lokal?**
A: Cloud für schnellstes Onboarding/Teamzugriff; lokales Docker für Offline/PoCs/beschränkte Umgebungen.

**F: Docker startet nicht oder ist langsam.**
A: Stellen Sie 4 vCPU/8 GB RAM+ sicher, geben Sie die Zielports frei und überprüfen Sie die Containerprotokolle. Starten Sie Docker neu und versuchen Sie es erneut.

**F: Wo soll benutzerdefinierte Logik platziert werden?**
A: Fügen Sie einen **Python-Skript**-Schritt innerhalb eines **DataFlow** hinzu, um zu validieren, zu transformieren oder externe APIs aufzurufen.

**F: Wie externe Dienste aufrufen?**
A: Verwenden Sie `http.client` aus einem Python-Skript; mappen Sie die Antwort auf Ihr DataModel.

**F: Hauptbausteine?**
A: **DataModel**, **Component**, **DataFlow**, **MultiComponent**, **Python Script**.

**F: Fehler und Ausnahmen?**
A: Verwenden Sie den Netzwerkinspektor und die Studio-Protokolle; beheben Sie Typinkonsistenzen, veröffentlichen Sie erneut und testen Sie erneut. Siehe das Video in Abschnitt 8.

**F: Wie kauft man oder erhält man eine Testversion?**
A: Siehe Preise: [https://aqtra.io/#price](https://aqtra.io/#price). Kauf über den Anbieter oder direkt; für gehostete Bereitstellungen folgen Sie dem Partner-Onboarding.

---

## 10) Was kommt als Nächstes

- Muster & Best Practices (Benennung, Versionierung, Testabläufe).
- Erweiterte Integrationen (SSO, Datenbanken, Nachrichtenwarteschlangen).
- Team-Workflows (Code-Überprüfungen für Skripte, Umgebungsförderung).
- Community- & Support-Links (Slack/Telegram/Forum) — _hinzufügen, wenn verfügbar_.