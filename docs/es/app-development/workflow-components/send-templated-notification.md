# Enviar notificación con plantilla

![](../../assets/images/app-development/send-templated-notification-workflow.png)

## Información general
El paso “Enviar Notificación con Plantilla” dentro del flujo de trabajo se utiliza para enviar notificaciones a usuarios o grupos de usuarios utilizando plantillas preconfiguradas. Esto permite crear mensajes estandarizados pero personalizados, lo que mejora la comunicación y asegura la consistencia de los mensajes.

## Parámetros
**Configuración del paso:**

| Campo de configuración | Opciones de valor        | Propósito |
|------------------------|--------------------------|------------|
| Nombre del paso        | -                        | Nombre del paso |
| Tipo de notificación   | Smtp, Mail, SignalR      | Tipo de canal de entrega de notificaciones |
| Campo de información del usuario | Multiselección de Catálogo | Campo con información sobre un usuario o grupo de usuarios |
| Grupo de usuarios      | Multiselección de Catálogo | (Parámetro obsoleto, no utilizado) |
| Enrutamiento de usuarios| Multiselección de Catálogo | Configuración del enrutamiento de notificaciones |
| Nombre de usuario      | Multiselección de Catálogo | Usuario específico a notificar |
| Plantilla             | Multiselección de Catálogo | Selección de una plantilla de notificación |
| Tipo de renderizado    | Texto, Html, Docx, Xlsx   | Formato de renderizado de la plantilla |

## Casos
- **Notificaciones Automatizadas**: Se utilizan para enviar notificaciones estandarizadas, como recordatorios, confirmaciones de acciones o mensajes informativos.
- **Comunicación Efectiva**: Adecuado para crear mensajes diseñados profesionalmente para comunicaciones externas o internas.

## Excepciones
- **Requisitos de Personalización de Plantillas**: Las plantillas de notificación deben prepararse y configurarse con anticipación para garantizar que los mensajes sean relevantes para los propósitos de comunicación.
- **Gestionar Destinatarios de Notificaciones**: Es importante identificar a los destinatarios de los mensajes utilizando el campo de información del usuario y el nombre de usuario para asegurar que las notificaciones lleguen a los destinatarios correctos.