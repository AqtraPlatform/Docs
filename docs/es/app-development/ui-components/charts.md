# Gráficos

![](../../assets/images/app-development/charts.png)

## Información general
“Vista de Gráfico” es un Componente de UI diseñado para mostrar y personalizar la presentación gráfica de datos.

## Parámetros
**Propiedades del componente:**

| Grupo de configuraciones | Campo de configuración | Opciones de valor                          | Propósito                                      |
|--------------------------|------------------------|--------------------------------------------|-------------------------------------------------|
| (Configuraciones globales) | Componente              | -                                          | Selección de un componente a mostrar en el gráfico     |
|                          | Tipo de gráfico        | barra, barra horizontal, pastel, dona, línea | Tipo del gráfico                                     |
|                          | Campo de etiqueta      | -                                          | Campo para etiquetas en el gráfico                      |
|                          | Fuente de datos        | -                                          | Fuente de datos para el gráfico                    |
|                          | Mostrar leyenda        | verdadero, falso                            | Mostrar la leyenda en el gráfico                 |
|                          | Valor máximo del eje Y | -                                          | Valor máximo en el eje Y                 |
|                          | Valor mínimo del eje Y | -                                          | Valor mínimo en el eje Y                  |
|                          | Valor máximo del eje X | -                                          | Valor máximo en el eje X                 |
|                          | Valor mínimo del eje X | -                                          | Valor mínimo en el eje X                  |
|                          | ID de automatización   | -                                          | ID para automatización                |

**Propiedades CSS**

| Grupo de configuraciones | Campo de configuración | Opciones de valor | Propósito |
| --- | --- | --- | --- |
| Diseño | Ancho | - | Ancho del componente |
|      | Alto | - | Alto del componente |
|      | Crecer | verdadero, falso | La propiedad determina cuánto crecerá un elemento en relación con el resto de los elementos flexibles dentro del mismo contenedor |
|      | Margen | - | La propiedad define los rellenos exteriores en los cuatro lados del elemento |
|      | Relleno | - | La propiedad establece los rellenos internos en todos los lados del elemento |
|      | Visible        | verdadero, falso       | Visibilidad del componente    |
|      | Oculto         | verdadero, falso       | Ocultando un componente      |
| Apariencia | Radio de esquina | - | La propiedad se utiliza para redondear las esquinas de un elemento |
|      | Grosor del borde | - | La propiedad permite establecer los límites para el elemento |
| Brocha | Fondo | - | La propiedad establece el color de fondo del elemento |
|      | Brocha del borde | - | La propiedad establece el color del borde del elemento |

**Parámetros de la fuente de datos:**

| Campo de configuración | Opciones de valor | Propósito |
| --- | --- | --- |
| Título | - | Título de la fuente de datos |
| Valor | Opción múltiple
Catálogo | La propiedad permite seleccionar un valor de fuente de datos de los campos Entero y Número |
| Aceptar | Botón | Aplicación de personalización |
| Cancelar | Botón | Cancelación de personalización |

## Casos
- **Visualización de Datos**: Utilizado para crear gráficos y diagramas, permitiendo presentar datos de manera eficiente.
- **Tableros de Análisis**: Adecuado para tableros de análisis que requieren una visualización de estadísticas y métricas.

## Excepciones
- **Uso Especializado**: Limitado a la creación de gráficos y no es adecuado para otros tipos de visualizaciones.