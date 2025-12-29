# Workflow ausführen

![](../../assets/images/app-development/execute-workflow.png)

## Allgemeine Informationen
Der Schritt „Workflow ausführen“ wird verwendet, um einen bestimmten Workflow im System zu aktivieren und auszuführen.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld      | Wertoptionen | Zweck |
|-----------------------|--------------|-------|
| Schrittname           | -            | Name des Schrittes |
| Quellenschritt        | -            | Auswahl des vorherigen Schrittes |
| Komponente            | -            | Die Komponente, innerhalb der der Workflow ausgeführt wird |
| Workflow              | -            | Name des abzuschließenden Workflows |
| Eingabefeld der Komponente | -        | Das Feld in der Komponente, das verwendet wird, um Daten an den Workflow zu übertragen |

## Fälle
- **Dynamische Datenflusskontrolle**: Es kann verwendet werden, um spezifische Workflows basierend auf Daten zu starten, die aus vorherigen Dataflow-Schritten erhalten wurden, was es ermöglicht, flexible und anpassungsfähige Datenmanagementsysteme zu erstellen.

## Ausnahmen
- **Abhängigkeit von der Datenkorrektheit**: Um Fehler bei der Ausführung des Workflows zu vermeiden, ist es notwendig sicherzustellen, dass die an den Workflow gesendeten Daten genau und vollständig sind.
- **Koordination zwischen Dataflow und Workflow**: Es ist wichtig, die Interaktion zwischen Dataflow und Workflow sorgfältig zu konfigurieren, um einen reibungslosen und korrekten Transfer von Daten und Befehlen zwischen ihnen zu gewährleisten.

## Anwendungsszenario

Die erstellte Komponente dient als Schnittstelle zur Interaktion mit dem Datenmodell, das ein Feld „user_name“ vom Typ String enthält. Diese Komponente umfasst die Funktionalität zur Aktualisierung des Datenmodells mithilfe des Schrittes Modell aktualisieren innerhalb des Workflows. Um mit der Komponente zu interagieren, kann der Benutzer seinen Namen eingeben, auf eine Schaltfläche klicken, wonach die Daten gesendet werden und der Name nach dem Aktualisieren der Seite im Datenraster angezeigt wird.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1AgjjrOW-z2LPMj7sFWg_PKjHjFfVtxub/view?usp=sharing) herunterladen.