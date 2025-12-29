# Contraseña

![](../../assets/images/app-development/password.png)

## Información general
La contraseña es un componente básico de la interfaz de usuario diseñado para ingresar contraseñas de forma segura. Este componente se utiliza para crear campos de entrada de contraseña, asegurando la confidencialidad y protección de los datos ingresados.

## Parámetros
**Propiedades del componente**

| Grupo de configuraciones | Campo de configuración | Opciones de valor | Propósito |
| --- | --- | --- | --- |
|  | Nombre | - | Nombre del componente de la interfaz de usuario en el sistema |
| Común | Deshabilitado | true, false | La propiedad permite deshabilitar un elemento en el formulario |
|  | Requerido | true, false | La propiedad hace que el elemento sea obligatorio para ser completado antes de enviar el formulario |
|  | Mostrar claro | true, false | Muestra el ícono de limpiar (restablecer) el valor del campo |
|  | Autocompletar |  | Campo para establecer el valor del atributo HTML de autocompletar. Como regla general, utiliza username para el campo de entrada de nombre, y password, new-password o current-password para los campos de entrada correspondientes a diferentes tipos de contraseña. Funciona en conjunto con el parámetro Proporcionar formulario raíz para el control de la interfaz de usuario de la página. |
|  | Etiqueta | - | Contiene la tabla de contenido del contenedor de texto |
|  | Vinculación | Multiselección de Catálogo | Contiene un campo “String” relacionado del modelo |
| Eventos | Al cambiar el valor | - | Permite ejecutar el script especificado después de cambiar el valor del campo |
|  | Al presionar una tecla |  | Permite ejecutar el script especificado después de moverse al siguiente elemento de la página (tab) |
|  | Al soltar una tecla |  | Permite ejecutar el script especificado después de moverse al elemento anterior de la página (tab) |
|  | Al enfocar |  | Permite ejecutar un script en el momento en que un elemento es enfocado |
| Índice de tabulación |  | Entero positivo comenzando desde cero | Establece el orden en el que los campos activos (editables) son alternados a través del teclado (por ejemplo, usando la tecla Tab) |
| ID de automatización |  |  | ID de control para pruebas automatizadas y para transferir configuraciones CSS |

**Propiedades CSS**

| Grupo de configuraciones | Campo de configuración | Opciones de valor | Propósito |
| --- | --- | --- | --- |
| Diseño | Ancho | - | Ancho del componente |
|  | Alto | - | Alto del componente |
|  | Crecer | true, false | La propiedad determina cuánto crecerá un elemento en relación con el resto de los elementos flexibles dentro del mismo contenedor |
|  | Margen | - | La propiedad define los rellenos exteriores en los cuatro lados del elemento |
|  | Relleno | - | La propiedad establece los rellenos internos en todos los lados del elemento |
| Apariencia | Radio de esquina | - | La propiedad se utiliza para redondear las esquinas de un elemento |
|  | Grosor del borde | - | La propiedad permite establecer los límites para el elemento |
| Brocha | Fondo | - | La propiedad establece el color de fondo del elemento |
|  | Brocha del borde | - | La propiedad establece el color del borde del elemento |

## Casos
- **Formularios de autenticación**: Utilizados en formularios de inicio de sesión y registro para ingresar contraseñas de forma segura.
- **Formularios interactivos**: Habilitando formularios interactivos que requieren la entrada de datos confidenciales.

## Excepciones
- **Limitaciones de formato**: No admite formatos de texto complejos como hipervínculos o imágenes incrustadas.