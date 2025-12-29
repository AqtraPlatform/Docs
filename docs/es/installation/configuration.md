# Configuración Básica de la Plataforma

<br>

## Arquitectura de la Plataforma

La plataforma está construida sobre una arquitectura de microservicios que proporciona modularidad, escalabilidad y flexibilidad. Las características clave de la arquitectura incluyen:

- **Arquitectura de Microservicios**: El sistema se divide en microservicios separados, cada uno de los cuales realiza una función específica y opera de manera independiente.
- **Procesamiento Distribuido**: Los microservicios pueden distribuirse a través de diferentes nodos, proporcionando balanceo de carga y mayor resiliencia del sistema.
- **Contenerización y Orquestación**: Utilizar Docker para contenerizar microservicios y Kubernetes para orquestarlos facilita el despliegue, escalado y gestión de la aplicación.
- **Modularidad e interoperabilidad de microservicios**: La modularidad se logra al delinear claramente las funciones entre microservicios, y la comunicación entre ellos se realiza a través de APIs específicas y protocolos de interoperabilidad.

El sistema se presenta en once imágenes de contenedor Docker:

| Servicio         | Propósito                                                        |
| ---------------- | ---------------------------------------------------------------- |
| catalogs         | Almacenamiento y procesamiento de datos de usuario; soporte RLS  |
| data-flow        | Procesamiento y almacenamiento de scripts de datos personalizados |
| file-storage     | Almacenamiento de datos binarios                                   |
| identity         | Gestión de usuarios y autenticación                               |
| notification     | Envío de notificaciones                                           |
| scheduler        | Programador de eventos en el sistema; todos los eventos se llaman a través del bus |
| template-service  | Trabajo con plantillas                                           |
| view-service     | Almacenamiento de metadatos del sistema; orquestación de procesos de actualización de metadatos |
| workflow         | Scripting a través de la Máquina de Estados                       |
| web-studio       | Parte web del desarrollo de aplicaciones                          |
| web-workplace    | Parte web para ejecutar aplicaciones                              |

<br>

## Stack Tecnológico

- **Fundación**: La plataforma está construida sobre Net Core 8.0, una plataforma de desarrollo de software modular y de código abierto.
- **Lenguaje de Desarrollo**: C# se utiliza como el lenguaje de programación principal.
  <br>

## Infraestructura Adicional

- **PostgreSQL** (versión ≥13.0): Sistema de gestión de bases de datos objeto-relacional para almacenamiento de datos primarios.
- **Redis** (versión ≥5.0): Base de datos no relacional utilizada para almacenamiento en caché de datos.
- **RabbitMQ** (versión ≥3.0): Un software de intermediario de mensajes para manejar eventos y colas del sistema.
  <br>

## Partes Web

- Utiliza el marco web de front-end **Blazor**, parte de Net Core, para crear componentes web.
- Las Partes Web se ejecutan como **WebAssembly** (WASM) del lado del cliente.
  <br>

## Requisitos de Instalación

- **Kubernetes**: Se requiere un clúster de Kubernetes para que funcione la versión agrupada del producto.
  - **Configuración Mínima**:
    - 1 x Master (2 vCPU, 4GB RAM, 20GB SSD) - se recomiendan 3 nodos con el rol de Master.
    - 1 x Ingress (4 vCPU, 8GB RAM, 20GB SSD)
    - 3 x Worker (16 vCPU, 32GB RAM, 60GB SSD)
- **Sistema Operativo**: Ubuntu Server 22.04 LTS
  <br>

## Redes y Puertos

- Todo el tráfico de red utiliza el protocolo **TCP/IP**.
- Por defecto, cada microservicio (excepto web-studio) proporciona dos puertos:
  - **80**: API pública (HTTP/1.1).
  - **5001**: API privada (HTTP/2).
- **Web-studio**: Proporciona solo el puerto 80 para servir recursos estáticos.
- Todos los microservicios, con la excepción de web-studio, deben tener acceso a PostgreSQL, Redis y RabbitMQ.
  <br>

## Protocolos Utilizados

- **HTTP/1.1**: Para API pública.
- **GRPC**: Para API privada.
- **WebSocket**: Para el servicio de Notificación.
- **SIP sobre WebSocket**: Opcional, para integración con SIP en un web-workplace.
- **RTC/RTCP**: Opcional, para integración con SIP en un web-workplace.
  <br>

## Almacenamiento de Datos

Cada microservicio gestiona su propio esquema en la base de datos, sin superponerse con los demás.

| Servicio          | Esquema                    |
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

Cada microservicio es responsable de crear y migrar los metadatos de sus esquemas.

El servicio de catalogs, que es responsable de almacenar datos de usuario, crea una partición adicional en su esquema para cada tipo de dato, heredada de la tabla primaria, así como particiones adicionales para implementar RLS si es necesario. Cuando se forman estas particiones, se generan todos los índices adicionales y claves externas.

La composición de índices y claves externas depende de la configuración de la aplicación que estás construyendo en la plataforma.
<br>

## Gestión de Autorización y Permisos

- Autorización local utilizando **tokens JWT**.
- Capacidad para conectar sistemas de autorización externos (oAuth, OpenId Connect, autorización de Windows, SAML).
- **RBAC** (Control de Acceso Basado en Roles) para el control de acceso.
  <br>

## Recolección de métricas y trazas

Todos los servicios, excepto web-studio, proporcionan métricas en el formato ‘Prometheus’. Las métricas están disponibles a través de la ruta relativa /metrics. Para verificar la disponibilidad del servicio, se proporcionan dos rutas /hc y /liveness:

- hc - información detallada sobre todas las verificaciones;
- liveness - una respuesta corta sobre la disponibilidad del servicio.

Los registros son recolectados por el sistema mismo, todos los registros se escriben en el esquema de mantenimiento, y la visualización de registros está disponible en el web-studio.
El nivel de registro para cada servicio se configura por separado a través del web-studio, en la sección "Mantenimiento".
Se pueden conectar dos sistemas Zipkin o Jaeger para recolectar trazas. La recolección de trazas se configura a nivel de parámetro del servicio. Si deseas exportar trazas a Jaeger, necesitas al menos la versión 1.35.