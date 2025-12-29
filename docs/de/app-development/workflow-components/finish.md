# Finish

![](../../assets/images/app-development/finish.png)

## Allgemeine Informationen
Der Schritt „Finish“ innerhalb eines Workflows ist dafür vorgesehen, die Ausführung des aktuellen Workflows abzuschließen. Dieser Schritt wird typischerweise verwendet, um den Abschlusszeitpunkt eines Workflows explizit anzugeben, insbesondere in den alternativen Skripten, die im Bedingungen-Block definiert sind.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld | Zweck |
|------------------|-------|
| Schrittname      | Name des „Finish“-Schrittes |

## Fälle
- **Kontrollierte Workflow-Abschluss**: Wird verwendet, um den Abschlusszeitpunkt eines Workflows explizit anzugeben, was besonders wichtig in komplexen Prozessen mit vielen Bedingungen und Verzweigungen ist.
- **Alternative Ausführungspfade**: Geeignet für Skripte, in denen ein Workflow unter bestimmten Bedingungen, die vom Hauptausführungsfluss abweichen, beendet werden muss.

## Ausnahmen
- **Notwendigkeit einer ordnungsgemäßen Konfiguration**: Es ist wichtig sicherzustellen, dass der „Finish“-Schritt ordnungsgemäß in die Workflow-Logik eingebettet ist, damit der Prozess nicht vorzeitig unterbrochen oder wichtige Schritte übersprungen werden.