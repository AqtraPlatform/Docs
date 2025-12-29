# Suscribirse al conector

![](../../assets/images/app-development/subscribe-to-connector.png)

## Información general

El paso “Suscribirse al conector” es para suscribirse a recibir mensajes de varios sistemas de mensajería, como RabbitMQ o Kafka.

## Parámetros

**Configuración del paso:**

| Campo de configuración | Opciones de valor          | Propósito                                                      |
| ---------------------- | -------------------------- | -------------------------------------------------------------- |
| Nombre del paso        | -                          | Nombre del paso                                               |
| Sistema                | Selección múltiple del Catálogo | Contiene sistemas de integración preconfigurados              |
| Conector               | Selección múltiple del Catálogo | Contiene conectores preconfigurados en el sistema de integración |
| Ruta de consulta       | Selección múltiple del Catálogo | Contiene el “EndPoint” que se va a acceder                   |
| Nombre del método      | Get, Post, Put, Delete    | Tipo de solicitud que se va a ejecutar                        |

## Casos

- **Respuesta a eventos**: Recepción automática de notificaciones sobre eventos o cambios en los datos de fuentes externas.
- **Integración con sistemas de mensajería**: Interacción con varias plataformas de mensajería para asegurar un flujo de datos continuo.

## Excepciones

- **Funcionalidad limitada**: El paso está limitado a suscribirse a mensajes y no admite otros tipos de interacciones con sistemas externos.
- **Dependencia de sistemas externos**: Requiere una configuración y soporte confiables de los sistemas de mensajería utilizados.

## Escenario de aplicación

El componente está configurado para **suscribirse a una cola de RabbitMQ** y guardar los mensajes recibidos en una **base de datos**. Se utilizan pasos como "**Suscribirse al conector**", "**Ejecutar script**" para el procesamiento de datos, y "**Actualizar entrada**" para guardar mensajes en este proceso.

- La configuración del componente estará disponible más adelante.