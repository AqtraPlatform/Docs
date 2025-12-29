# Versionsbeschreibungen

!!! note "Die Aqtra-Plattform entwickelt sich ständig weiter!"
Neue Versionen werden normalerweise einmal im Monat veröffentlicht für:

    - Kubernetes-Cluster
    - Docker-Mini-Image

<br>

## Version 0.13.x

> **Funktionalität Hinzugefügt**

- **Neues Komponentenmodul**: Innerhalb der Komponente wurde das Modul **Webteile** hinzugefügt, das aus zwei Blöcken besteht: „Stile“ und „JavaScript“. Dieses Modul ähnelt dem Modul „Komponentenskript“, aber anstelle der Interaktion mit Python können Sie CSS-Stile im Block „Stile“ beschreiben und in JavaScript im Block „JavaScript“ interagieren;
- **Einrichten globaler Module im Anwendungsbereich**: Das Einrichten globaler CSS- und JavaScript-Module wurde in den **Haupteinstellungen** des **Anwendungsbereichs** hinzugefügt. Weitere Details **hier**;
- **Neue Werkzeuge im Wartungsmenü**: Eine Einstellung wurde für den Abschnitt **Dateispeicher** hinzugefügt. Weitere Details **hier**;
- **Neue Objektmodell-Einstellungen für Dateityp-Daten**: Jetzt können Sie die Validierung nach Dateityp und die Begrenzung der Dateigröße in Bytes festlegen;
- **XSRF/CSRF-Unterstützung**: Die Datei-Upload-Komponente eliminiert jetzt den binären Datentransfer über JS und fügt das Senden von XSRF hinzu. Anfragen zum Herunterladen von Dateien sind jetzt gezielt, und der direkte Zugriff auf den Dateispeicher ist ausgeschlossen. Verbesserungen wurden auch am Arbeitsplatz vorgenommen, um ein XSRF-Token beim Laden einer Seite zu erhalten, und der OData-Controller wurde verbessert, um Dateien zu laden. Das Senden von Anfragen vom Arbeitsplatz zum Herunterladen von Dateien ist jetzt ebenfalls gezielt, und der direkte Zugriff auf den Dateispeicher ist unmöglich.
  <br>

> **Design Aktualisiert**

- **Export/Import-Bereich**: Das Design des Export-/Importbereichs im **Anwendungen**-Menü wurde aktualisiert.
  <br>

## Version 0.12.x

> **Funktionalität Hinzugefügt**

- **Benachrichtigung senden**: Ein neuer Schritt im Datenfluss „Benachrichtigung senden“ wurde hinzugefügt. Dieser Schritt ermöglicht es Ihnen, einfache Benachrichtigungen an den Benutzer zu senden, was die Interaktion mit dem Benutzer über das Benachrichtigungssystem verbessert. Weitere Details hier: **Benachrichtigung senden**
- **Pivot-Tabelle**: Ein neues UI-Element „Pivot-Tabelle“ wurde für Datenanalyse und -visualisierung hinzugefügt. Weitere Details hier: **Pivot-Tabelle**
- **Änderungen an der **Listenansicht**:
  - Möglichkeit, die Komponente horizontal oder vertikal zu erweitern.
  - Die Möglichkeit, Drag & Drop für alle Gruppen einer Komponente oder nach Wahl zu aktivieren, wurde hinzugefügt.
  - Die Aktivierungsfunktion wurde zu Ereignissen nach der Verwendung von Drag & Drop hinzugefügt.
- **Änderungen an der **Datenansicht**:
  - Der Multiselect-Mechanismus wurde geändert. In den Einstellungen der Datenansicht gibt es jetzt eine Option „Auswahlmodus“ mit einer Auswahl: `None`, `Single`, `Multiple`, `Checkbox`.
  - Neue Ereignisse: `On Table Changed`, `On Header Changed`, `On Row Changed`, `On Cell Changed`.
  - Möglichkeit, die Anzahl der Zeilen im Paginator vorne auszuwählen.
- **Änderungen in der **Diagrammansicht**:
  - Die Einstellung des Farbschemas wurde entfernt.
  - Min/Max-Einstellungen wurden hinzugefügt.
- **SIP-Client-Integration**:
  - Möglichkeit, Anrufe vom Arbeitsplatz dank der SIP-Client-Integration zu tätigen. Weitere Details **hier**.
- **Platzhalterbilder für fehlende Bilder in den Einstellungen der Anwendungsbereiche und des UI-„Bildelements“**: Weitere Details in [Benutzerschnittstellendokumentation](user-interface/index.md) und [Bildelement](app-development/ui-components/image.md).
- **Neue Methoden zur Verwaltung des Zustands von UI-Elementen**. Weitere Details in **Dokumentation**.
- **Massen-Upload von Bildern über http.client und Dateispeicher in Datenfluss-Skripten**: Eine Funktion für den Massen-Upload von Bildern wurde hinzugefügt. Weitere Details in **Dokumentation**.
- **Optimierung des Veröffentlichungsmechanismus**: Der Veröffentlichungsmechanismus wurde mit einer Zustandsmaschine verbessert, die einen stabilen Prozess mit der Möglichkeit zur Rückgängigmachung im Fehlerfall bietet. Weitere Details in **Dokumentation**.

<br>

## Version 0.10.x

> **Funktionalität Hinzugefügt**
- Ein neuer Datenfluss-Schritt „Dateiinformationen abrufen“ wurde erstellt, der es Ihnen ermöglicht, Informationen über eine Datei anhand ihrer Kennung zu erhalten. Weitere Details in der Dokumentation: **Dateiinformationen abrufen**
- Ein Filter für das Feld „Komponente“ im Datenfluss-Schritt „Entität nach ID abrufen“ wurde hinzugefügt. Weitere Details hier: **Entität nach ID abrufen**  
  <br>

> **Design-Update**

- Hauptseite „Dashboard“. Weitere Details hier: **Dashboard**
- Das „Navigationsmenü“ wurde aus dem Menü „Anwendungen“ entfernt und befindet sich jetzt auf der Hauptseite. Weitere Details hier: **Navigationsmenü**
- Das Design der Datenfluss-Schritte wurde aktualisiert. Weitere Details hier: **Verfügbare Datenfluss-Schritte**
- Das Design des „Dateispeichers“ wurde aktualisiert. Weitere Details hier: **Dateispeicher**
- Das Design der „Systemwartung“ wurde aktualisiert. Weitere Details hier: **Systemwartung**
  <br>

## Version 0.9.x

> **Funktionalität hinzugefügt**

- Systemspezifische (plattform-spezifische) Funktionen
  - Benutzeroberflächen-Upload: Optimierung der Kompilierung von UI-Komponenten.
  - Refactoring des **Wartungsmenüs**. Verschieben der Steuerungstasten zum Tab „Systemwartung“ und Anzeigen von Protokollen mit ihren Einstellungen im Tab „Systemprotokolle“.
  - Job-Queue-Speichergenerator in Redis.
  - IronPython wurde von Version 2.7.12 auf 3.4.1 auf Workplace aktualisiert.
- Benutzerspezifische (Studio-spezifische) Funktionen - Elemente in **Interface Builder** auf der Komponenten-Seite kopieren/einfügen. - Dateien zum Stamm des [Dateispeichers](user-interface/file-storage.md) hinzufügen. - Möglichkeit, das Datenmodell der Referenzkomponenten (Katalog) in der Symbolleiste der Komponentenelemente für: `DataGrid`, `ListView`, `TreeView` zu verwenden.
  <br>

> **Änderungen der Benutzeroberfläche**

- Refactoring des Hauptmenüs des Studios:
  - Verschieben der folgenden Elemente in die rechte Ecke der oberen Symbolleiste: Lokalisierungsschalter und Schaltfläche zum Abmelden vom aktuellen Konto (Abmelden),
  - Der Profileintrag im Hauptmenü wurde entfernt.
- Das Symbol für den Menüeintrag Python-Module wurde neu gestaltet.
- Online-Hilfesymbole wurden in vielen Abschnitten des Studios hinzugefügt: Datenfluss-Schritte, Schaltflächen für Benutzeroberflächenelemente (Toolbox UI), Hauptanwendungsparameter sowie an vielen anderen Stellen im Studio, um einen schnelleren Zugriff auf die Online-Hilfe auf der Dokumentationsseite zu gewährleisten.  
  <br>

> **Wichtige Fehler behoben**

- Korrektur des `Cron` Task-Scheduler-Betriebs während des Imports/Exports von Komponenten.
- Beseitigung des `changeAuthor` Duplikats aus dem Datenmodell der Komponente.
- Stabilisierung der Auswahl von Workflow-Schritten.
- Korrektur des `Number` UI-Elements aus dem Panel der Komponentenelemente.
- Behebung des Betriebs des On-Focus-Events für einige der UI-Elemente: Tag, Zeit, Unterschrift.
  <br>

## Version 0.8.x

> **Wichtige und verbesserte Funktionalität hinzugefügt**

- Im Datenfluss-Schritt Form Action wurden die Parameter Open Sidebar und Open Modal hinzugefügt, die es Ihnen ermöglichen, eine Seitenleiste und ein modales Fenster zu öffnen, ähnlich wie dies über ein Python-Skript erfolgen kann.
- Übertragung der erforderlichen Attribute für Parameter, die im Schritt Get Action Model übertragen werden.
- Der Datenfluss-Schritt „Zugewiesene Rollen für Benutzer entfernen“ wurde hinzugefügt, der alle aktuellen Rollen, die dem Benutzer zugewiesen sind, entfernt und es Ihnen ermöglicht, ein neues Set von Rollen von Grund auf neu zu erstellen.
- **Python-Module** Menü wurde hinzugefügt, um die gemeinsame Bibliothek von Python-Modulen zu verwalten.
- Hintergrund-Einstellungen für UI-Steuerelemente wurden hinzugefügt, die es Ihnen ermöglichen, ein Bild in Standardformaten (z. B. png, svg, jpeg usw.) als Hintergrund für alle Steuerelemente festzulegen, die einen Abschnitt für Bürsten-Einstellungen haben.
- Das Symbol für die Datenmodellansicht im Datenfluss-Schritt wurde in das Augensymbol geändert.
- Der Parameter „Von Synchronisieren überspringen“ wurde durch die virtuelle Eigenschaft ersetzt. Felder, die als „Virtuelle Eigenschaft“ gekennzeichnet sind, werden beim Speichern der Komponente nicht in der Datenbank gespeichert.
- Einstellungen für die Power Web Application (PWA) im Abschnitt Manifest bearbeiten wurden hinzugefügt.
- Zusätzliche Einstellungen für die Anwendungsdomäne wurden hinzugefügt - Breadcrumbs anzeigen, Anmeldung, Gebietsschema.
  <br>
> **Wichtige behobene Fehler**

- Die Funktion der dynamischen Filter für die Data Grid-Steuerung wurde behoben.
- Das Feld „Erste Zeile, die ignoriert werden soll“ im Schritt Importdatei wird nach dem Speichern nicht auf 0 zurückgesetzt.
- Die Standardfarbe für die Anwendungsdomäne gilt für Steuerelemente des Button-Typs, die keine Standardfarbe festgelegt haben.
- Berechtigungen für ein Multikomponenten-Element sind im Modus „Zugriff einschränken“ nicht festgelegt.
  <br>

## Version 0.7.0

> **Wichtige und verbesserte Funktionalität hinzugefügt**

- Beim Auswählen einer Standardkomponente für eine Anwendungsdomäne im Abschnitt Haupteinstellungen können Sie die Seite auswählen, die für diese Komponente im Feld Standardseite geöffnet wird. Wenn keine Seite ausgewählt ist, wird standardmäßig die erste Seite der Komponente (Hauptseite) geöffnet.
- Ein neuer Schritt „Datenfluss ausführen“ wurde zum Datenfluss hinzugefügt, der es Ihnen ermöglicht, neue Datenflüsse zu starten, einschließlich Datenflüsse aus anderen Komponenten, innerhalb des aktuellen Datenflusses.
- Der veraltete Schritt „Zielgruppe abrufen“ im Datenfluss wurde entfernt, und der Schritt „Formularaktion“ wurde in die Gruppe „Modelltransformation“ verschoben. Die Gruppe „Sonstiges“ wurde vollständig entfernt.
- Die Suche zur Konfiguration der „Feldzuordnung“ wurde für den Schritt „Anwenden von verzögerten Aktualisierungsoperationen“ hinzugefügt.
- Für die UI-Steuerung **Textbereich** wurde eine Auto-Größe-Option hinzugefügt, die es Ihnen ermöglicht, die Größe des Feldes zu erweitern, wenn Sie eine größere Menge an Text eingeben müssen.
- Der Schritt „Abfrageentität nach Filter“ im Datenfluss wurde durch automatische Erstellung von Indizes und Datenbanknormalisierung optimiert.
- Eine Benachrichtigung über die bevorstehende Lizenzablauf wurde hinzugefügt. Die Nachricht erscheint 10 Tage vor dem Ablaufdatum der aktuellen Lizenz.
- Swagger-APIs, die für den Datenfluss generiert wurden, zeigen jetzt den Namen des Datenflusses als API-Namen an.
- Die Möglichkeit, die Benutzergeolokalisierung über das Component Script über die Funktion context.PlatformServices.GeolocationPosition anzufordern, wurde hinzugefügt.
- Die Möglichkeit, die Standardeinstellung für die Gebietsschema der Anwendungsdomäne in den Haupteinstellungen festzulegen, wurde hinzugefügt.
- Die Möglichkeit, ein Favicon für die Anwendungsdomäne in den Einstellungen des Home-Menüs: Domäne: Haupteinstellungen festzulegen, wurde hinzugefügt.
  <br>

> **Wichtige behobene Fehler**

- Die Funktion der dynamischen Filter für die Data Grid-Steuerung wurde behoben.
- Ein Problem, bei dem ein Fehler auftrat, wenn Felder aus Katalogtyp-Links sortiert wurden, wurde behoben.
- Die Stabilität des Datenrasters, einschließlich phantomfehlern beim Navigieren durch das Datenraster, wurde verbessert.
- Ein Problem mit dem Suchformular, das im Data Grid abgeschnitten wurde, wenn auf einen Filter geklickt wurde, wurde behoben.
- Die Ausgabe von Zeichenfolgenwerten für Enum wurde hinzugefügt.
- Falsche Systemoperationen mit der Remote-Abmeldung wurden behoben.
- Falsche Funktion des Timers im Schritt „Anwenden von verzögerten Aktualisierungsoperationen“ wurde behoben.
- Für UI-Steuerelemente des Label-Typs, die an ein Feld des Katalogtyps gebunden sind, wird die Farbeinstellung jetzt korrekt verarbeitet.
  <br>

## Version 0.6.x

> **Wichtige und verbesserte Funktionalität hinzugefügt**

- Erweiterte Funktionen zur Verwaltung des Hauptanwendungsmenüs - Erstellung hierarchischer Menüs und Festlegung von Menüsymbolen.
- Verbesserte Arbeit mit Python-Skripten - Hervorhebung der Python-Syntax, Autovervollständigung für Python-Systemmethoden sowie Autovervollständigung und Tipps für Methoden der integrierten Plattformbibliotheken wurden hinzugefügt (verfügbar über Ctrl-Space unter Win10/11 und Option-Space unter MacOS).
- Die Möglichkeit, zusätzliche Seitenleistenfenster über Component Script zu erstellen, wurde hinzugefügt.
- Die Möglichkeit, komplexe modale Fenster über Component Script mit Datenübertragung von modalen Fenstern zum aufrufenden Skript zu erstellen, wurde hinzugefügt.
- Der Aufruf des Component Script wurde ins Hauptmenü verschoben.
- Die Lokalisierung des Studios ins Russische wurde abgeschlossen.
- Im DataGrid-Steuerelement ist es jetzt möglich, beliebige Felder einer externen Komponente auszuwählen, wenn Referenzfelder des Katalogtyps angezeigt werden.
- Der Import-Export umfasst jetzt den Export und anschließenden Import von Berechtigungen und Rollen (das Exportieren von Dateien, die mit Version 0.6.x erstellt wurden, in frühere Versionen funktioniert, importiert jedoch keine enthaltenen Rollen und Berechtigungen).
- Der Import-Export überprüft jetzt verwandte Komponenten und warnt den Benutzer, wenn verwandte Komponenten nicht in der Exportliste enthalten sind.
- Auf Plattformebene wurde die Möglichkeit hinzugefügt, Einträge (Komponenteninstanzen) über ein Flag im Datenfluss "Eintrag aktualisieren" als für die physische Löschung verfügbar zu kennzeichnen.
- Die Möglichkeit für den Studio-Administrator, eine Liste von zur Löschung markierten Einträgen abzurufen und diejenigen zu entfernen, die keine Links zu Einträgen haben, die nicht zur Löschung bereit sind, wurde hinzugefügt.
  <br>

## Version 0.5.24

> **Wichtige und verbesserte Funktionalität hinzugefügt**

- Erweiterte Funktionen für dynamische und statische Filter in erweiterten Steuerelementen wie Datenraster, Listenansicht, Baumansicht, die eine On-the-Fly-Filterung von Daten vor der Anzeige für den Benutzer ermöglichen (Parameter wurden für Filter des Typs "enthält" usw. hinzugefügt).
- Erweiterung des Konzepts der Nutzung von Datenfluss & Workflow - jetzt können beide unabhängig von UI-Steuerelementen wie Schaltflächen erstellt und verwendet werden, was eine flexiblere Anwendungsstruktur ermöglicht und die Entwicklung vereinfacht.
- Viele neue Methoden, die über [Using Python](app-development/using-python.md) im Komponentenskript verfügbar sind, wurden hinzugefügt, wie das Aufrufen von Modalfenstern, Überprüfen der Bildschirmauflösung und des Gerätetyps zur Erstellung eines responsiven UI-Layouts.
- Die Möglichkeit, mit Nachrichtenwarteschlangensystemen (zum Beispiel RabbitMQ) aus dem Datenfluss zu arbeiten, wurde mit einem neuen Schritt [Subscribe to Connector](app-development/data-flow-components/subscribe-to-connector.md) hinzugefügt.
- Die Möglichkeit zur Batch-Datenverarbeitung im Datenfluss über neue Schritte [Deferred Update Entry](app-development/data-flow-components/deferred-update-entry.md) & [Apply Deferred Update Operations](app-development/data-flow-components/apply-deferred-update-operations.md) wurde hinzugefügt.
  <br>

## Version 0.4.4

> **Wichtige und verbesserte Funktionalität hinzugefügt**

- Neues Systemfeld "Name" wurde hinzugefügt, das zur Anzeige von Elementen aus Katalogen verwendet wird.
  - Bei der Anzeige eines einzelnen Elements aus dem Katalog (zum Beispiel unter Verwendung eines UI-Steuerelements "Auswahl", das auf den Katalog verweist) wird der Inhalt des Namensfelds jetzt immer angezeigt. Wenn das Namensfeld leer ist, wird der Systemkatalogname/Sequenznummer des Katalogeintrags angezeigt.
- Standard-Sortierungseinstellungen für Datenraster und Listenansicht wurden hinzugefügt.
- Automatische Ersetzung von Unicode-Sonderzeichen im Komponentenskript zur Linkgenerierung wurde hinzugefügt.
  <br>

> **Fehler korrigiert**

- Falsche Funktion des Paginators bezüglich des Wechsels mehrerer Tabellen auf einer Seite wurde behoben.
- Nicht funktionierende Scroll-Funktion in einigen Teilen des Studios wurde behoben.
  <br>

## Version 0.3.223

_Kubernetes-Cluster 0.3.223 | Docker-Mini-Image 0.2.118_

> **Wichtige und verbesserte Funktionalität hinzugefügt**

- Neuer Datenfluss-Schritt "Templated Notification senden" wurde hinzugefügt, der es ermöglicht, eine Benachrichtigung per E-Mail unter Verwendung einer angegebenen Vorlage zu senden.
- Transparenz-Eigenschaft für UI-Komponenten.
- Unterstützung für OAuth2-Authentifizierung für HTTP-Anfragen wurde hinzugefügt. Sie können jetzt die automatische Token-Generierung über OAuth konfigurieren, um eine Verbindung zur API herzustellen.
- Der Parameter "Antwort als Datei speichern" wurde im Schritt "API-Aufruf ausführen" hinzugefügt, um es Ihnen zu ermöglichen, eine Datei auf Anfrage über die API herunterzuladen.
- Die Schritte generieren jetzt keinen Newsletter mehr, sie generieren jetzt ein Feld im Modell für die spätere Verwendung, wie "Templated Notification senden".
  <br>

> **Fehler korrigiert**

- Fehler beim Arbeiten mit dem Datetime-Typ im Kalender wurden behoben.
- UI im Studio und Arbeitsplatz wurde behoben.
- Der Deaktiviert-Zustand für die Radiobutton-UI-Komponente wurde behoben.
- Lokalisierungsfehler wurden behoben.
- Die Suche im Dropdown ist jetzt nicht groß-/kleinschreibungsempfindlich.
- Probleme bei der Autorisierungsoperation einschließlich Abmeldefehlern wurden behoben. <br>