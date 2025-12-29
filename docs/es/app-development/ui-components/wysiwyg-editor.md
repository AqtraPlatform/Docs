# Editor WYSIWYG

![](../../assets/images/app-development/wysiwyg-editor.png)

## Información general
El editor WYSIWYG es un componente de interfaz de usuario diseñado para ingresar y editar texto enriquecido en formato WYSIWYG. Proporciona funcionalidad similar a editores como Wordpad, permitiendo a los usuarios formatear texto e insertar varios elementos multimedia con facilidad.

## Parámetros
**Propiedades del componente:**

| Grupo de configuraciones | Campo de configuración | Opciones de valor          | Propósito |
|-------------------------|-----------------------|----------------------------|-----------|
| (Configuraciones globales) | Nombre                | -                          | Nombre del componente de la interfaz en el sistema |
| Común                   | Deshabilitado         | true, false                | Deshabilitar un elemento |
|                         | Requerido             | true, false                | Campo requerido para completar |
|                         | Plugins               | -                          | Habilitar plugins |
|                         | Etiqueta              | -                          | Descripción del campo |
|                         | Vinculación           | Multiselección de Catálogo | Vinculación de datos |
| Eventos                 | Al cambiar el valor   | -                          | Evento de cambio de valor |
|                         | Al presionar tecla    | -                          | Evento de pulsación de tecla |
|                         | Al soltar tecla       | -                          | Evento de liberación de tecla |
|                         | Al enfocar            | -                          | Evento al enfocar un elemento |
| Índice de pestaña      | -                     | Entero                    | Orden de cambio de campo |

**Propiedades CSS:**

| Grupo de configuraciones | Campo de configuración | Opciones de valor          | Propósito |
|-------------------------|-----------------------|----------------------------|-----------|
| Diseño                  | Ancho                 | -                          | Ancho del componente |
|                         | Alto                  | -                          | Alto del componente |
|                         | Crecer                | true, false                | Estiramiento del componente |
|                         | Margen                | -                          | Relleno exterior |
|                         | Relleno              | -                          | Relleno interior |
| Apariencia              | Radio de esquina      | -                          | Radio de esquina |
|                         | Grosor de borde       | -                          | Grosor del borde |
| Brocha                  | Fondo                 | -                          | Color de fondo |
|                         | Brocha de borde       | -                          | Color del borde |

## Casos
- **Formateo de texto**: Utilizado para crear documentos y contenido ricamente formateados.
- **Edición de contenido**: Utilizado en sistemas de gestión de contenido para facilitar la edición de artículos, blogs y otros contenidos de texto.

## Excepciones
- **Complejidad de la interfaz**: Puede ser difícil de usar para usuarios sin experiencia con editores similares.
- **Limitaciones técnicas**: Dependiendo de la implementación, puede no soportar todas las características de editores de texto avanzados.