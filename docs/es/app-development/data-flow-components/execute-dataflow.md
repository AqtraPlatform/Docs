# Ejecutar flujo de datos

![](../../assets/images/app-development/execute-dataflow.png)

## Información general
El paso Ejecutar Flujo de Datos se utiliza para llamar a Dataflow desde cualquier componente publicado. Este paso te permite ejecutar un flujo de datos adicional en el contexto del proceso actual de procesamiento de datos.

Cuando se utiliza con un campo de matriz obtenido de una fuente externa o de un campo de matriz (propiedad), el paso analiza esta matriz y comienza el procesamiento paralelo de cada registro u objeto contenido en la matriz.

## Parámetros
**Configuración del paso:**

| Campo de configuración | Opciones de valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso fuente            | -                 | Selección del paso anterior |
| Componente             | -                 | El componente desde el cual se llama a Dataflow |
| Flujo de datos         | -                 | Nombre del flujo de datos a ejecutar |
| Campo de almacenamiento de resultados | - | Campo para guardar el resultado de la ejecución del flujo de datos |

## Casos
- **Actualización de datos de otros flujos de datos**: El paso “Ejecutar Flujo de Datos” es ideal para situaciones en las que deseas actualizar campos en el modelo actual con datos recopilados o procesados en otros flujos de datos. Esto hace posible integrar y sincronizar datos de manera efectiva entre diferentes procesos y componentes.
- **Llamada a flujo de datos externo**: Se utiliza para integrar y lanzar flujos de datos adicionales como parte del proceso actual de procesamiento de datos.

## Excepciones
- **Dependencia de la corrección de otros flujos de datos**: La efectividad del paso “Ejecutar Flujo de Datos” depende directamente de la precisión y fiabilidad de los datos obtenidos de otros flujos de datos. Todos los flujos de datos relacionados deben configurarse y probarse cuidadosamente para garantizar que los datos actualizados sean correctos y estén actualizados.

## Escenario de aplicación

Este componente crea un flujo de datos para realizar operaciones sobre los datos del componente actual. Incluye pasos de modelo de acción Obtener para recuperar el modelo de flujo de datos y pasos de ejecutar flujo de datos para ejecutar el flujo de datos con parámetros apropiados, como seleccionar el componente actual, elegir el flujo de datos a ejecutar, configurar campos de resultados y mostrar definiciones del componente de datos. Este componente permite operaciones de datos en el componente directamente desde la interfaz de la aplicación.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/1ekmRNTRgO30koKm04pyhEZsXG9W5T-O-/view?usp=sharing).