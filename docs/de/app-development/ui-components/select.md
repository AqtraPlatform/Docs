# Auswahl

![](../../assets/images/app-development/select.png)

## Allgemeine Informationen
„Auswahl“ ist ein Schnittstellenelement, das es dem Benutzer ermöglicht, eine Option aus der präsentierten Liste auszuwählen. Diese Komponente wird häufig verwendet, um Dropdown-Listen mit einer Auswahl von Optionen oder Kategorien zu erstellen.

## Parameter
**Komponenten Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld | Wertoptionen | Zweck |
| --- | --- | --- | --- |
|  | Name | - | Name der UI-Komponente im System |
| Allgemein | Deaktiviert | true, false | Die Eigenschaft ermöglicht es, ein Element im Formular zu deaktivieren |
|  | Erforderlich | true, false | Die Eigenschaft macht das Element erforderlich, um vor dem Absenden des Formulars ausgefüllt zu werden |
|  | Beschriftung | - | Enthält das Inhaltsverzeichnis des Textcontainers |
|  | Bindung | Multiselect von Katalog | Enthält ein verwandtes „Katalog“-Feld aus dem Modell |
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
- **Auswahl aus der Liste:** Benutzer können eine Option aus einer Liste von vorgeschlagenen Optionen auswählen.

## Ausnahmen
- **Unintuitive Schnittstelle:** Wenn die Liste nicht intuitiv oder verständlich für den Benutzer ist, kann dies Schwierigkeiten bei der Auswahl einer Option verursachen.
- **Downloadgeschwindigkeit:** Wenn die Liste zu lang ist, erfordert das Laden der ausgewählten Elemente zusätzliche Wartezeit.