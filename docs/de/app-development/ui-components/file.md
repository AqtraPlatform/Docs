# Datei

![](../../assets/images/app-development/file.png)

## Allgemeine Informationen
Die Komponente „Datei“ bietet die Möglichkeit, Dateien in der Benutzeroberfläche zu laden und anzuzeigen. Diese Komponente ist nützlich zum Hochladen und Anzeigen verschiedener Dateitypen, wie z. B. Bilder, Dokumente, Archive usw.

## Parameter
**Komponenten Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld | Wertoptionen | Zweck |
| --- | --- | --- | --- |
|  | Name | - | Name der UI-Komponente im System |
| Allgemein | Maximale Dateigröße in Bytes | - | Die Eigenschaft ermöglicht es, die maximale Größe der hochgeladenen Datei in Bytes anzugeben |
|  | Akzeptierte Dateien |  | Die Eigenschaft ermöglicht es, die Dateien anzugeben, die zum Download verfügbar sind |
|  | Nur lesen | true, false | Diese Eigenschaft ermöglicht es, das Hochladen von Dateien in Formulare zu deaktivieren |
|  | Deaktiviert | true, false | Die Eigenschaft ermöglicht es, ein Element im Formular zu deaktivieren |
|  | Erforderlich | true, false | Die Eigenschaft macht das Element erforderlich, um vor dem Absenden des Formulars ausgefüllt zu werden |
|  | Beschriftung | - | Enthält das Inhaltsverzeichnis des Textcontainers |
|  | Wert | - | - |
|  | Bindung | Mehrfachauswahl: Katalog | Verweis auf den Katalog des Dateityps |
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
|  | Rahmenstärke | - | Die Eigenschaft ermöglicht es, die Grenzen für das Element festzulegen |
| Pinsel | Hintergrund | - | Die Eigenschaft legt die Hintergrundfarbe des Elements fest |
|  | Rahmenpinsel | - | Die Eigenschaft legt die Farbe des Rahmens des Elements fest |

## Fälle
- **Dokumenten-Upload**: Ermöglicht Benutzern das Hochladen von Dokumenten, Bildern und anderen Dateien.
- **Dateiinformationen anzeigen:** Zeigt Informationen über die hochgeladene Datei an, wie z. B. ihren Namen und ihre Größe.

## Ausnahmen
- **Leistung**: Das Herunterladen großer Dateien oder einer großen Anzahl von Dateien kann die Leistung beeinträchtigen.