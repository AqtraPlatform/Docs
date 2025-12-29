# Textfeld

![](../../assets/images/app-development/text-field.png)

## Allgemeine Informationen
„Textfeld“ ist eine UI-Komponente, die zum Anzeigen und Konfigurieren von Texteingaben und -ausgaben entwickelt wurde.

## Parameter
**Komponenten Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld | Wertoptionen | Zweck |
| --- | --- | --- | --- |
|  | Name | - | Name der UI-Komponente im System |
| Allgemein | Deaktiviert | true, false | Die Eigenschaft ermöglicht es, ein Element im Formular zu deaktivieren |
|  | Erforderlich | true, false | Die Eigenschaft macht das Element erforderlich, um vor dem Absenden des Formulars ausgefüllt zu werden |
|  | Beschriftung | - | Enthält das Inhaltsverzeichnis des Textcontainers |
|  | Bindung | Mehrfachauswahl des Katalogs | Enthält ein verwandtes „String“-Feld aus dem Modell |
| Ereignisse | Bei Wertänderung | - | Ermöglicht das Ausführen des angegebenen Skripts nach der Änderung des Wertes des Feldes |
| Tab-Index |  | Positiver Ganzzahlwert, beginnend bei null | Legt die Reihenfolge fest, in der aktive (bearbeitbare) Felder über die Tastatur umgeschaltet werden (zum Beispiel mit der Tabulatortaste) |

**CSS-Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld | Wertoptionen | Zweck |
| --- | --- | --- | --- |
| Layout | Breite | - | Breite der Komponente |
|  | Höhe | - | Höhe der Komponente |
|  | Wachstum | true, false | Die Eigenschaft bestimmt, wie viel ein Element im Verhältnis zu den anderen Flex-Elementen im selben Container wachsen wird |
|  | Rand | - | Die Eigenschaft definiert die äußeren Abstände auf allen vier Seiten des Elements |
|  | Innenabstand | - | Die Eigenschaft legt die inneren Abstände auf allen Seiten des Elements fest |
| Erscheinungsbild | Eckenradius | - | Die Eigenschaft wird verwendet, um die Ecken eines Elements abzurunden |
|  | Rahmenstärke | - | Die Eigenschaft ermöglicht es, die Grenzen für das Element festzulegen |
| Pinsel | Hintergrund | - | Die Eigenschaft legt die Hintergrundfarbe des Elements fest |
|  | Rahmenpinsel | - | Die Eigenschaft legt die Farbe des Rahmens des Elements fest |

## Anwendungsfälle
- **Dateneingabeformulare**: Wird verwendet, um Textinformationen von Benutzern zu sammeln.
- **Schnittstelleneinstellungen**: Bietet eine Benutzeroberfläche zum Eingeben oder Ändern von Text.

## Ausnahmen
- **Eingeschränkte Funktionalität**: Eignet sich nur für die Texteingabe.