# Wählen Sie viele

![](../../assets/images/app-development/select-many.png)

## Allgemeine Informationen
Der Schritt „Wählen Sie viele“ wird verwendet, um ein Array-Typ-Feld in eine flache Liste zu konvertieren. Im Gegensatz zum Schritt „Sammlung extrahieren“ bewahrt „Wählen Sie viele“ die Modellsdaten aus dem vorherigen Schritt und fügt „Eltern“-Werte mit einem `$parent` Präfix für jedes Array-Element hinzu. Dies erweitert nicht nur das Array, sondern bewahrt auch den Kontext des übergeordneten Eintrags.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld | Wertoptionen | Zweck |
|------------------|--------------|-------|
| Schrittname      | -            | Name des Schrittes |
| Quellenschritt   | -            | Auswahl des vorherigen Schrittes |
| Modellpfad       | -            | Pfad zu einem Array-Feld im Datenmodell |

## Fälle
- **Kontext Erweiterung und Bewahrung**: Wird verwendet, um Datenarrays in eine flache Liste zu konvertieren, während die Beziehung zu den übergeordneten Daten bewahrt bleibt.
- **Verarbeitung von hierarchischen Strukturen**: Geeignet für Skripte, in denen Sie Daten aus Arrays verarbeiten müssen, ohne die Verbindung zu den „Eltern“-Daten-Elementen zu verlieren.

## Ausnahmen
- **Verarbeitung großer Arrays**: Die Verarbeitung großer Arrays kann ressourcenintensiver sein, da der Kontext der übergeordneten Daten bewahrt werden muss.

## Anwendungsszenario

Dieses Modul ist ein Werkzeug zur Erstellung und Verwaltung von Datenflüssen innerhalb der Anwendung. Der Schritt 'Wählen Sie viele' in diesem Modul wird verwendet, um mehrere Elemente aus einem Array von Daten auszuwählen, die in der vorherigen Phase des Datenflusses erhalten wurden. Das Modul ermöglicht es den Benutzern, Auswahl- und Datenverarbeitungsbedingungen gemäß ihren Anforderungen zu definieren.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1T9k35m8cg56vmM68LCT0brMeYQ2JIJ6U/view?usp=sharing) herunterladen.