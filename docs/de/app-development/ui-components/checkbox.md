# Checkbox

![](../../assets/images/app-development/checkbox.png)

## Allgemeine Informationen
Ein „Checkbox“ ist ein Schnittstellenelement, das es Benutzern ermöglicht, ein bestimmtes Parameter oder eine Option auszuwählen oder abzuwählen. Diese Komponente wird häufig verwendet, um Parameterlisten zu erstellen, Einstellungen zu verwalten oder mehrere Optionen gleichzeitig auszuwählen.

## Parameter
**Komponenten Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld | Wertoptionen | Zweck |
| --- | --- | --- | --- |
|  | Name | - | Name der UI-Komponente im System |
| Allgemein | Deaktiviert | true, false | Die Eigenschaft ermöglicht es, ein Element im Formular zu deaktivieren |
|  | Erforderlich | true, false | Die Eigenschaft macht das Element erforderlich, um das Formular abzusenden |
|  | Beschriftung | - | Enthält das Inhaltsverzeichnis des Textcontainers |
|  | Bindung | Multiselect von Katalog | Enthält ein verwandtes „Boolean“-Feld aus dem Modell |
| Ereignisse | Bei Wertänderung | - | Ermöglicht das Ausführen des angegebenen Skripts nach der Änderung des Wertes des Feldes |

**CSS-Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld | Wertoptionen | Zweck |
| --- | --- | --- | --- |
| Layout | Breite | - | Breite der Komponente |
|  | Höhe | - | Höhe der Komponente |
|  | Wachstum | true, false | Die Eigenschaft bestimmt, wie viel ein Element im Verhältnis zu den anderen Flex-Elementen im selben Container wachsen wird |
|  | Rand | - | Die Eigenschaft definiert die äußeren Abstände auf allen vier Seiten des Elements |
|  | Innenabstand | - | Die Eigenschaft legt die inneren Abstände auf allen Seiten des Elements fest |
| Erscheinungsbild | Eckenradius | - | Die Eigenschaft wird verwendet, um die Ecken eines Elements abzurunden |
|  | Randdicke | - | Die Eigenschaft ermöglicht es, die Grenzen für das Element festzulegen |
| Pinsel | Hintergrund | - | Die Eigenschaft legt die Hintergrundfarbe des Elements fest |
|  | Randpinsel | - | Die Eigenschaft legt die Farbe des Randes des Elements fest |

## Fälle
- **Optionsauswahl**: Benutzer können bestimmte Parameter oder Optionen auswählen oder abwählen.
- **Einstellungsverwaltung**: Checkbox wird verwendet, um bestimmte Einstellungen oder Funktionen zu aktivieren oder zu deaktivieren.
- **Mehrfachauswahl**: In der Checkbox-Gruppe können Benutzer mehrere Optionen gleichzeitig auswählen.

## Ausnahmen
- **Unintuitive Benutzeroberfläche:** Bei einer großen Anzahl von Kontrollkästchen auf einer Seite oder in komplexen Formularen können Benutzer Schwierigkeiten haben, Optionen auszuwählen.
- **Unklare Formulierungen:** Wenn die Formulierungen der Checkboxen nicht informativ oder unklar sind, verstehen Benutzer möglicherweise nicht, was sie auswählen.