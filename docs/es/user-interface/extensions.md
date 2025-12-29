# Menú de extensiones
<br>

El menú consta de 2 bloques:
- **Plantillas**
- **Configuraciones SMTP**
<br>

## Plantillas

Las plantillas se utilizan para el correo y las notificaciones de los usuarios y solo se pueden usar en el paso ‘Enviar Notificación con Plantilla’. Las plantillas se configuran en la sección ‘Aplicación/Plantillas’.
<br>

### Agregar/Eliminar Plantillas

- Para **agregar una nueva plantilla**, haga clic en el botón ‘AGREGAR’. 
- Para **eliminar una plantilla**, haga clic en la cruz en la lista común de todas las plantillas.
<br>

### Configuración del modelo de componente de plantilla

Al agregar o editar una plantilla, debe definir una estructura de Modelo de Objeto que interactuará con Dataflow y/o Workflow. Esto se hace configurando un conjunto de propiedades para cada uno de ellos, similar a la configuración de cualquier componente.
<br>

### Personalización del diseño y contenido de la plantilla

La plataforma utiliza ‘DevExpress Report Designer’ para crear plantillas. Estas plantillas se pueden usar para enviar notificaciones o crear documentos.

- Después de crear una nueva plantilla, se abre la ventana de edición. Aquí es donde puede agregar y personalizar elementos visuales a su plantilla, y hacer enlaces a las propiedades de su plantilla.
<br>

## Configuraciones SMTP

El servicio de correo se utiliza para enviar notificaciones a través de SMTP.

Recomendaciones para usar un servidor SMTP:

- **Durante el Desarrollo**: Se recomienda utilizar un servidor SMTP corporativo o servicios de software compartido como [sendinblue.com](http://www.sendinblue.com/). Evite usar un servidor personal para no caer en spam.
- **Para Uso Industrial**: Es preferible utilizar un servicio SMTP corporativo o comercial de pago.

Configure los siguientes ajustes para el servicio de correo:

| Campo de Configuración | Opciones de Valor | Propósito |
| ---------------------- | ------------------ | --------- |
| `Sender`      | -                  | Nombre del remitente predeterminado, por ejemplo `sender@company.com` |
| `User name`      | -                  | Inicio de sesión para el servidor SMTP, generalmente en el formato `user@company.com`. |
| `Password`      | -                  | Contraseña del servidor SMTP |
| `Host`      | -                  | Dirección del servidor SMTP, por ejemplo `http://smtp-relay.sendinblue.com/` |
| `Port`      | -                  | El puerto para el servidor SMTP depende del proveedor, por ejemplo 587 para sendinblue.com |
| `Enable SSL`      | `true`, `false` | Uso de SSL para cifrar datos. ‘True’ se utiliza generalmente para servidores SMTP modernos. |

<br>

### Ejemplo de uso de Plantilla y SMTP

1. Cree y personalice una plantilla.
2. Configure SMTP para enviar correos electrónicos.
3. En su flujo de trabajo, agregue el paso ‘Enviar Notificación con Plantilla’.
4. Seleccione el tipo de notificación SMTP y configure los parámetros para enviar el correo electrónico.
5. Elija su plantilla y establezca el tipo de renderizado en HTML.

Después de completar estos pasos, su flujo de trabajo enviará un correo electrónico utilizando la plantilla personalizada.