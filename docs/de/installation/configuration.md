# Grundlegende Plattformeinstellungen

<br>

## Plattformarchitektur

Die Plattform basiert auf einer Microservice-Architektur, die Modularität, Skalierbarkeit und Flexibilität bietet. Die wichtigsten Merkmale der Architektur umfassen:

- **Microservice-Architektur**: Das System ist in separate Microservices unterteilt, von denen jeder eine bestimmte Funktion erfüllt und unabhängig arbeitet.
- **Verteilte Verarbeitung**: Microservices können auf verschiedene Knoten verteilt werden, was Lastverteilung und erhöhte Systemresilienz bietet.
- **Containerisierung und Orchestrierung**: Die Verwendung von Docker zur Containerisierung von Microservices und Kubernetes zur Orchestrierung erleichtert die Bereitstellung, Skalierung und Verwaltung der Anwendung.
- **Modularität und Interoperabilität von Microservices**: Modularität wird durch klare Abgrenzung von Funktionen zwischen Microservices erreicht, und die Kommunikation zwischen ihnen erfolgt über spezifische APIs und Interoperabilitätsprotokolle.

Das System besteht aus elf Docker-Container-Images:

| Dienst           | Zweck                                                                                  |
| ---------------- | -------------------------------------------------------------------------------------- |
| catalogs         | Speicherung und Verarbeitung von Benutzerdaten; RLS-Unterstützung                      |
| data-flow        | Verarbeitung und Speicherung benutzerdefinierter Datenskripte                          |
| file-storage     | Binärdatenspeicherung                                                                  |
| identity         | Benutzerverwaltung und Authentifizierung                                               |
| notification     | Benachrichtigungen senden                                                              |
| scheduler        | Ereignisplaner im System; alle Ereignisse werden über den Bus aufgerufen               |
| template-service | Arbeiten mit Vorlagen                                                                  |
| view-service     | Speicherung von Systemmetadaten; Orchestrierung von Metadaten-Aktualisierungsprozessen |
| workflow         | Skripting über die State Machine                                                       |
| web-studio       | Anwendungsentwicklungs-Webteil                                                         |
| web-workplace    | Webteil zum Ausführen von Anwendungen                                                  |

<br>

## Technologie-Stack

- **Grundlage**: Die Plattform basiert auf Net Core 8.0, einer modularen Open-Source-Softwareentwicklungsplattform.
- **Entwicklungssprache**: C# wird als primäre Programmiersprache verwendet.
  <br>

## Zusätzliche Infrastruktur

- **PostgreSQL** (Version ≥13.0): Objektrelationales Datenbankverwaltungssystem für die primäre Datenspeicherung.
- **Redis** (Version ≥5.0): Eine nicht-relationale Datenbank zur Daten-Caching.
- **RabbitMQ** (Version ≥3.0): Ein Software-Message-Broker zur Behandlung von Systemereignissen und Warteschlangen.
  <br>

## Web-Teile

- Verwendet das **Blazor**-Frontend-Web-Framework, Teil von Net Core, zum Erstellen von Webkomponenten.
- Web-Teile werden als clientseitiges **WebAssembly** (WASM) ausgeführt.
  <br>

## Installationsanforderungen

- **Kubernetes**: Kubernetes-Cluster ist für die Cluster-Version des Produkts erforderlich.
  - **Mindestkonfiguration**:
    - 1 x Master (2 vCPU, 4GB RAM, 20GB SSD) - 3 Knoten mit Master-Rolle werden empfohlen.
    - 1 x Ingress (4 vCPU, 8GB RAM, 20GB SSD)
    - 3 x Worker (16 vCPU, 32GB RAM, 60GB SSD)
- **Betriebssystem**: Ubuntu Server 22.04 LTS
  <br>

## Netzwerk und Ports

- Der gesamte Netzwerkverkehr verwendet das **TCP/IP**-Protokoll.
- Standardmäßig stellt jeder Microservice (außer web-studio) zwei Ports bereit:
  - **80**: Öffentliche API (HTTP/1.1).
  - **5001**: Private API (HTTP/2).
- **Web-studio**: Stellt nur Port 80 für die Bereitstellung statischer Ressourcen bereit.
- Alle Microservices, mit Ausnahme von web-studio, müssen Zugriff auf PostgreSql, Redis und RabbitMQ haben.
  <br>

## Verwendete Protokolle

- **HTTP/1.1**: Für öffentliche API.
- **GRPC**: Für private API.
- **WebSocket**: Für den Notification-Dienst.
- **SIP over WebSocket**: Optional, für Integration mit SIP in einem Web-Workplace.
- **RTC/RTCP**: Optional, für Integration mit SIP in einem Web-Workplace.
  <br>

## Datenspeicherung

Jeder Microservice verwaltet sein eigenes Schema in der Datenbank, ohne sich mit anderen zu überschneiden.

| Dienst           | Schema                    |
| ---------------- | ------------------------- |
| catalogs         | catalogs                  |
| data-flow        | dataflow                  |
| file-storage     | file_storage              |
| identity         | identity                  |
| notification     | notification              |
| scheduler        | scheduler                 |
| template-service | template                  |
| view-service     | view_service, maintenance |
| workflow         | workflow, wfc_persistence |
| web-workplace    | workplace-host            |

<br>

Jeder Microservice ist für die Erstellung und Migration der Metadaten seiner Schemas verantwortlich.

Der Catalogs-Dienst, der für die Speicherung von Benutzerdaten verantwortlich ist, erstellt eine zusätzliche Partition in seinem Schema für jeden Datentyp, der von der primären Tabelle geerbt wird, sowie zusätzliche Partitionen zur Implementierung von RLS, falls erforderlich. Wenn diese Partitionen gebildet werden, werden alle zusätzlichen Indizes und externen Schlüssel generiert.

Die Zusammensetzung von Indizes und externen Schlüsseln hängt von der Konfiguration der Anwendung ab, die Sie auf der Plattform erstellen.
<br>

## Autorisierung & Berechtigungsverwaltung

- Lokale Autorisierung mit **JWT-Tokens**.
- Möglichkeit, externe Autorisierungssysteme anzuschließen (oAuth, OpenId Connect, Windows-Autorisierung, SAML).
- **RBAC** (Role-Based Access Control) für Zugriffskontrolle.
  <br>

## Sammeln von Metriken und Traces

Alle Dienste, außer web-studio, stellen Metriken im 'Prometheus'-Format bereit. Metriken sind über den relativen Pfad /metrics verfügbar. Um die Verfügbarkeit des Dienstes zu überprüfen, werden zwei Pfade bereitgestellt /hc und /liveness:

- hc - detaillierte Informationen zu allen Überprüfungen;
- liveness - eine kurze Antwort über die Verfügbarkeit des Dienstes.

Logs werden vom System selbst gesammelt, alle Logs werden in das Maintenance-Schema geschrieben, und die Protokollansicht ist im Web-Studio verfügbar.
Der Logging-Level für jeden Dienst wird separat über das Web-Studio im Abschnitt "Maintenance" konfiguriert.
Zwei Systeme, Zipkin oder Jaeger, können zum Sammeln von Traces angeschlossen werden. Die Trace-Sammlung wird auf der Ebene der Dienstparameter konfiguriert. Wenn Sie Traces nach Jaeger exportieren möchten, benötigen Sie mindestens Version 1.35.
