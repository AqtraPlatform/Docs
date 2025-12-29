# Switch Case

![](../../assets/images/app-development/switch-case.png)

## Allgemeine Informationen
Der „Switch Case“-Schritt innerhalb eines Workflows wird als bedingungsloser Schalteroperator verwendet, der es Ihnen ermöglicht, zwischen verschiedenen Skriptoptionen zu wählen. Dieser Schritt ist ideal, um die Prozesslogik basierend auf bestimmten Bedingungen zu steuern, die normalerweise durch Boolean- oder Enum-Felder angegeben werden. Bei Verwendung wird das Hauptskript immer deaktiviert und der Prozess wechselt zu einem der alternativen Zweige.
![](../../assets/images/app-development/switch-case-example.png)

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld     | Zweck |
|----------------------|------------|
| Schrittname          | Name des „Switch Case“-Schritts |
| Schalterquellenfeld  | Feld, basierend auf dessen Wert das Skript ausgewählt wird |

## Fälle
- **Prozesslogik-Verzweigung**: Wird verwendet, um bedingte Pfade in einem Workflow zu erstellen, bei denen die nächste Richtung basierend auf einer bestimmten Bedingung oder einem Wert bestimmt wird.
- **Verwaltung verschiedener Ausführungsskripte**: Geeignet für Skripte, bei denen ein Prozess je nach vordefinierten Bedingungen oder Benutzerauswahl unterschiedliche Ausführungen erfordert.

## Ausnahmen
- **Genauigkeit der Übergangsbedingungen**: Es ist notwendig, die Schalterbedingungen für jeden Fall genau zu definieren, um sicherzustellen, dass der richtige Ausführungspfad ausgewählt wird.
- **Komplexität der Verwaltung mehrerer Pfade**: Komplexe Workflows mit vielen möglichen Pfaden erfordern ein klares Verständnis und Management jedes einzelnen, um Fehler in der Prozesslogik zu vermeiden.