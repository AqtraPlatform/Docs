# Enviar notificación con plantilla

![](../../assets/images/app-development/send-templated-notification.png)

## Información general
El paso “Enviar Notificación con Plantilla” está diseñado para enviar notificaciones a usuarios o grupos de usuarios utilizando plantillas preconfiguradas. Este paso proporciona flexibilidad en la elección del método de entrega y los destinatarios de la notificación.

## Parámetros
**Configuración del paso:**

| Campo de configuración | Opciones de valor   | Propósito |
|------------------------|---------------------|------------|
| Nombre del paso        | -                   | Nombre del paso |
| Paso fuente            | -                   | Selección del paso anterior | 
| Tipo de notificación    | Smtp, Mail, SignalR | Tipo de canal de entrega de notificación |
| Campo de información del usuario | - | Lista de usuarios a ser notificados |
| Enrutamiento del usuario | - | Enrutamiento del usuario para entregar la notificación |
| Nombre de usuario      | -                   | Usuario específico a ser notificado |
| Plantilla             | -                   | Selección de plantillas de notificación preconfiguradas |
| Tipo de renderizado    | Texto, Html, Docx, Xlsx, Pdf | Tipo de renderizado de la plantilla de notificación  |
| Tema del mensaje      | Texto               | Línea de asunto para notificaciones por correo electrónico |

## Casos
- **Notificaciones Automatizadas**: Se utilizan para enviar notificaciones a usuarios utilizando plantillas preestablecidas para garantizar mensajes consistentes y precisos.
- **Flexibilidad en la Entrega de Mensajes**: Permite elegir entre diferentes canales de entrega (por ejemplo, SMTP, Mail, SignalR), lo que aumenta la cobertura y eficiencia de las comunicaciones.
- **Personalización de Notificaciones**: Soporta la personalización de notificaciones para usuarios o grupos específicos, así como varios formatos de contenido (texto, HTML, Docx, Xlsx).

## Excepciones
- **Requisito de un Canal de Entrega Configurado**: Para que las notificaciones se envíen con éxito, debe tener un canal de entrega funcional, como un servidor SMTP para notificaciones por correo electrónico.