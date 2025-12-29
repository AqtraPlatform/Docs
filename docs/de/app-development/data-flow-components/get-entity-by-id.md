# Get entity by id

![](../../assets/images/app-development/get-entity-by-id.png)

## Allgemeine Informationen
Der Schritt „Get Entity by ID“ wird verwendet, um ein Komponentenobjekt anhand seiner eindeutigen Kennung (ID) abzurufen. Dieser Schritt wird normalerweise in Kombination mit anderen Schritten verwendet, wie z.B. „Lookup“ oder „Update Entry“, die eine ID zurückgeben, die für diesen Schritt geeignet ist.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld | Wertoptionen | Zweck |
|------------------|--------------|-------|
| Schrittname      | -            | Name des Schrittes |
| Quellschritt     | -            | Auswahl des vorherigen Schrittes |
| Src-Feld         | -            | Feld, das die zu suchende ID enthält |
| Dst-Feldname     | -            | Feld, in dem das Ergebnis aufgezeichnet wird |
| Komponente       | -            | Komponente, die gesucht wird |

## Fälle
- **Datensuche nach ID**: Wird verwendet, um einen bestimmten Eintrag genau abzurufen, indem die ID aus der Komponente verwendet wird.

## Ausnahmen
- **Abhängigkeit von der ID-Genauigkeit**: Die genaue ID muss angegeben und in den Quelldaten verfügbar sein, damit die Abfrage erfolgreich ist.
- **Umgang mit Inkonsistenzen**: Wenn es keinen Eintrag mit der angegebenen ID gibt, kann der Schritt ein leeres Ergebnis zurückgeben.

## Anwendungsszenario

Diese Komponente ermöglicht das Hinzufügen eines Katalogfeldes und das Erstellen eines Datenflusses, um eine Entität anhand ihrer Kennung abzurufen. Das Katalogfeld wird auf der Seite platziert, um den entsprechenden Wert aus dem Katalog auszuwählen. Der Datenfluss umfasst einen Schritt „Get action model“ zur Initialisierung, einen Schritt „Get entity by id“ zum Abrufen der Entität anhand der Kennung unter Verwendung des ausgewählten Wertes aus dem Katalog und einen Schritt „Write response“ zur Ausgabe des Ergebnisses.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1eCxoYHKg0Zl8APxnUMRA9qmpqNkrtfuW/view?usp=sharing) herunterladen.