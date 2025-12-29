# Cargar catálogos por clave

![](../../assets/images/app-development/load-catalogs-by-key.png)

## Información general
El paso “Cargar Catálogos por Clave” funciona de manera similar al paso “Obtener Entidad por ID”, pero en lugar de requerir un ID de componente específico, identifica automáticamente cualquier campo de tipo Catálogo en el modelo de datos. Dependiendo de la elección del usuario, el paso recupera la entrada completa vinculada con el campo de tipo Catálogo seleccionado. Así, permite obtener información completa de cualquier enlace en los datos sin tener que especificar un ID específico.

## Parámetros
**Configuración del paso:**

| Campo de configuración | Opciones de valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso fuente            | -                 | Selección del paso anterior |

## Casos
- **Identificación Automática y Descarga de los Datos Vinculados**: Se utiliza para identificar y cargar automáticamente datos vinculados con campos de Catálogo.
- **Extracción de Datos Flexible**: Adecuado para scripts que requieren flexibilidad en la selección y extracción de datos de varios componentes relacionados.

## Excepciones
- **Carga Excesiva al Trabajar con un Gran Número de Catálogos**: Si hay un gran número de catálogos que se están abriendo, puede llevar tiempo adicional procesarlos.
- **Reemplazo Injustificado del paso “Obtener entidad por ID” con el paso “Cargar catálogos por clave”**: Si el número de catálogos vinculados no excede unos pocos, es mejor utilizar el paso “Obtener entidad por ID” para un mejor rendimiento.

## Escenario de aplicación

Este componente permite crear un flujo de datos comenzando desde la obtención de un modelo de datos vacío. Luego, se utiliza para recuperar el identificador de registro con catálogos, después de lo cual carga estos catálogos y muestra sus datos en el frontend.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/1_GImBJ3UCDo-T1dL6c85-wWgcUfpJIz3/view?usp=sharing).