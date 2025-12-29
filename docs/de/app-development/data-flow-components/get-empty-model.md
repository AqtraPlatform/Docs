# Leeres Modell abrufen

![](../../assets/images/app-development/get-empty-model.png)

## Allgemeine Informationen
Der Schritt „Leeres Modell abrufen“ wird in Datenfluss-Skripten verwendet, die keine Datenmodellabfrage am Eingang erfordern. Er wird häufig verwendet, wenn der Datenfluss aufgerufen wird, um regelmäßige Operationen auszuführen, wie z. B. das Generieren von Berichten, insbesondere wenn diese geplant sind (zum Beispiel durch cron).

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld      | Wertoptionen      | Zweck      |
|-----------------------|-------------------|------------|
| Schrittname           | -                 | Name des Schrittes |
| Eingabewerte validieren | true, false       | Gibt an, dass die Eingabewerte vor der Verarbeitung auf Richtigkeit überprüft werden sollen |

## Fälle
- **Regelmäßige Operationen**: Ideal für Datenflüsse, die regelmäßig ohne Eingabedaten ausgeführt werden sollen.
- **Anfangszustand des Datenflusses**: Wird verwendet, um den Datenfluss ohne vordefinierte Daten zu initialisieren, sodass Entwickler das Datenmodell selbst mit nachfolgenden Schritten erstellen und befüllen können.

## Ausnahmen
- **Keine Eingabedaten**: Bei Verwendung dieses Schrittes werden die Eingabedaten im Datenfluss nicht bereitgestellt. Das bedeutet, dass der Entwickler das Datenmodell in nachfolgenden Schritten initialisieren und befüllen muss.

## Anwendungsszenario

Diese Komponente ist eine Schnittstelle zum Hinzufügen eines neuen Namens über ein **Eingabefeld** im Frontend, gefolgt von der Aktualisierung des Datenmodells und der Anzeige des Ergebnisses in einem **Datagrid**. Der Datenfluss in der Komponente ermöglicht das Hinzufügen eines neuen Namens zum Modell und die Aktualisierung des Datensatzes im **Datagrid**.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1G3v4cZiteFdONpIjxPAf78a8gBTrh0w_/view?usp=sharing) herunterladen.