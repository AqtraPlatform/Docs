# Filtro de origen

![](../../assets/images/app-development/filter-source.png)

## Información general
El paso “Filtro de Origen” se utiliza para filtrar el flujo de datos en el flujo de datos. Permite ramificar flujos de datos según el valor del campo seleccionado y el operador de prueba especificado, como igual, no igual, mayor y menor.

## Parámetros
**Configuración del paso:**

| Campo de configuración | Opciones de valor   | Propósito |
|------------------------|---------------------|------------|
| Nombre del paso        | -                   | Nombre del paso |
| Paso de origen         | -                   | Selección del paso anterior |
| Campo de origen        | -                   | Campo a filtrar |
| Operador               | igual, no igual, mayor, menor | Operador para comparar valores de campo |
| Comparar con nulo     | verdadero, falso     | Indica si se debe comparar con nulo |
| Valor de filtro        | -                   | Valor a filtrar |

## Casos
- **Ramificación del flujo de datos**: Se utiliza para dividir un flujo de datos basado en condiciones específicas definidas en el filtro.
- **Segmentación de datos**: Adecuado para situaciones en las que necesita tratar diferentes segmentos de datos de manera diferente según criterios especificados.

## Excepciones
- **Precisión de la configuración del filtro**: Un filtro configurado incorrectamente puede resultar en la pérdida de datos importantes o la inclusión de datos innecesarios en el procesamiento.
- **Dependencia del campo seleccionado**: La efectividad del filtrado depende de la elección correcta del campo y del operador de comparación apropiado.

## Escenario de aplicación

Este componente es una interfaz con tres botones: `ExecuteFilterSource`, `ExecuteFilterSourceNotEqual`, y `ExecuteFilterSourceGreat`, cada uno de los cuales activa un flujo de datos dependiendo de la entrada en el campo `First`. Diferentes escenarios de prueba incluyen la verificación de condiciones de igualdad, desigualdad y mayor/menor que el valor especificado.

- Puede descargar la configuración del componente [aquí](https://drive.google.com/file/d/1OO5SymRdhmv3oED2EPG4twG5mypsqqs9/view?usp=sharing).