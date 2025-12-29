# Día

![](../../assets/images/app-development/day.png)

## Información general
Día es un componente de UI diseñado para mostrar o seleccionar días individuales. Este elemento se utiliza comúnmente en calendarios o sensores de fecha, permitiendo al usuario seleccionar días específicos para completar tareas o establecer recordatorios.

## Parámetros
**Propiedades del componente**

| Grupo de configuraciones | Campo de configuración | Opciones de valor | Propósito |
| --- | --- | --- | --- |
|  | Nombre | - | Nombre del componente de UI en el sistema |
| Común | Formato | - | La propiedad permite [configurar](https://docs.microsoft.com/ru-ru/dotnet/standard/base-types/custom-date-and-time-format-strings) la visualización de fecha y hora |
|  | Deshabilitado | true, false | La propiedad permite deshabilitar un elemento en el formulario |
|  | Requerido | true, false | La propiedad hace que el elemento sea obligatorio para ser completado antes de enviar el formulario |
|  | Etiqueta | - | Contiene la tabla de contenido del contenedor de texto |
|  | Vinculación | Multiselección de Catálogo | Contiene un campo de “Fecha” relacionado del modelo |
| Eventos | Al cambiar el valor | - | Permite ejecutar el script especificado después de cambiar el valor del campo |

**Propiedades CSS**

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
- **Selector de fecha**: Utilizado para seleccionar días específicos en interfaces donde se requiere una selección precisa de fechas.
- **Visualización de eventos**: Puede ser utilizado para mostrar eventos o recordatorios programados para días específicos.

## Excepciones
- **Funcionalidad limitada**: El componente Día está limitado a mostrar y seleccionar días, y no es adecuado para mostrar intervalos de tiempo más amplios.