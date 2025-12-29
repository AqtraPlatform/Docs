# Update-Eintrag

![](../../assets/images/app-development/update-entry.png)

## Allgemeine Informationen

Der Schritt „Update-Eintrag“ wird verwendet, um einen vorhandenen Eintrag im System zu erstellen, zu aktualisieren oder zu löschen. Dieser Schritt wird direkt ausgeführt, und das System wartet auf dessen Abschluss. Wenn während der Ausführung ein Fehler auftritt, wird die weitere Ausführung des Datenflusses gestoppt.

## Parameter

**Schritt Einstellungen:**

| Einstellungsfeld        | Wertoptionen   | Zweck                                          |
| ----------------------- | --------------- | ---------------------------------------------- |
| Schrittname             | -               | Name des Schrittes                             |
| Quellenschritt          | -               | Auswahl des vorherigen Schrittes               |
| Komponente              | -               | Zu aktualisierende Komponente                  |
| Feldkomponenten-Schlüssel| -               | Feld mit dem Schlüssel der Komponente zur Aktualisierung |
| Eintrag für Löschung markieren | true, false | Markierung für die Eintragslöschung           |
| Namensfeld              | -               | Name des Feldes, das aktualisiert werden soll  |
| Ergebnis-Speicherfeld   | -               | Feld zum Speichern des Ergebnisses der Operation |
| Felderzuordnung         | -               | Zuordnung von Feldern zwischen Datenfluss und Komponente |

## Fälle

- **Datenaktualisierung**: Wird verwendet, um Informationen in den vorhandenen Einträgen der Systemkomponenten zu aktualisieren, um sicherzustellen, dass die Daten genau und aktuell sind.
- **Löschen eines Eintrags**: Der Schritt „Update-Eintrag“ kann verwendet werden, um vorhandene Einträge im System zu löschen. Dies ist besonders relevant in Skripten, in denen veraltete oder falsche Informationen entfernt werden müssen, um die Daten im System genau und aktuell zu halten. Zum Beispiel kann dies das Löschen des Kontos eines Benutzers umfassen, der die Organisation verlassen hat, oder das Entfernen nicht verfügbarer Artikel aus dem Inventar. Es ist wichtig zu beachten, dass der Schritt so konfiguriert werden kann, dass er den Eintrag zur Löschung markiert, was es ermöglicht, den Löschprozess flexibler zu verwalten.

## Ausnahmen

- **Abhängigkeit von der Anwesenheit einer Instanz-ID**: Um Daten erfolgreich zu aktualisieren, muss die Instanz-ID der Komponente zuerst empfangen und übertragen werden.
- **Verwaltung von Laufzeitfehlern**: Jeder Fehler während des Datenaktualisierungsprozesses stoppt den Datenfluss, was eine sorgfältige Überwachung der Fehler- und Ausnahmebehandlung erfordert.

## Anwendungsszenario

Die Komponente präsentiert ein Szenario zum Hinzufügen, Bearbeiten und Löschen von Komponentenaufzeichnungen unter Verwendung des Schrittes „Update-Eintrag“.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1k1oMpI2YSF-P3zgsd2cORfRjFs3l7w0o/view?usp=sharing) herunterladen.