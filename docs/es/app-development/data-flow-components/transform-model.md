# Transform model

![](../../assets/images/app-development/transform-model.png)

## Información general
El paso “Transform Model” se utiliza para mapear y transformar campos en el modelo de datos. Esto implica cambiar los nombres de los campos y eliminar campos innecesarios del modelo. El paso crea una nueva copia del modelo de flujo de datos, lo que te permite modificar su estructura, que a menudo se utiliza para minimizar la respuesta como un modelo de datos. También se puede utilizar para optimizar el modelo de datos después de realizar múltiples operaciones de agrupamiento (Group by).

## Parámetros
**Configuración del paso:**

| Campo de configuración | Opciones de valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso fuente            | -                 | Seleccionar el paso anterior |
| Mapeo de campos        | -                 | Mapeo y cambio de campos en el modelo de datos |

## Casos
- **Optimización del modelo de datos**: Se utiliza para cambiar la estructura del modelo de datos, incluyendo el renombrado o eliminación de campos.

## Excepciones
- **Importancia del mapeo preciso**: Errores en la configuración de “Fields Mapping” pueden resultar en cambios no deseados en el modelo de datos.
- **Dependencia de los datos fuente**: La aplicación correcta del paso requiere una comprensión precisa de la estructura de los datos fuente.

## Escenario de aplicación

Este componente contiene un flujo de datos utilizado para la transformación de datos de acuerdo con reglas especificadas. El flujo de datos incluye pasos como Extract Collection y Execute Script, que permiten agregar nuevos registros a los arreglos de datos del cliente.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/1buQNdkjcnY8wgIUM9TjjI7KoikEcSmv3/view?usp=sharing)