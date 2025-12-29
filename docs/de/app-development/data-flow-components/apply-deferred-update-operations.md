# Anwenden von verzögerten Aktualisierungsoperationen

![](../../assets/images/app-development/apply-deferred-update-operations.png)

## Allgemeine Informationen
Der Schritt „Verzögerte Aktualisierungsoperationen anwenden“ wird für die massenhafte Anwendung von Aktualisierungen verwendet, die mit der Reihe von Schritten „Verzögerter Aktualisierungseintrag“ vorbereitet wurden. Dieser Schritt ermöglicht es Ihnen, die angesammelten Aktualisierungsoperationen effizient durchzuführen, indem Sie sie alle auf einmal anwenden.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld       | Wertoptionen | Zweck |
|------------------------|--------------|-------|
| Schrittname            | -            | Name des Schrittes |
| Batch-Chunks-Größe     | 1000         | Größe des zu verarbeitenden Datenbatches |
| Batch-Leerlaufzeit in ms | -          | Leerlaufzeit in Millisekunden zwischen den Batches |
| Anzahl paralleler Batches | 0         | Anzahl der parallel verarbeiteten Datenbatches |

## Fälle
- **Massenaktualisierung**: Ideal für Szenarien, in denen Sie Daten in großen Mengen aktualisieren müssen, z. B. wenn Sie eine große Menge an Daten synchronisieren oder wenn Sie schnell Änderungen an mehreren Systemkomponenten vornehmen müssen.
- **Leistungsoptimierung**: Verbessert die Leistung bei Massenaktualisierungen durch parallele Verarbeitung und effizientes Management von Datenbatches.

## Ausnahmen
- **Verwaltung der Aktualisierungsreihenfolge**: Es ist wichtig sicherzustellen, dass die Aktualisierungen korrekt sequenziert sind, insbesondere wenn die Daten in den verschiedenen Schritten des „Verzögerten Aktualisierungseintrags“ miteinander verknüpft sind.
- **Konfiguration der Batch-Verarbeitungsparameter**: Parameter wie Batch-Größe und Anzahl der parallelen Batches müssen sorgfältig konfiguriert werden, um eine Überlastung des Systems zu vermeiden und sicherzustellen, dass die Aktualisierungen effizient durchgeführt werden.

## Anwendungsszenario

Die Komponente mit einer benutzerdefinierten Definition konfiguriert einen Datenfluss zum Aktualisieren von Datensätzen. Die Benutzer beginnen mit dem Extrahieren des Aktionsmodells mithilfe des Schrittes „Aktionsmodell abrufen“. Dann wird der Schritt „Verzögerter Aktualisierungseintrag“ für verzögerte Aktualisierungen von Datensätzen verwendet, bei dem die Benutzer die Komponente, die Komponenten-ID und die Feldzuordnungen angeben können. Der Schritt „Verzögerte Aktualisierung anwenden“ ermöglicht die Konfiguration der Batch-Verarbeitung und der Parameter für die parallele Ausführung. Nach Abschluss dieser Schritte ist die Komponente bereit zum Aktualisieren, Erstellen oder Löschen von Datensätzen, was im Frontend erfolgt, wenn mit den entsprechenden Schnittstellenelementen interagiert wird.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/16uo9P5IWDv-QnT749fYDISyyWEbKrDVR/view?usp=sharing) herunterladen.