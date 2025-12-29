# Kontext für Modell registrieren

![](../../assets/images/app-development/register-context-for-model.png)

## Allgemeine Informationen
Der Schritt „Kontext für Modell registrieren“ wird im Kontext der LDAP-Integration verwendet, um den Sicherheitskontext von Benutzern zu registrieren, die in einem externen System registriert sind. Dieser Schritt stellt sicher, dass Daten über Benutzer und deren Rollen zwischen dem externen System und dem aktuellen System synchronisiert werden, wobei Schlüssel verwendet werden, um den Kontext zu identifizieren und zu registrieren.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld | Wertoptionen | Zweck |
|------------------|--------------|-------|
| Schrittname      | -            | Name des Schrittes |
| Quellenschritt   | -            | Auswahl des vorherigen Schrittes |
| Komponente       | -            | Komponente, für die der Kontext registriert wird |
| Namensfeld       | -            | Feld, das den Namen oder Identifikator der Entität angibt |
| Schlüssel        | -            | Schlüssel, die verwendet werden, um eine Entität eindeutig zu identifizieren |

## Fälle
- **LDAP-Integration**: Wird verwendet, um Benutzerdaten aus LDAP im aktuellen System zu synchronisieren und zu registrieren.
- **Rollen- und Zugriffsmanagement**: Geeignet für Skripte, die eine genaue Übereinstimmung und Verfolgung der Rollen von Benutzern, die in externen Systemen registriert sind, erfordern.

## Ausnahmen
- **Anforderungen an die Schlüsselgenauigkeit**: Die Schlüssel müssen genau übereinstimmen, um Benutzer im System korrekt zu identifizieren und zu registrieren.
- **Verwaltung von Änderungen in externen Systemen**: Änderungen in den Benutzerrollen oder -status in einem externen System erfordern ein entsprechendes Update im aktuellen System, was eine Herausforderung im Angesicht dynamisch wechselnder Daten darstellen kann.