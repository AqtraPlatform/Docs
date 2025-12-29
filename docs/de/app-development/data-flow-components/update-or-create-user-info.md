# Aktualisieren oder Erstellen von Benutzerinformationen

![](../../assets/images/app-development/update-or-create-user-info.png)

## Allgemeine Informationen
Der Schritt „Aktualisieren oder Erstellen von Benutzerinformationen“ wird verwendet, um vorhandene Benutzerinformationen zu aktualisieren oder einen neuen Benutzer zu erstellen. Dieser Schritt funktioniert ausschließlich mit der Komponente „Benutzerinformationen“. Wenn Benutzerinformationen aktualisiert werden und das Passwort nicht angegeben ist, bleibt es unverändert.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld  | Wertoptionen  | Zweck |
|-------------------|---------------|-------|
| Schrittname       | -             | Name des Schrittes |
| Quellenschritt    | -             | Auswahl des vorherigen Schrittes |
| Benutzerinformationsfeld | -       | Ein Feld, das Informationen über den Benutzer enthält |
| Benutzername      | -             | Name des Benutzers |
| Benutzerpasswort  | -             | Benutzerpasswort (erforderlich) |
| Benutzer deaktiviert | true, false | Aktivitätsstatus des Benutzers |
| Aktualisierungsfelder | name, email, lastName, userName, firstName, middleName | Felder zum Aktualisieren oder Erstellen von Benutzerinformationen |

## Fälle
- **Aktualisierung von Benutzerinformationen**: Wird verwendet, um Daten über vorhandene Benutzer zu ändern, einschließlich ihrer Kontaktdaten, Benutzernamen und anderer persönlicher Informationen.
- **Erstellen neuer Benutzer**: Geeignet zum Hinzufügen neuer Benutzer zum System, sodass Sie die Benutzerdatenbank schnell und effizient erweitern können.

## Ausnahmen
- **Bedarf an Datenakkuratheit**: Der Schritt erfordert eine genaue und aktuelle Dateneingabe, insbesondere beim Erstellen neuer Benutzer.
- **Passwortverwaltung**: Wenn Benutzerinformationen aktualisiert werden und das Passwort nicht angegeben ist, bleibt es unverändert. Bei der Erstellung eines Benutzers ist die Angabe eines Passworts obligatorisch.

## Anwendungsszenario

Die Komponente ist dafür ausgelegt, Benutzerinformationen zu verwalten. Sie umfasst das Abrufen von Benutzerinformationen, das Aktualisieren ihrer Daten und das Erstellen eines neuen Benutzerdatensatzes mit angegebenen Parametern.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1zrn1vRmP3BtXAp-FBsoc5OHj96JuGKvF/view?usp=sharing) herunterladen.