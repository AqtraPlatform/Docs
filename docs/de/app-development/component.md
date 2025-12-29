# Komponente

Komponenten sind die grundlegenden Bausteine der Plattform und bilden die Basis für die Erstellung von Anwendungen. Sie sind gekapselte Funktionseinheiten, die Daten, Benutzeroberflächen, Geschäftslogik und Prozessautomatisierung umfassen können.

## Komponententypen

1. **Einzelkomponente**:

   - Enthält das grundlegende Objektmodell zur Speicherung von Daten.
   - Beinhaltet ein UI-Modell mit Formularen und Steuerelementen.
   - Verfügt über ein Automatisierungsmodell mit Datenflüssen und Workflows.
   - Unterstützt Python-Skripte zur zusätzlichen Anpassung des Verhaltens.
   - Hat einzigartige Sicherheitsoptionen.

2. **Mehrfachkomponente**:
   - Kombiniert mehrere Komponenten, um komplexe Anwendungen zu erstellen.
   - Wird verwendet, um eine einzige Benutzeroberfläche zu erstellen, zum Beispiel in mobilen Anwendungen.

## Erstellen einer neuen Komponente

1. Öffnen Sie Studio ('https://<your-hosting-name>/studio').
2. Gehen Sie zum Menü Anwendungen/Komponenten.
3. Klicken Sie auf die Schaltfläche Hinzufügen, um eine neue Komponente oder Mehrfachkomponente zu erstellen.

## Grundlegende Komponenteneinstellungen

| Parameter         | Beschreibung                                                          |
| ----------------- | -------------------------------------------------------------------- |
| `Title`           | Der Name der Komponente, der den Benutzern angezeigt wird.                |
| `Proxy Mode`      | Bestimmt, ob die Komponente als Proxy fungiert.                         |
| `Restrict Access` | Beschränkt den Zugriff auf die Komponente.                                   |
| `Maker`           | Identifiziert den Ersteller oder Eigentümer der Komponente.                    |
| `Cron`            | Konfiguration der Startzeit einer Komponente mit Cron.                |
| `Run as User`     | Gibt den Benutzer an, in dessen Namen sie ausgeführt wird.              |
| `Access Mode`     | Definiert den Zugriffsmodus auf die Komponente.                         |
| `Description`     | Eine detaillierte Beschreibung der Komponente, ihres Zwecks und ihrer Funktionen. |
| `Domains`         | Die Domänen oder Kategorien, zu denen die Komponente gehört.            |

## Komponentenobjektmodell in der Plattform

Jede Komponente in der Plattform enthält automatisch die folgenden Felder:

- 'Id': Ein eindeutiger Komponentenbezeichner.
- 'creatorSubject': Das Subjekt, das das Objekt erstellt hat.
- 'updateSubject': Das Subjekt, das das Objekt aktualisiert hat.
- 'createdDate': Datum, an dem das Objekt erstellt wurde.
- 'updateDate': Datum, an dem das Objekt zuletzt aktualisiert wurde.

Komponenten können zusätzliche Elemente enthalten, die zu einem von elf Typen gehören können: 'string', 'datetime', 'catalog', 'number', 'integer', 'array', 'file', 'boolean', 'time', 'date', 'uri'. Jedes dieser Elemente hat seine eigenen Einstellungen.

Globale Einstellungen für alle Typen:

- 'Name': Systemname der Eigenschaft.
- 'Titel': Name der Eigenschaft, der in der Benutzeroberfläche angezeigt wird.
- 'Erforderlich': Gibt an, ob das Feld erforderlich ist.
- 'Primärschlüssel': Bestimmt, ob ein Feld ein eindeutiger Bezeichner ist.
- 'Abfrage': Bestimmt, ob das Feld in Abfragen verwendet werden kann.
- 'Virtuelle Eigenschaft': Schließt ein Feld von Synchronisierungsprozessen aus.

## Schnittstellen-Builder

Die Plattform bietet ein leistungsstarkes Tool zur Anpassung der Benutzeroberfläche für jede Komponente – den Schnittstellen-Builder. Es handelt sich um einen visuellen Editor, mit dem Sie mehrschichtige Benutzeroberflächen mithilfe von Drag-and-Drop-Funktionen erstellen und anpassen können. Der Schnittstellen-Builder ist ein Arbeitsbereich im Abschnitt Definition der Benutzeroberfläche zur Erstellung von Komponenten.

In diesem Abschnitt können Sie:

- Eine mehrschirmige App-Oberfläche mit einem intuitiven Drag-and-Drop-Editor erstellen.
- UI-Elemente aus den Kategorien Basis, Erweitert und Layout hinzufügen.
- Das Objektmodell für den Workflow und den Datenfluss der Anwendung konfigurieren.
- CSS-Stile für alle UI-Elemente anpassen.

Nachdem Sie UI-Elemente zum Seitenlayout Ihrer App hinzugefügt haben, können Sie die folgenden Operationen durchführen:

- **Kopieren:** Kopiert das aktuelle Element in die Zwischenablage.
- **Einfügen:** Fügt das kopierte Element an einem neuen Ort ein.
- **Verschieben:** Ändert die Position des Elements.
- **Eigenschaften:** Öffnet das Eigenschaftenfenster zur Konfiguration des Elements.
- **Vorschau:** Zeigt das Layout in einem Format an, das der Anwendung des Benutzers nahekommt.
- **Markup-Vorschau:** Zeigt das textuelle Web-Markup der Seite an.
- **Löschen:** Löscht das ausgewählte Element.
- **Datenfeld:** Ermöglicht es Ihnen, ein Element an ein Datenfeld (Datenbankverknüpfung) zu binden.

## Webparts-Modul: „Stile“ und „JavaScript“

Der Block „Stile“ ist dafür ausgelegt, die CSS-Stile zu beschreiben, die auf die Komponente angewendet werden, während der Block „JavaScript“ es Ihnen ermöglicht, Interaktionen mit der Benutzeroberfläche herzustellen und zusätzliche Funktionalitäten mit der Programmiersprache JavaScript bereitzustellen.

Auf diese Weise ermöglicht das Webparts-Modul Entwicklern, komplexere und interaktive Komponenten zu erstellen, indem verschiedene Programmiersprachen zur Beschreibung von Stilen und Funktionalitäten verwendet werden.<br>

### Verwendung von "JavaScript"

Beispiel für die Verwendung von JavaScript zur Implementierung von Funktionen zum Erstellen von Schaltflächen, deren Drücken einen Screenshot erstellt:

1. Um JavaScript-Funktionen aus dem Block „Webparts“ aufzurufen, ist es notwendig, die Methode context.InvokeInterop(methodName, objects) innerhalb des Komponentenskripts zu verwenden:

````python
def capturePage1():
    context.InvokeInterop("callScreenshot")

2. Next, we move to the 'JavaScript' section of the 'Web parts' block and prepare function:
```javascript
// Erstellen eines <script>-Elements zum Laden der html2canvas-Bibliothek
var script = document.createElement('script');
script.src = "https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js";
document.head.appendChild(script);

// Funktion zum Erstellen und Herunterladen eines Screenshots der Seite
function takeScreenshot() {
    // Capturing a screenshot of the entire body using html2canvas
    html2canvas(document.body).then(canvas => {
        // Creating a link for downloading the screenshot
        var link = document.createElement('a');
        link.href = canvas.toDataURL("image/png");
        link.download = "screenshot.png";
        // Adding the link to the HTML document and simulating a click to download the screenshot
        document.body.appendChild(link);
        link.click();
        // Removing the link from the document after the screenshot has been downloaded
        document.body.removeChild(link);
    });
}

// Methode zum Aufrufen der takeScreenshot-Funktion
this.callScreenshot = () => {
    takeScreenshot();
}

Dieser Code erstellt ein Skriptelement, das die Bibliothek html2canvas von einem Content Delivery Network (CDN) lädt. Nach dem Laden der Bibliothek wird eine Funktion takeScreenshot() definiert, die einen Screenshot der aktuellen Seite mit html2canvas aufnimmt.

Nach der Erstellung des Screenshots erstellt der Code ein <a>-Element, um den Download zu ermöglichen, setzt dessen href auf die Bild-URL im PNG-Format und das Download-Attribut auf screenshot.png. Dann fügt es diesen Link zum Dokumentenbody hinzu, emuliert einen Klick auf diesen Link, um den Screenshot herunterzuladen, und entfernt schließlich den Link aus dem Dokument.

### Verwendung von "Stilen"

Beispiel-CSS-Code, der die Hintergrundfarbe Ihres gesamten Arbeitsbereichs festlegt

```css
body {
    background-color: violet; /* Purple background color */
}
```

## Datenfluss und Workflow-Erstellung {: #dataflow-workflow }

Das Objektmodell jeder Komponente enthält Daten, die sowohl innerhalb der Komponente selbst als auch in den Prozessen ihrer Integration mit anderen Elementen des Systems verwendet werden. Diese Daten dienen als Grundlage für die Konfiguration und Ausführung von Datenflüssen und Workflows.

Um mit dem Erstellen eines Datenflusses oder Workflows zu beginnen, müssen Sie eines der Elemente aus den "Flows" in den Bereich des Interface-Builders ziehen, nach dem Sie den visuellen Editor des Datenflusses und Workflows anpassen können.

Erfahren Sie mehr über [Datenflusskomponenten](data-flow-components/index.md) und [Workflow-Komponenten](workflow-components/index.md)

## Veröffentlichung einer Komponente und Übertragung in die Weboberfläche {: #publication }

- Nachdem Sie die Konfiguration der Komponente abgeschlossen haben, müssen Sie sie als Teil einer neuen Veröffentlichung veröffentlichen.
- Die Verwaltung von Veröffentlichungen wird in [Anwendungen veröffentlichen](publishing-applications.md) beschrieben.
- Als Nächstes müssen Sie zum Menü „Start“ zurückkehren und zum „Navigationsmenü“ des gewünschten „Anwendungsbereichs“ gehen, auf „Menüelement hinzufügen“ klicken, die gewünschte Komponente auswählen, die Parameter ausfüllen und auf „Speichern“ klicken.

![Navigationsmenü](../assets/images/app-development/navigation-menu.png)