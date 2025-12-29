# Actualizar o crear información del usuario

![](../../assets/images/app-development/update-or-create-user-info.png)

## Información general
El paso “Actualizar o Crear Información del Usuario” se utiliza para actualizar la información de un usuario existente o crear un nuevo usuario. Este paso funciona exclusivamente con el componente “Información del Usuario”. Cuando se actualiza la información del usuario, si la contraseña no se especifica, permanecerá sin cambios.

## Parámetros
**Configuración del Paso:**

| Campo de Configuración | Opciones de Valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso fuente            | -                 | Selección del paso anterior |
| Campo de información del usuario | -       | Un campo que contiene información sobre el usuario |
| Nombre de usuario      | -                 | Nombre del usuario |
| Contraseña del usuario  | -                 | Contraseña del usuario (requerida) |
| Usuario deshabilitado  | true, false       | Estado de actividad del usuario |
| Campos a actualizar    | name, email, lastName, userName, firstName, middleName | Campos para actualizar o crear información del usuario |

## Casos
- **Actualización de Información del Usuario**: Se utiliza para cambiar datos sobre usuarios existentes, incluyendo su información de contacto, nombre de usuario y otra información personal.
- **Creación de Nuevos Usuarios**: Adecuado para agregar nuevos usuarios al sistema, permitiendo expandir rápidamente y de manera eficiente la base de datos de usuarios.

## Excepciones
- **Necesidad de Precisión de Datos**: El paso requiere la entrada de datos precisa y actualizada, especialmente al crear nuevos usuarios.
- **Gestión de Contraseñas**: Cuando se actualiza la información del usuario, si la contraseña no se especifica, permanecerá sin cambios. Al crear un usuario, especificar una contraseña es obligatorio.

## Escenario de aplicación

El componente está diseñado para gestionar la información del usuario. Implica recuperar la información del usuario, actualizar sus datos y crear un nuevo registro de usuario con los parámetros especificados.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/1zrn1vRmP3BtXAp-FBsoc5OHj96JuGKvF/view?usp=sharing)