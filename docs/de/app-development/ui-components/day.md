# Tag

![](../../assets/images/app-development/day.png)

## Allgemeine Informationen
Tag ist eine UI-Komponente, die entwickelt wurde, um einzelne Tage anzuzeigen oder auszuwählen. Dieses Element wird häufig in Kalendern oder Datensensoren verwendet, um dem Benutzer die Auswahl spezifischer Tage zu ermöglichen, um Aufgaben zu erledigen oder Erinnerungen festzulegen.

## Parameter
**Komponenten-Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld | Wertoptionen | Zweck |
| --- | --- | --- | --- |
|  | Name | - | Name der UI-Komponente im System |
| Allgemein | Format | - | Die Eigenschaft ermöglicht es Ihnen, das Datum und die Uhrzeit [zu konfigurieren](https://docs.microsoft.com/ru-ru/dotnet/standard/base-types/custom-date-and-time-format-strings) |
|  | Deaktiviert | true, false | Die Eigenschaft ermöglicht es Ihnen, ein Element im Formular zu deaktivieren |
|  | Erforderlich | true, false | Die Eigenschaft macht das Element erforderlich, um vor dem Absenden des Formulars ausgefüllt zu werden |
|  | Beschriftung | - | Enthält das Inhaltsverzeichnis des Textcontainers |
|  | Bindung | Mehrfachauswahl des Katalogs | Enthält ein verwandtes „Datum“-Feld aus dem Modell |
| Ereignisse | Bei Wertänderung | - | Ermöglicht es Ihnen, das angegebene Skript nach der Änderung des Wertes des Feldes auszuführen |

**CSS-Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld | Wertoptionen | Zweck |
| --- | --- | --- | --- |
| Layout | Breite | - | Breite der Komponente |
|  | Höhe | - | Höhe der Komponente |
|  | Wachstum | true, false | Die Eigenschaft bestimmt, wie viel ein Element im Verhältnis zu den anderen Flex-Elementen im selben Container wachsen wird |
|  | Rand | - | Die Eigenschaft definiert die äußeren Abstände auf allen vier Seiten des Elements |
|  | Innenabstand | - | Die Eigenschaft legt die inneren Abstände auf allen Seiten des Elements fest |
| Erscheinungsbild | Eckenradius | - | Die Eigenschaft wird verwendet, um die Ecken eines Elements abzurunden |
|  | Randdicke | - | Die Eigenschaft ermöglicht es Ihnen, die Grenzen für das Element festzulegen |
| Pinsel | Hintergrund | - | Die Eigenschaft legt die Hintergrundfarbe des Elements fest |
|  | Randpinsel | - | Die Eigenschaft legt die Farbe des Randes des Elements fest |

## Anwendungsfälle
- **Datumsauswahl**: Wird verwendet, um spezifische Tage in Schnittstellen auszuwählen, in denen eine präzise Datenauswahl erforderlich ist.
- **Ereignisanzeige**: Kann verwendet werden, um Ereignisse oder Erinnerungen anzuzeigen, die für bestimmte Tage geplant sind.

## Ausnahmen
- **Eingeschränkte Funktionalität**: Die Tag-Komponente ist auf die Anzeige und Auswahl von Tagen beschränkt und eignet sich nicht zur Anzeige breiterer Zeitintervalle.