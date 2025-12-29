# Obtener código de un solo uso para el usuario

![](../../assets/images/app-development/get-one-time-code-for-user.png)

## Información general
El paso “Obtener Código de Un Solo Uso para el Usuario” se utiliza para generar y enviar un código de un solo uso para iniciar sesión como parte de la autenticación de dos factores. Este paso funciona en conjunto con el paso “Confirmar Código de Un Solo Uso para el Usuario” y generalmente se aplica utilizando la funcionalidad “Enviar Notificación Plantillada”.

## Parámetros
**Configuración del Paso:**

| Campo de Configuración | Opciones de Valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso fuente            | -                 | Selección del paso anterior |
| Nombre de usuario      | -                 | Nombre o ID del usuario para quien se genera el código |
| Cliente para la solicitud | -               | Cliente o aplicación que inicia la solicitud de confirmación |
| Tiempo de vida del código | -              | La duración de un código |

## Casos
- **Autenticación de Dos Factores**: Se utiliza para proporcionar una capa adicional de seguridad al iniciar sesión generando un código temporal que el usuario debe confirmar.
- **Seguridad de Inicio de Sesión Mejorada**: Adecuado para escenarios donde se requieren medidas de seguridad mejoradas para prevenir el acceso no autorizado al sistema.

## Excepciones
- **Dependencia de la Precisión de los Datos del Usuario**: La precisión y relevancia de la información del usuario son críticas para la generación y envío exitoso de un código de un solo uso.
- **Gestión de la Duración del Código**: Debe configurar correctamente la duración del código para asegurarse de que su código esté actualizado y evitar problemas de acceso del usuario.

## Escenario de aplicación 

El componente agrega una nueva definición de cadena ForTestCode. Se crea un flujo de datos donde se obtiene un código de un solo uso para el usuario a través del modelo de acción Get y los pasos de Obtener información del usuario. El paso de script Execute se utiliza para pasar este código a la variable new_code, que luego se almacena en la definición ForTestCode del componente y se muestra en una ventana modal.

- Puede descargar la configuración del componente [aquí](https://drive.google.com/file/d/1_uPyqNOuOddurvwz-KteaoIIRQjgEzBH/view?usp=sharing)