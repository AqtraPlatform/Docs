# Proxy get entry

![](../../assets/images/app-development/proxy-get-entry.png)

## Información general
El paso “Proxy Get Entry” se utiliza para generar un modelo de una solicitud proxy con el fin de obtener una única entrada. Este paso está estrechamente relacionado con la configuración de “Proxy mode”, que se puede encontrar en la sección de “Settings”.

## Parámetros
**Configuración del paso:**

| Campo de configuración | Opciones de valor | Propósito |
|-----------------------|-------------------|------------|
| Nombre del paso       | -                 | Nombre del paso |
| Validar valores de entrada | true, false       | Indica que los valores de entrada deben ser verificados por corrección antes de procesarlos |

## Casos
- **Recuperación de una única entrada**: Se utiliza para generar y enviar solicitudes para una entrada específica a través de un servidor proxy.
- **Integración con sistemas externos**: Proporciona comunicación con sistemas y servicios externos para obtener datos utilizando proxy de consulta.

## Excepciones
- **Dependencia de la configuración del proxy**: El correcto funcionamiento del paso depende de la correcta configuración de “Proxy mode” en la sección de “Settings”.
- **Funcionalidad limitada**: El paso está especializado en recuperar registros únicos y no está diseñado para manejar múltiples consultas o datos.