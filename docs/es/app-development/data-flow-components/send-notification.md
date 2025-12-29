# Enviar notificación

![](../../assets/images/app-development/send-notification.png)

## Información general
El paso “Enviar Notificación” está diseñado para enviar notificaciones personalizadas a usuarios o grupos de usuarios. Este paso ofrece un alto grado de flexibilidad, permitiéndote establecer directamente el texto y el asunto de cada notificación, lo que lo hace ideal para situaciones que requieren mensajes personalizados.

## Parámetros
**Configuraciones del paso:**

| Campo de configuración | Opciones de valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso fuente            | -                 | Fuente de los datos para enviar la notificación |
| Campo de información del usuario | -       | Campo que contiene información sobre los destinatarios de la notificación |
| Nombre del usuario      | -                 | Nombre del usuario al que se enviará la notificación |
| Campo del cuerpo del mensaje | -           | Campo para el cuerpo del mensaje |
| Tema del mensaje       | Texto             | Asunto de la notificación |
| Cuerpo del mensaje     | Texto             | Texto personalizable de la notificación  |
| Tipo de notificación    | Smtp, Mail, SignalR | Tipo de notificación |

## Casos
- **Notificaciones Personalizadas**: Utilizadas para crear mensajes únicos para cada usuario o situación, asegurando la máxima relevancia y compromiso de los destinatarios.
- **Comunicación Flexible**: Adecuado para scripts donde se requieren mensajes especiales, como ofertas especiales, recordatorios individuales o boletines personalizados.

## Excepciones
- **Requisito de Detalle del Mensaje**: Se debe prestar atención al detalle y precisión al formular el texto de cada notificación.
- **Necesidad de Gestión Cuidadosa de Notificaciones**: Debido a que cada mensaje es personalizable individualmente, es importante gestionar cuidadosamente el proceso de creación y envío de notificaciones para evitar errores e inconsistencias.