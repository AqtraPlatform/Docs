# Versionsbeschreibungen

!!! note "Die Aqtra-Plattform entwickelt sich ständig weiter!"
Neue Versionen werden normalerweise einmal im Monat veröffentlicht für:

    - Kubernetes-Cluster
    - Docker-Mini-Image

<br>

## Version 0.13.x

> **Funktionalität hinzugefügt**

- **Neues Komponentenmodul**: Innerhalb der Komponente wurde das Modul **Web-Teile** hinzugefügt, das aus zwei Blöcken besteht: "Styles" und "JavaScript". Dieses Modul ähnelt dem Modul "Component Script", aber anstatt mit Python zu interagieren, können Sie CSS-Stile im Block "Styles" beschreiben und in JavaScript im Block "JavaScript" interagieren;
- **Einrichtung globaler Module in der Anwendungsdomäne**: Die Einrichtung globaler CSS- und JavaScript-Module wurde in den **Haupteinstellungen** der **Anwendungsdomäne** hinzugefügt. Weitere Einzelheiten **hier**;
- **Neue Tools im Wartungsmenü**: Eine Einstellung für den Abschnitt **Dateispeicher** wurde hinzugefügt. Weitere Einzelheiten **hier**;
- **Neue Objektmodelleinstellungen für Dateitypendaten**: Jetzt können Sie die Validierung nach Dateityp und die Begrenzung der Dateigröße in Bytes festlegen;
- **XSRF/CSRF-Unterstützung**: Die Datei-Upload-Komponente eliminiert jetzt die binäre Datenübertragung über JS und fügt XSRF-Senden hinzu. Anfragen zum Herunterladen von Dateien sind jetzt gezielt und direkter Zugriff auf file-storage ist ausgeschlossen. Verbesserungen wurden auch am work-place vorgenommen, um ein XSRF-Token beim Laden einer Seite zu erhalten, und der OData-Controller wurde verbessert, um Dateien zu laden. Das Senden von Anfragen von work-place zum Herunterladen von Dateien ist jetzt auch gezielt, und direkter Zugriff auf file-storage ist unmöglich.
  <br>

> **Design aktualisiert**

- **Export/Import-Abschnitt**: Das Design des Export/Import-Abschnitts des **Anwendungen**-Menüs wurde aktualisiert.
  <br>

## Version 0.12.x

> **Funktionalität hinzugefügt**

- **Benachrichtigung senden**: Ein neuer Schritt im Datenfluss "Send notification" wurde hinzugefügt. Dieser Schritt ermöglicht es Ihnen, einfache Benachrichtigungen an den Benutzer zu senden, was die Art und Weise, wie Sie über das Benachrichtigungssystem mit dem Benutzer interagieren, verbessert. Weitere Einzelheiten hier: **Send notification**
- **Pivot-Tabelle**: Ein neues UI-Element "Pivot Grid" wurde zur Datenanalyse und -visualisierung hinzugefügt. Weitere Einzelheiten hier: **Pivot grid**
- **Änderungen an **List view\*\*\*\*:
  - Möglichkeit, die Komponente horizontal oder vertikal zu erweitern.
  - Die Möglichkeit, Drag & Drop zu aktivieren, wurde für alle Gruppen einer Komponente oder nach Wahl hinzugefügt.
  - Die Aktivierungsfunktion wurde zu Events hinzugefügt nach Verwendung von Drag & Drop.
- **Änderungen an **Data grid\*\*\*\*:
  - Der Mehrfachauswahlmechanismus wurde geändert. In den Data grid-Einstellungen gibt es jetzt eine Option "Selection Mode" mit einer Auswahl: `None`, `Single`, `Multiple`, `Checkbox`.
  - Neue Ereignisse: `On Table Changed`, `On Header Changed`, `On Row Changed`, `On Cell Changed`.
  - Möglichkeit, die Anzahl der Zeilen im Paginator an der Front auszuwählen.
- **Änderungen in **Chart View\*\*\*\*:
  - Die Farbschema-Einstellung wurde entfernt.
  - Min/Max-Einstellungen wurden hinzugefügt.
- **SIP-Client-Integration**:
  - Möglichkeit, Anrufe von Workplace aus zu tätigen dank SIP-Client-Integration. Weitere Einzelheiten **hier**.
- **Platzhalterbilder für fehlende Bilder in den Einstellungen von Anwendungsdomänen und dem UI-Element "Image"**: Weitere Einzelheiten in der [Benutzeroberflächen-Dokumentation](user-interface/index.md) und [Bildkomponente](app-development/ui-components/image.md).
- **Neue Methoden zur Verwaltung des Zustands von UI-Elementen**. Weitere Einzelheiten in **Dokumentation**.
- **Massen-Upload von Bildern über http.client und Dateispeicher in Dataflow-Skripten**: Eine Funktion für den Massen-Upload von Bildern wurde hinzugefügt. Weitere Einzelheiten in **Dokumentation**.
- **Optimierung des Veröffentlichungsmechanismus**: Der Veröffentlichungsmechanismus wurde mit einer Zustandsmaschine verbessert, die einen stabilen Prozess mit der Möglichkeit zum Rollback bei Fehlern bietet. Weitere Einzelheiten in **Dokumentation**.

<br>

## Version 0.10.x

> **Funktionalität hinzugefügt**

- Ein neuer Dataflow-Schritt "Get file info" wurde erstellt, mit dem Sie Informationen über eine Datei anhand ihrer Kennung erhalten können. Weitere Einzelheiten in der Dokumentation: **Get file info**
- Ein Filter für das Feld "Component" innerhalb des Dataflow-Schritts "Get entity by id" wurde hinzugefügt. Weitere Einzelheiten hier: **Get entity by id**  
  <br>

> **Design-Update**

- "Dashboard" Hauptseite. Weitere Einzelheiten hier: **Dashboard**
- "Navigation menu" wurde aus dem Menü "Applications" entfernt und befindet sich jetzt auf der Hauptseite. Weitere Einzelheiten hier: **Navigation menu**
- Das Design der Dataflow-Schritte wurde aktualisiert. Weitere Einzelheiten hier: **Available Dataflow steps**
- Das Design von "File storage" wurde aktualisiert. Weitere Einzelheiten hier: **File storage**
- Das Design von "System maintenance" wurde aktualisiert. Weitere Einzelheiten hier: **System maintenance**
  <br>

## Version 0.9.x

> **Funktionalität hinzugefügt**

- Systemspezifische (Plattformspezifische) Funktionen
  - Laden der Benutzeroberfläche: Optimierung der Kompilierung von UI-Komponenten.
  - Refactoring des **Wartungsmenüs**. Verschieben von Steuerelementen auf die Registerkarte "System maintenance" und Anzeige von Protokollen mit ihren Einstellungen auf der Registerkarte "System logs".
  - Job-Queue-Speichergenerator in Redis.
  - IronPython wurde von Version 2.7.12 auf 3.4.1 am Workplace aktualisiert.
- Benutzerspezifische (Studio-spezifische) Funktionen - Kopieren/Einfügen von Elementen im **Interface Builder** auf der Komponentenseite. - Hinzufügen von Dateien zum Stammverzeichnis des [Dateispeichers](user-interface/file-storage.md). - Möglichkeit, das Datenmodell der Referenzkomponenten (Catalog) in der Komponentenelementleiste für: `DataGrid`, `ListView`, `TreeView` zu verwenden.
  <br>

> **Schnittstellenänderungen**

- Refactoring des Studio-Hauptmenüs:
  - Verschieben der folgenden Elemente in die rechte Ecke der oberen Menüleiste: Lokalisierungsschalter und Schaltfläche zum Abmelden vom aktuellen Konto (Logout),
  - das Menüelement Profil wurde entfernt.
- Das Symbol für das Menüelement Python Modules wurde neu gestaltet.
- Online-Hilfesymbole wurden in vielen Abschnitten des Studios hinzugefügt: Dataflow-Schritte, Schaltflächen für Benutzeroberflächenelemente (Toolbox UI), Hauptanwendungsparameter sowie an vielen anderen Stellen im Studio, um einen schnelleren Zugriff auf die Online-Hilfe auf der Dokumentationswebsite zu gewährleisten.  
  <br>

> **Wichtige behobene Fehler**

- Korrektur des Betriebs des `Cron`-Aufgabenplaners während des Imports/Exports von Komponenten.
- Beseitigung des `changeAuthor`-Duplikats aus dem Komponentendatenmodell.
- Stabilisierung der Workflow-Schrittauswahl.
- Korrektur des UI-Elements `Number` aus dem Komponentenelementpanel.
- Beheben des Betriebs des On focus-Ereignisses für einige der UI-Elemente: Day, Time, Signature.
  <br>

## Version 0.8.x

> **Wichtige und verbesserte Funktionalität hinzugefügt**

- Im Dataflow Form Action-Schritt wurden die Parameter Open Sidebar und Open Modal hinzugefügt, die es ermöglichen, eine Seitenleiste bzw. ein modales Fenster zu öffnen, ähnlich wie dies über ein Python-Skript erfolgen kann.
- Übertragung der erforderlichen Attribute für Parameter, die im Get Action Model-Schritt übertragen werden.
- Der Dataflow-Schritt "Remove assigned roles for user" wurde hinzugefügt, der alle aktuell dem Benutzer zugewiesenen Rollen entfernt und es ermöglicht, einen neuen Satz von Rollen von Grund auf neu zu erstellen.
- Das Menü **Python modules** wurde hinzugefügt, um die gemeinsame Bibliothek von Python-Modulen zu verwalten.
- Die Hintergrundeinstellung für UI-Steuerelemente wurde hinzugefügt, die es ermöglicht, ein Bild in Standardformaten (z. B. png, svg, jpeg usw.) als Hintergrund für alle Steuerelemente festzulegen, die einen Abschnitt Brush-Einstellungen haben.
- Das Datenmodell-Ansichtssymbol im Dataflow-Schritt wurde in das Augensymbol geändert.
- Der Parameter "Skip from Synchronize" wurde durch Virtual Property ersetzt. Felder, die als "Virtual Property" markiert sind, werden nicht in der Datenbank gespeichert, wenn die Komponente aufgezeichnet wird.
- Einstellungen für Power Web Application (PWA) im Abschnitt Edit manifest wurden hinzugefügt.
- Zusätzliche Einstellungen für Anwendungsdomänen wurden hinzugefügt - show breadcrumps, login, locale.
  <br>

> **Wichtige behobene Fehler**

- Die Arbeit dynamischer Filter für Data Grid-Steuerung wurde behoben.
- Das Feld "First line to ignore field" im Schritt Import File wird nach dem Speichern nicht auf 0 zurückgesetzt.
- Die Standardfarbe für die Anwendungsdomäne gilt für Steuerelemente des Schaltflächentyps, für die keine Standardfarbe festgelegt ist.
- Berechtigungen für eine Mehrkomponentenkomponente werden im eingeschränkten Zugriffsmodus nicht festgelegt.
  <br>

## Version 0.7.0

> **Wichtige und verbesserte Funktionalität hinzugefügt**

- Bei der Auswahl einer Standardkomponente für eine Anwendungsdomäne im Abschnitt Haupteinstellungen können Sie die Seite auswählen, die für diese Komponente im Feld Standardseite geöffnet wird. Wenn keine Seite ausgewählt ist, wird standardmäßig die erste Seite der Komponente (Hauptseite) geöffnet.
- Ein neuer Schritt "Execute Dataflow" wurde zum Dataflow hinzugefügt, mit dem Sie neue Dataflows starten können, einschließlich Dataflows aus anderen Komponenten, innerhalb des aktuellen Dataflows.
- Der veraltete Dataflow-Schritt "Get Audience" wurde entfernt, und der Schritt "Form Action" wurde in die Gruppe "Model Transformation" verschoben. Die Gruppe "Other" wurde vollständig entfernt.
- Eine Suche zur Konfiguration von "Field mapping" wurde für den Schritt "Apply Deferred update operations" hinzugefügt.
- Für das UI-Steuerelement **Text Area** wurde eine Auto-size-Option hinzugefügt, die es ermöglicht, die Größe des Felds zu erweitern, wenn Sie eine größere Textmenge eingeben müssen.
- Der Dataflow-Schritt "Query Entity by Filter" wurde über die automatische Erstellung von Indizes und Datenbanknormalisierung optimiert.
- Eine Benachrichtigung über den bevorstehenden Ablauf der Lizenz wurde hinzugefügt. Die Nachricht erscheint 10 Tage vor dem Ablaufdatum der aktuellen Lizenz.
- Für Dataflow generierte Swagger-APIs zeigen jetzt den Dataflow-Namen als API-Namen an.
- Die Möglichkeit, die Geolokalisierung des Benutzers über die Funktion context.PlatformServices.GeolocationPosition vom Component Script aus anzufordern, wurde hinzugefügt.
- Die Möglichkeit, die Standardeinstellung für die Gebietsschema-Einstellung für die Anwendungsdomäne festzulegen, wurde im Abschnitt Haupteinstellungen hinzugefügt.
- Die Möglichkeit, ein Favicon für die Anwendungsdomäne festzulegen, wurde in den Einstellungen des Home Menu: Domain: Main Settings hinzugefügt.
  <br>

> **Wichtige behobene Fehler**

- Die Arbeit dynamischer Filter für Data Grid-Steuerung wurde behoben.
- Ein Problem, bei dem ein Fehler beim Sortieren von Feldern aufgetreten ist, die aus Catalog-Typ-Links abgerufen wurden, wurde behoben.
- Die Stabilität des Data Grid, einschließlich Phantomfehlern beim Navigieren durch das Data Grid, wurde verbessert.
- Ein Problem mit dem Suchformular, das im Data Grid abgeschnitten wurde, wenn auf einen Filter geklickt wurde, wurde behoben.
- Die Ausgabe von Zeichenfolgenwerten für Enum wurde hinzugefügt.
- Falscher Systembetrieb mit Remote-Logout wurde behoben.
- Falscher Betrieb des Timers im Schritt "Apply deferred update operations" wurde behoben.
- Für UI-Steuerelemente vom Typ Label, die an ein Feld vom Typ Catalog gebunden sind, wird die Farbeinstellung jetzt korrekt verarbeitet.
  <br>

## Version 0.6.x

> **Wichtige und verbesserte Funktionalität hinzugefügt**

- Erweiterte Funktionen zur Verwaltung des Hauptanwendungsmenüs - Aufbau hierarchischer Menüs und Festlegen von Menüsymbolen.
- Verbesserte Arbeit mit Python-Skripten - Hervorhebung für Python-Syntax, Auto-Complete für Python-Systemmethoden sowie Auto-Complete und Tipps für Methoden integrierter Plattformbibliotheken wurden hinzugefügt (verfügbar über Ctrl-Space unter Win10/11 und Option-Space unter MacOS).
- Die Möglichkeit, zusätzliche Seitenleistenfenster über Component Script zu erstellen, wurde hinzugefügt.
- Die Möglichkeit, komplexe modale Fenster über Component Script mit Datenübertragung von modalen Fenstern zum aufrufenden Skript zu erstellen, wurde hinzugefügt.
- Der Component Script-Aufruf wurde in das Hauptmenü verschoben.
- Die Lokalisierung des Studios ins Russische wurde abgeschlossen.
- Im DataGrid-Steuerelement ist es jetzt möglich, beliebige Felder einer externen Komponente auszuwählen, wenn Referenzfelder vom Typ Catalog angezeigt werden.
- Import-Export umfasst jetzt den Export und den anschließenden Import von Berechtigungen und Rollen (das Exportieren von Dateien, die mit Version 0.6.x erstellt wurden, in frühere Versionen funktioniert, importiert jedoch keine enthaltenen Rollen und Berechtigungen).
- Import-Export prüft jetzt auf verwandte Komponenten und warnt den Benutzer, wenn verwandte Komponenten nicht in die Exportliste aufgenommen wurden.
- Auf Plattformebene wurde die Möglichkeit hinzugefügt, Einträge (Komponenteninstanzen) als für physisches Löschen verfügbar zu markieren über ein Flag im Dataflow-Schritt "Update Entry".
- Die Möglichkeit für den Studio-Administrator, eine Liste von Einträgen zu erhalten, die zum Löschen markiert sind, und diejenigen zu entfernen, die keine Verknüpfungen zu Einträgen haben, die nicht für das Löschen bereit sind, wurde hinzugefügt.
  <br>

## Version 0.5.24

> **Wichtige und verbesserte Funktionalität hinzugefügt**

- Erweiterte Funktionen für dynamische und statische Filter in erweiterten Steuerelementen wie Data Grid, List View, Tree View, die eine On-the-Fly-Filterung von Daten vor der Anzeige für den Benutzer ermöglichen (Parameter wurden für Filter vom Typ contains usw. hinzugefügt).
- Erweiterung des Konzepts der Verwendung von Dataflow & Workflow - beide können jetzt getrennt von UI-Steuerelementen wie Schaltflächen erstellt und verwendet werden, was eine flexiblere Anwendungsstruktur ermöglicht und die Entwicklung vereinfacht.
- Viele neue Methoden, die über [Python verwenden](app-development/using-python.md) im Component Script verfügbar sind, wurden hinzugefügt, wie z. B. das Aufrufen modaler Fenster, das Überprüfen der Bildschirmauflösung und des Gerätetyps, um ein responsives UI-Layout zu erstellen.
- Die Möglichkeit, mit Nachrichtenwarteschlangensystemen (z. B. RabbitMQ) aus dem Dataflow mit einem neuen Schritt [Subscribe to Connector](app-development/data-flow-components/subscribe-to-connector.md) zu arbeiten, wurde hinzugefügt.
- Die Möglichkeit zur Stapelverarbeitung von Daten im Dataflow über neue Schritte [Deferred Update Entry](app-development/data-flow-components/deferred-update-entry.md) & [Apply Deferred Update Operations](app-development/data-flow-components/apply-deferred-update-operations.md) wurde hinzugefügt.
  <br>

## Version 0.4.4

> **Wichtige und verbesserte Funktionalität hinzugefügt**

- Ein neues Systemspeicherfeld "Name" wurde hinzugefügt, das verwendet wird, um Elemente aus Catalogs anzuzeigen.
  - Beim Anzeigen eines einzelnen Elements aus Catalog (z. B. unter Verwendung eines UI-Steuerelements Select, das auf Catalog verweist), wird jetzt immer der Inhalt des Namensfelds angezeigt. Wenn das Namensfeld leer ist, wird der System-Catalog-Name/die Sequenznummer des Catalog-Eintrags angezeigt.
- Standardsortierungseinstellungen für Datagrid und Listview wurden hinzugefügt.
- Automatische Ersetzung von Unicode-Sonderzeichen im Component Script zur Linkgenerierung wurde hinzugefügt.
  <br>

> **Fehler behoben**

- Falscher Betrieb des Paginators in Bezug auf das Umschalten mehrerer Tabellen auf einer Seite wurde behoben.
- Nicht funktionierende Scrolling-Funktion in einigen Teilen des Studios wurde behoben.
  <br>

## Version 0.3.223

_Kubernetes-Cluster 0.3.223 | Docker-Mini-Image 0.2.118_

> **Wichtige und verbesserte Funktionalität hinzugefügt**

- Ein neuer Data-Flow-Schritt "Send templated notification" wurde hinzugefügt, mit dem Sie eine Benachrichtigung per E-Mail unter Verwendung einer angegebenen Vorlage senden können.
- Transparenzeigenschaft für UI-Komponenten.
- Unterstützung für OAuth2-Autorisierung für HTTP-Anfragen wurde hinzugefügt. Sie können jetzt die automatische Token-Generierung über OAuth konfigurieren, um eine Verbindung zur API herzustellen.
- Der Parameter "Store response as file" wurde im Schritt "Execute API call" hinzugefügt, um es zu ermöglichen, eine Datei über die API auf Anfrage herunterzuladen.
- Die Schritte generieren keinen Newsletter mehr, sie generieren jetzt ein Feld im Modell zur späteren Verwendung, wie z. B. "Send templated notification".
  <br>

> **Fehler behoben**

- Fehler beim Arbeiten mit dem Datetime-Typ im Kalender wurden behoben.
- Die Benutzeroberfläche im Studio und Workplace wurde behoben.
- Der Disabled-Zustand für die Radiobutton-UI-Komponente wurde behoben.
- Lokalisierungsfehler wurden behoben.
- Die Suche im Dropdown ist jetzt nicht mehr case-sensitive.
- Die Autorisierungsoperation einschließlich Log-out-Problemen wurde behoben. <br>
