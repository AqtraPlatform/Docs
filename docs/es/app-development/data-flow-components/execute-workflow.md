# Ejecutar Flujo de Trabajo

![](../../assets/images/app-development/execute-workflow.png)

## Información general
El paso “Ejecutar Flujo de Trabajo” se utiliza para activar y ejecutar un flujo de trabajo específico en el sistema.

## Parámetros
**Configuraciones del Paso:**

| Campo de Configuración | Opciones de Valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso fuente            | -                 | Selección del paso anterior |
| Componente             | -                 | El componente dentro del cual se realiza el flujo de trabajo |
| Flujo de trabajo       | -                 | Nombre del flujo de trabajo a completar |
| Campo de entrada del componente | -       | El campo en el componente utilizado para transferir datos al flujo de trabajo |

## Casos
- **Control dinámico del flujo de datos**: Se puede utilizar para lanzar flujos de trabajo específicos basados en datos obtenidos de pasos anteriores de Dataflow, lo que permite crear sistemas de gestión de datos flexibles y adaptativos.

## Excepciones
- **Dependencia de la corrección de los datos**: Para evitar errores en la ejecución del flujo de trabajo, es necesario asegurar que los datos enviados al flujo de trabajo sean precisos y completos.
- **Coordinación entre Dataflow y Flujo de Trabajo**: Es importante configurar cuidadosamente la interacción entre Dataflow y Flujo de Trabajo para garantizar una transferencia fluida y correcta de datos y comandos entre ellos.

## Escenario de aplicación

El componente creado sirve como una interfaz para interactuar con el modelo de datos que contiene un campo "user_name" de tipo cadena. Este componente incluye funcionalidad para actualizar el modelo de datos utilizando el paso Actualizar modelo dentro del Flujo de Trabajo. Para interactuar con el componente, el usuario puede ingresar su nombre, hacer clic en un botón, después de lo cual los datos se enviarán y el nombre se mostrará en la cuadrícula de datos después de actualizar la página.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/1AgjjrOW-z2LPMj7sFWg_PKjHjFfVtxub/view?usp=sharing).