# Ejecutar llamada a la API

![](../../assets/images/app-development/execute-api-call.png)

## Información general
El paso “Ejecutar llamada a la API” se utiliza para interactuar con sistemas externos a través de la API. Este paso se puede configurar para varios tipos de solicitudes, incluyendo recibir datos (GET), enviar datos (POST/PUT) o eliminar datos (DELETE) en un sistema externo. Dependiendo del contexto de uso, este paso puede ser uno de los primeros pasos en Dataflow para obtener datos o uno de los últimos pasos para actualizar datos en sistemas externos.

## Parámetros
**Configuración del paso:**

| Campo de configuración | Opciones de valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso fuente            | -                 | Seleccionar el paso anterior |
| Campo de almacenamiento de resultados | - | Un campo para almacenar el ID de una entrada creada o procesada |
| Sistema                | -                 | Elegir un sistema de integración |
| Conector               | -                 | Seleccionar un conector en el sistema de integración |
| Ruta de consulta       | -                 | EndPoint para la solicitud |
| Nombre del método      | Get, Post, Put, Delete | Tipo de solicitud a completar |
| Mapeo de parámetros    | -                 | Configuración dinámica para el filtrado de consultas |

## Casos
- **Obteniendo datos de fuentes externas**: Se utiliza para descargar datos de sistemas externos, lo que puede ser especialmente útil al integrarse con servicios o bases de datos externas.
- **Enviando o actualizando datos**: Adecuado para enviar datos a sistemas externos o actualizar datos existentes, por ejemplo, al sincronizar cambios realizados en el flujo de datos.
- **Eliminando datos**: Se puede utilizar para eliminar datos de sistemas externos, lo que ayuda a mantener la relevancia e integridad de los datos en los sistemas integrados.

## Excepciones
- **Necesidad de procesamiento asíncrono**: El paso se realiza de manera asíncrona, lo que requiere tener en cuenta el tiempo de respuesta de los sistemas externos y el impacto potencial en la secuencia de procesamiento de datos.
- **Requisito de configuración del conector**: La efectividad del paso depende de sistemas de integración y conectores correctamente configurados, así como de la precisión en la determinación del EndPoint y los parámetros de la solicitud.

## Escenario de aplicación

El componente crea una integración simple para recuperar datos, como el clima, a través de una API. En el flujo de datos, se utilizan pasos para configurar la solicitud de la API, incluyendo la ejecución de un script para crear variables de la API, llamar a la API y guardar los resultados. Luego, se selecciona y configura la integración en el sistema, y los resultados se muestran en el frontend utilizando un formulario vinculado a la ejecución del script. La función en el componente procesa los datos recuperados para la visualización del usuario.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/119_NZiqzENXCaqdmiZ7qj4ZmeHcje7je/view?usp=sharing).