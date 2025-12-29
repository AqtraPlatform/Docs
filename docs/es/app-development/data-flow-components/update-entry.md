# Actualizar entrada

![](../../assets/images/app-development/update-entry.png)

## Información general

El paso “Actualizar Entrada” se utiliza para crear, actualizar o eliminar una entrada existente en el sistema. Este paso se ejecuta directamente, y el sistema espera a que se complete. Si ocurre un error durante la ejecución, se detendrá la ejecución del flujo de datos.

## Parámetros

**Configuración del paso:**

| Campo de configuración   | Opciones de valor | Propósito                                      |
| ----------------------- | ----------------- | ---------------------------------------------- |
| Nombre del paso         | -                 | Nombre del paso                                |
| Paso fuente             | -                 | Selección del paso anterior                    |
| Componente              | -                 | Componente a actualizar                        |
| Clave del campo componente | -               | Campo con la clave del componente a actualizar |
| Marcar entrada para eliminación | true, false | Marca de eliminación de entrada                |
| Campo de nombre         | -                 | Nombre del campo a actualizar                  |
| Campo de almacenamiento de resultados | -     | Campo para guardar el resultado de la operación |
| Mapeo de campos        | -                 | Mapeo de campos entre el flujo de datos y el componente |

## Casos

- **Actualización de Datos**: Se utiliza para actualizar información en las entradas existentes de los componentes del sistema para asegurar que los datos sean precisos y estén actualizados.
- **Eliminación de una Entrada**: El paso “Actualizar Entrada” se puede utilizar para eliminar entradas existentes en el sistema. Esto es especialmente relevante en scripts donde necesitas eliminar información obsoleta o incorrecta para mantener los datos en el sistema precisos y actualizados. Por ejemplo, esto puede ser eliminar la cuenta de un usuario que ha dejado la organización o eliminar artículos no disponibles del inventario. Es importante notar que el paso se puede configurar para marcar la entrada para eliminación, lo que permite gestionar el proceso de eliminación de manera más flexible.

## Excepciones

- **Dependencia de la Presencia de un ID de Instancia**: Para actualizar datos con éxito, primero debe recibirse y transmitirse el ID de instancia del componente.
- **Gestión de Errores en Tiempo de Ejecución**: Cualquier error durante el proceso de actualización de datos detendrá el flujo de datos, lo que requiere una cuidadosa supervisión del manejo de errores y excepciones.

## Escenario de aplicación

El componente presenta un escenario para agregar, editar y eliminar registros de componentes utilizando el paso "Actualizar entrada".

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/1k1oMpI2YSF-P3zgsd2cORfRjFs3l7w0o/view?usp=sharing)