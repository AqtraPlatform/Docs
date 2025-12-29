# Obtener Modelo Vacío

![](../../assets/images/app-development/get-empty-model.png)

## Información general
El paso “Obtener Modelo Vacío” se utiliza en scripts de flujo de datos que no requieren la recuperación del modelo de datos en la entrada. Se usa a menudo cuando se llama al flujo de datos para realizar operaciones regulares, como la generación de informes, especialmente si están programadas (por ejemplo, mediante cron).

## Parámetros
**Configuración del Paso:**

| Campo de Configuración | Opciones de Valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Validar valores de entrada | true, false   | Indica que los valores de entrada deben ser verificados por corrección antes del procesamiento |

## Casos
- **Operaciones Regulares**: Ideal para flujos de datos programados para ejecutarse regularmente sin necesidad de datos de entrada.
- **Estado Inicial del Flujo de Datos**: Se utiliza para inicializar el flujo de datos sin datos preestablecidos, permitiendo a los desarrolladores crear y poblar el modelo de datos ellos mismos utilizando pasos posteriores.

## Excepciones
- **Sin Datos de Entrada**: Al usar este paso, los datos de entrada no se proporcionan en el flujo de datos. Esto significa que el desarrollador debe inicializar y poblar el modelo de datos en pasos posteriores.

## Escenario de aplicación

Este componente es una interfaz para agregar un nuevo nombre a través de un **campo de entrada** en el front end, luego actualizar el modelo de datos y mostrar el resultado en un **datagrid**. El flujo de datos en el componente permite agregar un nuevo nombre al modelo y actualizar el registro en el **datagrid**.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/1G3v4cZiteFdONpIjxPAf78a8gBTrh0w_/view?usp=sharing)