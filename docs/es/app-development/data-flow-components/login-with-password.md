# Iniciar sesión con contraseña

![](../../assets/images/app-development/login-with-password.png)

## Información general
El paso “Iniciar sesión con contraseña” se utiliza para crear una sesión de usuario basada en su nombre de usuario y contraseña. Este paso permite que el usuario sea autorizado en el sistema al verificar las credenciales proporcionadas y, si se verifica con éxito, crear una sesión de usuario.

## Parámetros
**Configuración del paso:**

| Campo de configuración | Opciones de valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso de origen         | -                 | Selección del paso anterior |
| Nombre de usuario      | -                 | Nombre de usuario para iniciar sesión |
| Contraseña de usuario  | -                 | Contraseña del usuario |
| Cliente para la solicitud | -               | Cliente o aplicación que inicia la solicitud de autenticación |

## Casos
- **Autenticación de usuario**: Paso utilizado en procesos de autenticación donde los usuarios ingresan sus credenciales para acceder al sistema o sus características.
- **Control de acceso**: Adecuado para sistemas que requieren que las credenciales del usuario sean verificadas antes de otorgar acceso a ciertos recursos o funcionalidades.

## Excepciones
- **Necesidad de precisión en las credenciales**: La efectividad del paso depende de la precisión de las credenciales ingresadas (nombre de usuario y contraseña).
- **Manejo de intentos de inicio de sesión fallidos**: Es importante manejar adecuadamente los intentos de inicio de sesión fallidos para evitar riesgos de seguridad potenciales, como ataques de fuerza bruta. Esto requiere implementar mecanismos para limitar el número de intentos de inicio de sesión o bloquear temporalmente el acceso después de varios intentos fallidos.

## Escenario de aplicación

El escenario implementa el inicio de sesión del usuario en el sistema utilizando un nombre de usuario y una contraseña. Después de iniciar el flujo de datos e ingresar el nombre de usuario y la contraseña en los campos correspondientes de la interfaz de usuario, el paso "Iniciar sesión con contraseña" autentica al usuario. Luego, utilizando el paso "Acción de formulario", se abre el componente seleccionado.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/1Kb9QNcCHXqetQmXGvBHScQSiRlA-542s/view?usp=sharing)