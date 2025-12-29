# Render-Vorlage

![](../../assets/images/app-development/render-template.png)

## Allgemeine Informationen
Der Schritt „Render-Vorlage“ wird verwendet, um Dokumente, insbesondere im PDF-Format, mithilfe von Daten aus Dataflow und im System verfügbaren Vorlagen zu erstellen. Der Schritt ermöglicht es, Daten in professionell gestaltete Dokumente umzuwandeln, die häufig bei der Erstellung von Berichten, Verträgen, Rechnungen und anderen offiziellen Dokumenten verwendet werden.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld | Wertoptionen | Zweck |
|------------------|--------------|-------|
| Schrittname      | -            | Name des Schrittes |
| Quellschritt     | -            | Auswahl aus vorherigen Schritten für die Datenquelle |
| Vorlage          | -            | Auswahl aus den verfügbaren Vorlagen zur Erstellung eines Dokuments |
| Render-Typ       | text, HTML, Docx, Xlsx, PDF | Format des zu generierenden Dokuments |
| Dateiname        | -            | Name der generierten Datei |
| Feldzuordnung    | -            | Zuordnung von Feldern zwischen einer Vorlage und einem Datenmodell |

## Anwendungsfälle
- **Erstellung von formalisierte Dokumenten**: Besonders nützlich für die automatisierte Erstellung offizieller Dokumente wie Berichte, Rechnungen und Verträge durch Anwendung vordefinierter Vorlagen.
- **Inhaltsanpassung**: Ermöglicht die Erstellung personalisierter Dokumente für Kunden oder Benutzer unter Verwendung von spezifischen Daten für jeden Fall, wie z. B. personalisierte Angebote oder angepasste Berichte.
- **Vorbereitung zur Dokumentenverteilung**: Wird verwendet, um Dokumente zu erstellen, die dann Benutzern zum Herunterladen zur Verfügung gestellt oder per E-Mail versendet werden können.

## Ausnahmen
- **Anforderung an die Qualität und Genauigkeit der Vorlagen**: Die Qualität der resultierenden Dokumente steht in direktem Zusammenhang mit der Genauigkeit und Professionalität der verwendeten Vorlagen.
- **Notwendigkeit einer Nachverfolgung zur Verteilung von Dokumenten**: Sobald ein Dokument generiert wurde, ist oft ein nachfolgender Schritt, wie „Formularaktion“ mit der Option „Datei herunterladen“, erforderlich, um das Dokument den Benutzern zur Verfügung zu stellen.

## Anwendungsszenario

Diese Komponente nutzt mehrere Schritte, um eine PDF-Datei zu erstellen und herunterzuladen. Zuerst wird das Datenmodell abgerufen, dann wird die PDF-Vorlage gerendert. Der Schritt „Formularaktion“ wird konfiguriert, um die Datei herunterzuladen, wobei das Datenfeld angegeben wird, das die Dateiinformationen enthält. Nach dem Schritt „Antwort schreiben“ wird die generierte Datei an das Frontend zum Herunterladen gesendet.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1Omst72osc9qf1FtxQcIohdARDzqwDKHT/view?usp=sharing) herunterladen.