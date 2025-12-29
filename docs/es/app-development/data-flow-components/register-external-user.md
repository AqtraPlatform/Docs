# Registrar usuario externo

![](../../assets/images/app-development/register-external-user.png)

## Información general
El paso “Registrar Usuario Externo” está destinado a registrar usuarios individuales o grupos de usuarios. Este paso está diseñado en el contexto de la integración LDAP y se utiliza para la integración con sistemas externos, facilitando el proceso de intercambio de usuarios de esos sistemas y luego iniciando sesión en el sistema actual.

## Parámetros
**Configuraciones del paso:**

| Campo de configuración | Opciones de valor | Propósito |
|-----------------------|-------------------|-----------|
| Nombre del paso       | -                 | Nombre del paso |
| Paso fuente           | -                 | Selección del paso anterior |
| Nombre de usuario     | -                 | Nombre de registro o ID de usuario |
| Campo clave           | -                 | Campo que contiene información clave para identificar al usuario |
| Proveedor de autenticación | -             | Proveedor de autenticación utilizado para registrar al usuario |

## Casos
- **Integración de Usuarios desde Sistemas Externos**: Se utiliza para intercambiar y registrar usuarios de LDAP u otros sistemas externos, asegurando su correcta integración en el sistema actual.
- **Automatización del Proceso de Registro**: Adecuado para scripts donde es necesario automatizar el proceso de registro de un gran número de usuarios, minimizando el trabajo manual y posibles errores.

## Excepciones
- **Dependencia de la Precisión de los Datos de Entrada**: La efectividad del paso depende de la precisión y completitud de los datos recibidos del sistema externo.