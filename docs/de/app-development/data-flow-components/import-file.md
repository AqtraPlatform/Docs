# Importdatei

![](../../assets/images/app-development/import-file.png)

## Allgemeine Informationen
Der Schritt „Importdatei“ wird verwendet, um Daten aus .csv-, Excel- oder JSON-Dateien zu importieren. Die Daten werden zeilenweise importiert und entsprechen dem im Abschnitt „Feldzuordnung“ beschriebenen Format. Um eine Datei zu importieren, sollten Sie die Datei in das Feld für den Dateityp laden und dieses Feld im Parameter „Dateiinformationsfeld“ angeben.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld     | Wertoptionen      | Zweck      |
|----------------------|-------------------|------------|
| Schrittname          | -                 | Name des Schrittes |
| Quellenschritt       | -                 | Auswahl des vorherigen Schrittes |
| Dateiinformationsfeld | -                 | Feld, das die zu importierende Datei enthält |
| Eingabedateityp     | .csv, .xlsx, .json| Dateiformat für den Import |
| Spaltentrenner       | ;                 | Spaltentrenner für CSV-Dateien |
| Erste Zeilen ignorieren| 0                | Anzahl der ersten Zeilen, die in der Datei ignoriert werden sollen |
| Feldzuordnung        | -                 | Zuordnung der Komponentenfelder zu den Dateispalten |

## Fälle
- **Tabellarische Daten importieren**: Wird verwendet, um Daten aus CSV- oder Excel-Dateien zu laden und die Zuordnung zwischen Dateispalten und Komponentenfeldern anzupassen.
- **Strukturierte Daten importieren**: Geeignet für den Import von JSON-Dateien, die strukturierte Daten enthalten.

## Ausnahmen
- **Falsche Feldzuordnung**: Fehler in der Einstellung „Feldzuordnung“ können zu einem fehlerhaften Datenimport führen.
- **Uninformative Zeilen ignorieren**: Sie müssen genau die Anzahl der Zeilen angeben, die ignoriert werden sollen, bevor Sie mit dem Import von Daten beginnen.

## Anwendungsszenario

Diese Komponente ist eine Schnittstelle zum Hochladen von Dateien im **CSV**- und **XLSX**-Format. Sie umfasst Felder für drei **CSV**-Datenmodellfelder und drei **XLSX**-Datenmodellfelder sowie ein Feld für den Datei-Upload. Zwei Datenflüsse werden für den Dateiimport, die Skriptausführung und die Datenspeicherung verwendet.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/10P0-XqSZOKV7wZzg8uH6NR1VnxZ0-8RB/view?usp=sharing) herunterladen.