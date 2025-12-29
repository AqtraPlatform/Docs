# Select

![](../../assets/images/app-development/select.png)

## Información general
“Select” es un elemento de interfaz que permite al usuario elegir una opción de la lista presentada. Este componente se utiliza ampliamente para crear listas desplegables con una elección de opción o categoría.

## Parámetros
**Propiedades del componente**

| Grupo de configuraciones | Campo de configuración | Opciones de valor | Propósito |
| --- | --- | --- | --- |
|  | Nombre | - | Nombre del componente de UI en el sistema |
| Común | Deshabilitado | true, false | La propiedad permite deshabilitar un elemento en el formulario |
|  | Requerido | true, false | La propiedad hace que el elemento sea obligatorio para ser completado antes de enviar el formulario |
|  | Etiqueta | - | Contiene la tabla de contenido del contenedor de texto |
|  | Vinculación | Multiselección de Catálogo | Contiene un campo “Catálogo” relacionado del modelo |
| Eventos | Al cambiar el valor | - | Permite ejecutar el script especificado después de cambiar el valor del campo |

**Propiedades CSS**

| Grupo de configuraciones | Campo de configuración | Opciones de valor | Propósito |
| --- | --- | --- | --- |
| Diseño | Ancho | - | Ancho del componente |
|  | Alto | - | Alto del componente |
|  | Crecimiento | true, false | La propiedad determina cuánto crecerá un elemento en relación con el resto de los elementos flexibles dentro del mismo contenedor |
|  | Margen | - | La propiedad define los rellenos exteriores en los cuatro lados del elemento |
|  | Relleno | - | La propiedad establece los rellenos internos en todos los lados del elemento |
| Apariencia | Radio de esquina | - | La propiedad se utiliza para redondear las esquinas de un elemento |
|  | Grosor del borde | - | La propiedad permite establecer los límites para el elemento |
| Brocha | Fondo | - | La propiedad establece el color de fondo del elemento |
|  | Brocha del borde | - | La propiedad establece el color del borde del elemento |

## Casos
- **Selección de la lista:** Los usuarios pueden seleccionar una opción de una lista de opciones sugeridas.

## Excepciones
- **Interfaz poco intuitiva:** Si la lista no es intuitiva o comprensible para el usuario, puede causar dificultades al seleccionar una opción.
- **Velocidad de descarga:** Si la lista es demasiado larga, cargar los elementos seleccionados requerirá una espera adicional.