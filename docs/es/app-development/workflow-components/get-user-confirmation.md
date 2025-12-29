# Obtener confirmación del usuario

![](../../assets/images/app-development/get-user-confirmation.png)

## Información general
El paso “Obtener Confirmación del Usuario” en el flujo de trabajo se utiliza para solicitar confirmación o realizar una acción del usuario. El paso envía una notificación al usuario con una solicitud para realizar una acción específica sobre el objeto, donde el objeto es el estado del modelo actual.

## Parámetros
**Configuraciones del Paso:**

| Campo de Configuración | Opciones de Valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso “Obtener Confirmación del Usuario” |
| Campo de confirmación  | -                 | Campo con opciones que se solicitarán al usuario |
| Campo de información del usuario | Multiselección de Catálogo | Campo con información sobre un usuario o grupo de usuarios |
| Enrutamiento de usuario | Multiselección de Catálogo | Objeto que es un contexto de seguridad |

## Casos
- **Solicitud de Confirmación del Usuario**: Ideal para scripts que requieren confirmación o elección de acción del usuario, como confirmar una transacción, aceptar el procesamiento de datos o elegir una opción de respuesta.
- **Participación Interactiva del Usuario en el Proceso**: Adecuado para un flujo de trabajo, donde es importante tener en cuenta las decisiones o elecciones del usuario para continuar o cambiar el proceso.

## Excepciones
- **Asegurar que la Solicitud Sea Clara**: Es importante formular claramente la solicitud de confirmación para que el usuario entienda qué acción se espera de él.
- **Gestionar las Respuestas del Usuario**: Las respuestas del usuario deben ser procesadas adecuadamente y tenidas en cuenta, especialmente en situaciones donde determinan el curso de las acciones posteriores en el flujo de trabajo.
- **Tener en Cuenta el Contexto de Seguridad y Permisos**: Al utilizar el parámetro de Enrutamiento de Usuario, es importante considerar el contexto de seguridad y los permisos correspondientes del usuario.