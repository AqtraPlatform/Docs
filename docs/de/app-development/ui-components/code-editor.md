# Code Editor

![](../../assets/images/app-development/code-editor.png)

## Allgemeine Informationen
Der Code-Editor ist eine spezialisierte UI-Komponente, die zum Eingeben und Anzeigen von Programmcode entwickelt wurde. Er unterstützt verschiedene Programmiersprachen wie JavaScript, Python usw. und bietet Funktionen für eine einfache Codebearbeitung, jedoch unterstützt das Element keinen Compiler.

## Parameter
**Komponenten-Eigenschaften:**

| Einstellungsgruppe | Einstellungsfeld   | Wertoptionen          | Zweck |
|--------------------|--------------------|-----------------------|-------|
| (Globale Einstellungen) | Name             | -                     | Name der UI-Komponente im System |
| Allgemein          | Deaktiviert        | true, false           | Deaktivierung eines Elements |
|                    | Erforderlich       | true, false           | Erforderliches Feld zum Ausfüllen |
|                    | Thema              | -                     | Visueller Stil des Editors |
|                    | Modus              | -                     | Programmiersprache |
|                    | Beschriftung       | -                     | Feldbeschreibung |
|                    | Bindung            | Multiselect des Katalogs | Datenbindung |
| Ereignisse         | Bei Wertänderung   | -                     | Ereignis bei Wertänderung |
|                    | Bei Tastendruck     | -                     | Ereignis bei Tastendruck |
|                    | Bei Tastenvorlage  | -                     | Ereignis bei Tastentfreigabe |
|                    | Bei Fokus          | -                     | Ereignis beim Fokussieren auf ein Element |
| Tab-Index          | -                  | Ganzzahl              | Reihenfolge des Feldwechsels |

**CSS-Eigenschaften:**

| Einstellungsgruppe | Einstellungsfeld   | Wertoptionen          | Zweck |
|--------------------|--------------------|-----------------------|-------|
| Layout             | Breite             | -                     | Breite der Komponente |
|                    | Höhe               | -                     | Höhe der Komponente |
|                    | Wachsen            | true, false           | Dehnen der Komponente |
|                    | Rand               | -                     | Äußere Polsterung |
|                    | Innenabstand       | -                     | Innere Polsterung |
| Erscheinung        | Eckenradius        | -                     | Eckenradius |
|                    | Randdicke          | -                     | Randdicke |
| Pinsel             | Hintergrund        | -                     | Hintergrundfarbe |
|                    | Randpinsel         | -                     | Randfarbe |

## Anwendungsfälle
- **Code-Bearbeitung**: Wird verwendet, um Programmcode in verschiedenen Programmiersprachen einzugeben und zu bearbeiten.
- **Schulung und Demonstration**: Wird zu Bildungs- und Demonstrationszwecken verwendet, um Codebeispiele zu zeigen.

## Ausnahmen
- **Funktionsbeschränkungen**: Je nach Implementierung werden möglicherweise nicht alle Funktionen fortschrittlicher Entwicklungsumgebungen unterstützt.