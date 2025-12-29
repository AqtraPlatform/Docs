# Vista de lista

![](../../assets/images/app-development/list-view.png)

## Información general
“Vista de lista” es un componente de UI utilizado para mostrar y configurar la presentación de datos en “tarjetas”.

## Parámetros
**Propiedades del componente**

| Grupo de configuraciones | Campo de configuración | Opciones de valor          | Propósito                         |
|--------------------------|-----------------------|----------------------------|------------------------------------|
|                          | Nombre                | -                          | Nombre del componente de UI en el sistema |
| Común                    | Componente            | Multiselección de Catálogo | Contiene una lista de todos los Componentes |
|                          | Número de columnas     | -                          | Número de columnas del contenedor      |
|                          | Número de filas       | -                          | Número de filas del contenedor         |
|                          | Espacio entre columnas | -                          | Espaciado entre columnas          |
|                          | Espacio entre filas    | -                          | Espaciado entre líneas           |
|                          | Tamaño de página      | -                          | Tamaño del contenedor                   |
|                          | Recarga manual        | true, false                | Capacidad para recargar datos manualmente |
|                          | Ocultar selector de página | true, false              | Ocultar selector de página            |
|                          | Habilitar arrastrar y soltar | true, false            | Habilitar la función de arrastrar y soltar             |
|                          | Grupo de arrastrar y soltar | -                        | Grupo de arrastrar y soltar (si lo hay)           |
|                          | ID de automatización   | -                          | ID para automatización     |
| Eventos                  | Al cargar la fuente de datos | -                        | Evento de carga de la fuente de datos |
|                          | Al cargar            | -                          | Evento de carga del componente      |
|                          | Al soltar            | -                          | Evento de arrastrar y soltar           |

**Propiedades CSS**

| Grupo de configuraciones | Campo de configuración | Opciones de valor          | Propósito                         |
|--------------------------|-----------------------|----------------------------|------------------------------------|
| Diseño                   | Ancho                 | -                          | Ancho del componente                  |
|                          | Alto                  | -                          | Alto del componente                  |
|                          | Margen                | -                          | Relleno exterior del componente          |
|                          | Relleno              | -                          | Relleno interior del componente       |
|                          | Visible               | true, false                | Visibilidad del componente               |
|                          | Oculto                | true, false                | Ocultamiento del componente               |
|                          | Orientación           | Horizontal, Vertical       | Orientación del componente              |
| Apariencia               | Radio de esquina      | -                          | Radio de redondeo de esquinas            |
|                          | Grosor del borde      | -                          | Grosor del borde del componente         |
|                          | Opacidad              | -                          | Transparencia del componente            |
| Brocha                   | Fondo                 | -                          | Color de fondo del componente               |
|                          | Brocha del borde      | -                          | Color del borde del componente            |

## Uso de la función de arrastrar y soltar
Primero, en el grupo de configuraciones “Común”, necesitas seleccionar la siguiente opción:

![](../../assets/images/app-development/enable-drag-and-drop.png)

Después de guardar y publicar, la función de arrastrar y soltar ya estará disponible para esta vista de lista en el lugar de trabajo. Para el correcto funcionamiento posterior, necesitas ir al script del componente y preparar la función para manejar el evento de arrastrar y soltar (al soltar).

Aquí hay un ejemplo de la función aplicada a un tablero kanban que consiste en una vista de lista principal y una vista de lista anidada. La principal realiza la función de las etapas del embudo de ventas y está en posición horizontal, mientras que la anidada contiene los tratos en sí y está en posición vertical. La función toma el ID del objeto que se está arrastrando (en este caso, el trato) y la etapa a la que se transfiere el trato, luego llama al flujo de datos y, si se completa con éxito, actualiza la vista de lista, moviendo el trato a una nueva etapa:

```python
def OnMove(dstList, srcList, dataObject, oldIdx, newIdx):
    context.Logger.Info("Callback on move")
    # The new Busy(boolean) method puts the UIElement into a loading status,
    # showing or hiding the loader
    srcList.Busy(True)
    dstList.Busy(True)
    
    # The new GetDynamicFilterValue(string) method computes the value of a Dynamic filter.
    # If there are two filters on one field, the first in the list is computed
    stage = dstList.GetDynamicFilterValue("data.Stage")
    
    # Creating a model to call the data-flow
    flowModel = {"Stage": stage, "OrderId": dataObject.Id}
    # Calling the data-flow with a new overload for onComplete and onError
    context.ExecuteDataflow("783cf3e3-d8f8-4551-8447-13be4f738e41", flowModel, 
    lambda res: OnDataflowComplete(res, dstList, srcList), 
    lambda ex: OnDataflowError(ex, dstList, srcList))

def OnDataflowComplete(dataResult, dstList, srcList):
    # The new Busy(boolean) method puts the UIElement into a loading status,
    # showing or hiding the loader
    srcList.Busy(False)
    dstList.Busy(False)
    # Refreshing the lists
    srcList.Refresh()
    dstList.Refresh()

def OnDataflowError(exception, dstList, srcList):
    # The new Error(boolean, string) method puts the UIElement into an error status,
    # displaying the error message
    srcList.Error(True, "An error occurred")
    dstList.Error(True)
    context.Logger.Error(exception, "An error occurred during the data-flow call")
```

## Casos
- **Visualización de datos**: Efectivo para presentar datos en forma de tarjetas o listas.
- **Interfaz de usuario**: Adecuado para interfaces que requieren representación de información en forma de tarjetas o listas.

## Excepciones
- **Flexibilidad limitada**: No es adecuado para mostrar datos más allá del formato de tarjeta o lista, ya que se especializa en una representación visual específica.
- **Limitaciones visuales**: El estilo y diseño pueden estar limitados por configuraciones CSS, que pueden no cumplir con todos los requisitos de diseño.