# Tiempo

![](../../assets/images/app-development/time.png)

## Información general
El tiempo es un componente de UI diseñado para ingresar y mostrar la hora. Este elemento se utiliza típicamente para establecer la hora de eventos o tareas, y para mostrar la hora en las interfaces de la aplicación.

## Parámetros
**Propiedades del componente**

| Grupo de configuraciones | Campo de configuración | Opciones de valor | Propósito |
| --- | --- | --- | --- |
|  | Nombre | - | Nombre del componente de UI en el sistema |
| Común | Deshabilitado | true, false | La propiedad permite deshabilitar un elemento en el formulario |
|  | Requerido | true, false | La propiedad hace que el elemento sea obligatorio para ser completado antes de enviar el formulario |
|  | Etiqueta | - | Contiene la tabla de contenido del contenedor de texto |
|  | Vínculo | Multiselección de Catálogo | Contiene un campo relacionado de “Tiempo” del modelo |
| Eventos | Al cambiar el valor | - | Permite ejecutar el script especificado después de cambiar el valor del campo |

**Propiedades de CSS**

| Grupo de configuraciones | Campo de configuración | Opciones de valor | Propósito |
| --- | --- | --- | --- |
| Diseño | Ancho | - | Ancho del componente |
|  | Alto | - | Alto del componente |
|  | Crecer | true, false | La propiedad determina cuánto crecerá un elemento en relación con el resto de los elementos flexibles dentro del mismo contenedor |
|  | Margen | - | La propiedad define los rellenos exteriores en los cuatro lados del elemento |
|  | Relleno | - | La propiedad establece los rellenos internos en todos los lados del elemento |
| Apariencia | Radio de esquina | - | La propiedad se utiliza para redondear las esquinas de un elemento |
|  | Grosor del borde | - | La propiedad permite establecer los límites para el elemento |
| Brocha | Fondo | - | La propiedad establece el color de fondo del elemento |
|  | Brocha del borde | - | La propiedad establece el color del borde del elemento |

## Casos
- **Configuración de tiempo**: Se utiliza para establecer una hora específica en programadores y calendarios.
- **Entrada de tiempo**: Proporciona una interfaz para que el usuario ingrese tiempo para diversos propósitos.

## Excepciones
- **Formato de tiempo**: Debe estar consciente de las restricciones de formato de tiempo establecidas en la configuración del componente.
- **Solo tiempo**: El componente de Tiempo está limitado a mostrar e ingresar solo la hora, sin fechas.