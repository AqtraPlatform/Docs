# Exportieren in Datei

![](../../assets/images/app-development/export-to-file.png)

## Allgemeine Informationen
Der Schritt „Exportieren in Datei“ wird verwendet, um Daten aus dem internen Dataflow-Modell in eine strukturierte Datei zu exportieren. Dieser Schritt unterstützt die Erstellung von Dateien im CSV-, Excel- und JSON-Format, sodass Sie verarbeitete Daten effizient übertragen und verteilen können.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld     | Wertoptionen      | Zweck |
|----------------------|-------------------|------------|
| Schrittname          | -                 | Name des Schrittes |
| Quellenschritt       | -                 | Auswahl aus vorherigen Schritten für die Datenquelle |
| Ausgabedateityp     | Csv, Excel, JSON  | Exportdateiformat |
| Dateiname            | -                 | Exportdateiname |
| Spaltentrenner       | ; (Standard)      | CSV-Dateitrennzeichen (Standard ";") |
| Arbeitsblattname (Wenn Eingabedateityp = Excel) | -                 | Blattname in der Excel-Datei |
| Felderzuordnung      | -                 | Zuordnung der Dataflow-Modellfelder und der Dateistruktur |

## Anwendungsfälle
- **Datenverteilung**: Ideal zum Erstellen von Berichten, Verteilen von Informationen an Kunden oder Partner und Übertragen von Daten zwischen verschiedenen Systemen oder Abteilungen.
- **Datenarchivierung**: Kann verwendet werden, um wichtige Informationen in einem strukturierten und leicht zugänglichen Format zu speichern.
- **Integration mit anderen Systemen**: Ermöglicht es Ihnen, Daten für die anschließende Integration oder Verarbeitung durch andere Systeme, die CSV-, Excel- oder JSON-Formate unterstützen, vorzubereiten.

## Ausnahmen
- **Kompatibilität des Dateiformats**: Es ist wichtig, die Exporteinstellungen zu optimieren, um sicherzustellen, dass die generierten Dateien mit den Erwartungen und Anforderungen der Endbenutzer oder Systeme kompatibel sind.
- **Optimierung der Leistung bei großen Datenmengen**: Bei der Exportierung großer Datenmengen müssen Sie die Leistung und mögliche Dateigrößenbeschränkungen (Standard 1 MB) berücksichtigen.

## Anwendungsszenario

Die erstellte Komponente dient als Werkzeug zum Exportieren von Daten aus dem System. Sie umfasst mehrere Schritte wie das Abrufen des Datenmodells, Filtern und Exportieren in eine Excel-Datei. Der Benutzer kann die Datenfilterung vor dem Export anpassen und die Ergebnisse in einem praktischen Format über die Schaltfläche in der Benutzeroberfläche herunterladen.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1haTgN7Qyu6rD3GSYcDKPEMu3V_KcOdVt/view?usp=sharing) herunterladen.