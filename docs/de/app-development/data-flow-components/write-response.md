# Antwort schreiben

![](../../assets/images/app-development/write-response.png)

## Allgemeine Informationen
Der Schritt „Antwort schreiben“ spielt eine Schlüsselrolle in Dataflow, da er dafür ausgelegt ist, das endgültige Ergebnis an den Aufrufer zurückzugeben. Dieser Schritt ist normalerweise der letzte Schritt in jedem Dataflow und fasst die empfangenen Daten zusammen und sendet sie an die anfordernde Quelle zurück.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld | Wertoptionen | Zweck |
|------------------|--------------|-------|
| Schrittname      | -            | Name des Schrittes |
| Quellenschritt   | -            | Auswahl des vorherigen Schrittes |

## Fälle
- **Rückgabe von Dataflow-Ergebnissen**: Wird verwendet, um die Ergebnisse des Dataflow-Prozessdaten an den Aufrufer zurückzusenden, was in der Datenanalyse und im Fehlermanagement entscheidend sein kann.
- **Datenumwandlung vor der Antwort**: Kann mit dem Schritt „Transformationsmodell“ kombiniert werden, um Daten vor dem Versand zu transformieren oder zu filtern, sodass Sie den Inhalt der Antwort optimieren und an die Anforderungen des Aufrufers anpassen können.

## Anwendungsszenario

Die Komponente enthält benutzerdefinierte Daten Definitionen (Definitionen) und bietet die Möglichkeit, Daten mithilfe von Datenflüssen zu erstellen und zu verwalten. Sie implementiert Schritte zum Abrufen von Datenmodellen (Get-Aktionsmodell) und zum Schreiben von Antworten (Antwort schreiben), sodass Benutzer über die Benutzeroberfläche mit Daten interagieren und diese im Frontend der Anwendung nutzen können.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1qNTgk1uYrMO3uUkDRmTO3i4En5mbG22i/view?usp=sharing) herunterladen.