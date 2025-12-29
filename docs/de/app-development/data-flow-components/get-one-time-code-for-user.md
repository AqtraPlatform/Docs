# Einmalcode für Benutzer abrufen

![](../../assets/images/app-development/get-one-time-code-for-user.png)

## Allgemeine Informationen
Der Schritt „Einmalcode für Benutzer abrufen“ wird verwendet, um einen Einmalcode zu generieren und zu senden, der für die Anmeldung im Rahmen der Zwei-Faktor-Authentifizierung erforderlich ist. Dieser Schritt funktioniert in Verbindung mit dem Schritt „Einmalcode für Benutzer bestätigen“ und wird normalerweise mit der Funktion „Vorlagenbenachrichtigung senden“ angewendet.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld   | Wertoptionen | Zweck |
|---------------------|-------------------|------------|
| Schrittname         | -                 | Name des Schrittes |
| Quellenschritt      | -                 | Auswahl des vorherigen Schrittes |
| Benutzername        | -                 | Name oder ID des Benutzers, für den der Code generiert wird |
| Client für Anfrage   | -               | Client oder Anwendung, die die Bestätigungsanfrage initiiert |
| Code-Lebensdauer    | -                 | Die Lebensdauer eines Codes |

## Fälle
- **Zwei-Faktor-Authentifizierung**: Wird verwendet, um eine zusätzliche Sicherheitsebene bei der Anmeldung bereitzustellen, indem ein temporärer Code generiert wird, den der Benutzer bestätigen muss.
- **Erweiterte Anmeldesicherheit**: Geeignet für Szenarien, in denen erweiterte Sicherheitsmaßnahmen erforderlich sind, um unbefugten Zugriff auf das System zu verhindern.

## Ausnahmen
- **Abhängigkeit von der Genauigkeit der Benutzerdaten**: Die Genauigkeit und Relevanz der Benutzerinformationen ist entscheidend für die erfolgreiche Generierung und den Versand eines Einmalcodes.
- **Verwaltung der Code-Lebensdauer**: Sie müssen die Lebensdauer des Codes korrekt konfigurieren, um sicherzustellen, dass Ihr Code aktuell ist und um Probleme beim Benutzerzugriff zu vermeiden.

## Anwendungsszenario 

Die Komponente fügt eine neue String-Definition ForTestCode hinzu. Ein Datenfluss wird erstellt, bei dem ein Einmalcode für den Benutzer über die Schritte Get-Aktionsmodell und Get-Benutzerinformationen abgerufen wird. Der Schritt „Skript ausführen“ wird verwendet, um diesen Code in die Variable new_code zu übergeben, die dann in der ForTestCode-Definition der Komponente gespeichert und in einem modalen Fenster angezeigt wird.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1_uPyqNOuOddurvwz-KteaoIIRQjgEzBH/view?usp=sharing) herunterladen.