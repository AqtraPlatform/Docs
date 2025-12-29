# Distinct

![](../../assets/images/app-development/distinct.png)

## Información general
El paso Distinct se utiliza para eliminar entradas duplicadas del flujo de datos, dejando solo valores únicos. Este proceso ayuda a optimizar el procesamiento de datos al eliminar duplicados y reducir la cantidad de datos analizados.

## Parámetros
**Configuraciones del paso:**

| Campo de configuración | Opciones de valor | Propósito                           |
|------------------------|-------------------|--------------------------------------|
| Nombre del paso        | -                 | Nombre del paso en el flujo de datos        |
| Paso fuente            | -                 | Selección del paso anterior |
| Claves                 | -                 | Claves para verificar la unicidad      |

## Casos
- **Limpieza de datos**: Eliminación de entradas duplicadas para simplificar el análisis.
- **Preparación para la agregación**: Pre-limpieza de datos antes de realizar operaciones de agregación.

## Excepciones
- **Selección de claves**: La selección incorrecta de claves puede resultar en la pérdida de datos importantes.
- **Pérdida de información**: Riesgo de perder parte de los datos si el paso está configurado incorrectamente.

## Escenario de aplicación

Este componente verifica la disponibilidad de campos en el paso Distinct. Se hace clic en el botón "Distinct" en el frontend. Si el paso funciona correctamente, debería aparecer una línea de "execute" con una vista previa de la respuesta HTTP en la pestaña de Red, que contiene datos para tres registros.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/1dA9EzzJOn9sWBYhdvL__AcI1kJ5qNNLd/view?usp=sharing).