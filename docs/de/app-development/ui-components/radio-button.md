# Radio-Button

![](../../assets/images/app-development/radio-button.png)

## Allgemeine Informationen
Die Komponente „Radio Button“ ist ein Schnittstellenelement, das es dem Benutzer ermöglicht, eine der bereitgestellten Optionen auszuwählen. Diese Komponente wird verwendet, um die Auswahl eines einzelnen Elements aus mehreren gegenseitig ausschließenden Optionen zu implementieren.

## Parameter
**Komponenten Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld | Wertoptionen | Zweck |
| --- | --- | --- | --- |
|  | Name | - | Name der UI-Komponente im System |
| Allgemein | Deaktiviert | true, false | Die Eigenschaft ermöglicht es, ein Element im Formular zu deaktivieren |
|  | Erforderlich | true, false | Die Eigenschaft macht das Element erforderlich, um das Formular abzusenden |
|  | Beschriftung | - | Enthält das Inhaltsverzeichnis des Textcontainers |
|  | Bindung | Multiselect von Katalog | Enthält ein verwandtes „Katalog“-Feld aus dem Modell |
| Ereignisse | Bei Wertänderung | - | Ermöglicht das Ausführen des angegebenen Skripts nach der Änderung des Wertes des Feldes |
|  | Bei Fokus |  | Ermöglicht das Ausführen des angegebenen Skripts, wenn das Element fokussiert ist |

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

## Fälle
- **Einzelauswahl:** Benutzer können nur eine Option aus der Liste auswählen.
- **Gegenseitig ausschließende Optionen:** Die Radio-Button-Komponente wird verwendet, um eine Gruppe von gegenseitig ausschließenden Optionen zu erstellen, von denen nur eine ausgewählt werden kann.

## Ausnahmen
- **Nicht genügend Informationen:** Wenn die Beschriftungen der Radio-Buttons nicht ausreichend informativ sind, können Benutzer Schwierigkeiten haben, Optionen auszuwählen.
- **Schwierige Wahl:** Bei einer großen Anzahl von Radio-Buttons oder unklarer Organisation kann die Wahl für die Benutzer schwierig sein.