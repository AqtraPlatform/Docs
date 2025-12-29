# Switch

![](../../assets/images/app-development/switch.png)

## Allgemeine Informationen
Die „Switch“-Komponente ist ein Schnittstellenelement, das es dem Benutzer ermöglicht, eine bestimmte Funktion, Option oder einen Zustand zu aktivieren oder zu deaktivieren. Diese Komponente wird häufig verwendet, um die Möglichkeit zu bieten, schnell zwischen zwei Zuständen (Wahr/Falsch) zu wechseln.

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
|  | Wachstum | true, false | Die Eigenschaft bestimmt, wie viel ein Element im Verhältnis zu den anderen Flex-Elementen im selben Container wachsen wird |
|  | Rand | - | Die Eigenschaft definiert die äußeren Abstände auf allen vier Seiten des Elements |
|  | Innenabstand | - | Die Eigenschaft legt die inneren Abstände auf allen Seiten des Elements fest |
| Erscheinungsbild | Eckenradius | - | Die Eigenschaft wird verwendet, um die Ecken eines Elements abzurunden |
|  | Randdicke | - | Die Eigenschaft ermöglicht es, die Grenzen für das Element festzulegen |
| Pinsel | Hintergrund | - | Die Eigenschaft legt die Hintergrundfarbe des Elements fest |
|  | Randpinsel | - | Die Eigenschaft legt die Farbe des Randes des Elements fest |.

## Anwendungsfälle 
- **Binäre Auswahl:** Switch wird für binäre Auswahlen wie ein/aus Ton, Benachrichtigungen und andere Optionen verwendet.
- **Zustandsverwaltung:** Sie können Switch verwenden, um den Zustand eines bestimmten Schnittstellenelements zu verwalten.

## Ausnahmen
- **Unklarer Status:** Wenn nicht offensichtlich ist, was der aktivierte und deaktivierte Status bedeutet, können Benutzer verwirrt sein.