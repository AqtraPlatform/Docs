# Obtener entidad por id

![](../../assets/images/app-development/get-entity-by-id.png)

## Información general
El paso “Obtener Entidad por ID” se utiliza para obtener un elemento de componente por su identificador único (ID). Este paso se utiliza generalmente en combinación con otros pasos, como “Buscar” o “Actualizar Entrada”, que devuelven un ID que es adecuado para este paso.

## Parámetros
**Configuración del paso:**

| Campo de configuración | Opciones de valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso de origen         | -                 | Seleccionando el paso anterior |
| Campo de origen        | -                 | Campo que contiene el ID a buscar |
| Nombre del campo de destino | -             | Campo donde se registrará el resultado |
| Componente             | -                 | Componente que se está buscando |

## Casos
- **Búsqueda de datos por ID**: Se utiliza para recuperar con precisión una entrada específica utilizando el ID del componente.

## Excepciones
- **Dependencia de la precisión del ID**: El ID exacto debe ser especificado y estar disponible en los datos de origen para que la consulta sea exitosa.
- **Manejo de inconsistencias**: Si no hay ninguna entrada con el ID especificado, el paso puede devolver un resultado vacío.

## Escenario de aplicación

Este componente permite agregar un campo de tipo catálogo y crear un flujo de datos para recuperar una entidad por su identificador. El campo de tipo catálogo se coloca en la página para seleccionar el valor correspondiente del catálogo. El flujo de datos incluye un paso 'Obtener modelo de acción' para la inicialización, un paso 'Obtener entidad por id' para recuperar la entidad por identificador utilizando el valor seleccionado del catálogo, y un paso 'Escribir respuesta' para mostrar el resultado.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/1eCxoYHKg0Zl8APxnUMRA9qmpqNkrtfuW/view?usp=sharing).