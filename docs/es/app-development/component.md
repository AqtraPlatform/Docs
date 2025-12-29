# Componente

Los componentes son los bloques de construcción clave en la plataforma, proporcionando la base para construir aplicaciones. Son unidades encapsuladas de funcionalidad que pueden incluir datos, interfaz de usuario, lógica de negocio y automatización de procesos.

## Tipos de Componente

1. **Componente Único**:

   - Contiene el modelo de objeto básico para almacenar datos.
   - Incluye un modelo de UI con formularios y controles.
   - Tiene un modelo de automatización con flujos de datos y flujos de trabajo.
   - Soporta scripts de Python para personalización adicional del comportamiento.
   - Tiene opciones de seguridad únicas.

2. **Componente Múltiple**:
   - Combina múltiples Componentes para crear aplicaciones complejas.
   - Se utiliza para construir una única interfaz de usuario, por ejemplo, en aplicaciones móviles.

## Creando un Nuevo Componente

1. Abre Studio ('https://<your-hosting-name>/studio').
2. Ve al menú Aplicaciones/Componentes.
3. Haz clic en el botón Agregar para crear un nuevo componente o componente múltiple.

## Configuraciones Básicas del Componente

| Parámetro         | Descripción                                                          |
| ----------------- | -------------------------------------------------------------------- |
| `Title`           | El nombre del componente que se muestra a los usuarios.                |
| `Proxy Mode`      | Determina si el componente actuará como un proxy.                     |
| `Restrict Access` | Restringe el acceso al componente.                                   |
| `Maker`           | Identifica al creador o propietario del componente.                    |
| `Cron`            | Configuración del tiempo de inicio de un componente usando Cron.       |
| `Run as User`     | Especifica el usuario en nombre del cual se ejecutará.               |
| `Access Mode`     | Define el modo de acceso al componente.                              |
| `Description`     | Una descripción detallada del componente, su propósito y funciones.  |
| `Domains`         | Los dominios o categorías a los que pertenece el componente.          |

## Modelo de Objeto del Componente en la Plataforma

Cada componente en la plataforma incluye automáticamente los siguientes campos:

- 'Id': Un identificador único del componente.
- 'creatorSubject': El sujeto que ha creado el objeto.
- 'updateSubject': El sujeto que ha actualizado el objeto.
- 'createdDate': Fecha en que se creó el objeto.
- 'updateDate': Fecha en que se actualizó por última vez el objeto.

Los componentes pueden incluir elementos adicionales, que pueden pertenecer a uno de once tipos: 'string', 'datetime', 'catalog', 'number', 'integer', 'array', 'file', 'boolean', 'time', 'date', 'uri'. Cada uno de estos elementos tiene sus propias configuraciones.

Configuraciones globales para todos los tipos:

- 'Name': Nombre del sistema de la propiedad.
- 'Title': Nombre de la propiedad que se mostrará en la interfaz.
- 'Required': Especifica si el campo es obligatorio.
- 'Primary Key': Determina si un campo es un identificador único.
- 'Query': Determina si el campo puede ser utilizado en consultas.
- 'Virtual property': Excluye un campo de los procesos de sincronización.

## Constructor de Interfaz

La plataforma ofrece una herramienta poderosa para personalizar la interfaz de usuario para cada componente: el Constructor de Interfaz. Es un editor visual que te permite crear y personalizar interfaces de usuario de múltiples componentes utilizando características de arrastrar y soltar. El Constructor de Interfaz es un espacio de trabajo en la sección de Definición de la Interfaz de Creación de Componentes.

En esta sección, puedes:

- Crear una interfaz de aplicación de múltiples pantallas utilizando un editor intuitivo de arrastrar y soltar.
- Agregar elementos de UI de las categorías Básica, Avanzada y Diseño.
- Configurar el modelo de objeto para el Flujo de Trabajo y el Flujo de Datos de la aplicación.
- Personalizar estilos CSS para todos los elementos de UI.

Después de agregar elementos de UI al diseño de la página de tu aplicación, puedes realizar las siguientes operaciones:

- **Copiar:** Copia el elemento actual al portapapeles.
- **Pegar:** Pega el elemento copiado en una nueva ubicación.
- **Mover:** Cambia la posición del elemento.
- **Propiedades:** Abre el panel de propiedades para configurar el elemento.
- **Vista previa:** Muestra el diseño en un formato que se asemeja a la aplicación del usuario.
- **Vista previa de marcado:** Muestra el marcado web textual de la página.
- **Eliminar:** Elimina el elemento seleccionado.
- **Campo de datos:** Permite vincular un elemento a un campo de datos (enlace a la base de datos).

## Módulo de partes web: “Estilos” y “JavaScript”

El bloque “Estilos” está diseñado para describir los estilos CSS que se aplican al componente, mientras que el bloque “JavaScript” permite establecer interacción con la interfaz de usuario y proporcionar funcionalidad adicional utilizando el lenguaje JavaScript.

De esta manera, el módulo de Partes Web permite a los desarrolladores crear componentes más complejos e interactivos utilizando diferentes lenguajes de programación para describir estilos y funcionalidad.<br>

### Usando "JavaScript"

Ejemplo de uso de JavaScript para implementar funcionalidad para crear botones, al presionar los cuales se toma una captura de pantalla:

1. Para llamar a funciones de JavaScript desde el bloque 'Partes web', es necesario usar el método context.InvokeInterop(methodName, objects) dentro del script del Componente:

````python
def capturePage1():
    context.InvokeInterop("callScreenshot")

2. Next, we move to the 'JavaScript' section of the 'Web parts' block and prepare function:
```javascript
// Creando un elemento <script> para cargar la biblioteca html2canvas
var script = document.createElement('script');
script.src = "https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js";
document.head.appendChild(script);

// Función para crear y descargar una captura de pantalla de la página
function takeScreenshot() {
    // Capturing a screenshot of the entire body using html2canvas
    html2canvas(document.body).then(canvas => {
        // Creating a link for downloading the screenshot
        var link = document.createElement('a');
        link.href = canvas.toDataURL("image/png");
        link.download = "screenshot.png";
        // Adding the link to the HTML document and simulating a click to download the screenshot
        document.body.appendChild(link);
        link.click();
        // Removing the link from the document after the screenshot has been downloaded
        document.body.removeChild(link);
    });
}

// Método para llamar a la función takeScreenshot
this.callScreenshot = () => {
    takeScreenshot();
}

Este código crea un elemento de script que carga la biblioteca html2canvas desde una Red de Entrega de Contenido (CDN). Después de cargar la biblioteca, se define una función takeScreenshot() que captura una captura de pantalla de la página actual utilizando html2canvas.

Después de crear la captura de pantalla, el código crea un elemento <a> para hacer posible la descarga, establece su href en la URL de la imagen en formato PNG y el atributo de descarga en screenshot.png. Luego, agrega este enlace al cuerpo del documento, emula un clic en este enlace para descargar la captura de pantalla y, finalmente, elimina el enlace del documento.

### Usando "Estilos"

Ejemplo de código CSS que establece el color de fondo de todo tu espacio de trabajo

```css
body {
    background-color: violet; /* Purple background color */
}
```

## Flujo de datos y construcción de flujos de trabajo {: #dataflow-workflow }

El modelo de objeto de cada Componente contiene datos que se utilizan tanto dentro del Componente mismo como en los procesos de su integración con otros elementos del sistema. Estos datos sirven como base para configurar y ejecutar flujos de datos y flujos de trabajo.

Para comenzar a construir un Flujo de datos o Flujo de trabajo, necesitas arrastrar uno de los elementos desde "Flujos" al área del constructor de interfaz, después de lo cual podrás personalizar el editor visual del flujo de datos y del flujo de trabajo.

Lee más sobre [Componentes de flujo de datos](data-flow-components/index.md) y [Componentes de flujo de trabajo](workflow-components/index.md)

## Publicación de un Componente y Transferencia a la Interfaz Web {: #publication }

- Después de haber terminado de configurar el componente, debes publicarlo como parte de una nueva publicación.
- La gestión de publicaciones se describe en [Publicación de Aplicaciones](publishing-applications.md).
- A continuación, necesitas volver al menú 'Inicio' e ir al 'menú de navegación' del 'dominio de aplicación' deseado, hacer clic en 'Agregar elemento de menú', seleccionar el componente deseado, completar los parámetros y hacer clic en 'Guardar'.

![Menú de navegación](../assets/images/app-development/navigation-menu.png)