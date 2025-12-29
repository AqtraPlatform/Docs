# Seleccionar muchos

![](../../assets/images/app-development/select-many.png)

## Información general
El paso “Seleccionar muchos” se utiliza para convertir un campo de tipo array en una lista plana. A diferencia del paso “Extraer colección”, “Seleccionar muchos” preserva los datos del modelo del paso anterior y añade valores de “padre” con un prefijo `$parent` para cada elemento del array. Esto no solo expande el array, sino que también preserva el contexto de la entrada padre.

## Parámetros
**Configuración del paso:**

| Campo de configuración | Opciones de valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso fuente            | -                 | Seleccionando el paso anterior |
| Ruta del modelo        | -                 | Ruta a un campo de array en el modelo de datos |

## Casos
- **Expansión y preservación del contexto**: Se utiliza para convertir arrays de datos en una lista plana mientras se preserva la relación con los datos padre.
- **Procesamiento de estructuras jerárquicas**: Adecuado para scripts donde necesitas procesar datos de arrays sin perder la conexión con los elementos de datos “padre”.

## Excepciones
- **Procesamiento de arrays grandes**: Procesar arrays grandes puede ser más intensivo en recursos debido a la necesidad de preservar el contexto de los datos padre.

## Escenario de aplicación

Este componente es una herramienta para crear y gestionar flujos de datos dentro de la aplicación. El paso 'Seleccionar muchos' en este componente se utiliza para elegir múltiples elementos de un array de datos obtenidos en la etapa anterior del flujo de datos. El componente permite a los usuarios definir condiciones de selección y procesamiento de datos de acuerdo con sus requisitos.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/1T9k35m8cg56vmM68LCT0brMeYQ2JIJ6U/view?usp=sharing).