# Benachrichtigung senden

![](../../assets/images/app-development/send-notification.png)

## Allgemeine Informationen
Der Schritt „Benachrichtigung senden“ ist dafür konzipiert, benutzerdefinierte Benachrichtigungen an Benutzer oder Benutzergruppen zu senden. Dieser Schritt bietet ein hohes Maß an Flexibilität, da Sie den Text und das Thema jeder Benachrichtigung direkt festlegen können, was ihn ideal für Situationen macht, die personalisierte Nachrichten erfordern.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld   | Wertoptionen | Zweck |
|------------------|-------------------|------------|
| Schrittname        | -                 | Name des Schrittes |
| Quellenschritt      | -                 | Quelle der Daten zum Senden der Benachrichtigung |
| Benutzerinformationsfeld  | -                 | Feld, das Informationen über die Empfänger der Benachrichtigung enthält |
| Benutzername        | -                 | Name des Benutzers, an den die Benachrichtigung gesendet wird |
| Nachrichtenkörperfeld | -               | Feld für den Text der Nachricht |
| Nachrichtenthema    | Text                | Betreff der Benachrichtigung |
| Nachrichtenkörper     | Text                 | Anpassbarer Text der Benachrichtigung  |
| Benachrichtigungstyp| Smtp, Mail, SignalR                 | Benachrichtigungstyp |

## Fälle
- **Personalisierte Benachrichtigungen**: Wird verwendet, um einzigartige Nachrichten für jeden Benutzer oder jede Situation zu erstellen, um maximale Relevanz und Engagement der Empfänger sicherzustellen.
- **Flexible Kommunikation**: Geeignet für Skripte, in denen spezielle Nachrichten erforderlich sind, wie z. B. Sonderangebote, individuelle Erinnerungen oder personalisierte Newsletter.

## Ausnahmen
- **Anforderung an die Detailgenauigkeit der Nachricht**: Bei der Formulierung des Textes jeder Benachrichtigung sollte auf Details und Präzision geachtet werden.
- **Notwendigkeit einer sorgfältigen Benachrichtigungsverwaltung**: Da jede Nachricht individuell anpassbar ist, ist es wichtig, den Prozess der Erstellung und des Versands von Benachrichtigungen sorgfältig zu verwalten, um Fehler und Inkonsistenzen zu vermeiden.