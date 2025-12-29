# Confirmar solicitud de correo electrónico del usuario

![](../../assets/images/app-development/confirm-user-email-request.png)

## Información general
El paso “Confirmar Solicitud de Correo Electrónico del Usuario” se utiliza para habilitar al usuario que fue creado originalmente con la bandera “Deshabilitado”. Este proceso implica verificar al usuario a través del correo electrónico utilizando el paso “Enviar Notificación Plantillada”. El paso requiere un dominio de aplicación con una URI pública y un servidor SMTP configurado para enviar notificaciones por correo electrónico.

## Parámetros
**Configuraciones del Paso:**

| Campo de Configuración | Opciones de Valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso fuente            | -                 | Seleccionando el paso anterior |
| Campo de información del usuario | -       | Un campo que contiene información sobre el usuario |
| Nombre del usuario      | -                 | Nombre del usuario cuya confirmación se debe obtener |
| Cliente para la solicitud | -               | El cliente o aplicación que inicia la solicitud de confirmación |

## Casos
- **Habilitación de Nuevos Usuarios**: Este paso se utiliza para habilitar a los usuarios que han sido registrados como deshabilitados al verificar su correo electrónico. Esto proporciona una capa adicional de verificación y seguridad.
- **Gestión de Acceso de Usuarios**: Adecuado para sistemas que requieren verificación de correo electrónico del usuario antes de que se pueda otorgar acceso completo a la funcionalidad del sistema.

## Excepciones
- **Requisito de un servidor SMTP configurado**: Se requiere un servidor SMTP configurado para que las notificaciones de correo electrónico de confirmación se envíen con éxito.
- **Dependencia del dominio de la aplicación y URI pública**: Este paso requiere un dominio de aplicación con una URI pública para asegurar que la operación sea correcta y que el proceso de verificación esté disponible para el usuario.