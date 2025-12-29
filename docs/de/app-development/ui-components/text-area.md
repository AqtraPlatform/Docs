# Textbereich

![](../../assets/images/app-development/text-area.png)

## Allgemeine Informationen
Der Textbereich ist eine grundlegende UI-Komponente, die zum Eingeben und Anzeigen von mehrzeiligem Text entwickelt wurde. Er eignet sich ideal zum Tippen großer Textmengen, wie z.B. Kommentare oder Beschreibungen, und bietet ausreichend Platz für ein einfaches Tippen.

## Parameter
**Komponenten-Eigenschaften:**

| Einstellungsgruppe | Einstellungsfeld   | Wertoptionen         | Zweck |
|--------------------|--------------------|----------------------|-------|
| (Globale Einstellungen) | Name             | -                    | Name der UI-Komponente im System |
| Allgemein          | Deaktiviert        | true, false          | Deaktivierung eines Elements |
|                    | Automatische Größe | true, false          | Automatische Größenkontrolle |
|                    | Erforderlich       | true, false          | Pflichtfeld zum Ausfüllen |
|                    | Beschriftung       | -                    | Beschreibung des Eingabefelds |
|                    | Bindung           | Mehrfachauswahl des Katalogs | Datenbindung |
| Ereignisse         | Bei Wertänderung   | -                    | Ereignis bei Wertänderung |
| Tab-Index          | -                  | Ganzzahl             | Reihenfolge des Feldwechsels |

**CSS-Eigenschaften:**

| Einstellungsgruppe | Einstellungsfeld   | Wertoptionen         | Zweck |
|--------------------|--------------------|----------------------|-------|
| Layout             | Breite             | -                    | Breite der Komponente |
|                    | Höhe               | -                    | Höhe der Komponente |
|                    | Wachsen            | true, false          | Dehnen der Komponente |
|                    | Rand               | -                    | Äußere Polsterung |
|                    | Innenabstand       | -                    | Innere Polsterung |
| Erscheinung        | Eckenradius        | -                    | Eckenradius |
|                    | Randdicke          | -                    | Randdicke |
| Pinsel             | Hintergrund        | -                    | Hintergrundfarbe |
|                    | Randpinsel         | -                    | Randfarbe |

## Anwendungsfälle
- **Mehrzeilige Eingabe**: Ideal für Formulare, die große Textmengen erfordern.
- **Kommentare & Beschreibungen**: Wird verwendet, um Kommentare, Beschreibungen oder andere Skripte zu schreiben, bei denen eine mehrzeilige Eingabe erforderlich ist.

## Ausnahmen
- **Eingeschränkte Formatierung**: Wie die meisten Texteingabefelder schränkt der Textbereich die Verwendung komplexer Formatierungen, wie Hyperlinks oder eingebettete Bilder, ein.