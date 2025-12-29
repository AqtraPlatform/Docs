# Nachschlageverweis

![](../../assets/images/app-development/lookup-reference.png)

## Allgemeine Informationen
Der Schritt „Nachschlageverweis“ wird verwendet, um nach Verweisen auf Komponenteninstanzen anhand externer Schlüssel zu suchen. Dieser Prozess erfordert, dass mindestens eine Eigenschaft mit dem Flag „Primärschlüssel“ im zu durchsuchenden Komponenten konfiguriert ist.

Die Suche erfolgt über diese Eigenschaft, und das Ergebnis der Suche in Form der ID (ganzzahlig) des gefundenen Datensatzes wird in der im „Feldnamen“ angegebenen Variablen gespeichert. Wenn keine Instanz einer Komponente mit einem solchen Schlüssel gefunden wird, ist die Variable null.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld | Wertoptionen | Zweck |
|------------------|--------------|-------|
| Schrittname      | -            | Name des Schrittes |
| Quellenschritt   | -            | Auswahl des vorherigen Schrittes |
| Komponente       | -            | Komponente, die durchsucht wird |
| Feldname         | -            | Name des Feldes, in dem das Suchergebnis gespeichert wird |

## Fälle
- **Primärschlüssel-Suche**: Wird verwendet, um die Verfügbarkeit zu bestimmen und Instanzen von Komponenten anhand eindeutiger Identifikatoren zu identifizieren.
- **Komponentendatenverknüpfung**: Geeignet für Skripte, in denen Sie Daten aus verschiedenen Komponenten basierend auf eindeutigen Schlüsseln verknüpfen möchten.

## Ausnahmen
- **Anforderung an den Primärschlüssel**: Die Komponente muss einen Primärschlüssel konfiguriert haben, um eine erfolgreiche Suche zu gewährleisten.
- **Umgang mit fehlenden Datensätzen**: Wenn keine Instanz mit dem angegebenen Schlüssel vorhanden ist, wird der Wert der Variablen null sein, was zusätzliche Verarbeitung erfordern kann.

## Anwendungsszenario

Diese Komponente nutzt den Schritt Nachschlageverweis, um die Datensatz-ID in der Tabelle „Sortieraufgabe“ basierend auf der eingegebenen Sortiernummer zu finden. Nach Eingabe der Sortiernummer und Ausführung des Datenflusses wird die entsprechende Datensatz-ID im Frontend angezeigt.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1LZzqHGc7I5IdAVLmK6H1_ItODiiruSAJ/view?usp=sharing) herunterladen.