# Passwort

![](../../assets/images/app-development/password.png)

## Allgemeine Informationen
Das Passwort ist eine grundlegende UI-Komponente, die zum sicheren Eingeben von Passwörtern entwickelt wurde. Diese Komponente wird verwendet, um Passwort-Eingabefelder zu erstellen, die die Vertraulichkeit und den Schutz der eingegebenen Daten gewährleisten.

## Parameter
**Komponenten Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld | Wertoptionen | Zweck |
| --- | --- | --- | --- |
|  | Name | - | Name der UI-Komponente im System |
| Allgemein | Deaktiviert | true, false | Die Eigenschaft ermöglicht es, ein Element im Formular zu deaktivieren |
|  | Erforderlich | true, false | Die Eigenschaft macht das Element erforderlich, um vor dem Absenden des Formulars ausgefüllt zu werden |
|  | Klar anzeigen | true, false | Zeigt das Symbol zum Löschen (Zurücksetzen) des Feldwerts an |
|  | Automatische Vervollständigung |  | Feld zum Festlegen des Wertes des Autocomplete-HTML-Attributs. In der Regel verwenden Sie den Benutzernamen für das Eingabefeld für den Namen und password, new-password oder current-password für die entsprechenden Eingabefelder für verschiedene Passworttypen. Funktioniert in Verbindung mit dem Parameter Provide Root Form für die Seiten-UI-Steuerung. |
|  | Beschriftung | - | Enthält das Inhaltsverzeichnis des Textcontainers |
|  | Bindung | Mehrfachauswahl des Katalogs | Enthält ein verwandtes „String“-Feld aus dem Modell |
| Ereignisse | Bei Wertänderung | - | Ermöglicht das Ausführen des angegebenen Skripts nach der Änderung des Wertes des Feldes |
|  | Bei Tastendruck |  | Ermöglicht das Ausführen des angegebenen Skripts nach dem Wechsel zum nächsten Seitenelement (Tab) |
|  | Bei Tastenvorlage |  | Ermöglicht das Ausführen des angegebenen Skripts nach dem Wechsel zum vorherigen Seitenelement (Tab) |
|  | Bei Fokus |  | Ermöglicht das Ausführen eines Skripts, sobald ein Element fokussiert wird |
| Tab-Index |  | Positiver ganzzahliger Wert, beginnend bei null | Legt die Reihenfolge fest, in der aktive (bearbeitbare) Felder über die Tastatur umgeschaltet werden (zum Beispiel mit der Tabulatortaste) |
| Automatisierungs-ID |  |  | Steuer-ID für automatisierte Tests und für die Übertragung von CSS-Einstellungen |

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
- **Authentifizierungsformulare**: Wird in Anmelde- und Registrierungsformularen verwendet, um Passwörter sicher einzugeben.
- **Interaktive Formulare**: Ermöglicht interaktive Formulare, die die Eingabe vertraulicher Daten erfordern.

## Ausnahmen
- **Formatierungsbeschränkungen**: Unterstützt keine komplexen Textformate wie Hyperlinks oder eingebettete Bilder.