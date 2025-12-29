# Eliminar roles asignados para el usuario

![](../../assets/images/app-development/remove-assigned-roles-for-user.png)

## Información general
El paso “Eliminar Roles Asignados para el Usuario” se utiliza para restablecer todos los roles asignados a un usuario en particular. Esto permite a los administradores del sistema y a los gerentes de procesos eliminar roles de usuario, simplificando la gestión de permisos y controles de seguridad.

## Parámetros
**Configuraciones del Paso:**

| Campo             | Opciones de Valor  | Propósito |
|------------------|--------------------|------------|
| Nombre del paso   | -                  | Nombre del paso |
| Paso fuente       | -                  | Seleccionar el paso anterior |
| Campo de ID de usuario | Nombre de una variable de tipo información de usuario | Campo que contiene el ID del usuario para el restablecimiento de roles |

## Casos
- **Gestión de Acceso y Roles**: Este paso es ideal para scripts donde deseas cambiar o restablecer rápidamente los roles de usuario, como cuando cambian las responsabilidades laborales o cuando un empleado se va.
- **Asegurando la Seguridad del Sistema**: Se utiliza para prevenir el acceso no autorizado a datos sensibles o características del sistema al eliminar roles de usuarios que ya no necesitan tales permisos de acceso.

## Excepciones
- **Dependencia de la Precisión en la Identificación del Usuario**: La efectividad del paso depende de la identificación precisa del usuario cuyos roles deseas restablecer.
- **Necesidad de Obtener el ID del Usuario Primero**: El paso requiere que primero obtengas un ID de usuario interno, lo cual se puede hacer a través del paso “Obtener Información del Usuario” u otros métodos de autenticación.