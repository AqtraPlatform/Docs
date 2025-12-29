# Confirmar código de un solo uso para el usuario

![](../../assets/images/app-development/confirm-one-time-code-for-user.png)

## Información general
El paso “Confirmar Código de Un Solo Uso para el Usuario” se utiliza para confirmar el código de un solo uso que fue generado para el usuario en el paso anterior “Obtener Código de Un Solo Uso para el Usuario”. Este paso es clave en el proceso de autenticación de dos factores, permitiéndote verificar la corrección del código ingresado por el usuario para acceder al sistema.

## Parámetros
**Configuraciones del Paso:**

| Campo de Configuración | Opciones de Valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso fuente            | -                 | Selección del paso anterior |
| Campo de código del usuario | -           | El campo en el que el usuario ingresa el código recibido para confirmación |

## Casos
- **Confirmación de Autenticación de Dos Factores**: Aplicado para completar el proceso de autenticación de dos factores al requerir que los usuarios ingresen el código que se les envió en el paso anterior.
- **Mejorando la Seguridad de Acceso**: Utilizado en escenarios donde se requiere un control de acceso al sistema mejorado para prevenir inicios de sesión no autorizados.

## Excepciones
- **Dependencia de la corrección del código ingresado**: La efectividad del paso depende de la precisión en la entrada del código por parte del usuario.
- **Validez Limitada del Código**: Si el código expira, debe ser reemitido, lo que puede resultar en retrasos en la autenticación.

## Escenario de aplicación

El componente crea un flujo de datos para confirmar el código de un solo uso del usuario. El paso del modelo de acción Obtener se utiliza para recuperar los datos del modelo. Luego, el código de la variable ForTestCode se limpia de caracteres innecesarios y se almacena en la variable _code utilizando el paso Ejecutar script. El paso Confirmar código de un solo uso para el usuario se utiliza para confirmar el código de un solo uso utilizando el valor de _code como el código del usuario. Finalmente, el resultado se pasa a través del paso Escribir respuesta.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/1_uPyqNOuOddurvwz-KteaoIIRQjgEzBH/view?usp=sharing)