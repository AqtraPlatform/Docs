# Extracción de colección

![](../../assets/images/app-development/extract-collection.png)

## Información general
El paso “Extracción de Colección” se utiliza para convertir un campo de matriz en una lista plana. Este campo se puede obtener ya sea de una fuente externa o de un campo (propiedad) de un componente de matriz.

En este paso, la matriz se analiza y el procesamiento de cada elemento de la matriz (entrada u objeto) se inicia como un flujo de datos interno separado. Cada uno de estos hilos se ejecuta de manera independiente entre sí. Los flujos de datos analizados utilizando el paso “Extracción de Colección” se pueden reensamblar a través del paso “Agrupar por”.

## Parámetros
**Configuración del paso:**

| Campo de configuración | Opciones de valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso fuente            | -                 | Selección del paso anterior |
| Ruta del modelo        | -                 | Ruta a un campo de matriz en el modelo de datos |

## Casos
- **Procesamiento de matriz de datos**: Se utiliza para extraer y procesar cada elemento de la matriz de datos de manera independiente.
- **División y agrupación posterior**: Adecuado para escenarios donde necesitas dividir estructuras de datos complejas en elementos más simples para un procesamiento y análisis posterior.

## Excepciones
- **Necesidad de especificar la fuente y la ruta exactas**: La indicación incorrecta de la fuente o la ruta al campo de matriz puede llevar a errores en el procesamiento de datos.

## Escenario de aplicación

Este componente permite procesar datos de almacén de clientes añadiendo nuevos registros utilizando los pasos **extracción de colección** y **ejecutar script**. Después de la ejecución del flujo de datos, cada registro recibe datos de campo adicionales.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/1Q1czyILIGHc7tVwPYpkgHIFfI87p5WvQ/view?usp=sharing).