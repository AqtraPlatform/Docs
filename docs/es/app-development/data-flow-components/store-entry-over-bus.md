# Entrada de tienda a través del bus

![](../../assets/images/app-development/store-entry-over-bus.png)

## Información general

El paso “Entrada de Tienda a Través del Bus” está diseñado para almacenar el modelo en los datos del componente (campos) a través del bus. Este paso siempre crea una nueva instancia del componente especificado y se utiliza para trabajar dinámicamente con los datos en el sistema. El paso se llama de manera asíncrona.

## Parámetros

**Configuración del paso:**

| Campo de configuración | Opciones de valor      | Propósito                                                                             |
| ---------------------- | ---------------------- | ----------------------------------------------------------------------------------- |
| Nombre del paso        | -                      | Nombre del paso                                                                      |
| Paso fuente            | -                      | Selección del paso anterior                                                          |
| Componente             | -                      | Selección de los componentes disponibles para guardar la entrada                    |
| Nombre                 | String                 | Nombre del sistema de la entrada que se mostrará utilizando enlaces del tipo Catálogo |
| Claves                 | AÑADIR CLAVE           | Para componentes con la bandera de Restringir acceso, especificando las claves para mapear los campos |
| Campo clave            | Multiselección de Catálogo | Campos que contienen las claves primarias del componente seleccionado                |
| Mapeo de campos       | -                      | Configuración dinámica del mapeo de modelos de componentes al modelo de flujo de datos |

## Casos

- **Creación de Nuevas Instancias de Componentes**: Se utiliza para crear automáticamente nuevas entradas en componentes basados en datos en el flujo de datos.

## Excepciones

- **Dependencia de la Disponibilidad de Claves Primarias en el Componente**: La efectividad del paso depende de la disponibilidad y corrección de las claves primarias en el componente objetivo, especialmente si el componente tiene la bandera de Restringir acceso.
- **Requisito de Procesamiento Asíncrono**: El paso se realiza de manera asíncrona, lo que puede afectar la secuencia y el tiempo de procesamiento del sistema.

## Escenario de aplicación

Este componente permite recuperar datos de la integración seleccionada y almacenarlos en los campos correspondientes de los modelos de datos creados. Los datos recuperados pueden ser utilizados en otras partes del sistema para su posterior procesamiento o visualización.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/1jFuXBG8v-YuICBozvoCPAm0FfBQhApvG/view?usp=sharing)