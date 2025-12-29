# Datum / Uhrzeit

![](../../assets/images/app-development/date-time.png)

## Allgemeine Informationen
Datum/Uhrzeit ist eine UI-Komponente zum Eingeben und Anzeigen von Datum und Uhrzeit. Sie wurde entwickelt, um eine benutzerfreundliche Schnittstelle zur Auswahl von Datum/Uhrzeit bereitzustellen und diese Daten in einem bestimmten Format anzuzeigen.

## Parameter
**Komponenten-Eigenschaften:**

| Einstellungsgruppe | Einstellungsfeld | Wertoptionen         | Zweck                 |
|--------------------|------------------|----------------------|-----------------------|
| (Globale Einstellungen) | Name             | -                    | Name der UI-Komponente im System |
| Datum Uhrzeit      | Format           | Datum, Uhrzeit, Datum & Uhrzeit | Anzeigeformat         |
|                    | Standardwert     | -                    | Standardwert         |
|                    | Minimales Datum   | -                    | Minimales Datum      |
|                    | Maximales Datum   | -                    | Maximales Datum      |
| Allgemein          | Bindung          | -                    | Bindung an Daten     |
|                    | Erforderlich      | true, false          | Erforderlich auszufüllen |

**CSS-Eigenschaften:**

| Einstellungsgruppe | Einstellungsfeld | Wertoptionen         | Zweck                 |
|--------------------|------------------|----------------------|-----------------------|
| Layout             | Breite           | -                    | Breite der Komponente |
|                    | Höhe             | -                    | Höhe der Komponente   |
|                    | Rand             | -                    | Äußere Polsterung     |
|                    | Innenabstand     | -                    | Innere Polsterung     |
| Erscheinungsbild    | Eckenradius      | -                    | Eckenradius           |
|                    | Rahmenstärke     | -                    | Rahmenstärke          |
| Pinsel             | Hintergrund      | -                    | Hintergrundfarbe      |
|                    | Rahmenpinsel     | -                    | Rahmenfarbe           |

## Anwendungsfälle
- **Ereignisdatumsauswahl**: Wird verwendet, um ein Datum im Kalender auszuwählen oder die Uhrzeit des Ereignisses festzulegen.
- **Nach Datum filtern**: Kann in Filtern verwendet werden, um Daten nach Datum/Uhrzeit zu filtern.
- **Zeitintervalle anzeigen**: Geeignet für Aufgaben, die das Anzeigen von Zeitintervallen beinhalten, wie in Jobplanern.

## Ausnahmen
- **Formatierung**: Datum/Uhrzeit ist nicht für die Eingabe von Freitext gedacht, sondern wird ausschließlich für die Arbeit mit Daten und Uhrzeiten verwendet.