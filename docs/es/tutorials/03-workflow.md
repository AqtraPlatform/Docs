# Tutorial №3

<br>

## Usando Python

### Introducción

<br>

La plataforma proporciona la capacidad de usar Python para diversos propósitos como un lenguaje de scripting/programación conveniente y ampliamente conocido.

Los scripts de Python soportados por la plataforma deben usar la versión 3.0 de Python, como se describe aquí: https://docs.python.org/3/. La guía completa para desarrolladores se puede encontrar en la sección "Usando Python".

La versión de Python utilizada por la plataforma se llama Iron Python, que proporciona una interfaz para el código C#. Proporciona dos bibliotecas importantes que deben ser importadas al principio del script — `clr` y `system`. Estas bibliotecas proporcionan acceso a entidades de la plataforma que pueden ser consultadas y controladas desde el script.
<br>

### Formas de Usar Scripts de Python en la Plataforma

<br>

Hay varias formas de usar Python en la plataforma:

- Permite controlar formularios de aplicación diseñados y ejecutados utilizando la plataforma, así como proporcionar índices personalizados que pueden ser activados en respuesta a un evento, como un cliente presionando un botón.
  <br>

- Llamando a una Función Dentro de un "Script de Componente", por Ejemplo, Cuando se Presiona un Botón:

  - Para hacer esto, necesitas definir una función dentro del Script de Componente, luego ir a un elemento de control de UI como un Botón, ir a la sección "Acciones" y establecer el parámetro "Tipo de Comando" en "Ejecutar Script". Luego necesitas ingresar el nombre y los parámetros de llamada (si los hay) de tu script en los campos proporcionados.
    <br>

- Usando una Función Dentro de un Script de Componente para Eventos de Cambio de Valor:
  - Para hacer esto, necesitas definir una función dentro del script del componente, luego ir a un elemento de control de UI como un cuadro de texto, etc., luego ir a la sección "Eventos" e ingresar el nombre de tu script en el campo "Al cambiar el valor".
  - Ten en cuenta que esta función solo se llamará si los datos en el campo han cambiado y el foco del elemento de control de UI en el formulario sale de este elemento de control de UI.

<br>

- Suscribiéndose a Cambios de Datos Usando el Método `context.DataModel.Model.Subscribe()`:
  - La forma más fácil de hacer esto es definir una función para interceptar todos los cambios (por ejemplo, `def check_all_changes()`) en tu script de componente, y luego suscribirte a ella.
  - Tu función será llamada cada vez que haya un cambio en los datos actuales del elemento de control de UI, en el momento en que este elemento de control de UI pierde el foco (por ejemplo, cuando el usuario cambia a otro elemento de control de UI o a otra aplicación).

<br>

- Como parte de una acción de DataFlow, ejecuta un script para definir la lógica de toma de decisiones, transformar datos y establecer variables internas que se utilizarán como parte de los scripts de DataFlow. Puedes ver ejemplos de uso de scripts de Python para DataFlow en la sección "Usando Python".

<br>

### Usando Python para Acceder a Componentes de la Plataforma

<br>

Para acceder a los componentes de la plataforma, primero necesitas importar las bibliotecas clr de IronPython, como se muestra a continuación.

```
#Add IronPython library that imports system CRL (.NET) names into Python
import clr
```

Después de importar, varios objetos pueden ser accedidos desde dentro del script de Python a través de la variable del sistema `context`.

<br>

### Usando context.Model & context.DataModel

<br>

`context.Model` & `context.DataModel` proporcionan acceso a varios campos de datos del modelo de la plataforma.

Para context.Model, los campos de datos incluyen tanto los campos de componente predeterminados proporcionados por la plataforma como los campos personalizados añadidos por el desarrollador del componente.

Para context.DataModel, solo están disponibles los campos personalizados añadidos por los desarrolladores de componentes.

Se recomienda que se use context.DataModel para acceder a todos los campos personalizados, y que context.Model se use solo para acceder a los campos internos del componente predeterminado.

Si escribimos un script de componente que accede a este modelo, las siguientes variables del modelo del sistema estarán disponibles en nuestro script a través de context.Model:
- `Id` - identificador interno, generado automáticamente por la plataforma para cada componente. Si Id == 0, significa que los datos del componente aún no se han guardado, indicando que estamos en el modo de entrada de datos para esta instancia particular de los datos del componente, como agregar una nueva factura en nuestro Tutorial #1.
- `createDate` - fecha establecida internamente cuando se creó por primera vez la instancia de datos de este componente
- `name` (String) - nombre amigable para el sistema que se tomará por defecto para mostrar enlaces a través de campos de tipo Catálogo
- `updateDate` - fecha establecida internamente de la última actualización de la instancia de datos de este componente.
- `CreatorSubject` - datos que muestran qué usuario agregó la instancia de datos de este componente particular.
- `changeAuthor` - datos que muestran qué usuario actualizó por última vez este componente particular

Además, los siguientes atributos específicos del componente estarán disponibles para nuestro componente del Tutorial #1 a través de context.DataModel (recomendado) o context.Model:

- `InvoiceName` - nombre único para nuestra nueva factura
- `InvoiceState` - estado actual de nuestra nueva factura
- `InvoiceNumber` - identificador numérico único para nuestra factura
- `InvoiceDueDate` - fecha de vencimiento de nuestra factura
- `InvoiceTotalValue` - valor total de nuestra factura

Ahora escribamos un script de ejemplo que prellenará algunos campos para una nueva factura.

<br>

```python
#Start of the script
#Add IronPython library that imports system CRL (.NET) names into Python
import clr

#Get Component’s DataModel reference
datamodel = context.DataModel.Model
# context.Model.Id shows internal Id for the component data instance
if (context.Model.Id == 0):
# If context.Model.Id is 0, then the instance has not yet been created,
# That means we are creating a new invoice
# We will then set some fields with default values
# Since this is a new Invoice,
# We’ll set it’s status to Under Review and provide default number and name
datamodel.InvoiceNumber = 11111
datamodel.InvoiceName = 'PLEASE_SET_A_UNIQUE_NAME'
datamodel.InvoiceState = 0
#End of the script
```

<br>

Ahora, si abrimos la aplicación del Tutorial #1 y hacemos clic en el botón "Agregar" para añadir una nueva factura, la pantalla se verá así:

<br>

![Tutorial 3.1](../assets/images/tutorials/tut3.1.png)

<br>

### Usando context.Properties

<br>

`context.Properties` permite el acceso a todos los elementos del componente y se puede utilizar, por ejemplo, para utilizar funciones de elementos de control de UI de formularios para gestionar un elemento de control de UI específico.

Para acceder a un elemento de control de UI, utiliza `context.Properties` de la siguiente manera:

```
context.Properties.<Internal_UI_Control_Name>.<UIControlProperty> = <Value>
```

Aquí, `<Internal_UI_Control_Name>` debe ser reemplazado con el nombre de tu elemento de control de UI que configuraste durante el diseño. Por ejemplo, en el caso del Tutorial #1, establecimos el nombre interno para el elemento de control de UI InvoiceState como se muestra a continuación:

<br>

![Tutorial 3.2](../assets/images/tutorials/tut3.2.png)

<br>

Ahora podemos usar este nombre interno para establecer la siguiente lógica:

1. Al crear una nueva factura, el estado se establece en "En Revisión".
2. Cambiar el campo de estado está prohibido, lo que significa que este campo debe estar deshabilitado pero visible.

La forma de hacerlo es usar la propiedad `Disable` de nuestro elemento de control de UI para establecerlo en `True`. Esto hará que el campo aparezca, pero no puede ser cambiado por el usuario que crea la nueva factura. Esto se hace añadiendo una línea de código como se muestra a continuación:

```
context.Properties.UI_InvoiceStatus.Disabled = True
```

Agregar esto a nuestro script de componente resultará en los siguientes cambios en nuestro formulario de adición de nueva factura.

<br>

![Tutorial 3.3](../assets/images/tutorials/tut3.3.png)

<br>

Como puedes ver, el campo "Estado de la Factura" ahora está deshabilitado.

Otro campo frecuentemente utilizado `context.Properties` para gestionar elementos de control de UI es `Visible`. Si se establece en `False`, este elemento de control de UI específico no aparecerá en el formulario. Luego se puede volver a habilitar estableciéndolo en `True`. Esto se puede hacer para cualquier elemento de control de UI, incluidos paneles que contienen varios elementos de control de UI diferentes.

Un ejemplo de cómo se puede usar en el contexto de nuestro Tutorial #1 para ocultar inicialmente el campo "Estado de la Factura" se muestra a continuación.

<br>

```python
if (context.Model.Id == 0):
    context.Properties.UI_InvoiceStatus.Visible = False
if (context.Model.Id > 0):
    context.Properties.UI_InvoiceStatus.Visible = True
```

<br>

También existe el campo `Hidden`, que oculta/muestra elementos de la interfaz de usuario, similar al campo `Visible`.

Otro campo frecuentemente utilizado `context.Properties` es `Required`. Si se establece en `True`, el elemento de control de UI específico se vuelve obligatorio (no puede estar vacío), y si se establece en `False`, se vuelve opcional. Ten en cuenta que esto solo cambia el estado del elemento de control de UI para la propiedad personalizada en la instancia actual del formulario, no la propiedad personalizada en sí, la plantilla del formulario, o los elementos de control de UI para esta propiedad personalizada en otros formularios.

<br>
### Usando context.Form

<br>

`context.Form` se puede usar para acceder a los datos del formulario (por ejemplo, para propósitos de validación durante el procesamiento del formulario, antes de que los datos del formulario se guarden en el almacenamiento interno) o para gestionar la representación visual del formulario, como al establecer un mensaje de error.

Para hacer esto, utiliza `context.Form.Get(<CustomFieldName>)` para obtener un objeto que representa un campo específico. Luego puedes usar las siguientes funciones con este objeto.

- `context.Form.Get(<CustomFieldName>).SetValue(<Value>)` — establece el valor para un control de UI específico en el formulario actual.
- `context.Form.Get(<CustomFieldName>).AddError(<StringValue>)` — establece un mensaje de error que se muestra debajo de un control de UI específico en el formulario actual.
- `context.Form.Get(<CustomFieldName>).ClearError()` — borra el mensaje de error mostrado debajo de un control de UI específico en el formulario actual.

La siguiente extensión de script muestra cómo verificar la situación en la que el usuario no cambió el nombre de factura predeterminado que establecimos anteriormente en los ejemplos del Tutorial #1.

<br>

```python
if datamodel.InvoiceName == 'PLEASE_SET_A_UNIQUE_NAME':
    context.Form.Get("InvoiceName").AddError("Please set a unique invoice name")
else:
    context.Form.Get("InvoiceName").ClearError()
```

<br>

El resultado se verá como la siguiente captura de pantalla si el nombre predeterminado no fue cambiado:

<br>

![Tutorial 3.4](../assets/images/tutorials/tut3.4.png)

<br>

### Usando context.Commands

<br>

`context.Commands` se puede usar para gestionar la UI del componente que se está ejecutando actualmente, cambiar el contenido del formulario actual, abrir diferentes páginas, abrir nuevos componentes, regresar a la página anterior, o incluso lanzar nuevos Workflows, Dataflows o Scripts.

Estos comandos se utilizan típicamente dentro de scripts llamados por la acción ExecuteScript usando botones, y en casos similares. Por ejemplo, en nuestro Tutorial #1, el botón Regresar a Todas las Facturas puede usar el siguiente script para volver a la página anterior:

<br>

```python
def navigate_back():
    context.Commands.NavigationBack()
```

<br>

Este script debe ser parte del script del componente y configurarse para el botón Regresar a Todas las Facturas, en la sección `Actions` -> `Command Type`: `Execute Script` -> `Method Name`: `navigate back`.

<br>

Otras funciones disponibles de context.Commands:

- `context.Commands.AddItem(GUID)` - agregar un elemento de control de UI a la página usando el GUID.
- `context.Commands.ChangePageAsync(GUID)` - abrir una página usando su GUID
- `context.Commands.ChangePageByName(«PageName»)` - cambiar la página del componente actual a una nueva página usando el nombre interno
- `context.Commands.OpenComponent(GUID ComponentID, GUID PageID)` - abrir un nuevo componente y una página específica dentro del componente
- `context.Commands.EditItem(GUID UI_ControlID, EntityId)` - desplazar el enfoque de la UI a un elemento de control de UI específico y datos específicos (usando su identificador interno)
- `context.Commands.ExecuteWorkflow(GUID WorkflowID)` - ejecutar un workflow usando su identificador. Además, puedes establecer WaitComplete en verdadero o falso si es necesario.
- `context.Commands.ExecuteDataflow(GUID dataflow identifier, ContextID)` - ejecutar un dataflow usando su GUID y el contexto de datos especificado.
- `context.Commands.ExecuteScript(String ScriptName, StringParams Script)` - ejecutar un script (función) desde el Script del Componente con algunos parámetros.