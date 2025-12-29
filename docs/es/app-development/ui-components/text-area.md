# Área de texto

![](../../assets/images/app-development/text-area.png)

## Información general
El área de texto es un componente básico de la interfaz de usuario diseñado para ingresar y mostrar texto en múltiples líneas. Es ideal para escribir grandes cantidades de texto, como comentarios o descripciones, y proporciona suficiente espacio para una escritura fácil.

## Parámetros
**Propiedades del componente:**

| Grupo de configuraciones | Campo de configuración | Opciones de valor         | Propósito |
|-------------------------|-----------------------|---------------------------|------------|
| (Configuraciones globales) | Nombre                | -                         | Nombre del componente de la interfaz de usuario en el sistema |
| Común                   | Deshabilitado         | true, false               | Deshabilitar un elemento |
|                         | Tamaño automático     | true, false               | Control de dimensiones automático |
|                         | Requerido             | true, false               | Campo obligatorio para completar |
|                         | Etiqueta              | -                         | Descripción del campo de entrada |
|                         | Vinculación           | Multiselección de Catálogo | Vinculación de datos |
| Eventos                 | Al cambiar el valor   | -                         | Evento de cambio de valor |
| Índice de tabulación    | -                     | Entero                   | Orden de cambio de campo |

**Propiedades CSS:**

| Grupo de configuraciones | Campo de configuración | Opciones de valor         | Propósito |
|-------------------------|-----------------------|---------------------------|------------|
| Diseño                  | Ancho                 | -                         | Ancho del componente |
|                         | Alto                  | -                         | Alto del componente |
|                         | Crecer                | true, false               | Estiramiento del componente |
|                         | Margen                | -                         | Relleno exterior |
|                         | Relleno              | -                         | Relleno interior |
| Apariencia              | Radio de esquina      | -                         | Radio de esquina |
|                         | Grosor del borde      | -                         | Grosor del borde |
| Brocha                  | Fondo                 | -                         | Color de fondo |
|                         | Brocha del borde      | -                         | Color del borde |

## Casos
- **Entrada de múltiples líneas**: Ideal para formularios que requieren grandes cantidades de texto.
- **Comentarios y descripciones**: Utilizado para escribir comentarios, descripciones o cualquier otro script donde se requiera entrada de múltiples líneas.

## Excepciones
- **Formato limitado**: Al igual que la mayoría de los campos de entrada de texto, el área de texto restringe el uso de formatos complejos, como hipervínculos o imágenes incrustadas.