# Switch case

![](../../assets/images/app-development/switch-case.png)

## Información general
El paso “Switch Case” dentro de un flujo de trabajo se utiliza como un operador de conmutación incondicional que te permite elegir entre diferentes opciones de script. Este paso es ideal para controlar la lógica del proceso basada en ciertas condiciones, generalmente especificadas por campos Booleanos o Enum. Cuando se utiliza, el script principal siempre está deshabilitado y el proceso va a una de las ramas alternativas.
![](../../assets/images/app-development/switch-case-example.png)

## Parámetros
**Configuraciones del paso:**

| Campo de configuración | Propósito |
|------------------------|-----------|
| Nombre del paso        | Nombre del paso “Switch Case” |
| Campo de origen de conmutación | Campo basado en el valor del cual se selecciona el script |

## Casos
- **Ramificación de la lógica del proceso**: Se utiliza para crear caminos condicionales en un flujo de trabajo donde la siguiente dirección se determina en función de una cierta condición o valor.
- **Gestión de diferentes scripts de ejecución**: Adecuado para scripts donde un proceso requiere una ejecución diferente dependiendo de condiciones predefinidas o selección del usuario.

## Excepciones
- **Precisión de las condiciones de transición**: Es necesario definir con precisión las condiciones de conmutación para cada caso para asegurar que se seleccione el camino de ejecución correcto.
- **Complejidad de la gestión de múltiples caminos**: Flujos de trabajo complejos con muchos caminos posibles requieren una comprensión y gestión clara de cada uno de ellos para evitar errores en la lógica del proceso.