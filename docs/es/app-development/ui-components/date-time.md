# Fecha / Hora

![](../../assets/images/app-development/date-time.png)

## Información general
Fecha/Hora es un componente de UI para ingresar y mostrar la fecha y la hora. Está diseñado para proporcionar una interfaz fácil de usar para seleccionar la fecha/hora, así como para mostrar estos datos en un formato específico.

## Parámetros
**Propiedades del Componente:**

| Grupo de configuraciones | Campo de configuración | Opciones de valor         | Propósito                 |
|-------------------------|------------------------|---------------------------|----------------------------|
| (Configuraciones globales) | Nombre                 | -                         | Nombre del Componente de UI en el sistema |
| Fecha Hora              | Formato                | Fecha, Hora, Fecha y Hora | Formato de visualización  |
|                         | Valor predeterminado   | -                         | Valor predeterminado      |
|                         | Fecha mínima           | -                         | Fecha mínima              |
|                         | Fecha máxima           | -                         | Fecha máxima              |
| Común                   | Vinculación            | -                         | Vinculación a Datos       |
|                         | Requerido              | true, false               | Requerido para completar   |

**Propiedades CSS:**

| Grupo de configuraciones | Campo de configuración | Opciones de valor         | Propósito                 |
|-------------------------|------------------------|---------------------------|----------------------------|
| Diseño                  | Ancho                  | -                         | Ancho del componente       |
|                         | Alto                   | -                         | Alto del componente        |
|                         | Margen                 | -                         | Relleno exterior           |
|                         | Relleno               | -                         | Relleno interior           |
| Apariencia              | Radio de esquina       | -                         | Radio de esquina           |
|                         | Grosor del borde       | -                         | Grosor del borde           |
| Brocha                  | Fondo                  | -                         | Color de fondo             |
|                         | Brocha del borde       | -                         | Color del borde            |

## Casos
- **Selección de Fecha del Evento**: Utilizado para seleccionar una fecha en el calendario o para establecer la hora del evento.
- **Filtrar por Fecha**: Puede ser utilizado en filtros para filtrar datos por fecha/hora.
- **Mostrar Intervalos de Tiempo**: Adecuado para tareas que implican mostrar intervalos de tiempo, como en programadores de trabajos.

## Excepciones
- **Formato**: Fecha/Hora no está destinado para la entrada de texto libre, sino que se utiliza estrictamente para trabajar con fechas y horas.