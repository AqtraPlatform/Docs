# Rohmodell abrufen

![](../../assets/images/app-development/get-raw-model.png)

## Allgemeine Informationen
Der Schritt „Rohmodell abrufen“ wird in einem Datenfluss verwendet, der die Verarbeitung eines benutzerdefinierten Datenmodells erfordert, das nicht dem Standardkomponentenmodell, dem Workflow oder anderen Standardoptionen entspricht. Typische Anwendungsfälle umfassen Datenflüsse, die aus einem Komponentenskript aufgerufen werden, mit innerhalb des Skripts definierten Variablen, sowie die Verarbeitung von Formulardaten innerhalb einer Multi-Komponenten-Struktur.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld      | Wertoptionen      | Zweck      |
|-----------------------|-------------------|------------|
| Schrittname           | -                 | Name des Schrittes |
| Eingabewerte validieren | true, false       | Gibt an, dass die Eingabewerte vor der Verarbeitung auf Richtigkeit überprüft werden sollen |

## Fälle
- **Integration mit Komponentenskript**: Wird für Datenflüsse verwendet, die aus einem Komponentenskript aufgerufen werden, wenn spezifische Variablen oder Daten erforderlich sind.
- **Verarbeitung von Multi-Komponenten-Formulardaten**: Geeignet für Skripte, bei denen Datenflüsse mit Daten arbeiten, die aus Formularen in einer Multi-Komponenten-Struktur stammen.

## Ausnahmen
- **Anforderung an die Modellkonfiguration**: Sie müssen das Datenmodell im JSON-Format vorkonfigurieren.
- **Merkmale des Modellformats**: Eine unsachgemäße Modellkonfiguration kann zu fehlerhafter Datenverarbeitung oder Datenflussfehlern führen.