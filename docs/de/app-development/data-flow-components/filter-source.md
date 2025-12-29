# Filterquelle

![](../../assets/images/app-development/filter-source.png)

## Allgemeine Informationen
Der Schritt „Filterquelle“ wird verwendet, um den Datenstrom im Datenfluss zu filtern. Er ermöglicht es, Datenströme basierend auf dem Wert des ausgewählten Feldes und dem angegebenen Testoperator, wie gleich, ungleich, größer und kleiner, zu verzweigen.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld   | Wertoptionen       | Zweck |
|--------------------|---------------------|------------|
| Schrittname        | -                   | Name des Schrittes |
| Quellenschritt     | -                   | Auswahl des vorherigen Schrittes |
| Quellfeld          | -                   | Feld, das gefiltert werden soll |
| Operator           | gleich, ungleich, größer, kleiner | Operator zum Vergleichen von Feldwerten |
| Mit null vergleichen | true, false         | Gibt an, ob mit null verglichen werden soll |
| Filterwert         | -                   | Wert, der gefiltert werden soll |

## Fälle
- **Datenstromverzweigung**: Wird verwendet, um einen Datenstrom basierend auf spezifischen Bedingungen, die im Filter definiert sind, zu teilen.
- **Datensegmentierung**: Geeignet für Situationen, in denen verschiedene Segmente von Daten je nach festgelegten Kriterien unterschiedlich behandelt werden müssen.

## Ausnahmen
- **Genauigkeit der Filtereinstellungen**: Ein falsch gesetzter Filter kann zum Verlust wichtiger Daten oder zur Einbeziehung unnötiger Daten in die Verarbeitung führen.
- **Abhängigkeit vom ausgewählten Feld**: Die Effektivität des Filterns hängt von der korrekten Wahl des Feldes und dem geeigneten Vergleichsoperator ab.

## Anwendungsszenario

Diese Komponente ist eine Schnittstelle mit drei Schaltflächen: `ExecuteFilterSource`, `ExecuteFilterSourceNotEqual` und `ExecuteFilterSourceGreat`, von denen jede einen Datenfluss auslöst, abhängig von der Eingabe im `First`-Feld. Verschiedene Testszenarien umfassen das Überprüfen von Bedingungen auf Gleichheit, Ungleichheit und größer/kleiner als der angegebene Wert.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1OO5SymRdhmv3oED2EPG4twG5mypsqqs9/view?usp=sharing) herunterladen.