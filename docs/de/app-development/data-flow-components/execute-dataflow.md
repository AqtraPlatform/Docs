# Datenfluss ausführen

![](../../assets/images/app-development/execute-dataflow.png)

## Allgemeine Informationen
Der Schritt "Datenfluss ausführen" wird verwendet, um Dataflow von einer veröffentlichten Komponente aus aufzurufen. Dieser Schritt ermöglicht es Ihnen, einen zusätzlichen Datenfluss im Kontext des aktuellen Datenverarbeitungsprozesses auszuführen.

Wenn er mit einem Array-Feld verwendet wird, das aus einer externen Quelle oder aus einem Array-Feld (Eigenschaft) stammt, analysiert der Schritt dieses Array und startet die parallele Verarbeitung jedes Datensatzes oder Objekts, das im Array enthalten ist.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld    | Wertoptionen | Zweck |
|---------------------|--------------|-------|
| Schrittname         | -            | Name des Schrittes |
| Quellenschritt      | -            | Auswahl des vorherigen Schrittes |
| Komponente          | -            | Die Komponente, von der der Datenfluss aufgerufen wird |
| Datenfluss          | -            | Name des auszuführenden Datenflusses |
| Ergebnisfeld        | -            | Feld zum Speichern des Ergebnisses der Datenflussausführung |

## Anwendungsfälle
- **Aktualisierung von Daten aus anderen Datenflüssen**: Der Schritt "Datenfluss ausführen" ist ideal für Situationen, in denen Sie Felder im aktuellen Modell mit Daten aktualisieren möchten, die in anderen Datenflüssen gesammelt oder verarbeitet wurden. Dies ermöglicht eine effektive Integration und Synchronisierung von Daten zwischen verschiedenen Prozessen und Komponenten.
- **Externer Datenflussaufruf**: Wird verwendet, um zusätzliche Datenflüsse als Teil des aktuellen Datenverarbeitungsprozesses zu integrieren und zu starten.

## Ausnahmen
- **Abhängigkeit von der Richtigkeit anderer Datenflüsse**: Die Effektivität des Schrittes "Datenfluss ausführen" hängt direkt von der Genauigkeit und Zuverlässigkeit der aus anderen Datenflüssen erhaltenen Daten ab. Alle verwandten Datenflüsse sollten sorgfältig konfiguriert und getestet werden, um sicherzustellen, dass die aktualisierten Daten korrekt und aktuell sind.

## Anwendungsszenario

Diese Komponente erstellt einen Datenfluss, um Operationen auf den Daten der aktuellen Komponente durchzuführen. Sie umfasst Schritte des Get-Aktionsmodells, um das Datenflussmodell abzurufen, und Schritte des Datenflussausführens, um den Datenfluss mit geeigneten Parametern wie der Auswahl der aktuellen Komponente, der Wahl des auszuführenden Datenflusses, der Konfiguration der Ergebnisfelder und der Anzeige von Definitionen aus der Datenkomponente auszuführen. Diese Komponente ermöglicht Datenoperationen an der Komponente direkt über die Anwendungsoberfläche.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1ekmRNTRgO30koKm04pyhEZsXG9W5T-O-/view?usp=sharing) herunterladen.