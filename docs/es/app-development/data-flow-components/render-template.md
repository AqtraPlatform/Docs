# Renderizar plantilla

![](../../assets/images/app-development/render-template.png)

## Información general
El paso “Renderizar Plantilla” se utiliza para crear documentos, especialmente en formato PDF, utilizando datos de Dataflow y plantillas disponibles en el sistema. Este paso permite convertir datos en documentos diseñados profesionalmente, que se utilizan ampliamente en la generación de informes, contratos, facturas y otros documentos oficiales.

## Parámetros
**Configuración del paso:**

| Campo de configuración | Opciones de valor  | Propósito |
|------------------------|--------------------|------------|
| Nombre del paso        | -                  | Nombre del paso |
| Paso fuente            | -                  | Selección de pasos anteriores para la fuente de datos |
| Plantilla              | -                  | Selección de las plantillas disponibles para crear un documento |
| Tipo de renderizado    | text, HTML, Docx, Xlsx, PDF | Formato del documento a generar |
| Nombre del archivo      | -                  | Nombre del archivo generado |
| Mapeo de campos        | -                  | Mapeo de campos entre una plantilla y un modelo de datos |

## Casos
- **Generación de Documentos Formalizados**: Especialmente útil para la generación automatizada de documentos oficiales como informes, facturas y contratos, aplicando plantillas preestablecidas.
- **Personalización de Contenido**: Permite crear documentos personalizados para clientes o usuarios utilizando datos específicos de cada caso, como ofertas personalizadas o informes a medida.
- **Preparación para la Distribución de Documentos**: Se utiliza para crear documentos que luego pueden estar disponibles para que los usuarios los descarguen o se envíen por correo electrónico.

## Excepciones
- **Requisito de Calidad y Precisión de las Plantillas**: La calidad de los documentos resultantes está directamente relacionada con la precisión y profesionalismo de las plantillas utilizadas.
- **Necesidad de Seguimiento para Distribuir Documentos**: Una vez que se genera un documento, a menudo se requiere un paso de seguimiento, como “Acción de Formulario” con la opción “Descargar archivo”, para hacer el documento disponible para los usuarios.

## Escenario de aplicación

Este componente utiliza varios pasos para crear y descargar un archivo PDF. Primero, se recupera el modelo de datos, luego se renderiza la plantilla PDF. El paso de acción de formulario se configura para descargar el archivo, especificando el campo de datos que contiene la información del archivo. Después del paso de Escribir Respuesta, el archivo generado se envía al frontend para su descarga.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/1Omst72osc9qf1FtxQcIohdARDzqwDKHT/view?usp=sharing).