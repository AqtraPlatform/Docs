# Update model field

![](../../assets/images/app-development/update-model-field.png)

## Allgemeine Informationen
Der Schritt „Update Model Field“ innerhalb des Workflows wird verwendet, um ein bestimmtes Feld im Modell zu aktualisieren. Dieser Schritt ermöglicht es Ihnen, die Werte einzelner Felder im Datenmodell zu ändern, was besonders nützlich für das dynamische Datenmanagement während der Ausführung des Workflows ist.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld | Zweck |
|------------------|-------|
| Schrittname      | Name des Schrittes „Update Model Field“ |
| Modellfeld       | Modellfeld, das Sie aktualisieren möchten |
| Wert             | Wert, auf den das Feld aktualisiert wird |
| Quellfeld        | Quellfeld, dessen Wert für die Aktualisierung verwendet wird |

## Fälle
- **Dynamische Datenaktualisierung**: Wird verwendet, um Werte im Modell basierend auf während des Workflows generierten Daten zu ändern, z. B. um den Status einer Aufgabe zu aktualisieren oder Konfigurationsoptionen zu ändern.

## Ausnahmen
- **Genauigkeit und Relevanz der Daten**: Stellen Sie sicher, dass die aktualisierten Daten genau und aktuell sind, um unerwünschte Konsequenzen zu vermeiden.
- **Verständnis der Auswirkungen von Änderungen**: Es ist wichtig, die Auswirkungen der Aktualisierung eines Feldes auf das gesamte Workflow-Modell und die Logik zu verstehen, insbesondere in komplexen Systemen mit miteinander verbundenen Abhängigkeiten.