# Enviar notificación

![](../../assets/images/app-development/send-notification-workflow.png)

## Información general
El paso “Enviar Notificación” dentro del flujo de trabajo se utiliza para enviar notificaciones simples a un usuario o grupo de usuarios utilizando un ícono de campana. Esto te permite comunicarte de manera efectiva con los usuarios del sistema transmitiendo información o notificaciones importantes.

## Parámetros
**Configuraciones del paso:**

| Campo de configuración | Opciones de valor   | Propósito |
|------------------------|---------------------|-----------|
| Nombre del paso        | -                   | Nombre del paso |
| Tipo de notificación   | Smtp, Mail, SignalR | Tipo de canal de entrega de notificaciones |
| Campo de información del usuario | Multiselección de Catálogo | Campo que contiene el usuario o lista de usuarios |
| Nombre del usuario     | Multiselección de Catálogo | Usuario específico a ser notificado |
| Mensaje               | -                   | Texto de la notificación |

## Casos
- **Información del Usuario**: Se utiliza para informar a los usuarios sobre eventos importantes, cambios en el sistema, alarmas u otros mensajes que requieren atención.
- **Notificaciones Personalizadas**: Permite enviar notificaciones a usuarios o grupos específicos, haciendo que la comunicación sea más dirigida y efectiva.

## Excepciones
- **Necesidad de Información de Usuario Actualizada**: La entrega efectiva de notificaciones requiere información de usuario actualizada, incluyendo detalles de contacto del usuario.
- **Selección del Canal de Entrega Correcto**: Debes elegir cuidadosamente el tipo de canal de entrega (Smtp, Mail, SignalR) dependiendo de las preferencias de los usuarios y las capacidades técnicas del sistema.