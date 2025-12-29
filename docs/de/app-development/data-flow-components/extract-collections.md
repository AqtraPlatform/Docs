# Extrahieren der Sammlung

![](../../assets/images/app-development/extract-collection.png)

## Allgemeine Informationen
Der Schritt „Extrahieren der Sammlung“ wird verwendet, um ein Array-Feld in eine flache Liste zu konvertieren. Dieses Feld kann entweder aus einer externen Quelle oder aus einem Feld (Eigenschaft) eines Array-Komponenten stammen.

In diesem Schritt wird das Array analysiert und die Verarbeitung jedes Array-Elements (Eintrag oder Objekt) wird als separater interner Datenfluss gestartet. Jeder dieser Threads wird unabhängig voneinander ausgeführt. Datenflüsse, die mit dem Schritt „Extrahieren der Sammlung“ analysiert wurden, können über den Schritt „Gruppieren nach“ wieder zusammengefügt werden.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld | Wertoptionen | Zweck |
|------------------|--------------|-------|
| Schrittname      | -            | Name des Schrittes |
| Quellenschritt   | -            | Auswahl des vorherigen Schrittes |
| Modellpfad       | -            | Pfad zu einem Array-Feld im Datenmodell |

## Anwendungsfälle
- **Datenarray-Verarbeitung**: Wird verwendet, um jedes Element des Datenarrays unabhängig zu extrahieren und zu verarbeiten.
- **Aufteilen und anschließendes Gruppieren**: Geeignet für Szenarien, in denen komplexe Datenstrukturen in einfachere Elemente aufgeteilt werden müssen, um sie weiter zu verarbeiten und zu analysieren.

## Ausnahmen
- **Genauigkeit bei der Angabe der Quelle und des Pfades erforderlich**: Falsche Angaben zur Quelle oder zum Pfad des Array-Feldes können zu Fehlern bei der Datenverarbeitung führen.

## Anwendungsszenario

Diese Komponente ermöglicht die Verarbeitung von Lagerdaten des Kunden, indem neue Datensätze mit den Schritten **Extrahieren der Sammlung** und **Skript ausführen** hinzugefügt werden. Nach der Ausführung des Datenflusses erhält jeder Datensatz zusätzliche Felddaten.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1Q1czyILIGHc7tVwPYpkgHIFfI87p5WvQ/view?usp=sharing) herunterladen.