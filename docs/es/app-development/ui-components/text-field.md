# Campo de texto

![](../../assets/images/app-development/text-field.png)

## Información general
“Campo de texto” es un componente de UI diseñado para mostrar y configurar la entrada y salida de texto.

## Parámetros
**Propiedades del componente**

| Grupo de configuraciones | Campo de configuración | Opciones de valor | Propósito |
| --- | --- | --- | --- |
|  | Nombre | - | Nombre del componente de UI en el sistema |
| Común | Deshabilitado | true, false | La propiedad permite deshabilitar un elemento en el formulario |
|  | Requerido | true, false | La propiedad hace que el elemento sea obligatorio para ser completado antes de enviar el formulario |
|  | Etiqueta | - | Contiene la tabla de contenido del contenedor de texto |
|  | Vínculo | Multiselección de Catálogo | Contiene un campo “String” relacionado del modelo |
| Eventos | Al cambiar el valor | - | Permite ejecutar el script especificado después de cambiar el valor del campo |
| Índice de tabulación |  | Entero positivo comenzando desde cero | Establece el orden en el que los campos activos (editables) se alternan a través del teclado (por ejemplo, usando la tecla Tab) |

**Propiedades CSS**

| Grupo de configuraciones | Campo de configuración | Opciones de valor | Propósito |
| --- | --- | --- | --- |
| Diseño | Ancho | - | Ancho del componente |
|  | Alto | - | Alto del componente |
|  | Crecer | true, false | La propiedad determina cuánto crecerá un elemento en relación con el resto de los elementos flexibles dentro del mismo contenedor |
|  | Margen | - | La propiedad define los rellenos exteriores en los cuatro lados del elemento |
|  | Relleno | - | La propiedad establece los rellenos interiores en todos los lados del elemento |
| Apariencia | Radio de esquina | - | La propiedad se utiliza para redondear las esquinas de un elemento |
|  | Grosor del borde | - | La propiedad permite establecer los límites para el elemento |
| Brocha | Fondo | - | La propiedad establece el color de fondo del elemento |
|  | Brocha del borde | - | La propiedad establece el color del borde del elemento |

## Casos
- **Formularios de entrada de datos**: Utilizados para recopilar información de texto de los usuarios.
- **Configuraciones de interfaz**: Proporciona una interfaz de usuario para ingresar o modificar texto.

## Excepciones
- **Funcionalidad limitada**: Adecuado solo para entrada de texto.