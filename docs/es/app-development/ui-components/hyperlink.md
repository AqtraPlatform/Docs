# Hipervínculo

![](../../assets/images/app-development/hyperlink.png)

## Información general
El hipervínculo en la Plataforma es un componente de front-end para crear hipervínculos. Permite a los usuarios navegar fácilmente entre diferentes partes de la aplicación o hacia recursos externos, asegurando una navegación eficiente e intuitiva.

## Parámetros
**Propiedades del componente**

| Grupo de configuraciones | Campo de configuración | Opciones de valor | Propósito |
| --- | --- | --- | --- |
|  | Nombre | - | Nombre del componente de UI en el sistema |
| Común | Etiqueta | - | Contiene el nombre del contenedor de texto |
|  | Vinculación | Multiselección de Catálogo | Contiene un campo “Uri” relacionado del modelo |
|  | Valor | - | Permite especificar un valor estático para el campo, utilizado para especificar un enlace |
| Texto | Tamaño de fuente | - | La propiedad determina el tamaño de la fuente |
|  | Color | - | Un módulo en CSS que trabaja con colores, tipos de color y transparencia. |
|  | Negrita | true, false | Propiedad que permite hacer el texto en negrita |
|  | Cursiva | true, false | Propiedad que permite poner el texto en cursiva |
|  | Alineación del texto | Izquierda, Derecha, Centro, Justificar | La propiedad se utiliza para establecer la alineación horizontal del texto |

**Propiedades de CSS**

| Grupo de configuraciones | Campo de configuración | Opciones de valor | Propósito |
| --- | --- | --- | --- |
| Diseño | Ancho | - | Ancho del componente |
|  | Altura | - | Altura del componente |
|  | Crecimiento | true, false | La propiedad determina cuánto crecerá un elemento en relación con el resto de los elementos flex dentro del mismo contenedor |
|  | Margen | - | La propiedad define los rellenos exteriores en los cuatro lados del elemento |
|  | Relleno | - | La propiedad establece los rellenos internos en todos los lados del elemento |
| Apariencia | Radio de esquina | - | La propiedad se utiliza para redondear las esquinas de un elemento |
|  | Grosor del borde | - | La propiedad permite establecer los límites para el elemento |
| Brocha | Fondo | - | La propiedad establece el color de fondo del elemento |
|  | Brocha de borde | - | La propiedad establece el color del borde del elemento |

## Casos 
- **Navegación del sitio**: Se utiliza para crear enlaces a otras páginas de la aplicación o sitios web externos, mejorando la interfaz de usuario.
- **Mejora de la experiencia del usuario**: Proporciona acceso fácil a recursos e información importantes, mejorando la experiencia del usuario con la aplicación.

## Excepciones
- **Limitaciones de funcionalidad**: Un hipervínculo puede tener interoperabilidad limitada al ofrecer solo funcionalidad básica de clic.
- **Dependencia del contexto**: Es importante considerar el contexto en el que se utilizan los enlaces para asegurar una navegación efectiva y evitar malentendidos.