# WYSIWYG-Editor

![](../../assets/images/app-development/wysiwyg-editor.png)

## Allgemeine Informationen
Der WYSIWYG-Editor ist eine UI-Komponente, die zum Eingeben und Bearbeiten von Rich-Text im WYSIWYG-Format entwickelt wurde. Er bietet Funktionen, die ähnlichen Editoren wie Wordpad entsprechen, und ermöglicht es den Benutzern, Text einfach zu formatieren und verschiedene Medienelemente einzufügen.

## Parameter
**Komponenten-Eigenschaften:**

| Einstellungsgruppe | Einstellungsfeld   | Wertoptionen          | Zweck |
|--------------------|--------------------|-----------------------|-------|
| (Globale Einstellungen) | Name             | -                     | Name der UI-Komponente im System |
| Allgemein          | Deaktiviert        | true, false           | Deaktivierung eines Elements |
|                    | Erforderlich       | true, false           | Erforderliches Feld zum Ausfüllen |
|                    | Plugins            | -                     | Aktivierung von Plugins |
|                    | Beschriftung       | -                     | Feldbeschreibung |
|                    | Bindung            | Multiselect des Katalogs | Datenbindung |
| Ereignisse         | Bei Wertänderung   | -                     | Ereignis bei Wertänderung |
|                    | Bei Tastendruck     | -                     | Ereignis bei Tastendruck |
|                    | Bei Tastenvorlage  | -                     | Ereignis bei Tastentastenfreigabe |
|                    | Bei Fokus          | -                     | Ereignis beim Fokussieren auf ein Element |
| Tab-Index          | -                  | Ganzzahl              | Reihenfolge des Feldwechsels |

**CSS-Eigenschaften:**

| Einstellungsgruppe | Einstellungsfeld   | Wertoptionen          | Zweck |
|--------------------|--------------------|-----------------------|-------|
| Layout             | Breite             | -                     | Breite der Komponente |
|                    | Höhe               | -                     | Höhe der Komponente |
|                    | Wachsen            | true, false           | Dehnung der Komponente |
|                    | Rand               | -                     | Äußere Polsterung |
|                    | Innenabstand       | -                     | Innere Polsterung |
| Erscheinungsbild    | Eckenradius        | -                     | Eckenradius |
|                    | Randdicke          | -                     | Randdicke |
| Pinsel             | Hintergrund        | -                     | Hintergrundfarbe |
|                    | Randpinsel         | -                     | Randfarbe |

## Anwendungsfälle
- **Textformatierung**: Wird verwendet, um reichhaltig formatierte Dokumente und Inhalte zu erstellen.
- **Inhaltsbearbeitung**: Wird in Content-Management-Systemen verwendet, um das Bearbeiten von Artikeln, Blogs und anderen Textinhalten zu erleichtern.

## Ausnahmen
- **Komplexität der Benutzeroberfläche**: Kann für Benutzer ohne Erfahrung mit ähnlichen Editoren schwierig zu bedienen sein.
- **Technische Einschränkungen**: Je nach Implementierung möglicherweise nicht alle Funktionen fortschrittlicher Texteditoren unterstützt.