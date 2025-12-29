# Skript ausführen

![](../../assets/images/app-development/execute-script.png)

## Allgemeine Informationen
Der Schritt „Skript ausführen“ ist dafür konzipiert, Python-Skripte mit standardmäßigen Python-Bibliotheken auszuführen.

Dieser Schritt ermöglicht es Ihnen, Python-Skripte beliebiger Komplexität im aktuellen Datenflussmodell auszuführen. Mit dem Skript können Sie das Modell ändern, indem Sie neue Variablen hinzufügen oder die Werte vorhandener Variablen ändern.

Beispiele für die Verwendung:
- Um den Wert einer Variablen aus dem Schritt „Aktionsmodell abrufen“ zu erhalten: `item ['data'] ['Property_name'] `
- Um eine neue Variable im Skript zu erstellen: `item ['Property_name'] `

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld | Wertoptionen | Zweck |
|------------------|--------------|-------|
| Schrittname      | -            | Name des Schrittes |
| Quellenschritt   | -            | Auswahl des vorherigen Schrittes |

## Anwendungsfälle
- **Anpassung der Datenverarbeitung**: Geeignet für komplexe Datenverarbeitungslogik, die mit standardmäßigen Datenflusswerkzeugen nicht umgesetzt werden kann.
- **Hinzufügen und Ändern von Daten**: Geeignet für Szenarien, die das Hinzufügen neuer Daten oder das Ändern vorhandener Daten im Modell erfordern.

## Ausnahmen
- **Bedarf an Python-Kenntnissen**: Erfordert Kenntnisse in Python und ein Verständnis der Logik der Arbeit mit Datenflüssen.
- **Variablen-Typisierung**: Strenge Typisierung von Variablen kann zusätzliche Aufmerksamkeit beim Schreiben von Skripten erfordern. Unterstützte Typen: `@number`, `@integer`, `@string`, `@uuid`, `@boolean`, `@uri`, `@date`, `@date-time`, `@time`, `@catalog`, `@array`.

## Anwendungsszenario

Diese Komponente zeigt verschiedene Nutzungsszenarien des Schrittes „Skript ausführen“ innerhalb eines Datenflusses, einschließlich der Erstellung neuer Variablen unterschiedlicher Typen und der Modifizierung von Werten verfügbarer Felder im Datenmodell.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/18fbg2g2rcvXORI7i31zu81NdSKwMqE99/view?usp=sharing) herunterladen.