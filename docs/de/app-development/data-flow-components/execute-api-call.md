# API-Aufruf ausführen

![](../../assets/images/app-development/execute-api-call.png)

## Allgemeine Informationen
Der Schritt „API-Aufruf ausführen“ wird verwendet, um mit externen Systemen über die API zu interagieren. Dieser Schritt kann für verschiedene Arten von Anfragen konfiguriert werden, einschließlich des Empfangs von Daten (GET), des Sendens von Daten (POST/PUT) oder des Löschens von Daten (DELETE) in einem externen System. Abhängig vom Nutzungskontext kann dieser Schritt einer der ersten Schritte im Dataflow sein, um Daten zu erhalten, oder einer der letzten Schritte, um Daten in externen Systemen zu aktualisieren.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld   | Wertoptionen | Zweck |
|-------------------|-------------------|------------|
| Schrittname       | -                 | Name des Schrittes |
| Quellenschritt    | -                 | Auswahl des vorherigen Schrittes |
| Ergebnisfeld      | -                 | Ein Feld zum Speichern der ID eines erstellten oder verarbeiteten Eintrags |
| System            | -                 | Auswahl eines Integrationssystems |
| Connector         | -                 | Auswahl eines Connectors im Integrationssystem |
| Abfragepfad       | -                 | Endpunkt für die Anfrage |
| Methodenname      | Get, Post, Put, Delete | Art der Anfrage, die abgeschlossen werden soll |
| Parameterzuordnung| -                 | Dynamische Konfiguration zur Abfragefilterung |

## Anwendungsfälle
- **Daten von externen Quellen abrufen**: Wird verwendet, um Daten von externen Systemen herunterzuladen, was besonders nützlich sein kann, wenn man mit externen Diensten oder Datenbanken integriert.
- **Daten senden oder aktualisieren**: Geeignet zum Senden von Daten an externe Systeme oder zum Aktualisieren vorhandener Daten, beispielsweise beim Synchronisieren von Änderungen, die im Dataflow vorgenommen wurden.
- **Daten löschen**: Kann verwendet werden, um Daten aus externen Systemen zu löschen, was hilft, die Relevanz und Integrität der Daten in integrierten Systemen aufrechtzuerhalten.

## Ausnahmen
- **Bedarf an asynchroner Verarbeitung**: Der Schritt wird asynchron ausgeführt, was die Berücksichtigung der Reaktionszeit externer Systeme und der potenziellen Auswirkungen auf die Datenverarbeitungsreihenfolge erfordert.
- **Anforderung an die Connector-Konfiguration**: Die Effektivität des Schrittes hängt von korrekt konfigurierten Integrationssystemen und Connectors sowie von der Genauigkeit der Bestimmung des Endpunkts und der Anfrageparameter ab.

## Anwendungsszenario

Die Komponente erstellt eine einfache Integration zum Abrufen von Daten, wie z.B. Wetter, über eine API. Im Datenfluss werden Schritte verwendet, um die API-Anfrage zu konfigurieren, einschließlich der Ausführung eines Skripts zur Erstellung von API-Variablen, dem Aufruf der API und dem Speichern der Ergebnisse. Anschließend wird die Integration im System ausgewählt und konfiguriert, und die Ergebnisse werden im Frontend über ein Formular angezeigt, das mit der Skriptausführung verknüpft ist. Die Funktion in der Komponente verarbeitet die abgerufenen Daten zur Anzeige für den Benutzer.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/119_NZiqzENXCaqdmiZ7qj4ZmeHcje7je/view?usp=sharing) herunterladen.