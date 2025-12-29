# Nummer

![](../../assets/images/app-development/number.png)

## Allgemeine Informationen
Die „Nummer“-Komponente ist eine Schnittstelle zum Eingeben von numerischen Werten. Diese Komponente ermöglicht es Benutzern, Zahlen einzugeben und kann für verschiedene Zwecke verwendet werden, wie z. B. das Eingeben von Zahlen, Mengen oder anderen numerischen Daten.

## Parameter
**Komponenten-Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld | Wertoptionen | Zweck |
| --- | --- | --- | --- |
|  | Name | - | Name der UI-Komponente im System |
| Allgemein | Deaktiviert | true, false | Die Eigenschaft ermöglicht es, ein Element im Formular zu deaktivieren |
|  | Erforderlich | true, false | Die Eigenschaft macht das Element erforderlich, um vor dem Absenden des Formulars ausgefüllt zu werden |
|  | Beschriftung | - | Enthält das Inhaltsverzeichnis des Textcontainers |
|  | Bindung | Multiselect des Katalogs | Enthält das zugehörige „Integer“- und „Number“-Feld aus dem Modell |
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

## Anwendungsfälle
- **Eingabe numerischer Werte:** Benutzer können Zahlen in die Nummer-Komponente eingeben, wie z. B. Produktmengen oder numerische Parameter.
- **Bereichsgrenze:** Mindest- und Höchstwerte ermöglichen es, die eingegebenen Zahlen auf einen bestimmten Bereich zu beschränken.
- **Zahl mit Pfeilen ändern:** Benutzer können eine Zahl mit den Auf- und Ab-Pfeilen erhöhen oder verringern.

## Ausnahmen
- **Eingabe nicht-numerischer Daten:** Es können nur numerische Daten eingegeben werden.