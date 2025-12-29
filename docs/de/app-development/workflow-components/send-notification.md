# Benachrichtigung senden

![](../../assets/images/app-development/send-notification-workflow.png)

## Allgemeine Informationen
Der Schritt „Benachrichtigung senden“ innerhalb des Workflows wird verwendet, um einfache Benachrichtigungen an einen Benutzer oder eine Gruppe von Benutzern über ein Glockensymbol zu senden. Dies ermöglicht eine effektive Kommunikation mit den Systembenutzern, indem wichtige Informationen oder Benachrichtigungen übermittelt werden.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld   | Wertoptionen        | Zweck |
|--------------------|---------------------|------------|
| Schrittname        | -                   | Name des Schrittes |
| Benachrichtigungstyp | Smtp, Mail, SignalR | Art des Benachrichtigungsübertragungskanals |
| Benutzerinformationsfeld | Mehrfachauswahl aus Katalog | Feld, das Benutzer oder eine Liste von Benutzern enthält |
| Benutzername       | Mehrfachauswahl aus Katalog | Spezifischer Benutzer, der benachrichtigt werden soll |
| Nachricht          | -                   | Benachrichtigungstext |

## Fälle
- **Benutzerinformationen**: Wird verwendet, um Benutzer über wichtige Ereignisse, Systemänderungen, Alarme oder andere Nachrichten, die Aufmerksamkeit erfordern, zu informieren.
- **Personalisierte Benachrichtigungen**: Ermöglicht das Senden von Benachrichtigungen an spezifische Benutzer oder Gruppen, wodurch die Kommunikation gezielter und effektiver wird.

## Ausnahmen
- **Bedarf an aktuellen Benutzerinformationen**: Eine effektive Zustellung von Benachrichtigungen erfordert aktuelle Benutzerinformationen, einschließlich der Kontaktdaten der Benutzer.
- **Auswahl des richtigen Übertragungskanals**: Sie müssen sorgfältig den Typ des Übertragungskanals (Smtp, Mail, SignalR) wählen, abhängig von den Vorlieben der Benutzer und den technischen Möglichkeiten des Systems.