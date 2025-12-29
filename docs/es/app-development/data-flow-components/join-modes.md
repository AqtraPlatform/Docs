# Unir modelos

![](../../assets/images/app-development/join-models.png)

## Información general
El paso “Unir Modelos” está diseñado para fusionar datos de dos fuentes diferentes. Agrega datos de la fuente del “Paso Derecho” a los datos de la fuente del “Paso Izquierdo” si se encuentran entradas coincidentes en ambas fuentes.

El paso crea un nuevo modelo de datos al fusionar los flujos de datos definidos en los parámetros del “Paso Izquierdo” y “Paso Derecho”. El paso espera a que ambos flujos terminen de procesarse y luego ordena y fusiona los datos.

## Parámetros
**Configuraciones del paso:**

| Campo de configuración | Opciones de valor | Propósito |
|-----------------------|-------------------|-----------|
| Nombre del paso       | -                 | Nombre del paso |
| Paso izquierdo        | -                 | Fuente de datos para el lado izquierdo de los flujos fusionados |
| Paso derecho          | -                 | Fuente de datos para el lado derecho de los flujos fusionados |
| Clave izquierda       | -                 | Clave para fusionar datos de la fuente izquierda |
| Clave derecha         | -                 | Clave para fusionar datos de la fuente derecha |
| Mapa                  | -                 | Mapeo de campos entre las fuentes izquierda y derecha |

## Casos
- **Fusión de Flujos de Datos**: Se utiliza para fusionar dos flujos de datos diferentes en un modelo, lo que permite analizar y procesar los datos fusionados.
- **Enriquecimiento de Datos**: Se utiliza para agregar información adicional de un conjunto de datos a otro, mejorando así la completitud de la información.

## Excepciones
- **Necesidad de una Clave de Fusión Exacta**: Errores en la definición de la “Clave Izquierda” y “Clave Derecha” pueden llevar a una fusión de datos incorrecta o ineficiente.

## Escenario de aplicación

Este componente permite **probar** y **verificar** la funcionalidad de un flujo de datos donde los datos son **fusionados** de diferentes fuentes. Proporciona **mapeo de campos** y **verificación de fusión de datos** en el **frontend** y en la vista previa de la **respuesta HTTP**.

- Puedes descargar la configuración del componente [aquí](https://drive.google.com/file/d/1YRpXJwNSTp_jOPxP-j0M9SvocZw1W6Tt/view?usp=sharing).