# Restablecer a borrador

![](../../assets/images/app-development/reset-to-draft.png)

## Información general
El paso “Restablecer a Borrador” dentro del flujo de trabajo se utiliza para devolver el script al estado de “no en ejecución”. Este paso es útil en situaciones donde necesitas poder editar o revisar una solicitud o proceso mientras está siendo aprobado o ejecutado.

## Parámetros
**Configuraciones del paso:**

| Campo de configuración | Propósito |
|------------------------|-----------|
| Nombre del paso        | Nombre del paso “Restablecer a Borrador” |

## Casos
- **Edición Durante el Proceso de Aprobación**: Se utiliza para proporcionar una oportunidad de realizar cambios en una aplicación o proceso que ya está en la etapa de aprobación o implementación, lo cual puede ser necesario para corregir o aclarar la información.
- **Gestión de Procesos Flexible**: Adecuado para scripts donde necesitas la capacidad de revertir un proceso a su estado inicial para prevenir errores o ejecuciones incorrectas.

## Excepciones
- **Monitorear el Proceso de Reversión**: Debes asegurarte de que el proceso de reversión no comprometa la integridad de los datos y la lógica del flujo de trabajo.