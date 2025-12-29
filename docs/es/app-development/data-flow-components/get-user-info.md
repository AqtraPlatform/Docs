# Obtener información del usuario

![](../../assets/images/app-development/get-user-info.png)

## Información general
El paso “Obtener Información del Usuario” se utiliza para obtener datos sobre el usuario de la plataforma, como correo electrónico, nombre y apellido, para su posterior procesamiento en el flujo de datos actual. Este paso es necesario para la mayoría de las operaciones de usuario, excepto para crear un nuevo usuario.

**Obtención de Información del Usuario**
1. **Usando la bandera ‘Obtener información del usuario de la solicitud’**: El paso intentará recuperar datos sobre el usuario actual. Para que funcione correctamente, es necesario que el flujo de datos se llame en nombre de un usuario específico (por ejemplo, desde un formulario de solicitud o a través de una solicitud Proxy). Si se llama en nombre de la plataforma (por ejemplo, en el flujo de datos de entrada), el resultado será nulo.
2. **Sin la bandera ‘Obtener información del usuario de la solicitud’**: El usuario puede ser definido:
   - A través del nombre del sistema, utilizando un parámetro String del modelo de flujo de datos actual.
   - A través de un enlace al directorio de información del usuario, por ejemplo, los campos creatorSubject o changeAuthor.

## Parámetros
**Configuraciones del Paso:**

| Campo de Configuración     | Opciones de Valor | Propósito |
|----------------------------|-------------------|-----------|
| Nombre del paso             | -                 | Nombre del paso |
| Paso fuente                 | -                 | Selección del paso anterior |
| Obtener información del usuario de la solicitud | - | Bandera para obtener información sobre el usuario actual |
| Campo de información del usuario | -           | Campo de identificación del usuario |
| Nombre del usuario          | -                 | Nombre del usuario |
| Campo de almacenamiento del resultado | -       | Campo para guardar la información obtenida sobre el usuario |

## Casos
- **Recuperación de Datos del Usuario para Procesamiento**: Se utiliza para extraer información del usuario para su uso posterior en el flujo de datos.
- **Enviar Notificaciones Personalizadas**: En casos donde se necesita enviar notificaciones por correo electrónico personalizadas a los usuarios, se utiliza el paso “Obtener Información del Usuario” para obtener sus direcciones de correo electrónico. Esta información se pasa luego al paso diseñado para enviar notificaciones.

## Excepciones
- **Manejo de Usuario No Encontrado**: En casos cuando no se puede identificar al usuario, el resultado será nulo, lo que requiere un procesamiento adicional en el flujo de datos.

## Escenario de aplicación

El componente "Obtener información del usuario" está diseñado para recuperar información sobre un usuario. Dentro de un flujo de datos, este paso se utiliza para consultar datos del usuario basados en criterios especificados, como un nombre de usuario u otra información identificativa. Por ejemplo, dentro de un flujo de datos, puedes especificar el nombre de un usuario para recuperar información sobre él y luego usar esta información para acciones posteriores, como mostrarla en una pantalla o actualizar una base de datos.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/16keZXK_MXlWLmcSA4a-nLvhx-GPP3RPy/view?usp=sharing)