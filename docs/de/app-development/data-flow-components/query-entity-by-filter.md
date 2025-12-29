# Abfrageentität nach Filter

![](../../assets/images/app-development/query-entity-by-filter.png)

## Allgemeine Informationen
Der Schritt „Abfrageentität nach Filter“ wird verwendet, um Einträge in einer bestimmten Komponente zu suchen. Im Gegensatz zu Schritten, die Filter oder Identifikatoren zur Suche verwenden, ist dieser Schritt darauf ausgelegt, direkt nach Einträgen in einer Komponente zu suchen.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld | Wertoptionen | Zweck |
|------------------|--------------|-------|
| Schrittname      | -            | Name des Schrittes |
| Quellenschritt   | -            | Auswahl des vorherigen Schrittes |
| Komponente       | -            | Komponente, die durchsucht wird |
| Ziel-Feldname    | -            | Name des Feldes, in dem das Abfrageergebnis gespeichert wird |

## Fälle
- **Direkte Komponentensuche**: Wird verwendet, um direkt nach Einträgen in einer bestimmten Komponente zu suchen.

## Ausnahmen
- **Komponentenabhängigkeit**: Die Effektivität des Schrittes ist direkt mit der Struktur und dem Inhalt der Daten in der ausgewählten Komponente verbunden.

## Anwendungsszenario

Der Datenfluss demonstriert verschiedene Nutzungsszenarien der Abfrageentität nach Filter zur Datenfilterung. Jedes Szenario umfasst das Hinzufügen von Get Action Model und Abfrageentität nach Filter-Schritten, das Ausfüllen von Feldern und das Anwenden von Filtern sowie einen Write Response-Schritt zur Ausgabe der Ergebnisse.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1FBXtSNuk7-KmyGofhghsJJiVrV_xebT1/view?usp=sharing) herunterladen.