# Bestätigen Sie den Einmalcode für den Benutzer

![](../../assets/images/app-development/confirm-one-time-code-for-user.png)

## Allgemeine Informationen
Der Schritt „Bestätigen Sie den Einmalcode für den Benutzer“ wird verwendet, um den Einmalcode zu bestätigen, der im vorherigen Schritt „Einmalcode für den Benutzer abrufen“ generiert wurde. Dieser Schritt ist der Schlüssel im Prozess der Zwei-Faktor-Authentifizierung und ermöglicht es Ihnen, die Richtigkeit des vom Benutzer eingegebenen Codes zu überprüfen, um auf das System zuzugreifen.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld  | Wertoptionen | Zweck |
|-------------------|--------------|-------|
| Schrittname       | -            | Name des Schrittes |
| Quellenschritt    | -            | Auswahl des vorherigen Schrittes |
| Benutzercodefeld  | -            | Das Feld, in dem der Benutzer den erhaltenen Code zur Bestätigung eingibt |

## Fälle
- **Bestätigung der Zwei-Faktor-Authentifizierung**: Wird angewendet, um den Prozess der Zwei-Faktor-Authentifizierung abzuschließen, indem die Benutzer aufgefordert werden, den Code einzugeben, der ihnen im vorherigen Schritt gesendet wurde.
- **Erhöhung der Zugriffssicherheit**: Wird in Szenarien verwendet, in denen eine verbesserte Zugriffskontrolle auf das System erforderlich ist, um unbefugte Anmeldungen zu verhindern.

## Ausnahmen
- **Abhängigkeit von der Richtigkeit des eingegebenen Codes**: Die Wirksamkeit des Schrittes hängt von der Genauigkeit der Eingabe des Codes durch den Benutzer ab.
- **Begrenzte Gültigkeit des Codes**: Wenn der Code abläuft, muss er erneut ausgegeben werden, was zu Verzögerungen bei der Authentifizierung führen kann.

## Anwendungsszenario

Die Komponente erstellt einen Datenfluss, um den Einmalcode des Benutzers zu bestätigen. Der Get-Aktionsmodell-Schritt wird verwendet, um die Modaldaten abzurufen. Dann wird der Code aus der ForTestCode-Variablen von überflüssigen Zeichen bereinigt und in der _code-Variablen unter Verwendung des Execute-Skript-Schrittes gespeichert. Der Schritt „Bestätigen Sie den Einmalcode für den Benutzer“ wird verwendet, um den Einmalcode mit dem _code-Wert als Benutzercode zu bestätigen. Schließlich wird das Ergebnis durch den Write-Response-Schritt übergeben.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1_uPyqNOuOddurvwz-KteaoIIRQjgEzBH/view?usp=sharing) herunterladen.