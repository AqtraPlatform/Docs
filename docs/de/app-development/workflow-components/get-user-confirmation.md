# Benutzerbestätigung einholen

![](../../assets/images/app-development/get-user-confirmation.png)

## Allgemeine Informationen
Der Schritt „Benutzerbestätigung einholen“ im Workflow wird verwendet, um eine Bestätigung anzufordern oder eine Aktion vom Benutzer auszuführen. Der Schritt sendet eine Benachrichtigung an den Benutzer mit der Aufforderung, eine bestimmte Aktion am Objekt durchzuführen, wobei das Objekt den Zustand des aktuellen Modells darstellt.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld    | Wertoptionen          | Zweck |
|---------------------|-----------------------|------------|
| Schrittname         | -                     | Name des Schrittes „Benutzerbestätigung einholen“ |
| Bestätigungsfeld    | -                     | Feld mit Optionen, die vom Benutzer angefordert werden |
| Benutzerinformationsfeld | Mehrfachauswahl aus Katalog | Feld mit Informationen über einen Benutzer oder eine Benutzergruppe |
| Benutzerweiterleitung | Mehrfachauswahl aus Katalog | Objekt, das einen Sicherheitskontext darstellt |

## Fälle
- **Anforderung der Benutzerbestätigung**: Ideal für Skripte, die eine Bestätigung oder die Wahl einer Aktion vom Benutzer erfordern, wie z. B. die Bestätigung einer Transaktion, die Zustimmung zur Datenverarbeitung oder die Auswahl einer Antwortoption.
- **Interaktive Benutzerbeteiligung am Prozess**: Geeignet für einen Workflow, bei dem es wichtig ist, die Entscheidungen oder Wahlmöglichkeiten des Benutzers zu berücksichtigen, um den Prozess fortzusetzen oder zu ändern.

## Ausnahmen
- **Sicherstellen, dass die Anfrage klar ist**: Es ist wichtig, die Bestätigungsanfrage klar zu formulieren, damit der Benutzer versteht, welche Aktion von ihm erwartet wird.
- **Verwaltung der Benutzerantworten**: Benutzerantworten sollten angemessen verarbeitet und berücksichtigt werden, insbesondere in Situationen, in denen sie den Verlauf weiterer Aktionen im Workflow bestimmen.
- **Berücksichtigung des Sicherheitskontexts und der Berechtigungen**: Bei der Verwendung des Parameters Benutzerweiterleitung ist es wichtig, den Sicherheitskontext und die entsprechenden Benutzerberechtigungen zu berücksichtigen.