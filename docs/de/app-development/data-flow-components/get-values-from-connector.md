# Werte vom Connector abrufen

![](../../assets/images/app-development/get-values-from-connector.png)

## Allgemeine Informationen
Der Schritt „Werte vom Connector abrufen“ ermöglicht es Ihnen, Daten über eine Abfrage an externe Systeme mithilfe der konfigurierten Connectoren abzurufen. Der Schritt kann zeitgesteuert oder im Auftrag des Benutzers aufgerufen werden.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld      | Wertoptionen               | Zweck |
|-----------------------|---------------------------|-------|
| Schrittname           | -                         | Name des Schrittes |
| System                | Mehrfachauswahl aus Katalog | Enthält vorkonfigurierte Integrationssysteme |
| Connector             | Mehrfachauswahl aus Katalog | Enthält vorkonfigurierte Connectoren im Integrationssystem |
| Abfragepfad           | Mehrfachauswahl aus Katalog | Enthält den „EndPoint“, der aufgerufen werden soll |
| Methodenname          | Get, Post, Put, Delete    | Art der auszuführenden Anfrage |
| Parameterzuordnung    | -                         | Eine dynamische Entität, die es Ihnen ermöglicht, eine Anfrage über eine ausgewählte API zu filtern |

## Anwendungsfälle
- **Geplante Aktualisierung von Daten**: Der Schritt wird verwendet, um Daten im Eingabedatenfluss automatisch auf einer geplanten Basis über Cron zu aktualisieren, um rechtzeitige und aktuelle Informationen zu erhalten.
- **Individuelle Abfrageanpassung**: Der Schritt ist so konfiguriert, dass spezifische Abfragen an verschiedene externe Systeme gesendet werden, was eine flexible Integration und Verarbeitung von Daten aus mehreren Quellen ermöglicht.
- **Optimierung des Datenflusses**: Der Schritt wird effizient genutzt, um Daten aus externen Systemen zu extrahieren, wodurch der Bedarf an manueller Verarbeitung minimiert und die Leistung des Datenflusses verbessert wird.

## Ausnahmen
- **Abfragemethoden**: Obwohl verschiedene Abfragemethoden (Get, Post, Put, Delete) unterstützt werden, ist eine sorgfältige Anpassung erforderlich, die von Fall zu Fall unter Berücksichtigung der spezifischen Merkmale des externen Systems und des Datentyps erfolgt.
- **Automatisierung mit Einschränkungen**: Die Möglichkeit, einen geplanten Schritt automatisch aufzurufen, bietet Komfort, erfordert jedoch eine Feinabstimmung der Parameter und die Überprüfung der Zugänglichkeit externer Systeme.

## Anwendungsszenario

Diese Komponente verarbeitet Zeichendaten. Wir erstellen fünf Datenmodelle für ihre Attribute: character_id, character_name, character_species, character_status und gender. Dann wählen wir eine Integration, zum Beispiel Rick and Morty, und fügen die folgenden Schritte hinzu: Werte vom Connector abrufen, Sammlung extrahieren, Eintrag über Bus speichern und Antwort schreiben.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1zWIWzpqccbocpDCfVUNIkGW2grrWJ5Yn/view?usp=sharing) herunterladen.