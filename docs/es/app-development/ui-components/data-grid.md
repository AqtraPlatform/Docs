# Data Grid

![](../../assets/images/app-development/data-grid.png)

## Información general
Data Grid es un potente componente de UI diseñado para mostrar e interactuar con grandes cantidades de datos en forma tabular. Este componente es ideal para presentar datos en filas y columnas, así como para proporcionar funcionalidad de ordenación y filtrado.

## Parámetros
**Propiedades del Componente:**

| Grupo de configuraciones | Campo de configuración | Opciones de valor        | Propósito                          |
|-------------------------|------------------------|--------------------------|-------------------------------------|
| (Configuraciones globales) | Nombre                | -                        | Nombre del Componente de UI en el sistema   |
|                         | Columnas              | -                        | Definición de columnas y sus propiedades   |
|                         | Componente            | Multiselección de Catálogo | Contiene una lista de todos los Componentes |
|                         | Filtros estáticos     | Botón                  | Se utiliza para especificar filtros estáticos |
|                         | Filtros dinámicos     | Botón                  | La propiedad se utiliza para especificar filtros dinámicos |
|                         | Tamaño de página      | -                        | Tamaño de la página                     |
|                         | Recarga manual        | -                        | Recarga manual de datos          |
|                         | Modo de selección     | ninguno, único, múltiple, casilla de verificación | Modo de selección de ítems          |
|                         | ID de automatización   | -                        | ID para automatización     |
| Eventos                 | Al cargar la fuente de datos | - | Evento de carga de la fuente de datos |
|                         | Al seleccionar filas   | -             | Evento de selección de filas |
|                         | Al cargar             | -      | Evento de carga del componente |
|                         | Al cambiar la tabla    | -        | Evento de cambio de tabla |
|                         | Al cambiar el encabezado | -      | Evento de cambio de encabezado |
|                         | Al cambiar la fila     | -         | Evento de cambio de fila |
|                         | Al cambiar la celda    | -         | Evento de cambio de celda |

**Propiedades CSS:**

| Grupo de configuraciones | Campo de configuración | Opciones de valor        | Propósito                          |
|-------------------------|------------------------|--------------------------|-------------------------------------|
| Diseño                  | Ancho                  | -                        | Ancho del componente                   |
|                         | Alto                   | -                        | Alto del componente                   |
|                         | Margen                 | -                        | Relleno exterior                      |
|                         | Relleno               | -                        | Relleno interior                   |
|                         | Visible                | -                        | Visibilidad del componente                |
|                         | Oculto                 | -                        | Ocultando un Componente                  |
| Apariencia              | Radio de esquina       | -                        | Radio de esquina                   |
|                         | Grosor del borde       | -                        | Grosor del borde                       |
| Brocha                  | Fondo                  | -                        | Color de fondo                           |
|                         | Brocha del borde       | -                        | Color del borde                          |

**Modelo de Configuración de DataGrid**

Los siguientes ajustes se utilizan para modificar las columnas del componente de UI DataGrid: 

| Campo de configuración | Opciones de valor                           | Propósito                                              |
|-----------------------|--------------------------------------------|---------------------------------------------------------|
| Valor de traducción   | -                                          | Encabezado de columna                                       |
| Mostrar encabezado    | true, false                                | Esta propiedad permite personalizar la visualización del encabezado de la columna |
| Ordenable             | true, false                                | La propiedad permite configurar la capacidad de ordenar la tabla por la columna seleccionada |
| Filtrable             | true, false                                | Esta propiedad permite configurar la capacidad de filtrar la tabla por la columna seleccionada |
| Visible               | true, false                                | La propiedad determina la visibilidad de la columna                   |
| Texto plano           | true, false                                | Propiedad para mostrar una columna como texto plano    |
| Ancho                 | -                                          | Ancho de la columna en la tabla                                |
| Formato de visualización | -                                      | Formato de visualización de datos de la columna                       |
| Icono                 | Disponible solo para Editar registro, Abrir aplicación | Una propiedad que contiene una selección de iconos disponibles         |
| Tipo de comando       | Abrir aplicación, Editar registro             | La propiedad permite seleccionar la acción que se realizará al hacer clic en la columna |
| Agregar campo         | Botón                                     | La propiedad permite agregar campos para la salida en la columna   |

## Casos
- **Visualización de Datos**: Ideal para mostrar datos en una forma tabular fácil de entender.
- **Paneles Administrativos**: Ampliamente utilizado en interfaces de gestión para ver y editar datos.
- **Aplicaciones de Análisis**: Permite analizar y ordenar grandes cantidades de información.

## Excepciones
- **Visualización Limitada**: Data Grid no es adecuado para visualizaciones de datos complejas como gráficos o tablas.
- **Procesamiento de Datos**: El componente está diseñado para mostrar datos, no para procesar o calcular datos.