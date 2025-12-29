# Visor de PDF

![](../../assets/images/app-development/pdf-viewer.png)

## Información general
El componente Visor de PDF permite ver e interactuar con documentos PDF directamente en la interfaz de usuario. Este componente es útil para mostrar archivos PDF como informes, instrucciones y otros documentos.

## Parámetros
**Propiedades del componente**

| Grupo de configuraciones | Campo de configuración | Opciones de valor | Propósito |
| --- | --- | --- | --- |
|  | Nombre | - | Nombre del componente de la interfaz de usuario en el sistema |
| Común | Vinculación | Multiselección de Catálogo | Contiene un campo “Archivo” relacionado del modelo |
|  | Archivo | Botón | Permite cargar un archivo con una extensión .pdf |

**Propiedades CSS**

| Grupo de configuraciones | Campo de configuración | Opciones de valor | Propósito |
| --- | --- | --- | --- |
| Diseño | Ancho | - | Ancho del componente |
|  | Alto | - | Alto del componente |
|  | Crecimiento | true, false | La propiedad determina cuánto crecerá un elemento en relación con el resto de los elementos flexibles dentro del mismo contenedor |
|  | Margen | - | La propiedad define los rellenos exteriores en los cuatro lados del elemento |
|  | Relleno | - | La propiedad establece los rellenos internos en todos los lados del elemento |
| Apariencia | RadioDeEsquina | - | La propiedad se utiliza para redondear las esquinas de un elemento |
|  | GrosorDelBorde | - | La propiedad permite establecer los límites para el elemento |
| Brocha | Fondo | - | La propiedad establece el color de fondo del elemento |
|  | BrochaDelBorde | - | La propiedad establece el color del borde del elemento |

## Casos
- **Visualización de Informes:** Permite a los usuarios ver informes y documentación en formato PDF.

## Excepciones
- **Limitaciones de Formato:** El Visor de PDF admite documentos PDF estándar, pero puede no mostrar correctamente formatos complejos o documentos protegidos.
- **Rendimiento:** Usar documentos PDF grandes o un gran número de elementos interactivos puede afectar el rendimiento.