# Entrada de consulta proxy

![](../../assets/images/app-development/proxy-query-entry.png)

## Información general
El paso “Entrada de Consulta Proxy” se utiliza para generar un modelo de consulta proxy utilizando un filtro (**Consulta**) para recuperar una o múltiples entradas. Este paso funciona en conjunto con la configuración de “Modo Proxy” en la sección de “Configuraciones”. Para que el modelo de datos del componente funcione correctamente, se deben definir propiedades con la bandera **Consulta**.

## Parámetros
**Configuraciones del Paso:**

| Campo de Configuración | Opciones de Valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Filtro de Consulta     | -                 | Filtro para definir una entrada específica para una consulta |
| Configuraciones de modo proxy | -         | Referencia a las configuraciones de modo proxy definidas en “Configuraciones” |

## Casos
- **Consultas Filtradas en Proxy**: Utilizado en el flujo de datos de entrada para componentes marcados como proxy para ejecutar consultas con filtrado de datos.
- **Recuperación de Datos Específicos**: Recupera una entrada específica basada en ciertos criterios de filtrado.

## Excepciones
- **Dependencia de Configuración del Componente**: Requiere ciertas propiedades con la bandera **Consulta** en el modelo de datos del componente.
- **Uso Limitado**: El paso está diseñado para recuperar datos basados en filtros y no es adecuado para consultas generales sin especificación.