# Distinct

![](../../assets/images/app-development/distinct.png)

## Allgemeine Informationen
Der Distinct-Schritt wird verwendet, um doppelte Einträge aus dem Datenstrom zu entfernen und nur eindeutige Werte zu hinterlassen. Dieser Prozess hilft, die Datenverarbeitung zu optimieren, indem Duplikate eliminiert und die Menge der analysierten Daten reduziert wird.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld | Wertoptionen | Zweck                           |
|------------------|--------------|---------------------------------|
| Schrittname      | -            | Name des Schrittes im Datenfluss |
| Quellenschritt   | -            | Auswahl des vorherigen Schrittes |
| Schlüssel        | -            | Schlüssel zur Überprüfung der Eindeutigkeit |

## Fälle
- **Datenbereinigung**: Entfernen von doppelten Einträgen zur Vereinfachung der Analyse.
- **Vorbereitung auf Aggregation**: Vorreinigung der Daten vor der Durchführung von Aggregationsoperationen.

## Ausnahmen
- **Auswahl der Schlüssel**: Falsche Auswahl der Schlüssel kann zum Verlust wichtiger Daten führen.
- **Informationsverlust**: Risiko, Teile der Daten zu verlieren, wenn der Schritt falsch konfiguriert ist.

## Anwendungsszenario

Diese Komponente überprüft die Verfügbarkeit von Feldern im Distinct-Schritt. Der "Distinct"-Button wird im Frontend angeklickt. Wenn der Schritt korrekt funktioniert, sollte eine "execute"-Zeile mit einer Vorschau der HTTP-Antwort im Netzwerk-Tab erscheinen, die Daten für drei Datensätze enthält.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1dA9EzzJOn9sWBYhdvL__AcI1kJ5qNNLd/view?usp=sharing) herunterladen.