# Número

![](../../assets/images/app-development/number.png)

## Información general
El componente “Número” es una interfaz para ingresar valores numéricos. Este componente permite a los usuarios ingresar números y puede ser utilizado para diversos propósitos, como ingresar números, cantidades u otros datos numéricos.

## Parámetros
**Propiedades del componente**

| Grupo de configuraciones | Campo de configuración | Opciones de valor | Propósito |
| --- | --- | --- | --- |
|  | Nombre | - | Nombre del componente de UI en el sistema |
| Común | Deshabilitado | true, false | La propiedad permite deshabilitar un elemento en el formulario |
|  | Requerido | true, false | La propiedad hace que el elemento sea obligatorio para ser completado antes de enviar el formulario |
|  | Etiqueta | - | Contiene la tabla de contenido del contenedor de texto |
|  | Vinculación | Multiselección de Catálogo | Contiene el campo “Entero” y “Número” asociado del modelo |
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
- **Ingreso de valores numéricos:** Los usuarios pueden ingresar números en el componente Número, como cantidades de productos o parámetros numéricos.
- **Límite de rango:** Los valores mínimo y máximo permiten limitar los números que se ingresan a un rango específico.
- **Cambiar número usando flechas:** Los usuarios pueden aumentar o disminuir un número utilizando las flechas hacia arriba y hacia abajo.

## Excepciones
- **Ingreso de datos no numéricos:** Solo se pueden ingresar datos numéricos.