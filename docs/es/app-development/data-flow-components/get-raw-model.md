# Obtener modelo en bruto

![](../../assets/images/app-development/get-raw-model.png)

## Información general
El paso “Obtener Modelo en Bruto” se utiliza en un flujo de datos, que requiere procesar un modelo de datos personalizado que no corresponde al modelo de componente estándar, flujo de trabajo u otras opciones estándar. Los casos de uso típicos incluyen flujos de datos llamados desde un Script de Componente con variables definidas dentro del script, así como el procesamiento de datos de formularios dentro de una estructura de múltiples componentes.

## Parámetros
**Configuración del paso:**

| Campo de configuración | Opciones de valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Validar valores de entrada | true, false   | Indica que los valores de entrada deben ser verificados por corrección antes del procesamiento |

## Casos
- **Integración con Script de Componente**: Utilizado para flujos de datos llamados desde el Script de Componente cuando se requieren variables o datos específicos.
- **Procesamiento de Datos de Formularios de Múltiples Componentes**: Adecuado para scripts donde los flujos de datos trabajan con datos obtenidos de formularios en una estructura de múltiples componentes.

## Excepciones
- **Requisito de Configuración del Modelo**: Debe preconfigurar el modelo de datos en formato JSON.
- **Características del Formato del Modelo**: Una configuración incorrecta del modelo puede resultar en un procesamiento de datos incorrecto o errores en el flujo de datos.