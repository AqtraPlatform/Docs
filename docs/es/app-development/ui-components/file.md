# Archivo

![](../../assets/images/app-development/file.png)

## Información general
El componente “Archivo” proporciona la capacidad de cargar y mostrar archivos en la interfaz de usuario. Este componente es útil para subir y visualizar diferentes tipos de archivos, como imágenes, documentos, archivos comprimidos, etc.

## Parámetros
**Propiedades del componente**

| Grupo de configuraciones | Campo de configuración | Opciones de valor | Propósito |
| --- | --- | --- | --- |
|  | Nombre | - | Nombre del componente de la interfaz de usuario en el sistema |
| Común | Tamaño máximo del archivo en bytes | - | La propiedad permite especificar el tamaño máximo del archivo subido en bytes |
|  | Aceptar archivos |  | La propiedad permite especificar los archivos que están disponibles para descargar |
|  | Solo lectura | true, false | Esta propiedad permite deshabilitar la carga de archivos en formularios |
|  | Deshabilitado | true, false | La propiedad permite deshabilitar un elemento en el formulario |
|  | Requerido | true, false | La propiedad hace que el elemento sea obligatorio para ser completado antes de enviar el formulario |
|  | Etiqueta | - | Contiene la tabla de contenido del contenedor de texto |
|  | Valor | - | - |
|  | Vinculación | Opción múltiple: Catálogo | Referencia al Catálogo de tipo de archivo |
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
- **Carga de documentos**: Permite a los usuarios cargar documentos, imágenes y otros archivos.
- **Ver información del archivo:** Muestra información sobre el archivo subido, como su nombre y tamaño.

## Excepciones
- **Rendimiento**: Descargar archivos grandes o un gran número de archivos puede afectar el rendimiento.