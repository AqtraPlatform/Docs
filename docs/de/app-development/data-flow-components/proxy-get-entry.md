# Proxy get entry

![](../../assets/images/app-development/proxy-get-entry.png)

## Allgemeine Informationen
Der Schritt „Proxy Get Entry“ wird verwendet, um ein Modell einer Proxy-Anfrage zu generieren, um einen einzelnen Eintrag zu erhalten. Dieser Schritt steht in engem Zusammenhang mit der Einstellung „Proxy-Modus“, die im Abschnitt „Einstellungen“ zu finden ist.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld      | Wertoptionen       | Zweck      |
|-----------------------|-------------------|------------|
| Schrittname           | -                 | Name des Schrittes |
| Eingabewerte validieren | true, false       | Gibt an, dass die Eingabewerte vor der Verarbeitung auf Richtigkeit überprüft werden sollen |

## Fälle
- **Einzelne Eintragsabfrage**: Wird verwendet, um Anfragen für einen bestimmten Eintrag über einen Proxy-Server zu generieren und zu senden.
- **Integration mit externen Systemen**: Ermöglicht die Kommunikation mit externen Systemen und Diensten, um Daten über Proxy-Abfragen zu erhalten.

## Ausnahmen
- **Abhängigkeit von Proxy-Einstellungen**: Der korrekte Betrieb des Schrittes hängt von der richtigen Einstellung des „Proxy-Modus“ im Abschnitt „Einstellungen“ ab.
- **Eingeschränkte Funktionalität**: Der Schritt ist spezialisiert auf das Abrufen einzelner Datensätze und ist nicht dafür ausgelegt, mehrere Abfragen oder Daten zu verarbeiten.