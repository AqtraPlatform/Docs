# Telefonnummer

![](../../assets/images/app-development/phone-number.png)

## Allgemeine Informationen

Die Telefonnummer ist eine UI-Komponente, die zum Eingeben und Anzeigen von Telefonnummern entwickelt wurde. Diese Komponente erleichtert die Eingabe von Telefonnummern und stellt sicher, dass die eingegebenen Daten korrekt formatiert und validiert werden.

## Parameter

**Komponenten-Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld | Wertoptionen          | Zweck                                                                                 |
| ------------------ | ---------------- | --------------------- | ------------------------------------------------------------------------------------- |
|                    | Name             | -                     | Name der UI-Komponente im System                                                      |
| Allgemein          | Deaktiviert      | true, false           | Diese Eigenschaft ermöglicht es, ein Element im Formular zu deaktivieren              |
|                    | Erforderlich     | true, false           | Diese Eigenschaft macht das Element erforderlich, um das Formular abzusenden          |
|                    | Beschriftung     | -                     | Enthält das Inhaltsverzeichnis des Textcontainers                                     |
|                    | Bindung          | Multiselect des Katalogs | Enthält ein verwandtes „String“-Feld aus dem Modell                                   |
| Ereignisse         | Bei Wertänderung | -                     | Ermöglicht das Ausführen des angegebenen Skripts nach der Änderung des Wertes des Feldes |

**CSS-Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld  | Wertoptionen | Zweck                                                                                                                   |
| ------------------ | ----------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------- | --- | ------------ |
| Layout             | Breite            | -             | Breite der Komponente                                                                                                   |
|                    | Höhe              | -             | Höhe der Komponente                                                                                                      |
|                    | Wachstum          | true, false   | Diese Eigenschaft bestimmt, wie viel ein Element im Verhältnis zu den anderen Flex-Elementen im selben Container wächst     |
|                    | Rand              | -             | Diese Eigenschaft definiert die äußeren Abstände auf allen vier Seiten des Elements                                       |
|                    | Innenabstand      | -             | Diese Eigenschaft legt die inneren Abstände auf allen Seiten des Elements fest                                           |
| Erscheinung        | Eckenradius       | -             | Diese Eigenschaft wird verwendet, um die Ecken eines Elements abzurunden                                                  |
|                    | Randdicke         | -             | Diese Eigenschaft ermöglicht es, die Grenzen für das Element festzulegen                                                  |
| Pinsel             | Hintergrund       | -             | Diese Eigenschaft legt die Hintergrundfarbe des Elements fest                                                              |
|                    | Randpinsel        | -             | Diese Eigenschaft legt die Farbe des Randes des Elements fest                                                            |     | Randfarbe    |

## Fälle

- **Nummerformatvalidierung:** Wird verwendet, um die eingegebene Telefonnummer zu validieren, um sicherzustellen, dass sie einem bestimmten nationalen oder internationalen Format entspricht.

## Ausnahmen

- **Eingeschränkte Formatierungsoptionen:** Die Funktion unterstützt möglicherweise nicht alle möglichen Telefonnummernformate, insbesondere nicht-standardisierte oder regionale Varianten.
- **Empfindlichkeit gegenüber Eingabefehlern:** Ungültige Benutzereingaben können zu Fehlern bei der Verarbeitung von Telefonnummern führen.