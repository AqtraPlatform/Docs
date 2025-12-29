# Datenraster

![](../../assets/images/app-development/data-grid.png)

## Allgemeine Informationen
Das Datenraster ist eine leistungsstarke UI-Komponente, die entwickelt wurde, um große Datenmengen in tabellarischer Form anzuzeigen und mit ihnen zu interagieren. Diese Komponente eignet sich ideal zur Präsentation von Daten in Zeilen und Spalten sowie zur Bereitstellung von Sortier- und Filterfunktionen.

## Parameter
**Komponenten-Eigenschaften:**

| Einstellungsgruppe | Einstellungsfeld      | Wertoptionen        | Zweck                          |
|--------------------|-----------------------|---------------------|--------------------------------|
| (Globale Einstellungen) | Name                | -                   | Name der UI-Komponente im System   |
|                    | Spalten             | -                   | Definieren von Spalten und deren Eigenschaften   |
|                    | Komponente           | Mehrfachauswahl aus Katalog | Enthält eine Liste aller Komponenten |
|                    | Statische Filter     | Schaltfläche        | Wird verwendet, um statische Filter anzugeben |
|                    | Dynamische Filter    | Schaltfläche        | Die Eigenschaft wird verwendet, um dynamische Filter anzugeben |
|                    | Seitengröße          | -                   | Größe der Seite                     |
|                    | Manuelles Neuladen   | -                   | Manuelles Neuladen der Daten          |
|                    | Auswahlmodus         | keine, einfach, mehrfach, Kontrollkästchen | Auswahlmodus für Elemente          |
|                    | Automatisierungs-ID   | -                   | ID für die Automatisierung     |
| Ereignisse         | Bei geladenem Datenquelle | -               | Ereignis beim Laden der Datenquelle |
|                    | Bei ausgewählten Zeilen | -                 | Ereignis bei der Zeilenauswahl |
|                    | Bei geladen          | -                   | Ereignis beim Laden der Komponente |
|                    | Bei Tabellenänderung | -                   | Ereignis bei Tabellenänderung |
|                    | Bei Kopfzeilenänderung | -                 | Ereignis bei Kopfzeilenänderung |
|                    | Bei Zeilenänderung   | -                   | Ereignis bei Zeilenänderung |
|                    | Bei Zellenänderung   | -                   | Ereignis bei Zellenänderung |

**CSS-Eigenschaften:**

| Einstellungsgruppe | Einstellungsfeld      | Wertoptionen        | Zweck                          |
|--------------------|-----------------------|---------------------|--------------------------------|
| Layout             | Breite                | -                   | Breite der Komponente                   |
|                    | Höhe                  | -                   | Höhe der Komponente                   |
|                    | Rand                  | -                   | Äußere Polsterung                      |
|                    | Innenabstand          | -                   | Innere Polsterung                   |
|                    | Sichtbar              | -                   | Sichtbarkeit der Komponente                |
|                    | Ausgeblendet          | -                   | Ausblenden einer Komponente                  |
| Erscheinungsbild   | Eckenradius           | -                   | Eckenradius                   |
|                    | Rahmenstärke          | -                   | Rahmenstärke                       |
| Pinsel             | Hintergrund           | -                   | Hintergrundfarbe                           |
|                    | Rahmenpinsel          | -                   | Rahmenfarbe                          |

**Datenraster-Konfigurationsmodell**

Die folgenden Einstellungen werden verwendet, um die Spalten der Datenraster-UI-Komponente zu ändern: 

| Einstellungsfeld   | Wertoptionen                           | Zweck                                              |
|--------------------|----------------------------------------|---------------------------------------------------|
| Übersetzungswert    | -                                      | Spaltenüberschrift                                 |
| Kopfzeile anzeigen  | wahr, falsch                           | Diese Eigenschaft ermöglicht es Ihnen, die Anzeige der Spaltenüberschrift anzupassen |
| Sortierbar        | true, false                                | Die Eigenschaft ermöglicht es Ihnen, die Fähigkeit zu konfigurieren, die Tabelle nach der ausgewählten Spalte zu sortieren |
| Filterbar         | true, false                                | Diese Eigenschaft ermöglicht es Ihnen, die Fähigkeit zu konfigurieren, die Tabelle nach der ausgewählten Spalte zu filtern |
| Sichtbar          | true, false                                | Die Eigenschaft bestimmt die Sichtbarkeit der Spalte                   |
| Klartext          | true, false                                | Eigenschaft, um eine Spalte als Klartext anzuzeigen    |
| Breite            | -                                          | Spaltenbreite in der Tabelle                                |
| Anzeigeformat     | -                                          | Anzeigeformat der Spaltendaten                       |
| Symbol            | Nur verfügbar für Datensatz bearbeiten, Anwendung öffnen | Eine Eigenschaft, die eine Auswahl verfügbarer Symbole enthält         |
| Befehlstyp       | Anwendung öffnen, Datensatz bearbeiten     | Die Eigenschaft ermöglicht es Ihnen, die Aktion auszuwählen, die durch Klicken auf die Spalte ausgeführt wird |
| Feld hinzufügen   | Schaltfläche                                | Die Eigenschaft ermöglicht es Ihnen, Felder für die Ausgabe in der Spalte hinzuzufügen   |

## Fälle
- **Datenanzeige**: Ideal zur Anzeige von Daten in einer leicht verständlichen tabellarischen Form.
- **Verwaltungspanels**: Weit verbreitet in Verwaltungsoberflächen zur Anzeige und Bearbeitung von Daten.
- **Analyseanwendungen**: Ermöglicht es Ihnen, große Mengen an Informationen zu analysieren und zu sortieren.

## Ausnahmen
- **Eingeschränkte Visualisierung**: Data Grid ist nicht für komplexe Datenvisualisierungen wie Grafiken oder Diagramme geeignet.
- **Datenverarbeitung**: Die Komponente ist dafür ausgelegt, Daten anzuzeigen, nicht um Daten zu verarbeiten oder zu berechnen.