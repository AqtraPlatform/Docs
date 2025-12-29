# Erweiterungsmenü
<br>

Das Menü besteht aus 2 Blöcken:
- **Vorlagen**
- **SMTP-Einstellungen**
<br>

## Vorlagen

Vorlagen werden für E-Mails und Benutzerbenachrichtigungen verwendet und können nur im Schritt „Templated Notification senden“ verwendet werden. Vorlagen werden im Abschnitt „Anwendung/Vorlagen“ konfiguriert.
<br>

### Hinzufügen/Entfernen von Vorlagen

- Um **eine neue Vorlage hinzuzufügen**, klicken Sie auf die Schaltfläche „HINZUFÜGEN“. 
- Um **eine Vorlage zu löschen**, klicken Sie auf das Kreuz in der allgemeinen Liste aller Vorlagen.
<br>

### Einrichten des Vorlagenkomponentenmodells

Beim Hinzufügen oder Bearbeiten einer Vorlage müssen Sie eine Objektmodellstruktur definieren, die mit Dataflow und/oder Workflow interagiert. Dies geschieht durch das Festlegen einer Reihe von Eigenschaften für jede von ihnen, ähnlich wie bei der Konfiguration einer beliebigen Komponente.
<br>

### Anpassen des Layouts und Inhalts der Vorlage

Die Plattform verwendet den „DevExpress Report Designer“, um Vorlagen zu erstellen. Diese Vorlagen können verwendet werden, um Benachrichtigungen zu senden oder Dokumente zu erstellen.

- Nach dem Erstellen einer neuen Vorlage öffnet sich das Bearbeitungsfenster. Hier können Sie visuelle Elemente zu Ihrer Vorlage hinzufügen und anpassen sowie Links zu Ihren Vorlageneigenschaften erstellen.
<br>

## SMTP-Einstellungen

Der Mailingdienst wird verwendet, um Benachrichtigungen über SMTP zu senden.

Empfehlungen zur Verwendung eines SMTP-Servers:

- **Während der Entwicklung**: Es wird empfohlen, einen Unternehmens-SMTP-Server oder Shareware-Dienste wie [sendinblue.com](http://www.sendinblue.com/) zu verwenden. Vermeiden Sie die Verwendung eines persönlichen Servers, um nicht im Spam zu landen.
- **Für den industriellen Einsatz**: Es ist vorzuziehen, einen Unternehmens- oder kostenpflichtigen kommerziellen SMTP-Dienst zu verwenden.

Konfigurieren Sie die folgenden Einstellungen für den Mailingdienst:

| Einstellungsfeld | Wertoptionen | Zweck |
| -------------- | ----------------- | ---------- |
| `Sender`       | -                 | Standard-Absendername, z.B. `sender@company.com` |
| `User name`    | -                 | Anmeldedaten für den SMTP-Server, normalerweise im `user@company.com`-Format. |
| `Password`     | -                 | Passwort für den SMTP-Server |
| `Host`         | -                 | Adresse des SMTP-Servers, z.B. `http://smtp-relay.sendinblue.com/` |
| `Port`         | -                 | Der Port für den SMTP-Server hängt vom Anbieter ab, z.B. 587 für sendinblue.com |
| `Enable SSL`   | `true`, `false`   | Verwendung von SSL zur Verschlüsselung von Daten. „True“ wird normalerweise für moderne SMTP-Server verwendet. |

<br>

### Beispiel für die Verwendung von Vorlage und SMTP

1. Erstellen und passen Sie eine Vorlage an.
2. Richten Sie SMTP ein, um E-Mails zu senden.
3. Fügen Sie in Ihrem Workflow den Schritt „Templated Notification senden“ hinzu.
4. Wählen Sie den SMTP-Benachrichtigungstyp aus und legen Sie die Parameter für den E-Mail-Versand fest.
5. Wählen Sie Ihre Vorlage aus und legen Sie den Render-Typ in HTML fest.

Nachdem Sie diese Schritte abgeschlossen haben, sendet Ihr Workflow eine E-Mail mit der angepassten Vorlage.