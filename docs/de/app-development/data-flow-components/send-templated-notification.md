# Send templated notification

![](../../assets/images/app-development/send-templated-notification.png)

## Allgemeine Informationen
Der Schritt „Send Templated Notification“ ist dafür konzipiert, Benachrichtigungen an Benutzer oder Benutzergruppen mithilfe von vordefinierten Vorlagen zu senden. Dieser Schritt bietet Flexibilität bei der Auswahl der Zustellmethode und der Empfänger der Benachrichtigung.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld  | Wertoptionen   | Zweck |
|-------------------|----------------|-------|
| Schrittname       | -              | Name des Schrittes |
| Quellenschritt    | -              | Auswahl des vorherigen Schrittes | 
| Benachrichtigungstyp | Smtp, Mail, SignalR | Art des Benachrichtigungszustellkanals |
| Benutzerinformationsfeld | -        | Liste der Benutzer, die benachrichtigt werden sollen |
| Benutzerweiterleitung | -          | Weiterleitung des Benutzers zur Zustellung der Benachrichtigung |
| Benutzername      | -              | Spezifischer Benutzer, der benachrichtigt werden soll |
| Vorlage           | -              | Auswahl aus vordefinierten Benachrichtigungsvorlagen |
| Renderart         | Text, Html, Docx, Xlsx, Pdf | Art der Darstellung der Benachrichtigungsvorlage  |
| Nachrichtenthema   | Text           | Betreffzeile für E-Mail-Benachrichtigungen |

## Fälle
- **Automatisierte Benachrichtigungen**: Wird verwendet, um Benachrichtigungen an Benutzer mithilfe vordefinierter Vorlagen zu senden, um konsistente und genaue Nachrichten sicherzustellen.
- **Flexibilität der Nachrichtenübermittlung**: Ermöglicht die Auswahl zwischen verschiedenen Zustellkanälen (z. B. SMTP, Mail, SignalR), was die Reichweite und Effizienz der Kommunikation erhöht.
- **Personalisierung von Benachrichtigungen**: Unterstützt die Anpassung von Benachrichtigungen für spezifische Benutzer oder Gruppen sowie verschiedene Inhaltsformate (Text, HTML, Docx, Xlsx).

## Ausnahmen
- **Anforderung eines konfigurierten Zustellkanals**: Damit Benachrichtigungen erfolgreich gesendet werden können, muss ein funktionierender Zustellkanal vorhanden sein, wie z. B. ein SMTP-Server für E-Mail-Benachrichtigungen.