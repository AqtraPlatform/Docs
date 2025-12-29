# Obtener información del archivo

![](../../assets/images/app-development/get-file-info.png)

## Información general
El paso “Obtener Información del Archivo” en Dataflow se utiliza para recuperar información sobre un archivo por su ID. Este paso proporciona acceso a varias propiedades del archivo, incluyendo su nombre, extensión (tipo), tamaño, fecha de actualización, creación y autor del archivo inicial y actualizado.

## Parámetros
**Configuraciones del Paso:**

| Campo de Configuración | Opciones de Valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso de origen         | -                 | Selección del paso anterior |
| Campo de origen        | -                 | Campo que contiene el ID del archivo |
| Nombre del campo de destino | -           | Campo donde se registrará la información sobre el archivo |

## Casos
- **Extracción de Información del Archivo**: Se utiliza para obtener información detallada sobre un archivo, lo que puede ser útil para el procesamiento o análisis de datos posteriores.
- **Preparación de Datos para Procesamiento Adicional**: La información obtenida sobre el archivo puede ser utilizada en pasos posteriores, como “Ejecutar Script” o “Filtrar Fuente”, para realizar operaciones específicas dependiendo de las propiedades del archivo.

## Excepciones
- **Dependencia de la Precisión de la Fuente de Datos**: La precisión de la información obtenida depende de la exactitud y relevancia de los datos en la fuente.
- **Información Limitada**: El paso proporciona solo información básica sobre el archivo y puede no incluir algunos datos específicos o adicionales.