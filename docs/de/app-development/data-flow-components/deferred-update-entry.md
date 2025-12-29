# Deferred update entry

![](../../assets/images/app-development/deferred-update-entry.png)

## Allgemeine Informationen
Der Schritt „Deferred Update Entry“ wird verwendet, um das verzögerte Update von Einträgen in einer bestimmten Komponente zu organisieren. Dieser Schritt ermöglicht es Ihnen, Aktionen zu sammeln, um Einträge zu erstellen, zu aktualisieren oder zu löschen, die dann ausgeführt werden, nachdem der Schritt „Apply Deferred Update Operations“ aktiviert wurde. Auf diese Weise können mehrere Update-Operationen gesammelt werden.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld      | Wertoptionen | Zweck |
|-----------------------|--------------|-------|
| Schrittname           | -            | Name des Schrittes |
| Quellenschritt        | -            | Auswahl des vorherigen Schrittes |
| Komponente            | -            | Zu aktualisierende Komponente |
| Feldkomponenten-Schlüssel | -        | Feld mit dem Schlüssel der Komponente, das aktualisiert werden soll |
| Eintrag zur Löschung markieren | true, false | Markierung für die Löschung des Eintrags |
| Namensfeld            | -            | Name des Feldes, das aktualisiert werden soll |
| Feldzuordnung         | -            | Zuordnung der Felder zwischen Datenfluss und Komponente |

## Fälle
- **Datenbatchverarbeitung**: Wird verwendet, um mehrere Datenaktualisierungsoperationen zu sammeln und sie dann in einer einzigen Transaktion auszuführen, was die Leistung verbessert und die Belastung des Systems verringert.
- **Komplexe Datenverwaltung**: Geeignet für Szenarien, die komplexe Logik für Datenaktualisierungen erfordern, einschließlich Erstellen, Ändern und Löschen von Einträgen innerhalb eines einzigen Workflows.

## Ausnahmen
- **Bedarf an nachfolgenden Updates**: Alle von diesem Schritt gesammelten Update-Operationen müssen über den Schritt „Apply Deferred Update Operations“ aktiviert werden, um sie auszuführen.

## Anwendungsszenario

Die Komponente mit einer benutzerdefinierten Definition konfiguriert einen Datenfluss zum Aktualisieren von Datensätzen. Die Benutzer beginnen mit der Extraktion des Aktionsmodells mithilfe des Schrittes „Get action model“. Anschließend wird der Schritt „Deferred update entry“ für verzögerte Updates von Datensätzen verwendet, bei dem die Benutzer die Komponente, die Komponenten-ID und die Feldzuordnungen angeben können. Der Schritt „Apply deferred update“ ermöglicht die Konfiguration von Batchverarbeitungs- und Parallelausführungsparametern. Nach Abschluss dieser Schritte ist die Komponente bereit zum Aktualisieren, Erstellen oder Löschen von Datensätzen, was im Frontend erfolgt, wenn mit den entsprechenden Schnittstellenelementen interagiert wird.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/16uo9P5IWDv-QnT749fYDISyyWEbKrDVR/view?usp=sharing) herunterladen.