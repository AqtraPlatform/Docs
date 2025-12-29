# Obtener modelo de flujo de trabajo

![](../../assets/images/app-development/get-workflow-model.png)

## Información general
El paso “Obtener Modelo de Flujo de Trabajo” se utiliza exclusivamente en flujos de datos que son llamados desde un flujo de trabajo. Permite obtener el modelo y los datos del flujo de trabajo que llama dentro del flujo de datos actual.

## Parámetros
**Configuración del paso:**

| Campo de configuración  | Opciones de valor | Propósito |
|-------------------------|-------------------|-----------|
| Nombre del paso         | -                 | Nombre del paso |
| Validar valores de entrada | true, false     | Indica que los valores de entrada deben ser verificados por corrección antes del procesamiento |

## Casos
- **Integración de Flujo de Datos y Flujo de Trabajo**: Permite integrar el flujo de datos con el flujo de trabajo proporcionando acceso al modelo y los datos del flujo de trabajo que llama.

## Excepciones
- **Uso Limitado**: El paso no está destinado para su uso en flujo de datos de entrada.

## Escenario de aplicación

El componente permite crear un flujo de datos para actualizar un registro en el componente de datos de origen. Incluye pasos como Obtener modelo de flujo de trabajo para obtener el modelo del flujo de trabajo, Actualizar entrada para actualizar el registro con los parámetros apropiados establecidos, y Escribir respuesta para output el resultado. Este componente se puede utilizar para actualizar datos en el componente de origen utilizando flujos de trabajo y elementos de UI.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/1F2ZFQlyMf6ZaxABcoOWib4T8AD8w-75Q/view?usp=sharing)