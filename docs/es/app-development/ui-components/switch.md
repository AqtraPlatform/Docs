# Interruptor

![](../../assets/images/app-development/switch.png)

## Información general
El componente “Interruptor” es un elemento de interfaz que permite al usuario habilitar o deshabilitar una función, opción o estado específico. Este componente se utiliza a menudo para proporcionar la capacidad de cambiar rápidamente entre dos estados (Verdadero/Falso).

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

**Propiedades CSS**

| Grupo de configuraciones | Campo de configuración | Opciones de valor | Propósito |
| --- | --- | --- | --- |
| Diseño | Ancho | - | Ancho del componente |
|  | Alto | - | Alto del componente |
|  | Crecer | true, false | La propiedad determina cuánto crecerá un elemento en relación con el resto de los elementos flexibles dentro del mismo contenedor |
|  | Margen | - | La propiedad define los rellenos exteriores en los cuatro lados del elemento |
|  | Relleno | - | La propiedad establece los rellenos internos en todos los lados del elemento |
| Apariencia | RadioEsquinas | - | La propiedad se utiliza para redondear las esquinas de un elemento |
|  | GrosorBorde | - | La propiedad permite establecer los límites para el elemento |
| Brocha | Fondo | - | La propiedad establece el color de fondo del elemento |
|  | BrochaBorde | - | La propiedad establece el color del borde del elemento |.

## Casos 
- **Selección Binaria:** El interruptor se utiliza para selecciones binarias como encender/apagar sonido, notificaciones y otras opciones.
- **Gestión de Estado:** Puedes usar el interruptor para gestionar el estado de un elemento de interfaz particular.

## Excepciones
- **Estado Poco Claro:** Si no está claro lo que significan los estados habilitado y deshabilitado, los usuarios pueden confundirse.