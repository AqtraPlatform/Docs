# Benutzerinformationen abrufen

![](../../assets/images/app-development/get-user-info.png)

## Allgemeine Informationen
Der Schritt „Benutzerinformationen abrufen“ wird verwendet, um Daten über den Plattformbenutzer zu erhalten, wie z.B. E-Mail, Vorname und Nachname, für die weitere Verarbeitung im aktuellen Datenfluss. Dieser Schritt ist für die meisten Benutzeroperationen erforderlich, mit Ausnahme der Erstellung eines neuen Benutzers.

**Benutzerinformationen abrufen**
1. **Mit dem Flag „Benutzerinformationen aus der Anfrage abrufen“**: Der Schritt versucht, Daten über den aktuellen Benutzer abzurufen. Damit dies korrekt funktioniert, ist es notwendig, dass der Datenfluss im Namen eines bestimmten Benutzers aufgerufen wird (zum Beispiel aus einem Anfrageformular oder über eine Proxy-Anfrage). Wenn im Namen der Plattform aufgerufen wird (z.B. im Eingabedatenfluss), wird das Ergebnis null sein.
2. **Ohne das Flag „Benutzerinformationen aus der Anfrage abrufen“**: Der Benutzer kann definiert werden:
   - Über den Systemnamen, unter Verwendung eines String-Parameters des aktuellen Datenflussmodells.
   - Über einen Link zum Benutzerinformationsverzeichnis, zum Beispiel die Felder creatorSubject oder changeAuthor.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld          | Wertoptionen       | Zweck |
|---------------------------|-------------------|------------|
| Schrittname               | -                 | Name des Schrittes |
| Quellenschritt            | -                 | Auswahl des vorherigen Schrittes |
| Benutzerinformationen aus der Anfrage abrufen | - | Flag zum Abrufen von Informationen über den aktuellen Benutzer |
| Benutzerinformationsfeld   | -                 | Benutzeridentifikationsfeld |
| Benutzername              | -                 | Name des Benutzers |
| Ergebnisfeld speichern     | -                 | Feld zum Speichern der erhaltenen Informationen über den Benutzer |

## Fälle
- **Benutzerdaten zur Verarbeitung abrufen**: Wird verwendet, um Benutzerinformationen für die anschließende Verwendung im Datenfluss zu extrahieren.
- **Personalisierte Benachrichtigungen senden**: In Fällen, in denen personalisierte E-Mail-Benachrichtigungen an Benutzer gesendet werden müssen, wird der Schritt „Benutzerinformationen abrufen“ verwendet, um deren E-Mail-Adressen zu erhalten. Diese Informationen werden dann an den Schritt weitergegeben, der für das Senden von Benachrichtigungen vorgesehen ist.

## Ausnahmen
- **Benutzer nicht gefunden**: In Fällen, in denen der Benutzer nicht identifiziert werden kann, wird das Ergebnis null sein, was zusätzliche Verarbeitung im Datenfluss erfordert.

## Anwendungsszenario

Die Komponente „Benutzerinformationen abrufen“ ist dafür ausgelegt, Informationen über einen Benutzer abzurufen. Innerhalb eines Datenflusses wird dieser Schritt verwendet, um Benutzerdaten basierend auf bestimmten Kriterien abzufragen, wie z.B. einem Benutzernamen oder anderen identifizierenden Informationen. Zum Beispiel können Sie innerhalb eines Datenflusses den Namen eines Benutzers angeben, um Informationen über ihn abzurufen, und diese Informationen dann für weitere Aktionen verwenden, wie z.B. sie auf einem Bildschirm anzuzeigen oder eine Datenbank zu aktualisieren.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/16keZXK_MXlWLmcSA4a-nLvhx-GPP3RPy/view?usp=sharing) herunterladen.