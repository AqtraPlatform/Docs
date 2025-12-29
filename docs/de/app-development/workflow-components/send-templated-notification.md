# Send templated notification

![](../../assets/images/app-development/send-templated-notification-workflow.png)

## Allgemeine Informationen
Der Schritt „Send Templated Notification“ innerhalb des Workflows wird verwendet, um Benachrichtigungen an Benutzer oder Benutzergruppen mithilfe vorkonfigurierter Vorlagen zu senden. Dies ermöglicht es Ihnen, standardisierte, aber personalisierte Nachrichten zu erstellen, was die Kommunikation verbessert und die Konsistenz der Nachrichten gewährleistet.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld   | Wertoptionen            | Zweck |
|-------------------|--------------------------|------------|
| Schrittname       | -                        | Name des Schrittes |
| Benachrichtigungstyp | Smtp, Mail, SignalR      | Art des Benachrichtigungsübertragungskanals |
| Benutzerinformationsfeld | Multiselect of Catalog | Feld mit Informationen über einen Benutzer oder eine Benutzergruppe |
| Benutzergruppe     | Multiselect of Catalog | (Veralteter Parameter, nicht verwendet) |
| Benutzerweiterleitung | Multiselect of Catalog | Konfiguration der Benachrichtigungsweiterleitung |
| Benutzername       | Multiselect of Catalog | Spezifischer Benutzer, der benachrichtigt werden soll |
| Vorlage            | Multiselect of Catalog | Auswahl einer Benachrichtigungsvorlage |
| Render-Typ         | Text, Html, Docx, Xlsx   | Format der Vorlagenanzeige |

## Fälle
- **Automatisierte Benachrichtigungen**: Wird verwendet, um standardisierte Benachrichtigungen zu senden, wie Erinnerungen, Aktionsbestätigungen oder Informationsnachrichten.
- **Effektive Kommunikation**: Geeignet für die Erstellung professionell gestalteter Nachrichten für externe oder interne Kommunikationen.

## Ausnahmen
- **Anforderungen an die Vorlagenanpassung**: Benachrichtigungsvorlagen müssen im Voraus vorbereitet und konfiguriert werden, um sicherzustellen, dass die Nachrichten für Kommunikationszwecke relevant sind.
- **Verwaltung der Benachrichtigungsempfänger**: Es ist wichtig, die Empfänger der Nachrichten mithilfe des Benutzerinformationsfelds und des Benutzernamens genau zu bestimmen, um sicherzustellen, dass die Benachrichtigungen die richtigen Empfänger erreichen.