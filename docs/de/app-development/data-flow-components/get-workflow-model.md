# Workflow-Modell abrufen

![](../../assets/images/app-development/get-workflow-model.png)

## Allgemeine Informationen
Der Schritt „Workflow-Modell abrufen“ wird ausschließlich in Datenflüssen verwendet, die von einem Workflow aufgerufen werden. Er ermöglicht es Ihnen, das Modell und die Daten des aufrufenden Workflows innerhalb des aktuellen Datenflusses abzurufen.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld      | Wertoptionen      | Zweck      |
|-----------------------|-------------------|------------|
| Schrittname           | -                 | Name des Schrittes |
| Eingabewerte validieren | true, false       | Gibt an, dass Eingabewerte vor der Verarbeitung auf Richtigkeit überprüft werden sollen |

## Fälle
- **Integration von Datenfluss und Workflow**: Ermöglicht die Integration des Datenflusses mit dem Workflow und bietet Zugriff auf das Modell und die Daten des aufrufenden Workflows.

## Ausnahmen
- **Eingeschränkte Verwendung**: Der Schritt ist nicht für die Verwendung im Eingabedatenfluss vorgesehen.

## Anwendungsszenario

Die Komponente ermöglicht es Ihnen, einen Datenfluss zum Aktualisieren eines Datensatzes in der Quellkomponente zu erstellen. Sie umfasst Schritte wie Workflow-Modell abrufen, um das Workflow-Modell zu erhalten, Eintrag aktualisieren, um den Datensatz mit den entsprechenden Parametern zu aktualisieren, und Antwort schreiben, um das Ergebnis auszugeben. Diese Komponente kann verwendet werden, um Daten in der Quellkomponente mithilfe von Workflows und UI-Elementen zu aktualisieren.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1F2ZFQlyMf6ZaxABcoOWib4T8AD8w-75Q/view?usp=sharing) herunterladen.