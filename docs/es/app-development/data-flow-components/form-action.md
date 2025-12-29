# Acción del formulario

![](../../assets/images/app-development/form-action.png)

## Información general
El paso “Acción del formulario” se utiliza para realizar diversas acciones en la interfaz de usuario (UI) en el frontend de la aplicación, como abrir páginas, ejecutar scripts, abrir ventanas modales, etc. El paso es el enlace entre la lógica del servidor y la interfaz de usuario, lo que te permite controlar dinámicamente el comportamiento de la UI.

## Parámetros
**Configuración del paso:**

| Campo de configuración | Opciones de valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso de origen         | Multiselección de Catálogo | Selección de los pasos anteriores |
| Acción del formulario   | Ejecutar script, Abrir página, Abrir componente, Abrir barra lateral, Abrir modal, Abrir archivo en nueva pestaña | Tipo de comando de la UI |
| Nombre del método      | (Si se selecciona ‘Ejecutar script’) | Nombre de la función de script a ejecutar |
| Abrir página           | (Si se selecciona ‘Abrir página’) | Lista de páginas a abrir |
| Campo de información del archivo | (Si se selecciona ‘Abrir archivo’ en nueva pestaña) | Campo de información del archivo a abrir |
| Abrir barra lateral    | Configuraciones para la barra lateral | Configuración para abrir la barra lateral |
| Abrir modal            | Configuraciones para ventanas modales | Configuración para abrir una ventana modal |

## Casos
- **Gestión dinámica de elementos de UI**: Usar “Abrir barra lateral” o “Abrir modal” permite mostrar dinámicamente barras laterales o modales con información adicional, formularios u otro contenido, lo que aumenta la interactividad y usabilidad de la interfaz.
- **Actualización de la cuadrícula de datos**: En un script donde el usuario carga nuevos datos, puedes agregar una función de actualización al formulario y la cuadrícula de datos se actualizará sin necesidad de refrescar la página.

## Excepciones
- **Se requiere paso de escritura de respuesta**: Después de realizar acciones como abrir una página o archivo, necesitas agregar un paso de “Escribir respuesta” para completar correctamente el flujo de datos.
- **Dependencia de pasos anteriores**: Al usar ciertas acciones, como “Abrir archivo en nueva pestaña”, necesitas tener un archivo apropiado preparado por los pasos anteriores.

## Escenario de aplicación

Este componente emplea varios métodos en el paso de Acción del formulario para interactuar con la interfaz de usuario en el frontend. Los usuarios pueden realizar diferentes acciones como ejecutar un script (Ejecutar script), abrir una página (Abrir página) o un componente (Abrir componente), descargar un archivo (Descargar archivo) y abrir un archivo en una nueva pestaña (Abrir archivo en nueva pestaña). Después de que se ejecutan estas acciones, los datos se procesan y se envían de vuelta al frontend utilizando el paso de Escribir respuesta.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/1AgjjrOW-z2LPMj7sFWg_PKjHjFfVtxub/view?usp=sharing)