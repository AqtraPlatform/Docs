# Escribir respuesta

![](../../assets/images/app-development/write-response.png)

## Información general
El paso “Escribir Respuesta” juega un papel clave en Dataflow, ya que está diseñado para devolver el resultado final al llamador. Este paso suele ser el último en cualquier Dataflow, resumiendo y enviando los datos recibidos de vuelta a la fuente solicitante.

## Parámetros
**Configuraciones del Paso:**

| Campo de Configuración | Opciones de Valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso fuente            | -                 | Selección del paso anterior |

## Casos
- **Devolviendo Resultados de Dataflow**: Se utiliza para enviar los resultados del proceso de datos de Dataflow de vuelta al llamador, lo cual puede ser crítico en análisis de datos y gestión de errores.
- **Transformación de Datos Pre-Respuesta**: Puede combinarse con el paso “Transformar Modelo” para transformar o filtrar datos antes de ser enviados, permitiéndole optimizar y personalizar el contenido de la respuesta para cumplir con los requisitos del llamador.

## Escenario de aplicación

El componente contiene definiciones de datos personalizadas (definiciones) y proporciona la capacidad de crear y gestionar datos utilizando flujos de datos. Implementa pasos para recuperar modelos de datos (modelo de acción Obtener) y escribir respuestas (escribir respuesta), permitiendo a los usuarios interactuar con los datos a través de la interfaz de usuario e interactuar con ellos en el frontend de la aplicación.

- Puede descargar la configuración del componente [aquí](https://drive.google.com/file/d/1qNTgk1uYrMO3uUkDRmTO3i4En5mbG22i/view?usp=sharing).