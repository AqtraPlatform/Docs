# Get Action Model

![](../../assets/images/app-development/get-action-model.png)

## Allgemeine Informationen
Der Schritt „Get Action Model“ ist dafür konzipiert, ein Aktionsmodell aus einer bestimmten Quelle oder einem bestimmten System zu extrahieren. Dieser Schritt kann verwendet werden, um Daten über spezifische Aktionen oder Prozesse zu erhalten, die für die weitere Verarbeitung oder Analyse innerhalb des Datenflusses erforderlich sind.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld      | Wertoptionen                | Zweck |
|-----------------------|-----------------------------|------------|
| Schrittname           | -                           | Name des Schrittes |
| Eingabewerte validieren | true, false                | Gibt an, ob die Eingabewerte vor der Verarbeitung auf Richtigkeit überprüft werden sollen |

## Fälle
- **UI-Integration**: Oft als erster Schritt im Datenfluss verwendet, insbesondere wenn der Datenfluss über die UI aktiviert wird, z. B. durch Drücken eines Buttons. Ermöglicht es, den aktuellen Zustand der Komponentendaten zum Zeitpunkt der Aktivierung zu erhalten.
- **Automatische Datenübertragung von der UI**: Wenn die Datenübertragung von UI-Elementen wie Buttons aktiviert ist, überträgt die Plattform automatisch die aktuellen Daten der Komponente, einschließlich der vom Benutzer vorgenommenen Änderungen.

## Ausnahmen
- **Datenabrufbeschränkungen**: Der Schritt ruft nur die Felder (Eigenschaften) der Komponentendaten ab. Um die in dem Component Script festgelegten Variablen zu erhalten, müssen andere Schritte wie „Get raw model“ verwendet werden.

## Anwendungsszenario

Die Komponente ist ein System zum Hinzufügen und Anzeigen von Daten mit verschiedenen Feldtypen. Sie umfasst die Möglichkeit, Felder unterschiedlicher Typen in der **Definition** hinzuzufügen und bietet eine Front-End-Oberfläche zum Eingeben von Werten sowie zum Anzeigen von Daten in einem **Datagrid** mit der Möglichkeit, die Seite zu aktualisieren. Diese Komponente nutzt die folgenden **Datenfluss-Schritte**: **Get action model**, **Update entry**, **Write response**.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/15M_FvmlFmkJXunTeeT6jtFolPvE5jCfk/view?usp=sharing) herunterladen.