# Obtener Modelo de Acción

![](../../assets/images/app-development/get-action-model.png)

## Información general
El paso “Obtener Modelo de Acción” está diseñado para extraer un modelo de acción de una fuente o sistema específico. Este paso se puede utilizar para obtener datos sobre acciones o procesos específicos que son necesarios para un procesamiento o análisis posterior dentro del flujo de datos.

## Parámetros
**Configuración del Paso:**

| Campo de Configuración | Opciones de Valor          | Propósito |
|------------------------|----------------------------|-----------|
| Nombre del paso        | -                          | Nombre del paso |
| Validar valores de entrada | true, false              | Especifica si los valores de entrada deben ser verificados por corrección antes del procesamiento |

## Casos
- **Integración de UI**: A menudo se utiliza como un paso inicial en el flujo de datos, especialmente cuando el flujo de datos se habilita desde la UI, por ejemplo, al presionar un botón. Permite obtener el estado actual de los datos del componente en el momento de habilitar.
- **Transferencia Automática de Datos desde la UI**: Cuando la transferencia de datos se habilita desde elementos de la UI como botones, la plataforma transmite automáticamente los datos actuales del componente, incluyendo los cambios realizados por el usuario.

## Excepciones
- **Limitaciones en la Recuperación de Datos**: El paso solo recupera los datos de los campos (propiedades) del componente. Para obtener las variables establecidas en el Script del Componente, es necesario utilizar otros pasos, como “Obtener modelo en bruto”.

## Escenario de aplicación

El componente es un sistema para agregar y mostrar datos utilizando varios tipos de campos. Incluye la capacidad de agregar campos de diferentes tipos en la **definición** y proporciona una interfaz de front-end para ingresar valores, así como para mostrar datos en un **datagrid** con la capacidad de actualizar la página. Este componente utiliza los siguientes **pasos de flujo de datos**: **Obtener modelo de acción**, **Actualizar entrada**, **Escribir respuesta**.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/15M_FvmlFmkJXunTeeT6jtFolPvE5jCfk/view?usp=sharing)