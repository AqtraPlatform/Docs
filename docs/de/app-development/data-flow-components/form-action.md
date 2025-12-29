# Formularaktion

![](../../assets/images/app-development/form-action.png)

## Allgemeine Informationen
Der Schritt „Formularaktion“ wird verwendet, um verschiedene Aktionen in der Benutzeroberfläche (UI) im Frontend der Anwendung auszuführen, wie das Öffnen von Seiten, das Ausführen von Skripten, das Öffnen von Modalfenstern usw. Der Schritt ist die Verbindung zwischen der Serverlogik und der Benutzeroberfläche, die es Ihnen ermöglicht, das Verhalten der UI dynamisch zu steuern.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld | Wertoptionen | Zweck |
|------------------|--------------|-------|
| Schrittname      | -            | Name des Schrittes |
| Quellschritt     | Mehrfachauswahl aus dem Katalog | Auswahl aus den vorherigen Schritten |
| Formularaktion    | Skript ausführen, Seite öffnen, Komponente öffnen, Sidebar öffnen, Modal öffnen, Datei in neuem Tab öffnen | UI-Befehlsart |
| Methodename      | (Wenn „Skript ausführen“ ausgewählt ist) | Name der auszuführenden Skriptfunktion |
| Seite öffnen     | (Wenn „Seite öffnen“ ausgewählt ist) | Liste der zu öffnenden Seiten |
| Dateiinformationsfeld | (Wenn „Datei in neuem Tab öffnen“ ausgewählt ist) | Dateiinformationsfeld zum Öffnen |
| Sidebar öffnen   | Einstellungen für die Sidebar | Konfiguration zum Öffnen der Sidebar |
| Modal öffnen     | Einstellungen für Modalfenster | Konfiguration zum Öffnen eines Modalfensters |

## Fälle
- **Dynamische Verwaltung von UI-Elementen**: Die Verwendung von „Sidebar öffnen“ oder „Modal öffnen“ ermöglicht es Ihnen, Sidebars oder Modale mit zusätzlichen Informationen, Formularen oder anderen Inhalten dynamisch anzuzeigen, was die Interaktivität und Benutzerfreundlichkeit der Oberfläche erhöht.
- **Datenrasteraktualisierung**: In einem Skript, in dem der Benutzer einige neue Daten lädt, können Sie eine Aktualisierungsfunktion zum Formular hinzufügen, und das Datenraster wird aktualisiert, ohne die Seite zu aktualisieren.

## Ausnahmen
- **Schritt „Antwort schreiben“ erforderlich**: Nach dem Ausführen von Aktionen wie dem Öffnen einer Seite oder Datei müssen Sie einen Schritt „Antwort schreiben“ hinzufügen, um den Datenfluss korrekt abzuschließen.
- **Abhängigkeit von vorherigen Schritten**: Bei der Verwendung bestimmter Aktionen, wie „Datei in neuem Tab öffnen“, müssen Sie eine geeignete Datei haben, die von den vorherigen Schritten vorbereitet wurde.

## Anwendungsszenario

Diese Komponente verwendet verschiedene Methoden im Schritt „Formularaktion“, um mit der Benutzeroberfläche im Frontend zu interagieren. Benutzer können verschiedene Aktionen ausführen, wie das Ausführen eines Skripts (Skript ausführen), das Öffnen einer Seite (Seite öffnen) oder einer Komponente (Komponente öffnen), das Herunterladen einer Datei (Datei herunterladen) und das Öffnen einer Datei in einem neuen Tab (Datei in neuem Tab öffnen). Nachdem diese Aktionen ausgeführt wurden, werden die Daten verarbeitet und mit dem Schritt „Antwort schreiben“ an das Frontend zurückgesendet.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1AgjjrOW-z2LPMj7sFWg_PKjHjFfVtxub/view?usp=sharing) herunterladen.