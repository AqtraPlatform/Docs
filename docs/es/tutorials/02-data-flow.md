# Tutorial №2 
<br>

## Creando una Aplicación Simple para un Concesionario de Autos
<br>

**Descripción de la Aplicación:**

Vamos a crear una aplicación que consiste en varios componentes que permite rastrear los autos disponibles para la venta, asignar un gerente para la firma de contratos y permitir que los gerentes cierren el trato.

**Crearemos los siguientes componentes:**

<br>

### Componente "Especialistas en Transacciones"

El primer componente será un formulario simple para agregar nuevos gerentes y consistirá en una sola propiedad personalizada:

<br>

![Tutorial 2.2](../assets/images/tutorials/tut2.1.png)

<br>

A continuación, pasamos a configurar nuestro espacio de trabajo, agregando un elemento de panel donde realizaremos nuestro trabajo. 

Luego, en la configuración del panel bajo el grupo de configuración "Diseño", cambia la orientación del panel a vertical y comienza a agregar los siguientes elementos: necesitaremos el manager_name que creamos y un botón. Debería verse así:

<br>

![Tutorial 2.2](../assets/images/tutorials/tut2.2.png)

<br>

A continuación, crea un flujo de datos, nómbralo "Agregar un gerente" y agrega los siguientes pasos: `get action model`, `update entry`, `write response`. Debería verse así:

<br>

![Tutorial 2.3](../assets/images/tutorials/tut2.3.png)

<br>

Configura el paso `Update entry` de la siguiente manera:

<br>

![Tutorial 2.4](../assets/images/tutorials/tut2.4.png)

<br>

**No olvides** establecer el `source step` para el paso `update entry`!

Después de configurar el flujo de datos, vincúlalo al botón de la siguiente manera: ve a la configuración del botón, haz clic en el grupo de configuración "acciones", establece el "tipo de comando" en "ejecutar flujo de datos" y selecciona el flujo de datos que creamos "Agregar un gerente".

Haz clic en "Guardar", "Listo para publicar". Publica el componente, luego agrégalo al lugar de trabajo utilizando el "menú de navegación" del dominio donde estás desplegando tu aplicación (en nuestro caso, este es el dominio "digital-workplace").

<br>

![Tutorial 2.5](../assets/images/tutorials/tut2.5.png)

<br>

Haz clic en "AGREGAR ELEMENTO DE MENÚ" y agrega nuestro componente:
<br>

![Tutorial 2.6](../assets/images/tutorials/tut2.6.png)

<br>

Ve a la `workplace` y agrega algunos gerentes para trabajar con ellos más adelante.

<br>

### Componente "Flota de Autos"

<br>

Con este componente, configuraremos la visualización de todos los autos y la información general sobre ellos, agregaremos un formulario para crear registros de nuevos autos, un formulario para asignar un gerente de transacciones a un auto, y un formulario para confirmar que el trato se ha completado con el posterior archivo del registro del auto. 

En este componente, crearemos una serie de propiedades personalizadas:

- `car_vin`: tipo de propiedad - `string`, título - `VIN`, configuraciones - `required`, `primary key`, `query`;
- `car_brand`: tipo de propiedad - `string`, título - `Car Brand`, configuraciones - `required`, `query`;
- `car_model`: tipo de propiedad - `string`, título - `Car Model`, configuraciones - `required`, `query`;
- `year_of_manufacture`: tipo de propiedad - `integer`, título - `Year of manufacture`, configuraciones - `required`, `query`;
- `color`: tipo de propiedad - `string`, título - `Color`, configuraciones - `required`, `query`;
- `price`: tipo de propiedad - `number`, título - `Price of the car`, configuraciones - `required`, `query`;
- `is_manager_exists`: tipo de propiedad - `boolean`, título - `Is manager exists`, configuraciones - `query`;
- `choosen_manager`: tipo de propiedad - `catalog`, componente - `Transaction Specialists` título - `Chosen Manager`, configuraciones - `query`;
- `is_archieved`: tipo de propiedad - `string`, configuraciones - `query`.

El componente constará de las siguientes partes (páginas):

<br>

1. **Página Principal**

Para agregar una página, necesitas encontrar el grupo `Layout` en el `Toolbox` y arrastrar el elemento `Page` al espacio de trabajo.
Esta página presentará una cuadrícula de datos con todos los coches disponibles para la venta y la información general sobre ellos para los gerentes de ventas. Además, agregaremos un botón a la página que redirigirá a un formulario para agregar coches a la lista, pero lo añadiremos más tarde.

Agrega un panel al espacio de trabajo, cambia la configuración de orientación a vertical, luego agrega dos paneles más. En el panel inferior, coloca el elemento de la cuadrícula de datos, y en el panel superior, agrega dos paneles más. En el panel izquierdo, coloca una etiqueta y escribe "Flota de coches" en su configuración de "valor de traducción". En el panel derecho, agrega un botón y escribe "Agregar un nuevo coche" en su "valor de traducción". Más tarde cambiaremos la configuración de "Acciones", pero por ahora, puedes cambiar el tamaño del botón en la configuración de "Diseño".

<br>

![Tutorial 2.7](../assets/images/tutorials/tuto2.7.png)

<br>

Puedes probar otras configuraciones.

A continuación, procede a configurar el `data grid`: haz clic en el ícono de engranaje y selecciona el componente para la cuadrícula de datos "Flota de coches". Luego, junto a columnas, haz clic en `+`, esto añadirá una columna a nuestra cuadrícula de datos, haz esto 5 veces.

Haz clic en la primera columna, luego "Agregar campo" y selecciona la propiedad `car_brand`. La configuración posterior debería verse así:

<br>

![Tutorial 2.8](../assets/images/tutorials/tut2.8.png)

<br>

Deberías configurar las siguientes columnas de manera similar en este orden: 2ª columna - `car_model`, 3ª columna - `year_of_manufacture`, 4ª columna - `color`, 5ª columna - `price`.

Además, en la configuración de la cuadrícula de datos, establece `Static filters`. Dado que vamos a mostrar coches que aún no han sido asignados a un gerente, establece la siguiente configuración:

<br>

![Tutorial 2.12](../assets/images/tutorials/tut2.12.png)

<br>

El resultado final en nuestro espacio de trabajo debería verse así:

<br>

![Tutorial 2.9](../assets/images/tutorials/tut2.9.png)

<br>

2. **Agregar un nuevo coche**

Esta página será accesible para el usuario al hacer clic en el botón "Agregar un nuevo coche" de nuestra página anterior. Comencemos a configurar nuestro espacio de trabajo.

Agrega un panel a la página. En su configuración, cambia la orientación de la página a vertical. A continuación, agrega dos paneles más. En el primer panel, también cambia la orientación a vertical y transfiere nuestras propiedades para que se vean así:

<br>

![Tutorial 2.10](../assets/images/tutorials/tut2.10.png)

<br>

En el panel inferior, agrega dos botones, establece su relleno como en el botón "Agregar un nuevo coche" y nómbralos de acuerdo: "Agregar un nuevo coche" y "Volver a todos los coches".

En la configuración del botón "Volver a todos los coches", establece las "Acciones" en "Abrir página" "Página principal". Hacer clic en este botón redirigirá al usuario a la página con la cuadrícula de datos. Para el botón "Agregar un nuevo coche", crea un flujo de datos, que vincularemos más tarde.

El flujo de datos constará de los siguientes pasos: `get action model`, `execute script`, `update entry`, `write response`. Vamos a configurarlos.

En el paso `execute script`, crea variables que se utilizarán para las propiedades `is_manager_exists` y `is_archieved`:

```
item["_is_manager_exists@boolean"] = False
item["_is_archieved@boolean"] = False
```

A continuación, configura el paso `Update entry`:

<br>

![Tutorial 2.13](../assets/images/tutorials/tut2.13.png)

<br>

A continuación, necesitamos mapear nuestros campos. **Recuerda** que los campos en la configuración de pasos se mapean con el prefijo data.`property_name`. Para las propiedades `is_archieved` y `is_manager_exists`, utiliza los valores de variable establecidos en el paso de script de ejecución, deja el campo `chosen_manager` vacío:

<br>

![Tutorial 2.14](../assets/images/tutorials/tut2.14.png)

<br>

**Siempre establece el paso de origen para cada paso excepto el primero. Esto no se mencionará más en la descripción del tutorial.**

Ahora que nuestro flujo de datos está completo, podemos vincularlo al botón "Agregar un nuevo coche" y guardar nuestro componente. El resultado final de nuestra página se muestra a continuación:

<br>

![Tutorial 2.15](../assets/images/tutorials/tut2.15.png)

<br>

3. **Nombrar un gerente**

Esta página se llamará como una ventana modal al hacer clic en una entrada particular en la cuadrícula de datos. Está diseñada para una única función: asignar un gerente a un coche particular. Pasemos a configurar el espacio de trabajo.
La página en sí se parecerá a la página "Agregar un nuevo coche", con la única diferencia de que añadiremos la propiedad `chosen_manager` al espacio de trabajo, que será la única propiedad disponible para modificación. Esto permite al gerente seleccionar un colega a quien transferirán el coche y el trato. Además, agregue dos botones, uno para cerrar la ventana modal llamado "Volver a todos los coches", y el otro llamado "Nombrar un gerente" que estará vinculado a un flujo de datos que crearemos más adelante.

**No olvide habilitar la configuración Deshabilitado en la configuración del TextBox para cada propiedad excepto `chosen_manager`.**

<br>

![Tutorial 2.16](../assets/images/tutorials/tut2.16.png)

<br>

El resultado final en esta página debería verse como el que se muestra a continuación:

<br>

![Tutorial 2.17](../assets/images/tutorials/tut2.17.png)

<br>

**Pasemos a configurar el flujo de datos**.

Necesitamos agregar los siguientes pasos: `get action model`, `execute script`, `lookup reference`, `update entry`, `write response`.

En el paso `execute script`, crearemos una variable que cambiará la propiedad `is_manager_exists` a True, haciendo que la entrada recién creada desaparezca de la cuadrícula de datos en la página Principal, donde hemos establecido filtros estáticos.

```
item["_is_manager_exists@boolean"] = True
```

A continuación, utilizamos el paso `Lookup reference`. Le recomiendo que lea sobre este paso en la sección de Flujo de Datos de nuestra documentación técnica. El paso debe configurarse como se muestra a continuación.

<br>

![Tutorial 2.18](../assets/images/tutorials/tut2.18.png)

<br>

A continuación, configuramos el paso `Update entry`, en la clave del componente de campo especifique el nombre del campo del paso `Lookup reference`:

<br>

![Tutorial 2.19](../assets/images/tutorials/tut2.19.png)

<br>

En 'Mapeo de campos' deje los campos vacíos excepto para `chosen_manager` y `is_manager_exists`, estos son los campos que queremos cambiar en el registro encontrado utilizando el paso `Lookup reference`.

<br>

![Tutorial 2.20](../assets/images/tutorials/tut2.20.png)

<br>

En el paso `write response`, necesitamos establecer el paso de origen.

Asigne este flujo de datos para que se ejecute cuando se presione el botón "Nombrar un gerente". Luego guarde el componente.

<br>

**Proceda al script del componente para construir la ventana modal**.

Para crear una ventana modal, puede usar el script a continuación. Para trabajar con el **script del componente** le recomiendo encarecidamente que lea la sección de documentación `Using Python`:

```
def show_model_info(model):
    context.Logger.Error("updated")

def open_custom_modal(sender, model):
    # Creating a modal window template using the GUID of a specific component
    dialog_builder = context.PlatformServices.DialogBuilder('component guid')
    # Setting the title for the modal window and selecting a specific page from the component's settings
    # Also setting the component instance ID to 1, so the first saved instance of component data will be used
    dialog_builder.WithEntryId(int(model[0].Id)).WithTitle("Appoint a manager").WithPageId('page id')
    # Setting the size of the modal window
    dialog_builder.WithVSize("650px").WithHSize("820px")
    dialog_builder.OnComplete(lambda model: show_model_info(model))
    dialog_builder.OnCancel(update_cars_success)
    # Opening the created modal window
    dialog_builder.OpenDialog()
    
def get_datagrid_cars(sender, *args):
    global datagrid_cars
    datagrid_cars = sender
    
def update_cars_success():
    datagrid_cars.Refresh()
```

Las funciones `get_datagrid_cars` y `update_cars_success` se utilizan para actualizar automáticamente la cuadrícula de datos después de alguna acción. Si no las utiliza, la cuadrícula de datos solo se actualizará después de refrescar la página en el navegador. Después de copiar, necesita guardar el componente y regresar al espacio de trabajo en la "Página Principal".

Necesita ir a la configuración de la cuadrícula de datos en el grupo de configuraciones `Events`, y asignar la ejecución de funciones a ciertas acciones en la cuadrícula de datos.

<br>

![Tutorial 2.21](../assets/images/tutorials/tut2.21.png)

<br>

Guarde el componente, luego proceda a configurar la siguiente página.

4. **Entrar en un contrato**

Esta página es un formulario que permite al gerente archivar un trato de coche particular cambiando el campo `is_archieved` a `True`.

La página es una copia de la página `Appoint a manager`, la única diferencia es que todos los campos tienen la configuración `Disabled` -> `True`. En la parte inferior, agregaremos dos botones, uno de los cuales lanzará el flujo de datos, y el otro redirigirá al usuario a la página del componente que aún no hemos creado.

La página en sí debería verse así:

<br>

![Tutorial 2.22](../assets/images/tutorials/tut2.22.png)

<br>

Pasemos a crear y configurar el flujo de datos. Necesitaremos 5 pasos: `get action model`, `execute script`, `update entry`, `form action`, `write response`.

En el paso `execute script`, crearemos una variable que establecerá el valor `True` en la propiedad `is_archieved`.

```
item["_is_archieved@boolean"] = True
```

La configuración del paso `update entry` debería verse así:

<br>

![Tutorial 2.23](../assets/images/tutorials/tut2.23.png)

<br>
En el campo de la clave del componente, proporcionaremos una referencia al registro que queremos editar, luego procederemos a "Mapeo de campos". Aquí dejamos todos los campos vacíos excepto por `is_archieved`. Aquí ponemos la variable que configuramos en el paso `execute script`.

A continuación está el paso `Form action`, al que volveremos después de crear el componente final. Por ahora, guarda el componente para evitar perder tu trabajo.

### Componente "Matriz de gerentes"

Este componente consistirá en una sola página y no crearemos propiedades personalizadas para él. Este componente solo será utilizado por gerentes que tengan acceso a él, permitiéndoles ver todos los coches que han sido movidos a la etapa de trato y asignados a un gerente particular.

Crea una cuadrícula de datos, vincúlala al componente `Car fleet` y agrega una columna para cada una de sus propiedades. El resultado debería verse así:

<br>

![Tutorial 2.24](../assets/images/tutorials/tut2.24.png)

<br>

Luego ve al grupo de configuraciones `Actions`, establece el tipo de comando en `Open application`, el componente en `Car fleet`, la página del componente en `Enter into a contract`, una página que creamos como la última página del componente `Car fleet`.

A continuación, haz clic en el botón `Action parameters` y mapea Id -> Id como se muestra a continuación.

<br>

![Tutorial 2.25](../assets/images/tutorials/tut2.25.png)

<br>

Guardemos el componente y vayamos a sus configuraciones. Además de nombrar y seleccionar el dominio requerido, necesitamos marcar la casilla `Restrict access` para que podamos establecer permisos de seguridad especiales para este componente.

Guardemos nuevamente, marquemos el componente como listo para publicar y agrégalo a la `Navigation menu` del dominio que estamos utilizando.

<br>

**Regresar al componente `Car fleet` en la página `Enter into a contract`**

Queda un botón sin usar, `Back to all contracts`, establezcamos su `Command type` en el grupo de configuraciones `Actions` a `Navigation back`.

A continuación, necesitamos volver al flujo de datos "El trato está hecho" y terminar de configurar el paso `Form action`. La configuración final del paso debería verse así:

<br>

![Tutorial 2.26](../assets/images/tutorials/tut2.26.png)

<br>

**No olvides seleccionar el `source step` en el paso `update entry`**.

Guarda, publica el componente, agrégalo al lugar de trabajo utilizando el `Navigation menu` y asegúrate de que todos los componentes estén en su lugar.

<br>

### Configuración de acceso al componente `Managers grid`

Necesitas ir al menú "Acceso" en la sección "Permisos" y hacer clic en el botón "Agregar" en la esquina superior derecha.

Se abrirá una ventana de configuración de permisos en tu pantalla, donde necesitas especificar el dominio y dar un nombre al permiso. Para otorgar acceso para manipular el componente `Managers grid`, ve a `Permissions`, ingresa a la sección `Components`, encuentra nuestro componente `Managers grid` y selecciona derechos de acceso completo para él. Haz clic en el botón "Guardar" y procede a la siguiente sección "Roles".

Aquí también necesitas hacer clic en el botón "AGREGAR", seleccionar el dominio requerido, nombrarlo y seleccionar el "Permiso" que creaste anteriormente. Luego procede a la sección `Users`.

En la sección `Users`, se enumeran todos los usuarios registrados en tu sistema. Haz clic en el usuario al que deseas otorgar derechos para usar este componente, en "Seleccionar contextos" elige "Plataforma" -> "Sistema" y en "Seleccionar roles" encuentra el rol que creaste anteriormente, luego haz clic en la casilla de verificación y haz clic en "Guardar".

<br>

### Conclusión

Has creado una pequeña y simple aplicación en la que trabajaste con varios componentes y aprendiste cómo enlazarlos. Aprendiste a crear ventanas modales y comenzaste a explorar la interacción entre lenguajes de programación y las herramientas de nuestra plataforma.

Intenta crear varios gerentes, agregar nuevos coches en venta, asignarles gerentes y tratar de cerrar tratos.
Por supuesto, esta aplicación es una prueba; se puede mejorar y hacer más compleja indefinidamente. Después de crearla, puedes usar otras herramientas por tu cuenta, construir lógica diferente y personalizar el diseño a tu gusto. ¡La plataforma te proporciona herramientas flexibles que hacen que el desarrollo sea más emocionante y fácil!

Las descripciones de las herramientas utilizadas en el tutorial se pueden encontrar en la sección "Desarrollo de Aplicaciones".