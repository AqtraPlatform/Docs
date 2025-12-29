# Finalizar

![](../../assets/images/app-development/finish.png)

## Información general
El paso “Finalizar” dentro de un flujo de trabajo está diseñado para completar la ejecución del flujo de trabajo actual. Este paso se utiliza típicamente para especificar explícitamente el punto de finalización de un flujo de trabajo, especialmente en los scripts alternativos definidos en el bloque de Condiciones.

## Parámetros
**Configuraciones del paso:**

| Campo de configuración | Propósito |
|-----------------------|-----------|
| Nombre del paso       | Nombre del paso “Finalizar” |

## Casos
- **Finalización Controlada del Flujo de Trabajo**: Se utiliza para especificar explícitamente el punto de finalización de un flujo de trabajo, lo cual es especialmente importante en procesos complejos con muchas condiciones y ramas.
- **Rutas de Ejecución Alternativas**: Adecuado para scripts donde un flujo de trabajo necesita terminar bajo ciertas condiciones que difieren del flujo principal de ejecución.

## Excepciones
- **Necesidad de Configuración Adecuada**: Es importante asegurarse de que el paso “Finalizar” esté correctamente integrado en la lógica del flujo de trabajo para que no interrumpa el proceso prematuramente o salte pasos importantes.