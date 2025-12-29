# Bild

![](../../assets/images/app-development/image.png)

## Allgemeine Informationen
Die Bildkomponente wird verwendet, um Bilder in der Benutzeroberfläche anzuzeigen. Diese Komponente ist ein Schlüsselelement für die Visualisierung und kann verwendet werden, um Fotos, Illustrationen und andere grafische Elemente anzuzeigen.

## Parameter
**Komponenten Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld | Wertoptionen | Zweck |
| --- | --- | --- | --- |
|  | Name | - | Name der UI-Komponente im System |
| Allgemein | Bindung | Mehrfachauswahl des Katalogs | Enthält ein zugehöriges „Datei“-Feld aus dem Modell |
|  | Datei | Schaltfläche | Ermöglicht das Hochladen einer Datei mit den Erweiterungen .png, .jpg und .svg |
| | Platzhalterbild anzeigen | Wahr, Falsch | Anzeige des Platzhalterbildes |
| | Kein Platzhalterbild | Datei vom Datenträger auswählen, Datei aus dem Speicher auswählen | Platzhalterbild, wenn kein Bild geladen ist | 

**CSS-Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld | Wertoptionen | Zweck |
| --- | --- | --- | --- |
| Layout | Breite | - | Breite der Komponente |
|  | Höhe | - | Höhe der Komponente |
|  | Wachsen | wahr, falsch | Die Eigenschaft bestimmt, wie viel ein Element im Verhältnis zu den anderen Flex-Elementen im selben Container wachsen wird |
|  | Rand | - | Die Eigenschaft definiert die äußeren Abstände auf allen vier Seiten des Elements |
|  | Innenabstand | - | Die Eigenschaft legt die inneren Abstände auf allen Seiten des Elements fest |
| Erscheinung | Eckenradius | - | Die Eigenschaft wird verwendet, um die Ecken eines Elements abzurunden |
|  | Randdicke | - | Die Eigenschaft ermöglicht es, die Grenzen für das Element festzulegen |
| Pinsel | Hintergrund | - | Die Eigenschaft legt die Hintergrundfarbe des Elements fest |
|  | Randpinsel | - | Die Eigenschaft legt die Farbe des Randes des Elements fest |

## Fälle
- **Fotoanzeige:** Wird verwendet, um benutzerdefinierte Fotos, Produktbilder und andere Objekte anzuzeigen.
- **Illustrationen und Grafiken:** Anwendbar zur Anzeige von Illustrationen, grafischen Elementen und Logos.

## Ausnahmen
- **Leistung:** Die Verwendung von großen oder mehreren Bildern auf einer Seite kann die Leistung beeinträchtigen.