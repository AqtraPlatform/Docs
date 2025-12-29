# Descripciones de la versión

!!! note "¡La Plataforma Aqtra está en constante evolución!"
Las nuevas versiones se publican normalmente una vez al mes para:

    - Clúster de Kubernetes
    - Mini-imagen de Docker

<br>

## Versión 0.13.x

> **Funcionalidad Añadida**

- **Nuevo Módulo de Componente**: Dentro del componente, se ha añadido el módulo **Web parts**, que consiste en dos bloques: “Estilos” y “JavaScript”. Este módulo es similar al módulo “Component Script”, pero en lugar de interactuar con Python, puedes describir estilos CSS en el bloque “Estilos” e interactuar en JavaScript en el bloque “JavaScript”;
- **Configuración de Módulos Globales en el Dominio de Aplicación**: Se han añadido configuraciones de módulos CSS y JavaScript globales en la **Configuración principal** del **Dominio de aplicación**. Más detalles **aquí**;
- **Nuevas Herramientas en el Menú de Mantenimiento**: Se ha añadido una configuración para la sección **Almacenamiento de archivos**. Más detalles **aquí**;
- **Nuevas Configuraciones del Modelo de Objeto para Datos de Tipo de Archivo**: Ahora puedes establecer validación por tipo de archivo y límite en el tamaño del archivo en bytes;
- **Soporte para XSRF/CSRF**: El componente de carga de archivos ahora elimina la transferencia de datos binarios a través de JS y añade el envío de XSRF. Las solicitudes para descargar archivos ahora son dirigidas y se excluye el acceso directo al almacenamiento de archivos. También se han realizado mejoras en el lugar de trabajo para recibir un token XSRF al cargar una página, y se ha mejorado el controlador OData para cargar archivos. El envío de solicitudes desde el lugar de trabajo para descargar archivos también es ahora dirigido, y el acceso directo al almacenamiento de archivos es imposible.
  <br>

> **Diseño Actualizado**

- **Sección de Exportar/Importar**: Se ha actualizado el diseño de la sección de exportar/importar del menú **Aplicaciones**.
  <br>

## Versión 0.12.x

> **Funcionalidad Añadida**

- **Enviar Notificación**: Se ha añadido un nuevo paso en Dataflow “Enviar notificación”. Este paso permite enviar notificaciones simples al usuario, lo que mejora la forma en que interactúas con el usuario a través del sistema de notificaciones. Más detalles aquí: **Enviar notificación**
- **Pivot Grid**: Se ha añadido un nuevo elemento de UI “Pivot Grid” para análisis y visualización de datos. Más detalles aquí: **Pivot grid**
- **Cambios en **Vista de lista**:
  - Capacidad para expandir el componente horizontal o verticalmente.
  - Se ha añadido la capacidad de habilitar Drag & Drop para todos los grupos de un componente o por elección.
  - Se ha añadido la función de habilitación a Eventos después de usar Drag & Drop.
- **Cambios en **Data grid**:
  - Se ha cambiado el mecanismo de multiselección. En la configuración de Data grid ahora hay una opción “Modo de selección” con una elección: `None`, `Single`, `Multiple`, `Checkbox`.
  - Nuevos eventos: `On Table Changed`, `On Header Changed`, `On Row Changed`, `On Cell Changed`.
  - Capacidad para seleccionar el número de líneas en el paginador en la parte frontal.
- **Cambios en **Vista de gráfico**:
  - Se ha eliminado la configuración de Esquema de Color.
  - Se han añadido configuraciones de Min/Max.
- **Integración de Cliente SIP**:
  - Capacidad para realizar llamadas desde el Lugar de trabajo gracias a la integración del cliente SIP. Más detalles **aquí**.
- **Imágenes de marcador de posición para imágenes faltantes en la configuración de dominios de aplicación y el elemento de UI "Imagen"**: Más detalles en [Documentación de Interfaz de Usuario](user-interface/index.md) y [Componente de Imagen](app-development/ui-components/image.md).
- **Nuevos métodos para gestionar el estado de los elementos de UI**. Más detalles en **documentación**.
- **Carga Masiva de Imágenes a través de http.client y Almacenamiento de Archivos en Scripts de Dataflow**: Se ha añadido una función para la carga masiva de imágenes. Más detalles en **documentación**.
- **Optimización del Mecanismo de Publicación**: Se ha mejorado el mecanismo de publicación utilizando una máquina de estados, proporcionando un proceso estable con la capacidad de retroceder en caso de errores. Más detalles en **documentación**.

<br>

## Versión 0.10.x

> **Funcionalidad Añadida**

- Se ha creado un nuevo paso de dataflow “Obtener información del archivo”, que te permite obtener información sobre un archivo por su identificador. Más detalles en la documentación: **Obtener información del archivo**
- Se ha añadido un filtro para el campo “Componente” dentro del paso de dataflow “Obtener entidad por id”. Más detalles aquí: **Obtener entidad por id**  
  <br>

> **Actualización de Diseño**

- Página principal “Tablero”. Más detalles aquí: **Tablero**
- El “menú de navegación” se ha eliminado del menú “Aplicaciones” y ahora se encuentra en la página principal. Más detalles aquí: **Menú de navegación**
- El diseño de los pasos de dataflow se ha actualizado. Más detalles aquí: **Pasos de Dataflow disponibles**
- El diseño de “Almacenamiento de archivos” se ha actualizado. Más detalles aquí: **Almacenamiento de archivos**
- El diseño de “Mantenimiento del sistema” se ha actualizado. Más detalles aquí: **Mantenimiento del sistema**
  <br>

## Versión 0.9.x

> **Funcionalidad Añadida**

- Características específicas del sistema (específicas de la plataforma)
  - Carga de interfaz de usuario: optimización de la compilación de componentes de UI.
  - Refactorización del **Menú de Mantenimiento**. Movimiento de botones de control a la pestaña “Mantenimiento del sistema”, y visualización de registros con sus configuraciones en la pestaña “Registros del sistema”.
  - Generador de almacenamiento de cola de trabajos en Redis.
  - IronPython se ha actualizado de la versión 2.7.12 a 3.4.1 en el Lugar de trabajo.
- Características específicas del usuario (específicas del estudio) - Copiar/pegar elementos en **constructor de interfaz** en la página del componente. - Añadir archivos a la raíz del [almacenamiento de archivos](user-interface/file-storage.md). - Capacidad para usar el Modelo de Datos de los componentes de referencia (Catálogo) en la barra de herramientas de elementos del componente para: `DataGrid`, `ListView`, `TreeView`.
  <br>

> **Cambios en la Interfaz**

- Refactorización del menú principal del estudio:
  - moviendo los siguientes elementos a la esquina derecha de la barra de herramientas superior: interruptor de localización y botón para cerrar sesión de la cuenta actual (logout),
  - se ha eliminado el elemento Perfil del menú principal.
- Se ha rediseñado el ícono del elemento del menú de Módulos de Python.
- Se han añadido íconos de ayuda en línea en muchas secciones del Estudio: pasos de dataflow, botones para elementos de interfaz de usuario (Toolbox UI), parámetros principales de la aplicación, así como en muchas otras ubicaciones en el estudio para asegurar un acceso más rápido a la ayuda en línea en el sitio de documentación.  
  <br>

> **Errores clave corregidos**

- Corrección de la operación del `Cron` programador de tareas durante la importación/exportación de componentes.
- Eliminación del duplicado `changeAuthor` del modelo de datos del componente.
- Estabilización de la selección de pasos de flujo de trabajo.
- Corrección del `Number` elemento de UI del panel de elementos del componente.
- Corrección de la operación del evento On focus para algunos de los elementos de UI: Día, Hora, Firma.
  <br>

## Versión 0.8.x

> **Funcionalidad Importante y Mejorada Añadida**

- En el paso de Acción de Formulario de dataflow, se han añadido los parámetros Abrir Barra Lateral y Abrir Modal, que te permiten abrir una barra lateral y una ventana modal, respectivamente, similar a cómo se puede hacer a través de un script de Python.
- Transferencia de los atributos requeridos para los parámetros transferidos en el paso Obtener Modelo de Acción.
- Se ha añadido el paso de dataflow “Eliminar roles asignados para el usuario”, que elimina todos los roles actuales asignados al usuario, permitiéndote crear un nuevo conjunto de roles desde cero.
- Se ha añadido el menú **Módulos de Python** para gestionar la biblioteca compartida de módulos de Python.
- Se ha añadido la configuración de fondo para los controles de UI, que te permite establecer una imagen en formatos estándar (por ejemplo, png, svg, jpeg, etc.) como fondo para todos los controles que tienen una sección de configuración de Brocha.
- El ícono de vista del modelo de datos en el paso de dataflow se ha cambiado al ícono de ojo.
- El parámetro “Omitir de Sincronizar” se ha reemplazado por Propiedad Virtual. Los campos marcados como “Propiedad Virtual” no se guardan en la base de datos cuando se registra el componente.
- Se han añadido configuraciones para la Aplicación Web Progresiva (PWA) en la sección Editar manifiesto.
- Se han añadido configuraciones adicionales del Dominio de Aplicación: mostrar migas de pan, inicio de sesión, localización.
  <br>

> **Errores Importantes Corregidos**

- Se ha corregido el funcionamiento de los filtros dinámicos para el control de Data Grid.
- El “Campo de primera línea a ignorar” en el paso de Importar Archivo no se restablece a 0 después de guardar.
- El color predeterminado para el dominio de aplicación se aplica a los controles de tipo botón que no tienen un color predeterminado establecido.
- Los permisos para un componente múltiple no se establecen en modo de acceso restringido.
  <br>

## Versión 0.7.0

> **Funcionalidad Importante y Mejorada Añadida**

- Al seleccionar un componente predeterminado para un dominio de aplicación en la sección de Configuración Principal, puedes seleccionar la página que se abrirá para este componente en el campo Página Predeterminada. Si no se selecciona ninguna página, se abrirá por defecto la primera página del componente (página principal).
- Se ha añadido un nuevo paso “Ejecutar Dataflow” al dataflow, que te permite lanzar nuevos dataflows, incluidos dataflows de otros componentes, dentro del dataflow actual.
- Se ha eliminado el obsoleto paso de dataflow “Obtener Audiencia”, y el paso “Acción de Formulario” se ha movido al grupo “Transformación de Modelo”. El grupo “Otros” se ha eliminado por completo.
- Se ha añadido la búsqueda para configurar “Mapeo de Campos” en el paso “Aplicar operaciones de actualización diferida”.
- Para el control de UI **Área de Texto**, se ha añadido una opción de Autoajuste, que te permite expandir el tamaño del campo si necesitas ingresar una mayor cantidad de texto.
- Se ha optimizado el paso de dataflow “Consultar Entidad por Filtro” mediante la creación automática de índices y la normalización de la base de datos.
- Se ha añadido un aviso de expiración inminente de la licencia. El mensaje aparece 10 días antes de la fecha de expiración de la licencia actual.
- Las APIs de Swagger generadas para Dataflow ahora muestran el nombre de Dataflow como el nombre de la API.
- Se ha añadido la capacidad de solicitar la geolocalización del usuario desde el Script de Componente a través de la función context.PlatformServices.GeolocationPosition.
- Se ha añadido la capacidad de establecer la configuración de localización predeterminada para el dominio de aplicación en la sección de Configuración Principal.
- Se ha añadido la capacidad de establecer un favicon para el dominio de aplicación en la configuración del Menú Principal: Dominio: Configuración Principal.
  <br>

> **Errores Importantes Corregidos**

- Se ha corregido el funcionamiento de los filtros dinámicos para el control de Data Grid.
- Se ha corregido un problema donde ocurría un error al ordenar campos recuperados de enlaces de tipo Catálogo.
- Se ha mejorado la estabilidad de la cuadrícula de datos, incluidos errores fantasma al navegar a través de la cuadrícula de datos.
- Se ha corregido un problema con el formulario de búsqueda que se cortaba en la cuadrícula de datos al hacer clic en un filtro.
- Se ha añadido la salida de valores de cadena para Enum.
- Se ha corregido el funcionamiento incorrecto del sistema con el cierre de sesión remoto.
- Se ha corregido el funcionamiento incorrecto del temporizador en el paso “Aplicar operaciones de actualización diferida”.
- Para los controles de UI de tipo Etiqueta, vinculados a un campo de tipo Catálogo, la configuración de Color ahora se procesa correctamente.
  <br>

## Versión 0.6.x

> **Funcionalidad Importante y Mejorada Añadida**

- Funciones avanzadas para gestionar el menú principal de la aplicación: construcción de menús jerárquicos y configuración de íconos de menú.
- Mejora en el trabajo con scripts de Python: resaltado para la sintaxis de Python, autocompletado para métodos del sistema de Python, así como autocompletado y sugerencias para métodos de bibliotecas integradas de la plataforma (disponibles a través de Ctrl-Space en Win10/11, y Option-Space en MacOS).
- Se ha añadido la capacidad de construir ventanas laterales adicionales a través del Script de Componente.
- Se ha añadido la capacidad de construir ventanas modales complejas a través del Script de Componente con transferencia de datos desde ventanas modales al script que llama.
- La llamada al Script de Componente se ha movido al menú principal.
- Se ha completado la localización del Estudio al ruso.
- En el control DataGrid, ahora es posible seleccionar campos arbitrarios de un componente externo al mostrar campos de referencia de tipo Catálogo.
- La importación-exportación ahora incluye la exportación y posterior importación de permisos y roles (exportar archivos creados con la versión 0.6.x a versiones anteriores funcionará, pero no importará roles y permisos incluidos).
- La importación-exportación ahora verifica componentes relacionados y advierte al usuario si algún componente relacionado no se incluyó en la lista de exportación.
- A nivel de plataforma, se ha añadido la capacidad de marcar entradas (instancias de componente) como disponibles para eliminación física a través de una bandera en el paso de dataflow “Actualizar Entrada”.
- Se ha añadido la capacidad para que el administrador del Estudio obtenga una lista de entradas marcadas para eliminación y elimine aquellas que no tienen enlaces a entradas que no están marcadas como listas para eliminación.
  <br>

## Versión 0.5.24

> **Funcionalidad Importante y Mejorada Añadida**

- Capacidades avanzadas para filtros dinámicos y estáticos en controles avanzados como Data Grid, Vista de Lista, Vista de Árbol, permitiendo filtrado de datos sobre la marcha antes de mostrarlos al usuario (se han añadido parámetros para filtros de tipo contiene, etc.).
- Ampliación del concepto de utilización de Dataflow y Workflow: ahora ambos pueden ser creados y utilizados por separado de controles de UI como botones, lo que permite una estructura de aplicación más flexible y simplifica el desarrollo.
- Se han añadido muchos nuevos métodos disponibles a través de [Uso de Python](app-development/using-python.md) en el Script de Componente, como llamar a ventanas modales, verificar la resolución de pantalla y el tipo de dispositivo para crear un diseño de UI responsivo.
- Se ha añadido la capacidad de trabajar con sistemas de colas de mensajes (por ejemplo, RabbitMQ) desde dataflow con un nuevo paso [Suscribirse al Conector](app-development/data-flow-components/subscribe-to-connector.md).
- Se ha añadido la capacidad de procesamiento de datos por lotes en Dataflow a través de nuevos pasos [Actualizar Entrada Diferida](app-development/data-flow-components/deferred-update-entry.md) y [Aplicar Operaciones de Actualización Diferida](app-development/data-flow-components/apply-deferred-update-operations.md).
  <br>

## Versión 0.4.4

> **Funcionalidad Importante y Mejorada Añadida**

- Se ha añadido un nuevo campo de almacenamiento del sistema “Nombre”, utilizado para mostrar elementos de Catálogos.
  - Al mostrar un solo elemento de Catálogo (por ejemplo, utilizando un control de UI Seleccionar que hace referencia al Catálogo), el contenido del campo Nombre ahora se mostrará siempre. Si el campo Nombre está vacío, se mostrará el nombre del Catálogo del sistema/número de secuencia de la entrada del Catálogo.
- Se han añadido configuraciones de ordenación predeterminadas para Datagrid y Vista de Lista.
- Se ha añadido la sustitución automática de caracteres especiales Unicode en el Script de Componente para la generación de enlaces.
  <br>

> **Errores Corregidos**

- Se ha corregido el funcionamiento incorrecto del paginador con respecto al cambio de varias tablas en una página.
- Se ha corregido la función de desplazamiento que no funcionaba en algunas partes del Estudio.
  <br>

## Versión 0.3.223

_Clúster de Kubernetes 0.3.223 | Mini-imagen de Docker 0.2.118_

> **Funcionalidad Importante y Mejorada Añadida**

- Se ha añadido un nuevo paso de flujo de datos “Enviar notificación con plantilla”, que te permite enviar una notificación por correo electrónico utilizando una plantilla especificada.
- Propiedad de transparencia para componentes de UI.
- Se ha añadido soporte para autorización OAuth2 para solicitudes HTTP. Ahora puedes configurar la generación automática de tokens a través de OAuth para conectarte a la API.
- Se ha añadido el parámetro “Almacenar respuesta como archivo” en el paso “Ejecutar llamada a API” para permitirte descargar un archivo a través de la API a solicitud.
- Los pasos ya no generan un boletín, ahora generan un campo en el modelo para uso posterior, como “Enviar notificación con plantilla”.
  <br>

> **Errores Corregidos**

- Se han corregido errores al trabajar con el tipo DateTime en el calendario.
- Se ha corregido la UI en el Estudio y el Lugar de trabajo.
- Se ha corregido el estado Deshabilitado para el componente de UI Radiobutton.
- Se han corregido errores de localización.
- La búsqueda en Dropdown ahora es insensible a mayúsculas y minúsculas.
- Se ha corregido la operación de autorización, incluidos problemas de cierre de sesión. <br>