# Preparar claves externas

![](../../assets/images/app-development/prepare-external-keys.png)

## Información general
El paso “Preparar Claves Externas” se utiliza para convertir los identificadores internos del componente en claves de sistema externas. Este paso se utiliza ampliamente para preparar y enviar datos a sistemas externos, incluida la integración con LDAP. Facilita el proceso de transferencia de información de usuario a un sistema externo, incluyendo el contexto relevante.

En el transcurso del paso, los ID internos del componente son reemplazados por las claves primarias que se especifican para este componente, lo que asegura la correcta asignación de datos entre los sistemas internos y externos.

## Parámetros
**Configuración del paso:**

| Campo de configuración | Opciones de valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso de origen         | -                 | Fuente de datos de conversión de claves |

## Casos
- **Integración con Sistemas Externos**: Se utiliza para adaptar datos internos para su correcta integración y envío a sistemas externos como LDAP.
- **Preparar Datos para Exportación**: Adecuado para scripts donde los ID internos necesitan ser transformados para cumplir con los estándares y requisitos de los sistemas externos.

## Excepciones
- **Relevancia y Precisión de los Datos**: La efectividad del paso depende de la precisión y relevancia de los datos internos y su cumplimiento con la estructura del sistema externo.
- **Gestión de Asignación de Datos**: Debe asegurarse de que todos los ID internos estén correctamente asignados a las claves primarias del sistema externo para evitar errores de integración.