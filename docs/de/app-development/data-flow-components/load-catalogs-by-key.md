# Kataloge nach Schlüssel laden

![](../../assets/images/app-development/load-catalogs-by-key.png)

## Allgemeine Informationen
Der Schritt „Kataloge nach Schlüssel laden“ funktioniert ähnlich wie der Schritt „Entität nach ID abrufen“, erfordert jedoch anstelle einer spezifischen Komponenten-ID die automatische Identifizierung eines beliebigen Katalogtypfelds im Datenmodell. Je nach Auswahl des Benutzers ruft der Schritt den vollständigen Eintrag ab, der mit dem ausgewählten Katalogtypfeld verknüpft ist. Dadurch können Sie vollständige Informationen aus jedem Link in den Daten abrufen, ohne eine spezifische ID angeben zu müssen.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld | Wertoptionen | Zweck |
|------------------|--------------|-------|
| Schrittname      | -            | Name des Schrittes |
| Quellenschritt   | -            | Auswahl des vorherigen Schrittes |

## Fälle
- **Automatische Identifizierung und Herunterladen der verknüpften Daten**: Wird verwendet, um Daten zu identifizieren und automatisch zu laden, die mit Katalogfeldern verknüpft sind.
- **Flexible Datenextraktion**: Geeignet für Skripte, die Flexibilität bei der Auswahl und Extraktion von Daten aus verschiedenen verwandten Komponenten erfordern.

## Ausnahmen
- **Übermäßige Belastung bei der Arbeit mit einer großen Anzahl von Katalogen**: Wenn eine große Anzahl von Katalogen geöffnet wird, kann es zusätzliche Zeit in Anspruch nehmen, diese zu verarbeiten.
- **Unbegründeter Ersatz des Schrittes „Entität nach ID abrufen“ durch den Schritt „Kataloge nach Schlüssel laden“:** Wenn die Anzahl der verknüpften Kataloge nicht mehr als einige beträgt, ist es besser, den Schritt „Entität nach ID abrufen“ für eine bessere Leistung zu verwenden.

## Anwendungsszenario

Diese Komponente ermöglicht es Ihnen, einen Datenfluss zu erstellen, der mit dem Abrufen eines leeren Datenmodells beginnt. Anschließend wird sie verwendet, um den Datensatzidentifikator mit Katalogen abzurufen, nach dem sie diese Kataloge lädt und deren Daten im Frontend ausgibt.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1_GImBJ3UCDo-T1dL6c85-wWgcUfpJIz3/view?usp=sharing) herunterladen.