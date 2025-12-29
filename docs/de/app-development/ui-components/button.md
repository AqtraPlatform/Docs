# Button

![](../../assets/images/app-development/button.png)

## Allgemeine Informationen
Ein Button ist die Hauptbenutzeroberflächenkomponente, die verwendet wird, um Befehle auszuführen oder Aktionen in einer Anwendung zu initiieren. Er kann so konfiguriert werden, dass Prozesse ausgeführt, Benutzeraktionen bestätigt oder als Navigationswerkzeug dient.

## Parameter
**Komponenten Eigenschaften:**

| Einstellungsgruppe | Einstellungsfeld   | Wertoptionen         | Zweck |
|--------------------|--------------------|----------------------|-------|
| (Globale Einstellungen) | Name             | -                    | Name der Benutzeroberflächenkomponente im System |
| Allgemein          | Icon               | -                    | Icon laden (.svg) |
|                    | Deaktiviert        | true, false          | Deaktivierung eines Elements |
|                    | Beschriftung       | -                    | Button-Text |
| Text               | Schriftgröße       | -                    | Größe der Schrift |
|                    | Farbe              | -                    | Textfarbe (CSS) |
|                    | Fett               | true, false          | Fette Schrift |
|                    | Kursiv             | true, false          | Kursivschrift |
|                    | Textausrichtung    | Links, Rechts, Mitte, Blocksatz | Textausrichtung |
| Aktionen           | Befehlstyp        | Verschiedene Befehle | Aktion durch Buttonklick |
|                    | Zugriff einschränken | true, false        | Zugriffsbeschränkung |

**CSS Eigenschaften:**

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
- **Formularübermittlung**: Verwendung eines Buttons zur Übermittlung von Formulardaten an den Server oder zur Initiierung der Verarbeitung von Formulardaten in der Anwendung.
- **Navigation**: Zuweisung eines Buttons zur Navigation zwischen verschiedenen Bildschirmen oder Abschnitten der Anwendung.
- **Interaktive Elemente**: Erstellung von Buttons zur Steuerung interaktiver Elemente, wie z.B. das Ändern von Inhalten auf einer Seite.

## Ausnahmen
- **Einschränkungen bei der Anzahl der Aktionen**: Es kann nur eine Aktion einem Button zugewiesen werden (Datenfluss ausführen, Skript ausführen usw.).