# Exportar a Archivo

![](../../assets/images/app-development/export-to-file.png)

## Información general
El paso "Exportar a Archivo" se utiliza para exportar datos del modelo interno de Dataflow a un archivo estructurado. Este paso admite la creación de archivos en formatos CSV, Excel y JSON, lo que permite transferir y distribuir datos procesados de manera eficiente.

## Parámetros
**Configuración del Paso:**

| Campo de Configuración | Opciones de Valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso de origen         | -                 | Selección de pasos anteriores para la fuente de datos |
| Tipo de archivo de salida | Csv, Excel, JSON  | Formato del archivo de exportación |
| Nombre del archivo      | -                 | Nombre del archivo de exportación |
| Separador de columnas   | ; (predeterminado) | Separador de archivo CSV (predeterminado ";") |
| Nombre de la hoja (Si el tipo de archivo de entrada = Excel) | -                 | Nombre de la hoja en el archivo de Excel |
| Mapeo de campos        | -                 | Mapeo de campos del modelo de Dataflow y la estructura del archivo |

## Casos
- **Distribución de Datos**: Ideal para crear informes, distribuir información a clientes o socios, y transferir datos entre diferentes sistemas o departamentos.
- **Archivado de Datos**: Puede utilizarse para almacenar información importante en un formato estructurado y fácilmente accesible.
- **Integración con otros sistemas**: Permite preparar datos para una posterior integración o procesamiento por otros sistemas que admiten formatos CSV, Excel o JSON.

## Excepciones
- **Compatibilidad de formato de archivo**: Es importante ajustar la configuración de exportación para garantizar que los archivos generados sean compatibles con las expectativas y requisitos de los usuarios finales o sistemas.
- **Optimización del rendimiento para grandes volúmenes de datos**: Al exportar grandes volúmenes de datos, es necesario considerar el rendimiento y las posibles restricciones de tamaño de archivo (predeterminado 1 MB).

## Escenario de aplicación

El componente creado sirve como una herramienta para exportar datos del sistema. Incluye varios pasos como la obtención del modelo de datos, filtrado y exportación a un archivo de Excel. El usuario puede personalizar el filtrado de datos antes de exportar y descargar los resultados en un formato conveniente utilizando el botón en la interfaz de usuario.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/1haTgN7Qyu6rD3GSYcDKPEMu3V_KcOdVt/view?usp=sharing).