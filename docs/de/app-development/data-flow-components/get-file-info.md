# Dateiinformationen abrufen

![](../../assets/images/app-development/get-file-info.png)

## Allgemeine Informationen
Der Schritt „Dateiinformationen abrufen“ in Dataflow wird verwendet, um Informationen über eine Datei anhand ihrer ID abzurufen. Dieser Schritt bietet Zugriff auf verschiedene Eigenschaften der Datei, einschließlich ihres Namens, ihrer Erweiterung (Typ), Größe, Datum der Aktualisierung, Erstellung sowie des Autors der ursprünglichen und aktualisierten Datei.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld | Wertoptionen | Zweck |
|------------------|--------------|-------|
| Schrittname      | -            | Name des Schrittes |
| Quellenschritt   | -            | Auswahl des vorherigen Schrittes |
| Src-Feld         | -            | Feld, das die Datei-ID enthält |
| Dst-Feldname     | -            | Feld, in dem die Informationen über die Datei aufgezeichnet werden |

## Fälle
- **Dateiinformationsextraktion**: Wird verwendet, um detaillierte Informationen über eine Datei zu erhalten, die für die nachfolgende Datenverarbeitung oder Analyse nützlich sein können.
- **Daten für zusätzliche Verarbeitung vorbereiten**: Die erhaltenen Informationen über die Datei können in nachfolgenden Schritten, wie „Skript ausführen“ oder „Quelle filtern“, verwendet werden, um spezifische Operationen je nach den Eigenschaften der Datei durchzuführen.

## Ausnahmen
- **Abhängigkeit von der Genauigkeit der Datenquelle**: Die Genauigkeit der erhaltenen Informationen hängt von der Genauigkeit und Relevanz der Daten in der Quelle ab.
- **Eingeschränkte Informationen**: Der Schritt bietet nur grundlegende Informationen über die Datei und enthält möglicherweise nicht einige spezifische oder zusätzliche Daten.