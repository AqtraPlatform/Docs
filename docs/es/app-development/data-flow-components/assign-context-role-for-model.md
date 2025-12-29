# Asignar rol de contexto para el modelo

![](../../assets/images/app-development/assign-context-role-for-model.png)

## Información general
El paso “Asignar Rol de Contexto para el Modelo” se utiliza para vincular a un usuario o grupo de usuarios a un rol y contexto específicos. Este proceso requiere que al menos un rol esté configurado en la sección “Roles” del menú “Acceso”. Este paso permite establecer relaciones entre usuarios y roles en el contexto de un modelo de datos específico, proporcionando así control sobre el acceso y los permisos de los usuarios.

## Parámetros
**Configuraciones del paso:**

| Campo de configuración | Opciones de valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso fuente            | -                 | Selección del paso anterior |
| Campo UserId           | -                 | Campo de ID de usuario |
| Campo ContextId        | -                 | Campo de ID de contexto |
| Seleccionar contextos   | -                 | Selección de los contextos a los que se vinculará el rol |

## Casos
- **Gestión de acceso de usuarios**: Se utiliza para asignar roles a los usuarios, determinando su acceso y permisos dentro del sistema.
- **Gestión dinámica de roles al interactuar con la interfaz de usuario**: Este paso se utiliza eficazmente para cambiar o actualizar los roles de los usuarios en tiempo real según sus acciones e interacciones con los elementos de la interfaz de usuario. Esto hace posible adaptar el acceso y los permisos de los usuarios dependiendo de acciones o escenarios específicos de uso del sistema.

## Excepciones
- **Requisito de roles configurados**: Para un enlace exitoso, el sistema debe tener los roles apropiados preconfigurados.
- **Dependencia de la precisión del ID**: La identificación precisa de los ID de usuario y contextos es crítica para que el paso funcione correctamente.