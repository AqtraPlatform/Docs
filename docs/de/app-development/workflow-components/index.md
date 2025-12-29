# Workflow

## Was ist ein Workflow? {: #workflow }

Ein Workflow ist ein Mechanismus zur Verwaltung von Zuständen und Aufgaben in verschiedenen Komponentenskripten auf der Plattform. Er ermöglicht es Ihnen, die sequenzielle Ausführung von Aufgaben zu organisieren, Zustände beizubehalten und die Möglichkeit zu bieten, im Falle eines Fehlers neu zu starten.

### Wie erstelle ich einen Workflow?

1. **Toolbox öffnen**: Öffnen Sie das Toolbox-Menü im Komponentenfenster und gehen Sie zum Tab Flows.
2. **Workflow hinzufügen**: Klicken Sie auf das Workflow-Symbol und ziehen Sie es in den Arbeitsbereich. Ein neuer Workflow wird erscheinen, der konfiguriert werden kann.

Mit dem visuellen Builder des Workflows können Sie ein Workflow-Skript konfigurieren:

- **Hinzufügen von Phasen und Schritten**: Der Editor ermöglicht es Ihnen, Phasen und Schritte hinzuzufügen, die die Logik des Workflows bilden.
- **Sequenzkonfiguration**: Skripte werden von oben nach unten und von links nach rechts ausgeführt, was es Ihnen ermöglicht, einen konsistenten Fluss von Aufgaben zu erstellen.

### Workflow-Parameter

- **Workflow-Name**: Der Name, der verwendet wird, um den Workflow in der Komponente zu identifizieren.
- **Zugriff einschränken**: Wenn auf "Ja" gesetzt, wird ein Sicherheitskontext für den Workflow erstellt.

### Bearbeiten von Workflow-Phasen und -Schritten

- **Phasen hinzufügen**: Mit der "+"-Schaltfläche können Sie neue Phasen hinzufügen.
- **Phasen löschen**: Die "X"-Schaltfläche ermöglicht es Ihnen, unnötige Phasen zu löschen.
- **Phasen bearbeiten**: Nur der Phasenname kann geändert werden.
- **Schritte hinzufügen und löschen**: Schritte können innerhalb von Phasen hinzugefügt und entfernt werden, um spezifische Workflow-Aktionen zu definieren.

## Benachrichtigungsgruppe

Komponenten zum Senden von Benachrichtigungen und Bestätigungen:

- [Benachrichtigungsstufen](notifications-steps.md) - Übersicht über Benachrichtigungsstufen
- [Benachrichtigung senden](send-notification.md) - Benachrichtigungen an Benutzer senden
- [Vorlagenbasierte Benachrichtigung senden](send-templated-notification.md) - Vorlagenbasierte Benachrichtigungen senden
- [Benutzerbestätigung anfordern](get-user-confirmation.md) - Benutzerbestätigung anfordern

## Integrationsgruppe

Komponenten zur Integration mit anderen Systemen:

- [Integrationsstufen](integrations-steps.md) - Übersicht über Integrationsstufen
- [Datenfluss ausführen](execute-data-flow.md) - Datenfluss aus dem Workflow ausführen

## Gemeinsame Gruppe

Gemeinsame Workflow-Operationen:

- [Gemeinsame Schritte](common-steps.md) - Übersicht über gemeinsame Schritte
- [Modell aktualisieren](update-model.md) - Datenmodell aktualisieren
- [Abschließen](finish.md) - Workflow-Ausführung abschließen
- [Modellfeld aktualisieren](update-model-field.md) - Bestimmtes Modellfeld aktualisieren
- [Auf Entwurf zurücksetzen](reset-to-draft.md) - Workflow auf den Entwurfszustand zurücksetzen

## Bedingungen Gruppe

Bedingte Logik und Verzweigungen:

- [Bedingungsstufen](conditions-steps.md) - Übersicht über Bedingungsstufen
- [Switch Case](switch-case.md) - Switch-Case-Verzweigung
- [Wenn-Bedingung](if-condition.md) - Bedingte Verzweigung