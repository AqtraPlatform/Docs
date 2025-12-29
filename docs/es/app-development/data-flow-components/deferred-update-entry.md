# Entrada de actualización diferida

![](../../assets/images/app-development/deferred-update-entry.png)

## Información general
El paso “Entrada de Actualización Diferida” se utiliza para organizar la actualización diferida de entradas en un componente específico. Este paso permite acumular acciones para crear, actualizar o eliminar entradas, que luego se ejecutan después de que se habilita el paso “Aplicar Operaciones de Actualización Diferida”. De esta manera, se pueden recopilar múltiples operaciones de actualización.

## Parámetros
**Configuración del paso:**

| Campo de configuración | Opciones de valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso fuente            | -                 | Selección del paso anterior |
| Componente             | -                 | Componente a actualizar |
| Clave del campo del componente | -         | Campo con la clave del componente a actualizar |
| Marcar entrada para eliminación | true, false | Marca de eliminación de entrada |
| Campo de nombre        | -                 | Nombre del campo a actualizar |
| Mapeo de campos        | -                 | Mapeo de campos entre el flujo de datos y el componente |

## Casos
- **Procesamiento por lotes de datos**: Se utiliza para recopilar múltiples operaciones de actualización de datos y luego ejecutarlas en una sola transacción, mejorando el rendimiento y reduciendo la carga en el sistema.
- **Gestión de datos compleja**: Adecuado para escenarios que requieren lógica de actualización de datos compleja, incluyendo la creación, modificación y eliminación de entradas dentro de un solo flujo de trabajo.

## Excepciones
- **Necesidad de Actualizaciones Posteriores**: Todas las operaciones de actualización acumuladas por este paso deben ser habilitadas a través del paso “Aplicar Operaciones de Actualización Diferida” para poder realizarlas.

## Escenario de aplicación

El componente con una definición personalizada configura un flujo de datos para actualizar registros. Los usuarios comienzan extrayendo el modelo de acción utilizando el paso "Obtener modelo de acción". Luego, se utiliza el paso "Entrada de actualización diferida" para actualizaciones diferidas de registros, donde los usuarios pueden especificar el componente, el ID del componente y los mapeos de campos. El paso "Aplicar actualización diferida" permite configurar el procesamiento por lotes y los parámetros de ejecución paralela. Después de completar estos pasos, el componente está listo para actualizar, crear o eliminar registros, lo que ocurre en el frontend al interactuar con los elementos de interfaz correspondientes.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/16uo9P5IWDv-QnT749fYDISyyWEbKrDVR/view?usp=sharing)