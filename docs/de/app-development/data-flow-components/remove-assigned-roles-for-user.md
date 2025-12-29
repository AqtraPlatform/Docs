# Entfernen zugewiesener Rollen für Benutzer

![](../../assets/images/app-development/remove-assigned-roles-for-user.png)

## Allgemeine Informationen
Der Schritt „Entfernen zugewiesener Rollen für Benutzer“ wird verwendet, um alle Rollen zurückzusetzen, die einem bestimmten Benutzer zugewiesen sind. Dies ermöglicht es Systemadministratoren und Prozessmanagern, Benutzerrollen zu entfernen und vereinfacht die Verwaltung von Berechtigungen und Sicherheitskontrollen.

## Parameter
**Schritt Einstellungen:**

| Feld              | Wert Optionen       | Zweck |
|------------------|--------------------|------------|
| Schrittname      | -                  | Name des Schrittes |
| Quellschritt     | -                  | Auswahl des vorherigen Schrittes |
| Benutzer-ID-Feld | Name einer Variablen vom Typ Benutzerinfo | Feld, das die Benutzer-ID für den Rollenreset enthält |

## Fälle
- **Verwaltung von Zugriff und Rollen**: Dieser Schritt ist ideal für Skripte, in denen Sie Benutzerrollen schnell ändern oder zurücksetzen möchten, z. B. wenn sich die Arbeitsverantwortlichkeiten ändern oder wenn ein Mitarbeiter das Unternehmen verlässt.
- **Sicherstellung der Systemsicherheit**: Wird verwendet, um unbefugten Zugriff auf sensible Daten oder Systemfunktionen zu verhindern, indem Rollen von Benutzern entfernt werden, die solche Zugriffsberechtigungen nicht mehr benötigen.

## Ausnahmen
- **Abhängigkeit von der Genauigkeit der Benutzeridentifikation**: Die Wirksamkeit des Schrittes hängt von der genauen Identifizierung des Benutzers ab, dessen Rollen Sie zurücksetzen möchten.
- **Notwendigkeit, zuerst die Benutzer-ID zu erhalten**: Der Schritt erfordert, dass Sie zuerst eine interne Benutzer-ID erhalten, was über den Schritt „Benutzerinformationen abrufen“ oder andere Authentifizierungsmethoden erfolgen kann.