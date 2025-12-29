# Pdf-Viewer

![](../../assets/images/app-development/pdf-viewer.png)

## Allgemeine Informationen
Die PDF-Viewer-Komponente ermöglicht es Ihnen, PDF-Dokumente direkt in der Benutzeroberfläche anzuzeigen und mit ihnen zu interagieren. Diese Komponente ist nützlich, um PDF-Dateien wie Berichte, Anleitungen und andere Dokumente anzuzeigen.

## Parameter
**Komponenten-Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld | Wertoptionen | Zweck |
| --- | --- | --- | --- |
|  | Name | - | Name der UI-Komponente im System |
| Allgemein | Bindung | Mehrfachauswahl des Katalogs | Enthält ein zugehöriges „Datei“-Feld aus dem Modell |
|  | Datei | Schaltfläche | Ermöglicht das Hochladen einer Datei mit der .pdf-Erweiterung |

**CSS-Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld | Wertoptionen | Zweck |
| --- | --- | --- | --- |
| Layout | Breite | - | Breite der Komponente |
|  | Höhe | - | Höhe der Komponente |
|  | Wachstum | true, false | Die Eigenschaft bestimmt, wie viel ein Element im Verhältnis zu den anderen Flex-Elementen im selben Container wachsen wird |
|  | Rand | - | Die Eigenschaft definiert die äußeren Abstände auf allen vier Seiten des Elements |
|  | Innenabstand | - | Die Eigenschaft legt die inneren Abstände auf allen Seiten des Elements fest |
| Erscheinungsbild | Eckenradius | - | Die Eigenschaft wird verwendet, um die Ecken eines Elements abzurunden |
|  | Rahmenstärke | - | Die Eigenschaft ermöglicht es Ihnen, die Grenzen für das Element festzulegen |
| Pinsel | Hintergrund | - | Die Eigenschaft legt die Hintergrundfarbe des Elements fest |
|  | Rahmenpinsel | - | Die Eigenschaft legt die Farbe des Rahmens des Elements fest |

## Anwendungsfälle
- **Berichte anzeigen:** Ermöglicht es Benutzern, Berichte und Dokumentationen im PDF-Format anzuzeigen.

## Ausnahmen
- **Formatbeschränkungen:** Der PDF-Viewer unterstützt Standard-PDF-Dokumente, kann jedoch komplexe Formate oder geschützte Dokumente möglicherweise nicht korrekt anzeigen.
- **Leistung:** Die Verwendung großer PDF-Dokumente oder einer großen Anzahl interaktiver Elemente kann die Leistung beeinträchtigen.