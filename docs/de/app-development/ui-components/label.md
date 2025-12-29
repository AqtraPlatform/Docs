# Label

![](../../assets/images/app-development/label.png)

## Allgemeine Informationen
Label ist eine grundlegende UI-Komponente, die entwickelt wurde, um nicht bearbeitbare Textfelder auf Screenshots anzuzeigen. Diese Komponente wird häufig verwendet, um beschreibenden Text, Titel hinzuzufügen oder einfach Informationen anzuzeigen, die der Benutzer nicht ändern kann.

## Parameter
**Komponenten-Eigenschaften:**

| Einstellungsgruppe | Einstellungsfeld   | Wertoptionen         | Zweck |
|--------------------|--------------------|----------------------|-------|
| (Globale Einstellungen) | Name             | -                    | Name der UI-Komponente im System |
| Text               | Schriftgröße       | -                    | Größe der Schrift |
|                    | Farbe              | -                    | Textfarbe (CSS) |
|                    | Fett               | true, false          | Fette Schrift |
|                    | Kursiv            | true, false          | Kursivschrift |
|                    | Textausrichtung    | Links, Rechts, Mitte, Blocksatz | Textausrichtung |
| Allgemein          | Bindung           | Mehrfachauswahl aus Katalog | Bindung an Daten |
|                    | Wert               | -                    | Statischer Feldwert |
|                    | Format             | -                    | Daten-Eingabe/Ausgabeformat (Für DataTime) |

**CSS-Eigenschaften:**

| Einstellungsgruppe | Einstellungsfeld   | Wertoptionen         | Zweck |
|--------------------|--------------------|----------------------|-------|
| Layout             | Elemente ausrichten | Keine, Mitte, Ende, Anfang, Strecken | Ausrichten von Elementen in einem Flex-Container |
|                    | Breite             | -                    | Breite der Komponente |
|                    | Höhe               | -                    | Höhe der Komponente |
|                    | Wachsen            | true, false          | Strecken einer Komponente in einem Container |
|                    | Außenabstand       | -                    | Äußere Polsterung |
|                    | Innenabstand       | -                    | Innere Polsterung |
| Erscheinung        | Eckenradius        | -                    | Eckenradius |
|                    | Rahmenstärke       | -                    | Rahmenstärke |
| Pinsel             | Hintergrund        | -                    | Hintergrundfarbe |
|                    | Rahmenpinsel       | -                    | Rahmenfarbe |

## Anwendungsfälle
- **Informationstipps**: Verwendung eines Labels, um unterstützende Informationen neben anderen UI-Elementen bereitzustellen, wie z.B. die Funktionen von Schaltflächen oder Eingabedaten zu erklären.
- **Abschnittsüberschriften**: Labels können als Überschriften für verschiedene Abschnitte der Benutzeroberfläche dienen und den Inhalt klar abgrenzen, um die Benutzererfahrung zu verbessern.
- **Statusanzeige**: In Fällen, in denen es notwendig ist, den Status oder das Ergebnis einer Operation anzuzeigen, kann ein Label verwendet werden, um die entsprechenden Nachrichten anzuzeigen (zum Beispiel „Lädt...“, „Erfolgreich abgeschlossen“).

## Ausnahmen
- **Nicht-Bearbeitbarkeit**: Label ist nicht für Benutzereingaben oder die Bearbeitung von Text gedacht. Der Versuch, es für diese Zwecke zu verwenden, führt zu einem ineffektiven Interface-Design.
- **Formatbeschränkungen**: Während Label ein gewisses Maß an Textanpassung zulässt, kann es keine komplexen Textelemente wie Hyperlinks oder Inline-Bilder enthalten.