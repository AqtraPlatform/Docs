# Etiqueta

![](../../assets/images/app-development/label.png)

## Información general
La etiqueta es un componente básico de la interfaz de usuario diseñado para mostrar campos de texto no editables en capturas de pantalla. Este componente se utiliza ampliamente para agregar texto descriptivo, títulos o simplemente mostrar información que el usuario no puede cambiar.

## Parámetros
**Propiedades del componente:**

| Grupo de configuraciones | Campo de configuración | Opciones de valor         | Propósito |
|-------------------------|-----------------------|---------------------------|------------|
| (Configuraciones globales) | Nombre                | -                         | Nombre del componente de la interfaz de usuario en el sistema |
| Texto                   | Tamaño de fuente      | -                         | Tamaño de la fuente |
|                         | Color                 | -                         | Color del texto (CSS) |
|                         | Negrita               | true, false               | Fuente en negrita |
|                         | Cursiva               | true, false               | Fuente en cursiva |
|                         | Alineación de texto   | Izquierda, Derecha, Centro, Justificar | Alineación del texto |
| Común                   | Vinculación           | Multiselección de Catálogo | Vinculación a Datos |
|                         | Valor                 | -                         | Valor del campo estático |
|                         | Formato               | -                         | Formato de entrada/salida de datos (Para DataTime) |

**Propiedades CSS:**

| Grupo de configuraciones | Campo de configuración | Opciones de valor         | Propósito |
|-------------------------|-----------------------|---------------------------|------------|
| Diseño                  | Alinear elementos      | Ninguno, Centro, Fin, Inicio, Estirar | Alineación de elementos en un contenedor flex |
|                         | Ancho                 | -                         | Ancho del componente |
|                         | Alto                  | -                         | Alto del componente |
|                         | Crecer                | true, false               | Estiramiento de un componente en un contenedor |
|                         | Margen                | -                         | Relleno exterior |
|                         | Relleno              | -                         | Relleno interior |
| Apariencia              | Radio de esquina      | -                         | Radio de esquina |
|                         | Grosor del borde      | -                         | Grosor del borde |
| Brocha                  | Fondo                 | -                         | Color de fondo |
|                         | Brocha del borde      | -                         | Color del borde |

## Casos
- **Consejos de información**: Usar una etiqueta para proporcionar información de apoyo junto a otros elementos de la interfaz de usuario, como explicar las funciones de los botones o la entrada de datos.
- **Encabezados de sección**: Las etiquetas pueden servir como encabezados para diferentes secciones de la interfaz, delimitando claramente el contenido para mejorar la experiencia del usuario.
- **Visualización de estado**: En casos donde es necesario mostrar el estado o resultado de una operación, se puede usar una etiqueta para mostrar los mensajes correspondientes (por ejemplo, “Cargando...”, “Completado con éxito”).

## Excepciones
- **No editabilidad**: La etiqueta no está destinada para la entrada del usuario o la edición de texto. Intentar usarla para estos propósitos resultará en un diseño de interfaz ineficaz.
- **Restricciones de formato**: Si bien la etiqueta permite un cierto nivel de personalización del texto, no puede contener elementos de texto complejos como hipervínculos o imágenes en línea.