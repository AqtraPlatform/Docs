# Zurücksetzen der Benutzerpasswortanforderung

![](../../assets/images/app-development/reset-user-password-request.png)

## Allgemeine Informationen
Der Schritt „Zurücksetzen der Benutzerpasswortanforderung“ ist dafür vorgesehen, ein neues Passwort für den Benutzer zu generieren. Der Schritt funktioniert in Verbindung mit der „Send Templated Notification“, um sicherzustellen, dass die Benutzer ein neues Passwort erhalten. Der Schritt funktioniert nur, wenn Sie eine Anwendungsdomäne mit einer konfigurierten öffentlichen URI haben.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld   | Wertoptionen | Zweck |
|------------------|-------------------|------------|
| Schrittname        | -                 | Name des Schrittes |
| Quellenschritt      | -                 | Auswahl des vorherigen Schrittes |
| Benutzerinformationsfeld  | -                 | Ein Feld, das Informationen über den Benutzer enthält |
| Benutzername        | -                 | Benutzername, für den das Passwort zurückgesetzt wird |
| Client für die Anfrage | -               | Client oder Anwendung, die die Authentifizierungsanfrage initiiert |

## Fälle
- **Wiederherstellung des Benutzerzugriffs**: Wird in Skripten verwendet, in denen ein Benutzer sein Passwort vergessen hat und es zurücksetzen muss, um wieder auf das System zuzugreifen.

## Ausnahmen
- **Anforderung an eine Anwendungsdomäne mit einer öffentlichen URI**: Der Schritt erfordert eine konfigurierte Anwendungsdomäne mit einer öffentlichen URI, damit er korrekt funktioniert.
- **Abhängigkeit von der Benachrichtigungsmethode für Benutzer**: Die Wirksamkeit des Schrittes hängt von der Zuverlässigkeit und Verfügbarkeit der Benachrichtigungsmethode für Benutzer, wie z. B. E-Mail, ab, die zum Senden eines neuen Passworts verwendet wird.