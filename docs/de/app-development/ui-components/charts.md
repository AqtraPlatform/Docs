# Diagramme

![](../../assets/images/app-development/charts.png)

## Allgemeine Informationen
„Diagrammansicht“ ist eine UI-Komponente, die entwickelt wurde, um die grafische Darstellung von Daten anzuzeigen und anzupassen.

## Parameter
**Komponenten-Eigenschaften:**

| Einstellungsgruppe | Einstellungsfeld   | Wertoptionen                          | Zweck                                      |
|-----------------|------------------|--------------------------------------------|-------------------------------------------------|
| (Globale Einstellungen)         | Komponente        | -                                          | Auswahl einer Komponente, die im Diagramm angezeigt werden soll     |
|                 | Diagrammtyp       | Balken, horizontaler Balken, Kreis, Donut, Linie      | Art des Diagramms                                     |
|                 | Beschriftungsfeld      | -                                          | Feld für Beschriftungen im Diagramm                      |
|                 | Datenquelle      | -                                          | Datenquelle für das Diagramm                    |
|                 | Legende anzeigen      | wahr, falsch                                | Anzeige der Legende im Diagramm                 |
|                 | Y-Achse Max-Wert | -                                          | Maximalwert auf der Y-Achse                 |
|                 | Y-Achse Min-Wert | -                                          | Minimalwert auf der Y-Achse                  |
|                 | X-Achse Max-Wert | -                                          | Maximalwert auf der X-Achse                 |
|                 | X-Achse Min-Wert | -                                          | Minimalwert auf der X-Achse                  |
|                 | Automatisierungs-ID    | -                                          | ID für die Automatisierung                |

**CSS-Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld | Wertoptionen | Zweck |
| --- | --- | --- | --- |
| Layout | Breite | - | Breite der Komponente |
|  | Höhe | - | Höhe der Komponente |
|  | Wachsen | wahr, falsch | Die Eigenschaft bestimmt, wie viel ein Element im Verhältnis zu den anderen Flex-Elementen im selben Container wachsen wird |
|  | Rand | - | Die Eigenschaft definiert die äußeren Abstände auf allen vier Seiten des Elements |
|  | Innenabstand | - | Die Eigenschaft legt die inneren Abstände auf allen Seiten des Elements fest |
|          | Sichtbar        | wahr, falsch       | Sichtbarkeit der Komponente    |
|                 | Versteckt         | wahr, falsch       | Verstecken einer Komponente      |
| Erscheinung | Eckenradius | - | Die Eigenschaft wird verwendet, um die Ecken eines Elements abzurunden |
|  | Randdicke | - | Die Eigenschaft ermöglicht es Ihnen, die Grenzen für das Element festzulegen |
| Pinsel | Hintergrund | - | Die Eigenschaft legt die Hintergrundfarbe des Elements fest |
|  | Randpinsel | - | Die Eigenschaft legt die Farbe des Randes des Elements fest |

**Parameter der Datenquelle:**

| Einstellungsfeld | Wertoptionen | Zweck |
| --- | --- | --- |
| Titel | - | Titel der Datenquelle |
| Wert | Mehrfachauswahl
Katalog | Die Eigenschaft ermöglicht es Ihnen, einen Datenquellenwert aus den Integer- und Zahlenfeldern auszuwählen |
| OK | Schaltfläche | Anwendung der Anpassung |
| Abbrechen | Schaltfläche | Stornierung der Anpassung |

## Anwendungsfälle
- **Datenvisualisierung**: Wird verwendet, um Grafiken und Diagramme zu erstellen, die es Ihnen ermöglichen, Daten effizient zu präsentieren.
- **Analytische Dashboards**: Geeignet für analytische Dashboards, die eine visuelle Darstellung von Statistiken und Kennzahlen erfordern.

## Ausnahmen
- **Spezialisierte Nutzung**: Beschränkt auf die Erstellung von Grafiken und ist nicht für andere Arten von Visualisierungen geeignet.