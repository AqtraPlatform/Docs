# Store-Eintrag über Bus

![](../../assets/images/app-development/store-entry-over-bus.png)

## Allgemeine Informationen

Der Schritt „Store Entry Over Bus“ ist dafür ausgelegt, das Modell in den Komponentendaten (Felder) über den Bus zu speichern. Dieser Schritt erstellt immer eine neue Instanz der angegebenen Komponente und wird verwendet, um dynamisch mit den Daten im System zu arbeiten. Der Schritt wird asynchron aufgerufen.

## Parameter

**Schritt Einstellungen:**

| Einstellungsfeld | Wertoptionen          | Zweck                                                                                 |
| ---------------- | --------------------- | ------------------------------------------------------------------------------------- |
| Schrittname      | -                     | Name des Schrittes                                                                    |
| Quellschritt     | -                     | Auswahl des vorherigen Schrittes                                                      |
| Komponente       | -                     | Auswahl aus den verfügbaren Komponenten, um den Eintrag zu speichern                  |
| Name             | String                | Systemname des Eintrags, der über Links des Katalogtyps angezeigt werden soll        |
| Schlüssel        | ADD KEY               | Für Komponenten mit dem Restrict access-Flag, Angabe der Schlüssel zur Zuordnung der Felder |
| Schlüssel-Feld   | Mehrfachauswahl des Katalogs | Felder, die die Primärschlüssel der ausgewählten Komponente enthalten                |
| Felderzuordnung  | -                     | Dynamische Konfiguration der Zuordnung von Komponentenmodellen zum Datenflussmodell   |

## Fälle

- **Erstellen neuer Komponenteninstanzen**: Wird verwendet, um automatisch neue Einträge in Komponenten basierend auf Daten im Datenfluss zu erstellen.

## Ausnahmen

- **Abhängigkeit von der Verfügbarkeit der Primärschlüssel in der Komponente**: Die Effektivität des Schrittes hängt von der Verfügbarkeit und Richtigkeit der Primärschlüssel in der Zielkomponente ab, insbesondere wenn die Komponente das Restrict access-Flag hat.
- **Anforderung an die asynchrone Verarbeitung**: Der Schritt wird asynchron ausgeführt, was die Reihenfolge und die Verarbeitungszeit des Systems beeinflussen kann.

## Anwendungsszenario

Diese Komponente ermöglicht das Abrufen von Daten aus der ausgewählten Integration und das Speichern in den entsprechenden Feldern der erstellten Datenmodelle. Die abgerufenen Daten können dann in anderen Teilen des Systems für weitere Verarbeitung oder Anzeige verwendet werden.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1jFuXBG8v-YuICBozvoCPAm0FfBQhApvG/view?usp=sharing) herunterladen.