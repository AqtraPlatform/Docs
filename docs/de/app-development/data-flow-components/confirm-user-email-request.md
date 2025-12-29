# Bestätigen der Benutzer-E-Mail-Anfrage

![](../../assets/images/app-development/confirm-user-email-request.png)

## Allgemeine Informationen
Der Schritt „Bestätigen der Benutzer-E-Mail-Anfrage“ wird verwendet, um den Benutzer zu aktivieren, der ursprünglich mit dem Flag „Deaktiviert“ erstellt wurde. Dieser Prozess umfasst die Überprüfung des Benutzers per E-Mail unter Verwendung des Schrittes „Vorlagenbenachrichtigung senden“. Der Schritt erfordert eine Anwendungsdomäne mit einer öffentlichen URI und einen konfigurierten SMTP-Server, um E-Mail-Benachrichtigungen zu senden.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld   | Wertoptionen | Zweck |
|---------------------|-------------------|------------|
| Schrittname         | -                 | Name des Schrittes |
| Quellenschritt      | -                 | Auswahl des vorherigen Schrittes |
| Benutzerinformationsfeld | -             | Ein Feld, das Informationen über den Benutzer enthält |
| Benutzername        | -                 | Name des Benutzers, dessen Bestätigung eingeholt werden soll |
| Client für Anfrage  | -                 | Der Client oder die Anwendung, die die Bestätigungsanfrage initiiert |

## Fälle
- **Aktivierung neuer Benutzer**: Dieser Schritt wird verwendet, um Benutzer zu aktivieren, die als deaktiviert registriert wurden, indem ihre E-Mail überprüft wird. Dies bietet eine zusätzliche Ebene der Überprüfung und Sicherheit.
- **Benutzerzugriffsverwaltung**: Geeignet für Systeme, die eine E-Mail-Verifizierung des Benutzers erfordern, bevor der vollständige Zugriff auf die Systemfunktionen gewährt werden kann.

## Ausnahmen
- **Anforderung eines konfigurierten SMTP-Servers**: Ein konfigurierter SMTP-Server ist erforderlich, damit Bestätigungs-E-Mail-Benachrichtigungen erfolgreich gesendet werden können.
- **Abhängigkeit von Anwendungsdomäne und öffentlicher URI**: Dieser Schritt erfordert eine Anwendungsdomäne mit einer öffentlichen URI, um sicherzustellen, dass der Vorgang korrekt ist und dass der Verifizierungsprozess dem Benutzer zur Verfügung steht.