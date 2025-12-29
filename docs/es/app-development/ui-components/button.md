# Botón

![](../../assets/images/app-development/button.png)

## Información general
Un Botón es el componente principal de la interfaz de usuario utilizado para ejecutar comandos o iniciar acciones en una aplicación. Se puede configurar para ejecutar procesos, confirmar acciones del usuario o servir como herramienta de navegación.

## Parámetros
**Propiedades del Componente:**

| Grupo de configuraciones | Campo de configuración | Opciones de valor         | Propósito |
|-------------------------|-----------------------|---------------------------|------------|
| (Configuraciones globales) | Nombre                | -                         | Nombre del Componente de la UI en el sistema |
| Común                   | Icono                 | -                         | Carga de icono (.svg) |
|                         | Deshabilitado         | true, false               | Deshabilitar un elemento |
|                         | Etiqueta              | -                         | Texto del botón |
| Texto                   | Tamaño de fuente      | -                         | Tamaño de la fuente |
|                         | Color                 | -                         | Color del texto (CSS) |
|                         | Negrita               | true, false               | Fuente en negrita |
|                         | Cursiva              | true, false               | Fuente en cursiva |
|                         | Alineación del texto  | Izquierda, Derecha, Centro, Justificar | Alineación del texto |
| Acciones                | Tipo de comando       | Varios comandos           | Acción al hacer clic en el botón |
|                         | Restringir acceso     | true, false               | Limitación de acceso |

**Propiedades CSS:**

| Grupo de configuraciones | Campo de configuración | Opciones de valor         | Propósito |
|-------------------------|-----------------------|---------------------------|------------|
| Diseño                  | Ancho                 | -                         | Ancho del componente |
|                         | Alto                  | -                         | Alto del componente |
|                         | Crecer                | true, false               | Estiramiento del componente |
|                         | Margen                | -                         | Relleno exterior |
|                         | Relleno              | -                         | Relleno interior |
| Apariencia              | Radio de esquina      | -                         | Radio de esquina |
|                         | Grosor del borde      | -                         | Grosor del borde |
| Brocha                  | Fondo                 | -                         | Color de fondo |
|                         | Brocha del borde      | -                         | Color del borde |

## Casos
- **Envío de Formulario**: Uso de un botón para enviar datos de formulario al servidor o para iniciar el procesamiento de datos de formulario en la aplicación.
- **Navegación**: Asignación de un botón para navegar entre diferentes pantallas o secciones de la aplicación.
- **Elementos Interactivos**: Creación de botones para controlar elementos interactivos, como cambiar contenido en una página.

## Excepciones
- **Limitaciones en el Número de Acciones**: Solo se puede asignar una acción a un botón (ejecutar flujo de datos, ejecutar script, etc.).