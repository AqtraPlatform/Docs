# Aplicar operaciones de actualización diferida

![](../../assets/images/app-development/apply-deferred-update-operations.png)

## Información general
El paso “Aplicar Operaciones de Actualización Diferida” se utiliza para la aplicación masiva de actualizaciones que han sido preparadas utilizando la serie de pasos “Entrada de Actualización Diferida”. Este paso permite realizar las operaciones de actualización acumuladas de manera eficiente aplicándolas todas a la vez.

## Parámetros
**Configuraciones del paso:**

| Campo de configuración | Opciones de valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Tamaño del lote       | 1000              | Tamaño del lote de datos a procesar |
| Tiempo de espera inactivo en ms | -       | Tiempo de espera inactivo en milisegundos entre lotes |
| Número paralelo de lotes | 0               | Número de lotes de datos procesados en paralelo |

## Casos
- **Aplicación de Actualización Masiva**: Ideal para escenarios donde necesitas actualizar datos en masa, como cuando sincronizas una gran cantidad de datos o cuando necesitas realizar cambios rápidamente en múltiples componentes del sistema.
- **Optimización del Rendimiento**: Mejora el rendimiento para actualizaciones masivas a través del procesamiento paralelo y la gestión eficiente de lotes de datos.

## Excepciones
- **Gestión de Secuencia de Actualización**: Es importante asegurar que las actualizaciones estén secuenciadas correctamente, especialmente si los datos en los diferentes pasos de la “Entrada de Actualización Diferida” están interrelacionados.
- **Configuración de Parámetros de Procesamiento por Lotes**: Parámetros como el tamaño del lote y el número de lotes paralelos deben configurarse cuidadosamente para evitar sobrecargar el sistema y asegurar que las actualizaciones se realicen de manera eficiente.

## Escenario de aplicación

El componente con una definición personalizada configura un flujo de datos para actualizar registros. Los usuarios comienzan extrayendo el modelo de acción utilizando el paso "Obtener modelo de acción". Luego, se utiliza el paso "Entrada de actualización diferida" para actualizaciones diferidas de registros, donde los usuarios pueden especificar el componente, el ID del componente y los mapeos de campos. El paso "Aplicar actualización diferida" permite configurar los parámetros de procesamiento por lotes y ejecución paralela. Después de completar estos pasos, el componente está listo para actualizar, crear o eliminar registros, lo cual ocurre en el frontend al interactuar con los elementos de interfaz correspondientes.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/16uo9P5IWDv-QnT749fYDISyyWEbKrDVR/view?usp=sharing)