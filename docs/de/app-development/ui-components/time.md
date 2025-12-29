# Zeit

![](../../assets/images/app-development/time.png)

## Allgemeine Informationen
Zeit ist eine UI-Komponente, die zum Eingeben und Anzeigen von Zeit entwickelt wurde. Dieses Element wird typischerweise verwendet, um die Zeit von Ereignissen oder Aufgaben festzulegen und die Zeit in Anwendungsoberflächen anzuzeigen.

## Parameter
**Komponenten Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld | Wertoptionen | Zweck |
| --- | --- | --- | --- |
|  | Name | - | Name der UI-Komponente im System |
| Allgemein | Deaktiviert | true, false | Die Eigenschaft ermöglicht es, ein Element im Formular zu deaktivieren |
|  | Erforderlich | true, false | Die Eigenschaft macht das Element erforderlich, um das Formular vor dem Absenden auszufüllen |
|  | Beschriftung | - | Enthält das Inhaltsverzeichnis des Textcontainers |
|  | Bindung | Multiselect des Katalogs | Enthält ein verwandtes „Zeit“-Feld aus dem Modell |
| Ereignisse | Bei Wertänderung | - | Ermöglicht das Ausführen des angegebenen Skripts nach der Änderung des Wertes des Feldes |

**CSS-Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld | Wertoptionen | Zweck |
| --- | --- | --- | --- |
| Layout | Breite | - | Breite der Komponente |
|  | Höhe | - | Höhe der Komponente |
|  | Wachsen | true, false | Die Eigenschaft bestimmt, wie viel ein Element im Verhältnis zu den anderen Flex-Elementen im selben Container wachsen wird |
|  | Rand | - | Die Eigenschaft definiert die äußeren Abstände auf allen vier Seiten des Elements |
|  | Innenabstand | - | Die Eigenschaft legt die inneren Abstände auf allen Seiten des Elements fest |
| Erscheinungsbild | Eckenradius | - | Die Eigenschaft wird verwendet, um die Ecken eines Elements abzurunden |
|  | Randdicke | - | Die Eigenschaft ermöglicht es, die Grenzen für das Element festzulegen |
| Pinsel | Hintergrund | - | Die Eigenschaft legt die Hintergrundfarbe des Elements fest |
|  | Randpinsel | - | Die Eigenschaft legt die Farbe des Randes des Elements fest |

## Fälle
- **Zeiteinstellung**: Wird verwendet, um eine bestimmte Zeit in Planern und Kalendern festzulegen.
- **Zeiteingabe**: Bietet eine Schnittstelle für den Benutzer, um Zeit für verschiedene Zwecke einzugeben.

## Ausnahmen
- **Zeitformatierung**: Sie müssen sich der Zeitformatbeschränkungen bewusst sein, die in den Komponenteneinstellungen festgelegt sind.
- **Nur Zeit**: Die Zeitkomponente ist darauf beschränkt, nur die Zeit anzuzeigen und einzugeben, ohne Daten.