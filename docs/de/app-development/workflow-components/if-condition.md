# If-Bedingung

![](../../assets/images/app-development/if-condition.png)

## Allgemeine Informationen

Der Schritt „If-Bedingung“ innerhalb des Workflows wird verwendet, um den Wert eines Feldes mit der angegebenen Bedingung zu überprüfen. Dieser Schritt ermöglicht es Ihnen, bedingte Verzweigungen in einem Prozess zu implementieren, bei denen das Ausführen bestimmter Aktionen oder das Wechseln zu einem alternativen Skript vom Ergebnis einer Bedingungsprüfung abhängt. Ein alternatives Skript muss den Schritt „Fertigstellen“ enthalten.

## Parameter

**Schritt Einstellungen:**

| Einstellungsfeld   | Wertoptionen                 | Zweck                                   |
| ------------------ | ---------------------------- | --------------------------------------- |
| Schrittname        | -                            | Name des „If-Bedingung“ Schrittes      |
| Bedingungsfeld     | Mehrfachauswahl aus Katalog  | Feld zur Validierung der Bedingung     |
| Operator           | Gleich, Ungleich, Größer, Kleiner | Art des Operators zur Überprüfung der Bedingung |
| Mit null vergleichen | wahr, falsch                | Überprüfung auf Vergleich mit null      |
| Wert               | -                            | Wert, mit dem das Feld verglichen wird  |

## Fälle

- **Bedingte Ausführung von Aktionen**: Wird verwendet, um verschiedene Teile des Workflows basierend auf den Werten bestimmter Felder zu aktivieren, zum Beispiel, um unterschiedliche Prozesse basierend auf dem Status der Anfrage zu starten.
- **Logische Verzweigung in Prozessen**: Geeignet zur Erstellung komplexer logischer Ketten, bei denen verschiedene Ausführungsschritte von der Erfüllung spezifischer Bedingungen abhängen.

## Ausnahmen

- **Genauigkeit der Bedingungsdefinition**: Es ist wichtig, Bedingungen genau zu definieren und die Felder korrekt zu konfigurieren, um falsche Verzweigungen oder Fehler in der Workflow-Logik zu vermeiden.
- **Umgang mit verschiedenen Skripten**: Sie müssen klar planen, wie verschiedene Skripte je nach Ergebnis der Bedingungsprüfung behandelt werden, insbesondere in mehrstufigen oder komplexen Workflows.