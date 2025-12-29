# Tutorial №1

<br>

## Creando Tu Primera Aplicación — Inventario de Facturas

<br>

**Descripción de la Aplicación: Inventario de Facturas**

Vamos a crear una aplicación simple que te permita agregar, ver y editar facturas.

Cada factura contendrá los siguientes datos (ver la tabla a continuación).

| Breve Descripción    | Descripción Detallada                                         |
| -------------------- | ------------------------------------------------------------ |
| Número de Factura    | Número asignado a la factura por el proveedor.              |
| Título de la Factura | Descripción del ítem de la factura.                          |
| Monto Total de la Factura | Número que indica la cantidad de dinero facturado en la factura. |
| Fecha de Vencimiento de la Factura | Fecha en la que la factura debe ser pagada.                    |

<br>

Además, rastrearemos el estado de la factura de la siguiente manera (ver la tabla a continuación).

| ID  | Título Legible       | Descripción                                                                          |
| --- | -------------------- | ------------------------------------------------------------------------------------ |
| 0   | En Revisión          | Asignado inmediatamente tras la creación de la factura.                             |
| 1   | Aceptado para Pago   | Asignado después de la revisión de la factura y la aprobación para el pago.        |
| 2   | Rechazado            | Asignado después de que se completa la revisión, pero la factura no es aceptada para el pago. |
| 3   | Pagado               | Asignado después de que la factura es pagada.                                       |
| 4   | Vencido              | Indica que la factura está impaga y la fecha de vencimiento ha pasado.              |

<br>

La versión básica de la aplicación tendrá 2 pantallas principales.

- Una lista de todas las facturas en el sistema, que se puede filtrar y/o ordenar utilizando todos los campos de factura descritos anteriormente. La llamaremos “Todas las Facturas”.
- Una pantalla para agregar una nueva o editar una factura existente. La llamaremos “Editar/Ver Factura”.

Después de la creación, la aplicación se verá como la captura de pantalla a continuación.

<br>

![Tutorial 1](../assets/images/tutorials/tut1.png)

<br>

## Abriendo Studio

Crear una aplicación en la plataforma comienza con abrir Studio y agregar un componente.

Puedes abrir Studio usando el enlace https://<your_hosting_name>/studio/.

Por ejemplo, si el nombre de dominio donde implementaste tu instancia de la plataforma es [my.platform.io](http://my.platform.io/), puedes acceder a Studio usando la siguiente URL: “[https://my.platform.io/studio/”](https://my.platform.io/studio/%E2%80%9D).

Después de iniciar sesión en Studio, verás la siguiente pantalla con un menú a la izquierda que lista Inicio, Aplicaciones y Acceso. Selecciona Aplicaciones→Componentes.

<br>

![Tutorial 2](../assets/images/tutorials/tut2.png)

<br>

Verás una lista de todos los componentes existentes. Haz clic en el botón “Agregar” y selecciona la opción “Componente”, como se muestra a continuación.

<br>

![Tutorial 3](../assets/images/tutorials/tut3.png)

<br>

¡Felicidades, ahora tienes tu primer componente! Vamos a nombrarlo “Inventario de Facturas” y establecer algunos parámetros importantes.

Para nombrar tu componente, haz clic en el botón “Configuración” y luego coloca “Inventario de Facturas” en el campo “Nombre”.

Dado que nuestra aplicación solo será accesible para personas con las credenciales de inicio de sesión apropiadas, necesitamos asegurarnos de que el campo “Modo de Acceso” esté configurado como “Privado”.

## Configurando Campos de Datos Requeridos

Haz clic en Guardar para asegurarte de que tu componente esté guardado. Mostrará un mensaje de error porque aún no tenemos datos en nuestro componente. Vamos a agregar algunos datos.
Ve a la pestaña "Definición" y haz clic en el signo "+" junto a "Inventario de Facturas". La plataforma agregará automáticamente varios campos del sistema que ves en la captura de pantalla, así como tu primer campo de datos — Property_1.

<br>

![Tutorial 4](../assets/images/tutorials/tut4.png)

<br>

Haz clic en el ícono de editar (lápiz) en Property_1. Verás un nuevo panel abrirse a la derecha. Aquí es donde defines cómo deben ser interpretados tus campos de datos por el sistema.
Nombre — este es el nombre interno del sistema para su campo de datos (propiedad). Debe contener solo letras en inglés, sin espacios. Usará este nombre más adelante, por ejemplo, en scripts de Python para agregar alguna lógica avanzada a la aplicación.

_Note: a partir de la versión 0.4.x, también hay una propiedad del sistema “name” que se agrega automáticamente cuando se crea la primera propiedad y se utiliza cuando necesita mostrar a los usuarios valores para los usuarios al usar propiedades del tipo Catálogo (enlace a otro componente; utilizado para relaciones 1:1 y M:1) o Array (enlace a un array de otros componentes; utilizado para relaciones 1:M y M:M). A diferencia del Nombre interno del sistema que está presente para cada propiedad dentro del componente, el campo del sistema name es uno para todo el componente._

Título — así es como se nombrará su campo de datos en la interfaz de usuario. Aquí puede usar cualquier carácter que necesite.

Para los campos de datos que deben estar siempre no vacíos, asegúrese de que la casilla “Requerido” esté seleccionada.

El Tipo de Propiedad le permite seleccionar uno de los tipos de campo de datos disponibles.

Para comenzar, agregaremos el campo de datos Nombre de la Factura y estableceremos el tipo de propiedad en String. Dado que los nombres de las facturas provienen teóricamente de proveedores externos, pueden repetirse, por lo que no establecemos la bandera de Clave Primaria aquí.

<br>

![Tutorial 5](../assets/images/tutorials/tut5.png)

<br>

Una vez que hayamos terminado de configurar nuestro primer campo, hagamos clic en Guardar.

Ahora agreguemos los otros campos que necesitaremos en nuestra aplicación: número de factura, fecha de vencimiento de la factura, monto total de la factura y estado de la factura.

**Número de Factura** es el número de cuenta interno de cada factura única, que generalmente coincide con el nombre de la factura, pero nos aseguraremos de que tenga al menos 2 caracteres de longitud estableciendo el valor de Longitud Mínima en 2, como se muestra a continuación. También debe ser único para distinguir diferentes facturas, incluso si tienen los mismos nombres, por lo que establecemos la bandera de Clave Primaria. Esto le dice a la plataforma que no puede haber más de una propiedad Número de Factura con el mismo valor. Si se intenta crear un valor duplicado, el sistema dará un error.

<br>

![Tutorial 6](../assets/images/tutorials/tut6.png)

<br>

Para la fecha de vencimiento de la factura esperada, establezca el tipo de Propiedad en DateTime.

<br>

![Tutorial 7](../assets/images/tutorials/tut7.png)

<br>

El monto total de la factura debe establecerse como un número. También estableceremos el campo de Valor Mínimo en 0 para asegurarnos de que no haya facturas negativas (esto podría ser diferente en una aplicación financiera real donde se utilizan valores negativos, por ejemplo, para representar créditos de proveedores).

<br>

![Tutorial 8](../assets/images/tutorials/tut8.png)

<br>

Finalmente, agregaremos el campo “Estado de la Factura”. Como se indica en la descripción de la aplicación, este será un conjunto de estados que debería verse como sigue:

0|En Revisión  
1|Aceptado para Pago  
2|Rechazado  
3|Pagado  
4|Vencido  

Para esto, necesitamos establecer el tipo de propiedad en Integer (a partir de la versión 0.5.24 y superiores) y marcar la casilla Enum. Luego necesitamos agregar todos los estados disponibles en el formato <Número>|<Nombre>, como se muestra a continuación.

<br>

![Tutorial 9](../assets/images/tutorials/tut9.png)

<br>

Haga clic en “Guardar”. Debería ver el modelo de datos completamente configurado, como se muestra a continuación.

<br>

![Tutorial 10](../assets/images/tutorials/tut10.png)

<br>

## Configurando la Interfaz para Nuestra Aplicación

Ahora necesitamos configurar la interfaz de usuario para nuestra aplicación. Como se describió anteriormente, necesitaremos 2 pantallas:

1. Una pantalla para agregar una nueva o editar una factura existente. La llamaremos “Agregar/Ver Factura”.
2. Una lista de todas las facturas en el sistema, que se puede filtrar y/o ordenar utilizando todos los campos de factura descritos anteriormente. La llamaremos “Todas las Facturas”.

## Configurando la Página Agregar/Ver Factura

Ya tenemos una página predeterminada agregada automáticamente llamada “Página Principal” arriba.

En la versión actual de la plataforma, la primera página del componente por defecto se utiliza como un formulario para ver y editar datos del componente cuando no hay un formulario explícito para ver y editar. Por ejemplo, en nuestro caso, el control de interfaz de usuario Data Grid que utilizaremos para la página Todas las Facturas abrirá por defecto la primera página de nuestro componente.
Usaremos también la primera página para el formulario para ver y editar nuestra factura, y para esto la renombraremos de Página Principal a Agregar/Ver Facturas. Para hacer esto, haz clic en Página Principal y cambia el nombre en el diálogo que se abre (campos Nombre y Título).

El resultado se verá como se muestra a continuación.

<br>

![Tutorial 11](../assets/images/tutorials/tut11.png)

<br>

A continuación, para crear la vista de datos y el formulario de edición, arrastra los campos de datos (propiedades) desde la izquierda hacia el área del medio en el mismo orden que en la cuadrícula de datos mostrada arriba.

Los resultados deberían verse así.

<br>

![Tutorial 12](../assets/images/tutorials/tut12.png)

<br>

Haz clic en el botón Guardar. Ahora agreguemos una página para ver todas las facturas.

## Configuración de la Página de Todas las Facturas

Para hacer esto, abre los Componentes de UI en el panel derecho, selecciona Diseño, haz clic en Página y arrástralo al área del medio justo encima de nuestro formulario de vista de facturas. Una página llamada Nueva página 1 debería añadirse automáticamente, como se muestra a continuación.

<br>

![Tutorial 13](../assets/images/tutorials/tut13.png)

<br>

Ve a la Nueva página 1 haciendo clic en el botón con el mismo nombre, y renómbrala a Todas las Facturas.

Haz clic en Guardar. En la lista de Componentes de UI a la derecha, selecciona Diseño, luego selecciona Página y arrástralo al área del medio. Luego ve a la sección Avanzada y arrastra el elemento DataGrid al panel recién creado. Verás el resultado como se muestra a continuación.

<br>

![Tutorial 15](../assets/images/tutorials/tut15.png)

<br>

Haz clic en el ícono de Configuración (engranaje) en la esquina superior derecha del nuevo elemento DataGrid y selecciona Común en el panel derecho. Verás la selección del componente para mostrar datos en esta cuadrícula de datos. Selecciona Inventario de Facturas.

<br>

![Tutorial 16](../assets/images/tutorials/tut16.png)

<br>

Luego selecciona el ícono “+” junto a la etiqueta “Columnas” 5 veces (ya que tenemos 5 campos de datos que queremos mostrar aquí).

<br>

![Tutorial 17](../assets/images/tutorials/tut17.png)

<br>

Ahora para cada columna, haz clic en el área de la columna. Aparecerá un nuevo diálogo para configurar la columna.

Para cada columna, necesitarás establecer el encabezado con el nombre de la columna (por ejemplo, “Número de Factura,” “Nombre de Factura,” etc.).

También necesitas establecer la opción “Mostrar Encabezado” en “Activado.”

Si las opciones “Ordenable” y/o “Filtrable” están configuradas en “Activado,” habilitarás el ordenamiento y filtrado dinámico (similar a cómo se hace en Excel, por ejemplo).

Finalmente, necesitas hacer clic en el botón “Agregar campo” y seleccionar el campo de datos apropiado para mostrar en esta columna.

El ejemplo a continuación muestra la configuración para el campo “Número de Factura.” Las otras columnas están configuradas de manera similar.

<br>

![Tutorial 18](../assets/images/tutorials/tut18.png)

<br>

Después de haber configurado todas las columnas, ve a Acciones en el formulario a la derecha y asegúrate de que la opción “Mostrar botón de agregar” esté seleccionada. Esto permitirá agregar nuevas facturas a través de este DataGrid.

Además, establece el Tipo de Comando en “Editar Registro” para que podamos ver/editar cualquier factura en la lista haciendo clic en ella.

Consulta la ilustración a continuación para ver los resultados.

<br>

![Tutorial 19](../assets/images/tutorials/tut19.png)

<br>

Haz clic en el botón Guardar.

## Agregar Botones de Acción y Flujo de Datos para Guardar Datos

Después de haber creado las vistas de datos y los formularios de edición, necesitamos agregar lógica para guardar los datos del formulario en la base de datos y permitir que los usuarios lo activen.

Para hacer esto, necesitamos hacer dos cosas.

1. Agregar botones que utilizaremos para guardar los datos del formulario o para cancelar todos los cambios y volver a la lista de Todas las Facturas.
2. Para guardar los datos del formulario, agregaremos un flujo de trabajo simple que tomará los datos del formulario y los guardará en la base de datos.

<br>

## Agregar botones de Guardar y Volver a todas las facturas

<br>

Haz clic en “Caja de herramientas”, selecciona el campo “Botón” en la sección “Básico”, y arrastra el botón al área del medio de la pantalla. Establece el título del botón en Guardar. Para hacer esto, ve a la sección Común, y en el campo Valor de Traducción, escribe Guardar.

Agrega otro botón y establece el título en “Volver a todas las facturas.” El resultado debería verse como la imagen a continuación.

<br>

![Tutorial 20](../assets/images/tutorials/tut20.png)

<br>
Ahora haremos que el botón “Volver a todas las facturas” cambie la interfaz de usuario a la pestaña principal “Todas las facturas”. Para hacer esto, en el menú de Configuración para el botón inferior, selecciona “Acciones” y establece el “Tipo de Comando” en “Abrir Página” y la “Página del Componente” en “Todas las Facturas.” Haz clic en Guardar.

<br>

![Tutorial 21](../assets/images/tutorials/tut21.png)

<br>

## Agregando Flujo de Datos para Guardar

Para hacer que el botón Guardar en la aplicación guarde los datos ingresados como una factura, necesitamos agregar un flujo de datos.

Haz clic en “Caja de herramientas”, selecciona el campo “Flujo de datos” en la sección “Flujo”, y arrástralo al área central de la pantalla. Aparecerá un nuevo flujo de datos con el nombre predeterminado “Flujo de datos 1”, accesible a través del botón con el mismo nombre en el menú de configuración del componente principal, a la derecha del botón de Flujo de Datos de Entrada. Haz clic en el botón Flujo de datos 1 y renombra tu flujo de datos a Guardar.

El resultado debería verse así.

<br>

![Tutorial 22](../assets/images/tutorials/tut22.png)

<br>

A continuación, haz clic en el botón "+ AÑADIR ETAPA", luego "Agregar paso" y selecciona el paso "Obtener modelo de acción". Agrega otro paso y selecciona "Actualizar entrada", luego ve a la configuración de este paso. Puedes leer más sobre este paso en la sección "Flujo de datos". Configura el paso como se muestra a continuación:

<br>

![Tutorial 23](../assets/images/tutorials/tut23.png)

<br>

![Tutorial 24](../assets/images/tutorials/tut24.png)

<br>

A continuación, agrega el paso "Escribir respuesta", especifica el paso fuente en su configuración y guarda el componente.

Después de eso, en el menú de Configuración para el botón Guardar, selecciona Acciones y establece el Tipo de Comando en Ejecutar flujo de datos, y elige tu nuevo Guardar de la lista.

Haz clic en el botón Guardar. El resultado debería verse así.

<br>

![Tutorial 25](../assets/images/tutorials/tut25.png)

<br>
 
Haz clic en Guardar y Listo para publicar. Tu nuevo componente está creado y listo para ser publicado.

<br>

## Publicando y Probando Tu Aplicación

Ahora estás listo para publicar y probar tu aplicación.

Para publicar tu aplicación, haz clic en el botón Listo para publicar dentro de tu componente, luego ve a Estudio→Aplicaciones→Publicación. Selecciona tu componente Inventario de Facturas de la lista de componentes disponibles para publicación, y haz clic en el botón Publicar.

Luego puedes usar el botón Ver Aplicación dentro de tu Estudio (no siempre disponible), o ir a la URL <your-host-name> para ver tu aplicación en acción.

Completa los detalles de la factura y haz clic en Guardar. Luego haz clic en el botón “Volver a todas las facturas”. Tu primera factura será guardada, y verás la lista de todas las facturas disponibles.