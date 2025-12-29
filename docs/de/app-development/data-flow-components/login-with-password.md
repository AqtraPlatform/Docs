# Anmeldung mit Passwort

![](../../assets/images/app-development/login-with-password.png)

## Allgemeine Informationen
Der Schritt „Anmeldung mit Passwort“ wird verwendet, um eine Benutzersitzung basierend auf dem Benutzernamen und dem Passwort zu erstellen. Dieser Schritt ermöglicht es dem Benutzer, sich im System zu authentifizieren, indem die angegebenen Anmeldeinformationen überprüft werden und, falls die Überprüfung erfolgreich ist, eine Benutzersitzung erstellt wird.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld   | Wertoptionen | Zweck |
|---------------------|-------------------|------------|
| Schrittname         | -                 | Name des Schrittes |
| Quellenschritt      | -                 | Auswahl des vorherigen Schrittes |
| Benutzername        | -                 | Anmeldename |
| Benutzerpasswort    | -                 | Benutzerpasswort |
| Client für Anfrage   | -                 | Client oder Anwendung, die die Authentifizierungsanfrage initiiert |

## Fälle
- **Benutzerauthentifizierung**: Schritt, der in Authentifizierungsprozessen verwendet wird, bei denen Benutzer ihre Anmeldeinformationen eingeben, um auf das System oder dessen Funktionen zuzugreifen.
- **Zugangskontrolle**: Geeignet für Systeme, die eine Überprüfung der Benutzeranmeldeinformationen erfordern, bevor der Zugriff auf bestimmte Ressourcen oder Funktionen gewährt wird.

## Ausnahmen
- **Notwendigkeit der Genauigkeit der Anmeldeinformationen**: Die Wirksamkeit des Schrittes hängt von der Genauigkeit der eingegebenen Anmeldeinformationen (Benutzername und Passwort) ab.
- **Umgang mit fehlgeschlagenen Anmeldeversuchen**: Es ist wichtig, fehlgeschlagene Anmeldeversuche ordnungsgemäß zu behandeln, um potenzielle Sicherheitsrisiken wie Brute-Force-Angriffe zu vermeiden. Dies erfordert die Implementierung von Mechanismen zur Begrenzung der Anzahl der Anmeldeversuche oder zur vorübergehenden Sperrung des Zugriffs nach mehreren erfolglosen Versuchen.

## Anwendungsszenario

Das Szenario implementiert die Benutzeranmeldung im System mit einem Benutzernamen und Passwort. Nach dem Initiieren des Datenflusses und dem Eingeben des Anmeldenamens und des Passworts in die entsprechenden Felder der Benutzeroberfläche authentifiziert der Schritt „Anmeldung mit Passwort“ den Benutzer. Anschließend wird mit dem Schritt „Formularaktion“ die ausgewählte Komponente geöffnet.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1Kb9QNcCHXqetQmXGvBHScQSiRlA-542s/view?usp=sharing) herunterladen.