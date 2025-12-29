# Registrar contexto para el modelo

![](../../assets/images/app-development/register-context-for-model.png)

## Información general
El paso “Registrar contexto para el modelo” se utiliza en el contexto de la integración LDAP para registrar el contexto de seguridad de los usuarios registrados en un sistema externo. Este paso asegura que los datos sobre los usuarios y sus roles estén sincronizados entre el sistema externo y el sistema actual, utilizando claves para identificar y registrar el contexto.

## Parámetros
**Configuraciones del paso:**

| Campo de configuración | Opciones de valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso fuente            | -                 | Selección del paso anterior |
| Componente             | -                 | Componente para el cual se está registrando el contexto |
| Campo de nombre        | -                 | Campo que indica el nombre o identificador de la entidad |
| Claves                 | -                 | Claves utilizadas para identificar de manera única una entidad |

## Casos
- **Integración LDAP**: Utilizado para sincronizar y registrar datos de usuarios desde LDAP en el sistema actual.
- **Gestión de Roles y Accesos**: Adecuado para scripts que requieren una coincidencia y seguimiento precisos de los roles de los usuarios registrados en sistemas externos.

## Excepciones
- **Requisitos de Precisión de Claves**: Las claves deben coincidir con precisión para identificar y registrar correctamente a los usuarios en el sistema.
- **Gestión de Cambios en Sistemas Externos**: Los cambios en los roles o estados de los usuarios en un sistema externo requieren una actualización adecuada en el sistema actual, lo que puede ser un desafío ante datos que cambian dinámicamente.