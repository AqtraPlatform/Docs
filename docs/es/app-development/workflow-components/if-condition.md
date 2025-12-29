# Condición If

![](../../assets/images/app-development/if-condition.png)

## Información general

El paso “Condición If” dentro del flujo de trabajo se utiliza para verificar el valor de un campo contra la condición especificada. Este paso te permite implementar ramificaciones condicionales en un proceso donde realizar ciertas acciones o pasar a un script alternativo depende del resultado de una verificación de condición. Un script alternativo debe contener el paso “Finalizar”.

## Parámetros

**Configuraciones del paso:**

| Campo de configuración | Opciones de valor            | Propósito                                 |
| ---------------------- | ---------------------------- | ----------------------------------------- |
| Nombre del paso        | -                            | Nombre del paso “Condición If”           |
| Campo de condición     | Multiselección de Catálogo   | Campo de validación de condición          |
| Operador               | Igual, No igual, Mayor, Menor| Tipo de operador para verificar la condición |
| Comparar con nulo     | verdadero, falso             | Verificación de comparación con nulo      |
| Valor                  | -                            | Valor a comparar con el campo            |

## Casos

- **Ejecución Condicional de Acciones**: Se utiliza para activar diferentes partes del flujo de trabajo según los valores de ciertos campos, por ejemplo, para iniciar diferentes procesos según el estado de la solicitud.
- **Ramificación Lógica en Procesos**: Adecuado para crear cadenas lógicas complejas donde diferentes pasos de ejecución dependen de la satisfacción de condiciones específicas.

## Excepciones

- **Precisión en la Definición de Condiciones**: Es importante definir con precisión las condiciones y configurar correctamente los campos para validarlas para evitar ramificaciones incorrectas o errores en la lógica del flujo de trabajo.
- **Manejo de Diferentes Scripts**: Necesitas planificar claramente cómo se manejarán los diferentes scripts dependiendo del resultado de la verificación de la condición, especialmente en flujos de trabajo complejos o de múltiples pasos.