# Abonnieren des Connectors

![](../../assets/images/app-development/subscribe-to-connector.png)

## Allgemeine Informationen

Der Schritt „Abonnieren des Connectors“ dient dazu, Nachrichten von verschiedenen Messaging-Systemen wie RabbitMQ oder Kafka zu abonnieren.

## Parameter

**Schritt Einstellungen:**

| Einstellungsfeld | Wertoptionen          | Zweck                                                        |
| ---------------- | --------------------- | ------------------------------------------------------------ |
| Schrittname      | -                     | Name des Schrittes                                          |
| System           | Mehrfachauswahl aus Katalog | Enthält vorkonfigurierte Integrationssysteme                 |
| Connector        | Mehrfachauswahl aus Katalog | Enthält vorkonfigurierte Connectoren im Integrationssystem   |
| Abfragepfad      | Mehrfachauswahl aus Katalog | Enthält den „EndPoint“, der aufgerufen werden soll           |
| Methodenname     | Get, Post, Put, Delete | Art der auszuführenden Anfrage                               |

## Anwendungsfälle

- **Antwort auf Ereignisse**: Automatisches Empfangen von Benachrichtigungen über Ereignisse oder Änderungen von Daten aus externen Quellen.
- **Integration mit Messaging-Systemen**: Interaktion mit verschiedenen Messaging-Plattformen, um einen kontinuierlichen Datenfluss sicherzustellen.

## Ausnahmen

- **Eingeschränkte Funktionalität**: Der Schritt ist auf das Abonnieren von Nachrichten beschränkt und unterstützt keine anderen Arten von Interaktionen mit externen Systemen.
- **Abhängigkeit von externen Systemen**: Erfordert eine zuverlässige Konfiguration und Unterstützung von den verwendeten Messaging-Systemen.

## Anwendungsszenario

Die Komponente ist konfiguriert, um **eine RabbitMQ-Warteschlange zu abonnieren** und die empfangenen Nachrichten in einer **Datenbank** zu speichern. Schritte wie „**Abonnieren des Connectors**“, „**Skript ausführen**“ zur Datenverarbeitung und „**Eintrag aktualisieren**“ zum Speichern von Nachrichten werden in diesem Prozess verwendet.

- Die Konfiguration der Komponente wird später verfügbar sein.