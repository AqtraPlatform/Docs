# Referencia de búsqueda

![](../../assets/images/app-development/lookup-reference.png)

## Información general
El paso de “Referencia de búsqueda” se utiliza para buscar referencias a instancias de componentes mediante claves externas. Este proceso requiere que al menos una propiedad con la bandera de “Clave primaria” esté configurada en el componente que se va a buscar.

La búsqueda se realiza mediante esta propiedad, y el resultado de la búsqueda en forma de Id (entero) del registro encontrado se registrará en la variable especificada en el “Nombre del campo.” Si no se encuentra ninguna instancia de un componente con tal clave, la variable será nula.

## Parámetros
**Configuración del paso:**

| Campo de configuración | Opciones de valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso fuente            | -                 | Selección del paso anterior |
| Componente             | -                 | Componente que se está buscando |
| Nombre del campo       | -                 | Nombre del campo donde se registrará el resultado de la búsqueda |

## Casos
- **Búsqueda de clave primaria**: Se utiliza para determinar la disponibilidad e identificar instancias de componentes mediante identificadores únicos.
- **Vinculación de datos de componentes**: Adecuado para scripts donde se desea vincular datos de diferentes componentes basados en claves únicas.

## Excepciones
- **Requisito de clave primaria**: El componente debe tener una clave primaria configurada para asegurar una búsqueda exitosa.
- **Manejo de registros faltantes**: Si no hay ninguna instancia con la clave especificada, el valor de la variable será nulo, lo que puede requerir procesamiento adicional.

## Escenario de aplicación

Este componente utiliza el paso de Referencia de búsqueda para encontrar el ID del registro en la tabla "Tarea de clasificación" basado en el número de clasificación ingresado. Después de ingresar el número de clasificación y ejecutar el flujo de datos, el ID del registro correspondiente se muestra en el frontend.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/1LZzqHGc7I5IdAVLmK6H1_ItODiiruSAJ/view?usp=sharing)