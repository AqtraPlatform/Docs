# Agrupar Por

![](../../assets/images/app-development/group-by.png)

## Información general
El paso "Agrupar Por" se utiliza para recopilar y agrupar datos divididos en pasos anteriores, por ejemplo, utilizando la "Extracción de Colección". La función principal de este paso es agrupar datos por claves específicas especificadas por el usuario. El paso recopila los datos divididos y combina solo las entradas que coinciden con las claves especificadas.

## Parámetros
**Configuración del Paso:**

| Campo de Configuración | Opciones de Valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso fuente            | -                 | Seleccionar el paso anterior |
| Claves                 | -                 | Claves utilizadas para agrupar datos |

## Casos
- **Combinación de Datos Divididos**: Se utiliza para combinar datos divididos en los pasos anteriores, como la "Extracción de Colección", utilizando claves específicas.
- **Segmentación y Análisis de Datos**: Adecuado para casos donde es necesario analizar datos según categorías o criterios específicos.

## Excepciones
- **Dependencia de las Claves de Agrupación**: La precisión y relevancia de las claves son críticas para agrupar correctamente los datos.
- **Dificultad en el Procesamiento y Análisis de Datos**: Agrupar puede ser difícil si la estructura de los datos es variada o si las claves no identifican grupos de manera única.

## Escenario de aplicación

Este componente verifica la disponibilidad de campos en el paso Agrupar Por. En el flujo de datos, primero se agrega un paso de modelo de acción Obtener y un paso Agrupar Por. Luego, en el frontend, se abre el componente importado y se abre la pestaña "Red" en las herramientas de desarrollador del navegador. Después de eso, se hace clic en el botón "Agrupar por" en el frontend. Si el paso funciona correctamente, debería aparecer una línea "ejecutar" con una vista previa de la respuesta HTTP en la pestaña de Red, que contiene datos con la clave "ETO test123" y su agregación.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/1fKeJh3a0HHcG7VuFs-Tx5YdS7H6C7mI0/view?usp=sharing).