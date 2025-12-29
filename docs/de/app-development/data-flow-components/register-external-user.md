# Externen Benutzer registrieren

![](../../assets/images/app-development/register-external-user.png)

## Allgemeine Informationen
Der Schritt „Externen Benutzer registrieren“ dient der Registrierung einzelner Benutzer oder Benutzergruppen. Dieser Schritt ist im Kontext der LDAP-Integration konzipiert und wird für die Integration mit externen Systemen verwendet, um den Prozess des Austauschs von Benutzern aus diesen Systemen zu erleichtern und sie dann im aktuellen System anzumelden.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld | Wertoptionen | Zweck |
|------------------|--------------|-------|
| Schrittname      | -            | Name des Schrittes |
| Quellenschritt   | -            | Auswahl des vorherigen Schrittes |
| Benutzername     | -            | Registrierungsname oder Benutzer-ID |
| Schlüssel-Feld   | -            | Feld mit Schlüsselinformationen zur Identifizierung des Benutzers |
| Auth-Anbieter    | -            | Authentifizierungsanbieter, der zur Registrierung des Benutzers verwendet wird |

## Fälle
- **Integration von Benutzern aus externen Systemen**: Wird verwendet, um Benutzer aus LDAP oder anderen externen Systemen auszutauschen und zu registrieren, um ihre korrekte Integration in das aktuelle System sicherzustellen.
- **Automatisierung des Registrierungsprozesses**: Geeignet für Skripte, bei denen es notwendig ist, den Registrierungsprozess einer großen Anzahl von Benutzern zu automatisieren, um manuelle Arbeit und mögliche Fehler zu minimieren.

## Ausnahmen
- **Abhängigkeit von der Genauigkeit der Eingabedaten**: Die Effektivität des Schrittes hängt von der Genauigkeit und Vollständigkeit der Daten ab, die vom externen System empfangen werden.