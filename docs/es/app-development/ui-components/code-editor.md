# Editor de Código

![](../../assets/images/app-development/code-editor.png)

## Información general
El Editor de Código es un componente de UI especializado diseñado para ingresar y mostrar código de programa. Soporta varios lenguajes de programación como JavaScript, Python, etc., y proporciona funcionalidad para una fácil edición de código, pero el elemento no soporta un compilador.

## Parámetros
**Propiedades del Componente:**

| Grupo de configuraciones | Campo de configuración | Opciones de valor          | Propósito |
|-------------------------|-----------------------|----------------------------|-----------|
| (Configuraciones globales) | Nombre                | -                          | Nombre del Componente de UI en el sistema |
| Común                   | Deshabilitado         | true, false                | Deshabilitar un elemento |
|                         | Requerido             | true, false                | Campo requerido para completar |
|                         | Tema                  | -                          | Estilo visual del editor |
|                         | Modo                  | -                          | Lenguaje de programación |
|                         | Etiqueta              | -                          | Descripción del campo |
|                         | Vinculación           | Multiselección de Catálogo | Vinculación de datos |
| Eventos                 | Al cambiar valor      | -                          | Evento de cambio de valor |
|                         | Al presionar tecla    | -                          | Evento de presión de tecla |
|                         | Al soltar tecla       | -                          | Evento de liberación de tecla |
|                         | Al enfocar            | -                          | Evento al enfocar en un elemento |
| Índice de pestaña      | -                     | Entero                    | Orden de cambio de campo |

**Propiedades CSS:**

| Grupo de configuraciones | Campo de configuración | Opciones de valor          | Propósito |
|-------------------------|-----------------------|----------------------------|-----------|
| Diseño                  | Ancho                 | -                          | Ancho del componente |
|                         | Alto                  | -                          | Alto del componente |
|                         | Crecer                | true, false                | Estiramiento del componente |
|                         | Margen                | -                          | Relleno exterior |
|                         | Relleno              | -                          | Relleno interior |
| Apariencia              | Radio de esquinas     | -                          | Radio de las esquinas |
|                         | Grosor del borde      | -                          | Grosor del borde |
| Brocha                  | Fondo                 | -                          | Color de fondo |
|                         | Brocha del borde      | -                          | Color del borde |

## Casos
- **Edición de Código**: Utilizado para ingresar y editar código de programa en varios lenguajes de programación.
- **Entrenamiento y Demostración**: Utilizado con fines educativos y de demostración para mostrar ejemplos de código.

## Excepciones
- **Limitaciones de Funcionalidad**: Dependiendo de la implementación, puede no soportar todas las características de entornos de desarrollo avanzados.