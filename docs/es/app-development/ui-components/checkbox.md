# Checkbox

![](../../assets/images/app-development/checkbox.png)

## Información general
Un “Checkbox” es un elemento de interfaz que permite a los usuarios seleccionar o deseleccionar un parámetro u opción específica. Este componente se utiliza ampliamente para crear listas de parámetros, gestionar configuraciones o seleccionar múltiples opciones a la vez.

## Parámetros
**Propiedades del componente**

| Grupo de configuraciones | Campo de configuración | Opciones de valor | Propósito |
| --- | --- | --- | --- |
|  | Nombre | - | Nombre del componente de UI en el sistema |
| Común | Deshabilitado | true, false | La propiedad permite deshabilitar un elemento en el formulario |
|  | Requerido | true, false | La propiedad hace que el elemento sea obligatorio para ser completado antes de enviar el formulario |
|  | Etiqueta | - | Contiene la tabla de contenido del contenedor de texto |
|  | Vínculo | Multiselección de Catálogo | Contiene un campo “Booleano” relacionado del modelo |
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
|  | Brocha de borde | - | La propiedad establece el color del borde del elemento |

## Casos
- **Selección de opciones**: Los usuarios pueden seleccionar o deseleccionar ciertos parámetros u opciones.
- **Gestión de configuraciones**: El Checkbox se utiliza para habilitar o deshabilitar ciertas configuraciones o características.
- **Selección múltiple**: En el grupo de Checkbox, los usuarios pueden seleccionar múltiples opciones al mismo tiempo.

## Excepciones
- **Interfaz poco intuitiva:** Con un gran número de checkboxes en una página o en formularios complejos, los usuarios pueden tener dificultades para elegir opciones.
- **Formulaciones poco claras:** Si las formulaciones del Checkbox no son informativas o son confusas, los usuarios pueden no entender qué están eligiendo.