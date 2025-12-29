# Número de Teléfono

![](../../assets/images/app-development/phone-number.png)

## Información general

El Número de Teléfono es un componente de UI diseñado para ingresar y mostrar números de teléfono. Este componente facilita la entrada de números telefónicos, asegurando el formato correcto y la validación de los datos ingresados.

## Parámetros

**Propiedades del componente**

| Grupo de configuraciones | Campo de configuración | Opciones de valor          | Propósito                                                                               |
| ----------------------- | --------------------- | -------------------------- | ------------------------------------------------------------------------------------- |
|                         | Nombre                | -                          | Nombre del componente de UI en el sistema                                             |
| Común                  | Deshabilitado         | true, false                | La propiedad permite deshabilitar un elemento en el formulario                        |
|                         | Requerido             | true, false                | La propiedad hace que el elemento sea obligatorio para ser completado antes de enviar el formulario |
|                         | Etiqueta              | -                          | Contiene la tabla de contenido del contenedor de texto                                |
|                         | Vinculación           | Multiselección de Catálogo | Contiene un campo de “String” relacionado del modelo                                  |
| Eventos                | Al cambiar el valor   | -                          | Permite ejecutar el script especificado después de cambiar el valor del campo         |

**Propiedades CSS**

| Grupo de configuraciones | Campo de configuración | Opciones de valor | Propósito                                                                                                                   |
| ----------------------- | --------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------- | --- | ------------ |
| Diseño                 | Ancho                 | -                 | Ancho del componente                                                                                                       |
|                         | Alto                  | -                 | Alto del componente                                                                                                        |
|                         | Crecer                | true, false       | La propiedad determina cuánto crecerá un elemento en relación con el resto de los elementos flexibles dentro del mismo contenedor |
|                         | Margen                | -                 | La propiedad define los rellenos exteriores en los cuatro lados del elemento                                              |
|                         | Relleno              | -                 | La propiedad establece los rellenos internos en todos los lados del elemento                                              |
| Apariencia             | Radio de esquina      | -                 | La propiedad se utiliza para redondear las esquinas de un elemento                                                         |
|                         | Grosor del borde      | -                 | La propiedad permite establecer los límites para el elemento                                                               |
| Brocha                 | Fondo                 | -                 | La propiedad establece el color de fondo del elemento                                                                     |
|                         | Brocha del borde      | -                 | La propiedad establece el color del borde del elemento                                                                   |     | Color del borde |

## Casos

- **Validación del formato del número:** Se utiliza para validar el número de teléfono ingresado para asegurar que siga un formato nacional o internacional específico.

## Excepciones

- **Opciones de formato limitadas:** La función puede no soportar todos los formatos de número de teléfono posibles, especialmente variantes no estándar o regionales.
- **Sensibilidad a errores de entrada:** La entrada de usuario no válida puede resultar en errores en el procesamiento del número de teléfono.