# Multiselect

![](../../assets/images/app-development/multiselect.png)

## Allgemeine Informationen
„Multiselect“ ist eine UI-Komponente, die entwickelt wurde, um mehrfache Auswahl-Referenzlisten anzuzeigen und zu konfigurieren. Funktioniert nur mit dem Array-Feldtyp.

## Parameter
**Komponenten-Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld | Wertoptionen | Zweck |
| --- | --- | --- | --- |
|  | Name | - | Name der UI-Komponente im System |
| Allgemein | Deaktiviert | true, false | Diese Eigenschaft ermöglicht es, ein Element im Formular zu deaktivieren |
|  | Erforderlich | true, false | Diese Eigenschaft macht das Element erforderlich, um vor dem Absenden des Formulars ausgefüllt zu werden |
|  | Beschriftung | - | Enthält das Inhaltsverzeichnis des Textcontainers |
|  | Bindung | Multiselect von Katalog | Enthält ein verwandtes „Array“-Feld aus dem Modell |
| Ereignisse | Bei Wertänderung | - | Ermöglicht das Ausführen des angegebenen Skripts nach der Änderung des Wertes des Feldes |

**CSS-Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld | Wertoptionen | Zweck |
| --- | --- | --- | --- |
| Layout | Breite | - | Breite der Komponente |
|  | Höhe | - | Höhe der Komponente |
|  | Wachstum | true, false | Diese Eigenschaft bestimmt, wie viel ein Element im Verhältnis zu den anderen Flex-Elementen im selben Container wachsen wird |
|  | Rand | - | Diese Eigenschaft definiert die äußeren Abstände auf allen vier Seiten des Elements |
|  | Innenabstand | - | Diese Eigenschaft legt die inneren Abstände auf allen Seiten des Elements fest |
| Erscheinungsbild | Eckenradius | - | Diese Eigenschaft wird verwendet, um die Ecken eines Elements abzurunden |
|  | Randdicke | - | Diese Eigenschaft ermöglicht es, die Grenzen des Elements festzulegen |
| Pinsel | Hintergrund | - | Diese Eigenschaft legt die Hintergrundfarbe des Elements fest |
|  | Randpinsel | - | Diese Eigenschaft legt die Farbe des Randes des Elements fest |

## Fälle

## Ausnahmen
- **Eingeschränkte Funktionalität**: Nur geeignet für „Array“-Daten.