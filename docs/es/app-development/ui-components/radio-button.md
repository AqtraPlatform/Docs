# Botón de radio

![](../../assets/images/app-development/radio-button.png)

## Información general
El componente “Botón de Radio” es un elemento de interfaz que permite al usuario seleccionar una de las opciones proporcionadas. Este componente se utiliza para implementar la selección de un solo elemento de varias opciones mutuamente exclusivas.

## Parámetros
**Propiedades del componente**

| Grupo de configuraciones | Campo de configuración | Opciones de valor | Propósito |
| --- | --- | --- | --- |
|  | Nombre | - | Nombre del componente de UI en el sistema |
| Común | Deshabilitado | true, false | La propiedad permite deshabilitar un elemento en el formulario |
|  | Requerido | true, false | La propiedad hace que el elemento sea obligatorio para ser completado antes de enviar el formulario |
|  | Etiqueta | - | Contiene la tabla de contenido del contenedor de texto |
|  | Vínculo | Multiselección de Catálogo | Contiene un campo “Catálogo” relacionado del modelo |
| Eventos | Al cambiar el valor | - | Permite ejecutar el script especificado después de cambiar el valor del campo |
|  | Al enfocar |  | Permite ejecutar el script especificado al enfocar |

**Propiedades CSS**

| Grupo de configuraciones | Campo de configuración | Opciones de valor | Propósito |
| --- | --- | --- | --- |
| Diseño | Ancho | - | Ancho del componente |
|  | Alto | - | Alto del componente |
|  | Crecer | true, false | La propiedad determina cuánto crecerá un elemento en relación con el resto de los elementos flex dentro del mismo contenedor |
|  | Margen | - | La propiedad define los rellenos exteriores en los cuatro lados del elemento |
|  | Relleno | - | La propiedad establece los rellenos internos en todos los lados del elemento |
| Apariencia | Radio de esquina | - | La propiedad se utiliza para redondear las esquinas de un elemento |
|  | Grosor del borde | - | La propiedad permite establecer los límites para el elemento |
| Brocha | Fondo | - | La propiedad establece el color de fondo del elemento |
|  | Brocha del borde | - | La propiedad establece el color del borde del elemento |

## Casos
- **Selección de Opción Única:** Los usuarios solo pueden seleccionar una opción de la lista.
- **Opciones Mutuamente Exclusivas:** El componente Botón de Radio se utiliza para crear un conjunto de opciones mutuamente exclusivas de las cuales solo se puede seleccionar una.

## Excepciones
- **Información Insuficiente:** Si las etiquetas de los botones de radio no son suficientemente informativas, los usuarios pueden tener dificultades para seleccionar opciones.
- **Elección Difícil:** Con un gran número de botones de radio o una organización poco clara, la elección puede ser difícil para los usuarios.