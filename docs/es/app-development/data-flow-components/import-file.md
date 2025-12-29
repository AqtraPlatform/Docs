# Importar archivo

![](../../assets/images/app-development/import-file.png)

## Información general
El paso “Importar Archivo” se utiliza para importar datos de archivos .csv, Excel o JSON. Los datos se importan línea por línea, mapeándose al formato descrito en “Mapeo de Campos”. Para importar un archivo, debes cargar el archivo en el campo de tipo Archivo y especificar este campo en el parámetro "Campo de Información del Archivo".

## Parámetros
**Configuración del Paso:**

| Campo de Configuración | Opciones de Valor | Propósito |
|------------------------|-------------------|-----------|
| Nombre del paso        | -                 | Nombre del paso |
| Paso fuente            | -                 | Selección del paso anterior |
| Campo de información del archivo | -       | Campo que contiene el archivo a importar |
| Tipo de archivo de entrada | .csv, .xlsx, .json | Formato de archivo para importar |
| Separador de columnas  | ;                 | Separador de columnas para el archivo CSV |
| Primeras líneas a ignorar | 0              | Número de primeras líneas a ignorar en el archivo |
| Mapeo de campos       | -                 | Mapeo de campos del componente a columnas del archivo |

## Casos
- **Importar Datos Tabulares**: Utilizado para cargar datos de archivos CSV o Excel, personalizando el mapeo entre las columnas del archivo y los campos del componente.
- **Importar Datos Estructurados**: Adecuado para importar archivos JSON que contienen datos estructurados.

## Excepciones
- **Mapeo de Campos Incorrecto**: Errores en la configuración de “Mapeo de Campos” pueden resultar en una importación de datos incorrecta.
- **Ignorar Filas No Informativas**: Debes especificar exactamente el número de filas a ignorar antes de comenzar a importar datos.

## Escenario de aplicación

Este componente es una interfaz para cargar archivos en formatos **CSV** y **XLSX**. Incluye campos para tres campos del modelo de datos **CSV** y tres campos del modelo de datos **XLSX**, así como un campo para la carga de archivos. Se utilizan dos flujos de datos para la importación de archivos, ejecución de scripts y almacenamiento de datos.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/10P0-XqSZOKV7wZzg8uH6NR1VnxZ0-8RB/view?usp=sharing)