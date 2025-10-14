# Basic Platform Settings

<br>

## Platform Architecture

The platform is built on a microservice architecture that provides modularity, scalability, and flexibility. The key features of the architecture include:

- **Microservice Architecture**: The system is divided into separate microservices, each of which performs a specific function and operates independently.
- **Distributed Processing**: Microservices can be distributed across different nodes, providing load balancing and increased system resiliency.
- **Containerization and Orchestration**: Using Docker to containerize microservices and Kubernetes to orchestrate them makes it easier to deploy, scale, and manage the application.
- **Modularity and interoperability of microservices**: Modularity is achieved by clearly delineating functions between microservices, and communication between them takes place via specific APIs and interoperability protocols.

The system comes in eleven Docker container images:

| Service | Purpose |
| -------------- | ----------------------------------------------------------------- |
| catalogs | Storage and processing of user data; RLS support |
| data-flow | Processing and storing custom data scripts |
| file-storage | Binary data storage |
| identity | User management and authentication |
| notification | Sending notifications |
| scheduler | Event scheduler in the system; all events are called via the bus |
| template-service | Working with templates |
| view-service | Storage of system metadata; orchestration of metadata update processes |
| workflow | Scripting via the State Machine |
| web-studio | Application development web part |
| web-workplace | Web part for running applications |

<br>

## Technology Stack

- **Foundation**: The platform is built on Net Core 8.0, a modular open-source software development platform.
- **Development Language**: C# is used as the primary programming language.
  <br>

## Additional Infrastructure

- **PostgreSQL** (version ≥13.0): Object-relational database management system for primary data storage.
- **Redis** (version ≥5.0): A non-relational database used for data caching.
- **RabbitMQ** (version ≥3.0): A software message broker for handling system events and queues.
  <br>

## Web Parts

- Uses the **Blazor** front-end web framework, part of Net Core, to create web components.
- Web Parts are run as a client-side **WebAssembly** (WASM).
  <br>

## Installation Requirements

- **Kubernetes**: Kubernetes cluster is required for the clustered version of the product to work.
  - **Minimum Configuration**:
    - 1 x Master (2 vCPU, 4GB RAM, 20GB SSD) - 3 nodes with the Master role are recommended.
    - 1 x Ingress (4 vCPU, 8GB RAM, 20GB SSD)
    - 3 x Worker (16 vCPU, 32GB RAM, 60GB SSD)
- **Operating System**: Ubuntu Server 22.04 LTS
  <br>

## Networking and Ports

- All network traffic uses the **TCP/IP** protocol.
- By default, each microservice (except web-studio) provides two ports:
  - **80**: Public API (HTTP/1.1).
  - **5001**: Private API (HTTP/2).
- **Web-studio**: Provides only port 80 for serving static resources.
- All microservices, with the exception of web-studio, must have access to PostgreSql, Redis, and RabbitMQ.
  <br>

## Protocols Used

- **HTTP/1.1**: For public API.
- **GRPC**: For private API.
- **WebSocket**: For the Notification service.
- **SIP over WebSocket**: Optional, for integration with SIP in a web-workplace.
- **RTC/RTCP**: Optional, for integration with SIP in a web-workplace.
  <br>

## Storing Data

Each microservice manages its own scheme in the database, without overlapping with the others.

| Service          | Scheme                    |
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

Each microservice is responsible for creating and migrating the metadata of its schemes.

The catalogs service, which is responsible for storing user data, creates an additional partition in its scheme for each data type, inherited from the primary table, as well as additional partitions to implement RLS if necessary. When these partitions are formed, all additional indexes and external keys are generated.

The composition of indexes and external keys depends on the configuration of the application you are building in the platform.
<br>

## Authorization & Permissions Management

- Local authorization using **JWT tokens**.
- Ability to connect external authorization systems (oAuth, OpenId Connect, Windows authorization, SAML).
- **RBAC** (Role-Based Access Control) for access control.
  <br>

## Collecting metrics and traces

All services, except web-studio, provide metrics in the ‘Prometheus’ format. Metrics are available by the relative path /metrics. To check the availability of the service, two paths are provided /hc and /liveness:

- hc - detailed information on all checks;
- liveness - a short response about the availability of the service.

Logs are collected by the system itself, all logs are written to the maintenance scheme, and log viewing is available in the web-studio.
The logging level for each service is configured separately through the web-studio, the "Maintenance" section.
Two Zipkin or Jaeger systems can be connected to collect traces. Trace collection is configured at the service parameter level. If you want to export traces to Jaeger, you need at least version 1.35.
