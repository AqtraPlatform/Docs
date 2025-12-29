# Grundlegende Plattform-Einstellungen

<br>

## Plattformarchitektur

Die Plattform basiert auf einer Microservice-Architektur, die Modularität, Skalierbarkeit und Flexibilität bietet. Die Hauptmerkmale der Architektur umfassen:

- **Microservice-Architektur**: Das System ist in separate Microservices unterteilt, von denen jeder eine spezifische Funktion erfüllt und unabhängig arbeitet.
- **Verteilte Verarbeitung**: Microservices können über verschiedene Knoten verteilt werden, was Lastenausgleich und erhöhte Systemresilienz bietet.
- **Containerisierung und Orchestrierung**: Die Verwendung von Docker zur Containerisierung von Microservices und Kubernetes zur Orchestrierung erleichtert die Bereitstellung, Skalierung und Verwaltung der Anwendung.
- **Modularität und Interoperabilität von Microservices**: Modularität wird erreicht, indem die Funktionen zwischen Microservices klar abgegrenzt werden, und die Kommunikation zwischen ihnen erfolgt über spezifische APIs und Interoperabilitätsprotokolle.

Das System kommt in elf Docker-Container-Images:

| Dienst          | Zweck                                                               |
| --------------- | ------------------------------------------------------------------- |
| catalogs        | Speicherung und Verarbeitung von Benutzerdaten; RLS-Unterstützung   |
| data-flow       | Verarbeitung und Speicherung von benutzerdefinierten Datenskripten  |
| file-storage    | Speicherung von Binärdaten                                           |
| identity        | Benutzerverwaltung und Authentifizierung                             |
| notification    | Versand von Benachrichtigungen                                       |
| scheduler       | Ereignisplaner im System; alle Ereignisse werden über den Bus aufgerufen |
| template-service | Arbeiten mit Vorlagen                                              |
| view-service    | Speicherung von Systemmetadaten; Orchestrierung von Metadatenaktualisierungsprozessen |
| workflow        | Skripting über die Zustandsmaschine                                  |
| web-studio      | Webteil der Anwendungsentwicklung                                     |
| web-workplace    | Webteil zum Ausführen von Anwendungen                                |

<br>

## Technologiestack

- **Basis**: Die Plattform basiert auf Net Core 8.0, einer modularen Open-Source-Softwareentwicklungsplattform.
- **Entwicklungssprache**: C# wird als primäre Programmiersprache verwendet.
  <br>

## Zusätzliche Infrastruktur

- **PostgreSQL** (Version ≥13.0): Objekt-relationales Datenbankmanagementsystem für die primäre Datenspeicherung.
- **Redis** (Version ≥5.0): Eine nicht-relationale Datenbank, die für das Caching von Daten verwendet wird.
- **RabbitMQ** (Version ≥3.0): Ein Software-Nachrichtenbroker zur Verarbeitung von Systemereignissen und Warteschlangen.
  <br>

## Webteile

- Verwendet das **Blazor**-Frontend-Webframework, das Teil von Net Core ist, um Webkomponenten zu erstellen.
- Webteile werden als clientseitiges **WebAssembly** (WASM) ausgeführt.
  <br>

## Installationsanforderungen

- **Kubernetes**: Ein Kubernetes-Cluster ist erforderlich, damit die clusterbasierte Version des Produkts funktioniert.
  - **Mindestkonfiguration**:
    - 1 x Master (2 vCPU, 4GB RAM, 20GB SSD) - 3 Knoten mit der Master-Rolle werden empfohlen.
    - 1 x Ingress (4 vCPU, 8GB RAM, 20GB SSD)
    - 3 x Worker (16 vCPU, 32GB RAM, 60GB SSD)
- **Betriebssystem**: Ubuntu Server 22.04 LTS
  <br>

## Netzwerk und Ports

- Der gesamte Netzwerkverkehr verwendet das **TCP/IP**-Protokoll.
- Standardmäßig bietet jeder Microservice (außer web-studio) zwei Ports:
  - **80**: Öffentliche API (HTTP/1.1).
  - **5001**: Private API (HTTP/2).
- **Web-studio**: Bietet nur Port 80 zum Bereitstellen statischer Ressourcen.
- Alle Microservices, mit Ausnahme von web-studio, müssen Zugriff auf PostgreSQL, Redis und RabbitMQ haben.
  <br>

## Verwendete Protokolle

- **HTTP/1.1**: Für die öffentliche API.
- **GRPC**: Für die private API.
- **WebSocket**: Für den Benachrichtigungsdienst.
- **SIP über WebSocket**: Optional, für die Integration mit SIP in einem web-workplace.
- **RTC/RTCP**: Optional, für die Integration mit SIP in einem web-workplace.
  <br>

## Datenspeicherung

Jeder Microservice verwaltet sein eigenes Schema in der Datenbank, ohne sich mit den anderen zu überschneiden.

| Dienst          | Schema                    |
| --------------- | ------------------------- |
| catalogs        | catalogs                  |
| data-flow       | dataflow                  |
| file-storage    | file_storage              |
| identity        | identity                  |
| notification    | notification              |
| scheduler        | scheduler                 |
| template-service | template                  |
| view-service     | view_service, maintenance |
| workflow         | workflow, wfc_persistence |
| web-workplace    | workplace-host            |

<br>

Jeder Mikrodienst ist verantwortlich für die Erstellung und Migration der Metadaten seiner Schemata.

Der Katalogdienst, der für die Speicherung von Benutzerdaten verantwortlich ist, erstellt eine zusätzliche Partition in seinem Schema für jeden Datentyp, der von der Primärtabelle geerbt wird, sowie zusätzliche Partitionen zur Implementierung von RLS, falls erforderlich. Wenn diese Partitionen gebildet werden, werden alle zusätzlichen Indizes und externen Schlüssel generiert.

Die Zusammensetzung von Indizes und externen Schlüsseln hängt von der Konfiguration der Anwendung ab, die Sie auf der Plattform erstellen.
<br>

## Autorisierung & Berechtigungsmanagement

- Lokale Autorisierung mit **JWT-Token**.
- Möglichkeit, externe Autorisierungssysteme zu verbinden (oAuth, OpenId Connect, Windows-Autorisierung, SAML).
- **RBAC** (Role-Based Access Control) für die Zugriffskontrolle.
  <br>

## Erfassung von Metriken und Traces

Alle Dienste, außer web-studio, bieten Metriken im ‘Prometheus’-Format an. Metriken sind über den relativen Pfad /metrics verfügbar. Um die Verfügbarkeit des Dienstes zu überprüfen, sind zwei Pfade vorgesehen: /hc und /liveness:

- hc - detaillierte Informationen zu allen Prüfungen;
- liveness - eine kurze Antwort zur Verfügbarkeit des Dienstes.

Protokolle werden vom System selbst erfasst, alle Protokolle werden im Wartungsschema geschrieben, und die Protokollansicht ist im web-studio verfügbar. Das Protokollierungsniveau für jeden Dienst wird separat über das web-studio im Abschnitt "Wartung" konfiguriert. Zwei Zipkin- oder Jaeger-Systeme können angeschlossen werden, um Traces zu sammeln. Die Trace-Erfassung wird auf der Ebene der Dienstparameter konfiguriert. Wenn Sie Traces nach Jaeger exportieren möchten, benötigen Sie mindestens Version 1.35.