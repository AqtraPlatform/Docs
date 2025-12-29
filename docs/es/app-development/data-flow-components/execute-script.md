# Ejecutar script

![](../../assets/images/app-development/execute-script.png)

## Información general
El paso “Ejecutar Script” está diseñado para ejecutar scripts de Python utilizando bibliotecas estándar de Python.

Este paso te permite ejecutar scripts de Python de cualquier complejidad mientras trabajas con el modelo de flujo de datos actual. Usando el script, puedes cambiar el modelo añadiendo nuevas variables o modificando los valores de las existentes.

Ejemplos de uso:
- Para obtener el valor de una variable del paso “obtener modelo de acción”: `item ['data'] ['Property_name'] `
- Para crear una nueva variable en el script: `item ['Property_name'] `

## Parámetros
**Configuración del paso:**

| Campo de configuración | Opciones de valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso fuente            | -                 | Selección del paso anterior |

## Casos
- **Personalización del procesamiento de datos**: Adecuado para lógica de procesamiento de datos compleja que no se puede implementar con herramientas estándar de flujo de datos.
- **Adición y modificación de datos**: Adecuado para escenarios que requieren añadir nuevos datos o modificar datos existentes en el modelo.

## Excepciones
- **Necesidad de competencia en Python**: Requiere conocimiento de Python y comprensión de la lógica de trabajo con flujo de datos.
- **Tipado de variables**: El tipado estricto de variables puede requerir atención adicional al escribir scripts. Tipos soportados: `@number`, `@integer`, `@string`, `@uuid`, `@boolean`, `@uri`, `@date`, `@date-time`, `@time`, `@catalog`, `@array`.

## Escenario de aplicación

Este componente muestra varios escenarios de uso del paso Ejecutar Script dentro de un flujo de datos, incluyendo la creación de nuevas variables de diferentes tipos y la modificación de valores de campos disponibles en el modelo de datos.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/18fbg2g2rcvXORI7i31zu81NdSKwMqE99/view?usp=sharing)