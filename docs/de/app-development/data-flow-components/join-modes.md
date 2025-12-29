# Join-Modelle

![](../../assets/images/app-development/join-models.png)

## Allgemeine Informationen
Der Schritt „Join-Modelle“ ist dafür ausgelegt, Daten aus zwei verschiedenen Quellen zu kombinieren. Er fügt Daten aus der Quelle „Rechter Schritt“ zu den Daten aus der Quelle „Linker Schritt“ hinzu, wenn übereinstimmende Einträge in beiden Quellen gefunden werden.

Der Schritt erstellt ein neues Datenmodell, indem er die Datenflüsse zusammenführt, die in den Parametern „Linker Schritt“ und „Rechter Schritt“ definiert sind. Der Schritt wartet, bis beide Flüsse die Verarbeitung abgeschlossen haben, und sortiert und kombiniert dann die Daten.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld | Wertoptionen | Zweck |
|------------------|--------------|-------|
| Schrittname      | -            | Name des Schrittes |
| Linker Schritt    | -            | Datenquelle für die linke Seite der zusammengeführten Flüsse |
| Rechter Schritt   | -            | Datenquelle für die rechte Seite der zusammengeführten Flüsse |
| Linker Schlüssel  | -            | Schlüssel zum Zusammenführen von Daten aus der linken Quelle |
| Rechter Schlüssel | -            | Schlüssel zum Zusammenführen von Daten aus der rechten Quelle |
| Zuordnung        | -            | Zuordnungsfelder zwischen linken und rechten Quellen |

## Fälle
- **Zusammenführen von Datenflüssen**: Wird verwendet, um zwei verschiedene Datenflüsse in ein Modell zu integrieren, sodass Sie die zusammengeführten Daten analysieren und verarbeiten können.
- **Datenanreicherung**: Wird verwendet, um zusätzliche Informationen aus einem Datensatz zu einem anderen hinzuzufügen, wodurch die Vollständigkeit der Informationen verbessert wird.

## Ausnahmen
- **Bedarf an einem exakten Zusammenführungs-Schlüssel**: Fehler bei der Definition des „Linken Schlüssels“ und „Rechten Schlüssels“ können zu falschem oder ineffizientem Datenzusammenführen führen.

## Anwendungsszenario

Diese Komponente ermöglicht das **Testen** und **Überprüfen** der Funktionalität eines Datenflusses, bei dem Daten aus verschiedenen Quellen **zusammengeführt** werden. Sie bietet **Feldzuordnung** und **Datenzusammenführungsüberprüfung** im **Frontend** und in der **HTTP**-Antwortvorschau.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1YRpXJwNSTp_jOPxP-j0M9SvocZw1W6Tt/view?usp=sharing) herunterladen.