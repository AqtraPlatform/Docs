# Fortschrittsanzeige

![](../../assets/images/app-development/progress-bar.png)

## Allgemeine Informationen
Diese UI-Komponente wird verwendet, um die Fortschrittsanzeige anzuzeigen und zu konfigurieren.

## Parameter
**Komponenten Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld | Wertoptionen | Zweck  |
| --- | --- | --- | --- |
|  | Name | - | Name der UI-Komponente im System |
| Allgemein | Wert anzeigen | true, false | Die Eigenschaft wird verwendet, um die Werte der Fortschrittsanzeige anzuzeigen |
|  | Bestimmt | true, false | Die Eigenschaft ermöglicht es, die Fortschrittsanzeige als Animation zu gestalten |
|  | Umkehren | true, false | Die Eigenschaft ermöglicht es, die Fortschrittsanzeige umzukehren |
|  | Format | - | Die Eigenschaft ermöglicht es, das Daten-Ausgabeformat anzugeben |
|  | Wert | - | Die Eigenschaft ermöglicht es, einen Wert festzulegen |
|  | Bindung | Mehrfachauswahl des Katalogs | Enthält das zugehörige „Integer“-Feld aus dem Modell |
|  | Minimalwert | - | Die Eigenschaft ermöglicht es, einen Minimalwert anzugeben |
|  | Bindung | Mehrfachauswahl des Katalogs | Enthält das zugehörige „Integer“-Feld aus dem Modell für den Minimalwert  |
|  | Maximalwert | - | Die Eigenschaft ermöglicht es, einen Maximalwert anzugeben |
|  | Bindung | Mehrfachauswahl des Katalogs | Enthält das zugehörige „Integer“-Feld aus dem Modell für den Maximalwert  |

**CSS-Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld | Wertoptionen | Zweck |
| --- | --- | --- | --- |
| Layout | Breite | - | Breite der Komponente |
|  | Höhe | - | Höhe der Komponente |
|  | Wachsen | true, false | Die Eigenschaft bestimmt, wie viel ein Element im Verhältnis zu den anderen Flex-Elementen im selben Container wachsen wird |
|  | Rand | - | Die Eigenschaft definiert die äußeren Abstände auf allen vier Seiten des Elements |
|  | Innenabstand | - | Die Eigenschaft legt die inneren Abstände auf allen Seiten des Elements fest |
| Erscheinung | Eckenradius | - | Die Eigenschaft wird verwendet, um die Ecken eines Elements abzurunden |
|  | Randdicke | - | Die Eigenschaft ermöglicht es, die Grenzen für das Element festzulegen |
| Pinsel | Hintergrund | - | Die Eigenschaft legt die Hintergrundfarbe des Elements fest |
|  | Randpinsel | - | Die Eigenschaft legt die Farbe des Randes des Elements fest |
|  | Fortschritt | - | Die Eigenschaft legt die Farbe der Leiste des Elements fest |

## Anwendungsfälle
- Anzeige des Fortschritts von Aufgaben, Downloads oder anderen Prozessen.

## Ausnahmen
- Beschränkt auf die Verwendung zur Fortschrittsdarstellung und nicht geeignet für andere Arten von Visualisierungen.