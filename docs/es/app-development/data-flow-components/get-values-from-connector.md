# Obtener valores del conector

![](../../assets/images/app-development/get-values-from-connector.png)

## Información general
El paso “Obtener valores del conector” te permite recuperar datos a través de una consulta a sistemas externos utilizando los conectores configurados. El paso puede ser llamado por programación o en nombre del usuario.

## Parámetros
**Configuración del paso:**

| Campo de configuración | Opciones de valor          | Propósito |
|------------------------|----------------------------|-----------|
| Nombre del paso        | -                          | Nombre del paso |
| Sistema                | Multiselección de Catálogo | Contiene sistemas de integración preconfigurados |
| Conector               | Multiselección de Catálogo | Contiene conectores preconfigurados en el sistema de integración |
| Ruta de consulta       | Multiselección de Catálogo | Contiene el “EndPoint” que se va a acceder |
| Nombre del método      | Get, Post, Put, Delete     | Tipo de solicitud a ejecutar |
| Mapeo de parámetros    | -                          | Una entidad dinámica que te permite filtrar una solicitud a través de una API seleccionada |

## Casos
- **Actualización programada de datos**: El paso se utiliza para actualizar automáticamente los datos en el flujo de datos de entrada de manera programada a través de cron, asegurando obtener información oportuna y actualizada.
- **Personalización de consultas individuales**: El paso se configura para enviar consultas específicas a diferentes sistemas externos, permitiendo una integración flexible y el procesamiento de datos de múltiples fuentes.
- **Optimización del flujo de datos**: El paso se utiliza de manera eficiente para extraer datos de sistemas externos, minimizando la necesidad de procesamiento manual y mejorando el rendimiento del flujo de datos.

## Excepciones
- **Métodos de consulta**: Aunque se admiten varios métodos de consulta (Get, Post, Put, Delete), se requiere una personalización cuidadosa caso por caso, teniendo en cuenta las características específicas del sistema externo y el tipo de datos.
- **Automatización con limitaciones**: La capacidad de llamar automáticamente a un paso programado proporciona comodidad, pero requiere un ajuste fino de los parámetros y verificar la accesibilidad de los sistemas externos.

## Escenario de aplicación

Este componente maneja datos de personajes. Creamos cinco modelos de datos para sus atributos: character_id, character_name, character_species, character_status y gender. Luego, seleccionamos una integración, por ejemplo, Rick and Morty, y añadimos los siguientes pasos: Obtener valores del conector, Extraer colección, Almacenar entrada sobre bus y Escribir respuesta.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/1zWIWzpqccbocpDCfVUNIkGW2grrWJ5Yn/view?usp=sharing)