# Consultar entidad por filtro

![](../../assets/images/app-development/query-entity-by-filter.png)

## Información general
El paso “Consultar Entidad por Filtro” se utiliza para buscar entradas en un componente específico. A diferencia de los pasos, que utilizan filtros o identificadores para buscar, este paso está diseñado para buscar directamente entradas en un componente.

## Parámetros
**Configuración del paso:**

| Campo de configuración | Opciones de valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso de origen         | -                 | Seleccionar el paso anterior |
| Componente             | -                 | Componente que se está buscando |
| Nombre del campo de destino | -           | Nombre del campo en el que se guardará el resultado de la consulta |

## Casos
- **Búsqueda Directa de Componente**: Se utiliza para buscar directamente entradas en un componente específico.

## Excepciones
- **Dependencia del Componente**: La efectividad del paso está directamente relacionada con la estructura y el contenido de los datos en el componente seleccionado.

## Escenario de aplicación

El flujo de datos demuestra varios escenarios de uso de Consultar Entidad por Filtro para el filtrado de datos. Cada escenario incluye la adición de pasos de Obtener Modelo de Acción y Consultar Entidad por Filtro, llenando campos y aplicando filtros, así como un paso de Escribir Respuesta para la salida de resultados.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/1FBXtSNuk7-KmyGofhghsJJiVrV_xebT1/view?usp=sharing)