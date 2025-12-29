# Gruppieren nach

![](../../assets/images/app-development/group-by.png)

## Allgemeine Informationen
Der Schritt „Gruppieren nach“ wird verwendet, um Daten zu sammeln und zu gruppieren, die in vorherigen Schritten aufgeteilt wurden, beispielsweise mit der „Extrahieren Sammlung“. Die Hauptfunktion dieses Schrittes besteht darin, Daten nach bestimmten vom Benutzer angegebenen Schlüsseln zu gruppieren. Der Schritt sammelt die aufgeteilten Daten und kombiniert nur die Einträge, die mit den angegebenen Schlüsseln übereinstimmen.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld | Wertoptionen | Zweck |
|------------------|--------------|-------|
| Schrittname      | -            | Name des Schrittes |
| Quellenschritt   | -            | Auswahl des vorherigen Schrittes |
| Schlüssel        | -            | Schlüssel, die zum Gruppieren von Daten verwendet werden |

## Fälle
- **Kombinieren von aufgeteilten Daten**: Wird verwendet, um Daten zu kombinieren, die in den vorherigen Schritten, wie der „Extrahieren Sammlung“, unter Verwendung spezifischer Schlüssel aufgeteilt wurden.
- **Datensegmentierung und -analyse**: Geeignet für Fälle, in denen es notwendig ist, Daten nach bestimmten Kategorien oder Kriterien zu analysieren.

## Ausnahmen
- **Abhängigkeit von Gruppierungsschlüsseln**: Die Genauigkeit und Relevanz der Schlüssel sind entscheidend für die ordnungsgemäße Gruppierung der Daten.
- **Schwierigkeiten bei der Datenverarbeitung und -analyse**: Gruppierung kann schwierig sein, wenn die Datenstruktur variabel ist oder die Schlüssel Gruppen nicht eindeutig identifizieren.

## Anwendungsszenario

Diese Komponente überprüft die Verfügbarkeit von Feldern im Schritt Gruppieren nach. Im Datenfluss werden zunächst ein Get-Aktionsmodell-Schritt und ein Gruppieren nach Schritt hinzugefügt. Dann wird im Frontend die importierte Komponente geöffnet, und der „Netzwerk“-Tab in den Entwicklertools des Browsers wird geöffnet. Danach wird im Frontend auf die Schaltfläche „Gruppieren nach“ geklickt. Wenn der Schritt korrekt funktioniert, sollte eine „execute“-Zeile mit einer Vorschau der HTTP-Antwort im Netzwerk-Tab erscheinen, die Daten mit dem Schlüssel „ETO test123“ und deren Aggregation enthält.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1fKeJh3a0HHcG7VuFs-Tx5YdS7H6C7mI0/view?usp=sharing) herunterladen.