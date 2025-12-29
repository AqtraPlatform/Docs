# SVG

![](../../assets/images/app-development/svg.png)

## Información general
SVG (Scalable Vector Graphics) es un componente para integrar gráficos vectoriales en interfaces de usuario. Permite mostrar imágenes, lo que lo hace ideal para íconos, diagramas e ilustraciones complejas.

## Parámetros
**Propiedades del componente**

| Grupo de configuraciones | Campo de configuración | Opciones de valor | Propósito |
| --- | --- | --- | --- |
|  | Nombre | - | Nombre del componente de UI en el sistema |
| Común | Vinculación | Multiselección de Catálogo | Contiene un campo “Archivo” relacionado del modelo |
|  | Archivo | Botón | Permite cargar un archivo con una extensión .svg |

**Propiedades de CSS**

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

## Casos de uso
- **Íconos e Ilustraciones**: Se utiliza para agregar elementos gráficos claros y escalables.

## Excepciones
- **Rendimiento**: Imágenes SVG complejas o grandes pueden afectar el rendimiento de la página web.