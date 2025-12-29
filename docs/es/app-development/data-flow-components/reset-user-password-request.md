# Solicitud de restablecimiento de contraseña de usuario

![](../../assets/images/app-development/reset-user-password-request.png)

## Información general
El paso “Solicitud de Restablecimiento de Contraseña de Usuario” está diseñado para generar una nueva contraseña para el usuario. El paso funciona en conjunto con la “Enviar Notificación Plantillada” para asegurar que los usuarios reciban una nueva contraseña. El paso solo funciona si tienes un dominio de aplicación con una URI pública configurada.

## Parámetros
**Configuraciones del paso:**

| Campo de configuración | Opciones de valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso fuente            | -                 | Selección del paso anterior |
| Campo de información del usuario | -       | Un campo que contiene información sobre el usuario |
| Nombre de usuario      | -                 | Nombre de usuario para el cual se está restableciendo la contraseña |
| Cliente para la solicitud | -             | Cliente o aplicación que inicia la solicitud de autenticación |

## Casos
- **Recuperación de Acceso del Usuario**: Utilizado en scripts donde un usuario ha olvidado su contraseña y necesita restablecerla para volver a acceder al sistema.

## Excepciones
- **Requisito de un Dominio de Aplicación con una URI Pública**: El paso requiere un dominio de aplicación configurado con una URI pública para funcionar correctamente.
- **Dependencia del Método de Notificación al Usuario**: La efectividad del paso depende de la fiabilidad y disponibilidad del método de notificación al usuario, como el correo electrónico, utilizado para enviar una nueva contraseña.