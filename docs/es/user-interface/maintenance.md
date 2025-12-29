# Menú de mantenimiento

<br>

El menú de “Mantenimiento” es una herramienta poderosa para gestionar datos y mantener el sistema, especialmente después de actualizaciones importantes, migraciones de datos o cambios en la base de datos.
<br>

## Descripción general

- **Propósito**: Gestionar datos de PostgreSQL a través de ODATA, eliminar datos eliminados, analizar y gestionar registros del sistema.
- **Características**: La herramienta se utiliza principalmente después de actualizaciones de versión de la plataforma, importaciones de componentes o cambios masivos de datos.
  <br>

## Pestañas del menú de mantenimiento

<br>

### Registros del sistema

<br>

! [Registros del sistema] (system-logs.png)
<br>

- **Funcionalidad**: Ver los registros actuales del sistema y ajustar los niveles de registro (Trace, Debug, Information, Warning, Critical, Error, None).
  <br>

### Mantenimiento del sistema

<br>

! [Mantenimiento del sistema] (system-maintenance.png)
<br>

1. **Reconstruir referencias de base de datos**: Comprobar y reconstruir referencias cruzadas entre componentes o dentro de componentes (flujo de datos/proceso de trabajo).
2. **Reconstruir reglas RLS**: Reconstruir reglas de seguridad a nivel de fila para personalizar el acceso a los datos.
3. **Reconstruir caché**: Reconstruir la caché interna de la plataforma, resolviendo problemas con actualizaciones.
4. **Análisis marcado para eliminación**: Ver y gestionar registros marcados para eliminación utilizando la bandera ‘Marcar entrada para eliminación’ en el paso ‘Actualizar entrada’. Después de hacer clic en el botón “Análisis marcado para eliminación”, se muestran todas las entradas marcadas. Las entradas se seleccionan y eliminan a través de “Eliminar elementos seleccionados”. El sistema evitará que se eliminen entradas si hay entradas relacionadas no etiquetadas.
5. **Restablecer publicación actual**: Restablece el proceso de publicación si falla.
   <br>

### Almacenamiento de archivos

Esta sección añade la capacidad de configurar los siguientes ajustes para el almacenamiento de archivos:

| Tipos de archivo aceptables | Límite de tamaño de archivo en bytes |
| --------------------------- | ------------------------------------ |
| .\* (todos los tipos de archivo)  | tamaño seleccionado                  |

<br>

Puedes especificar tipos de filtro, separándolos con comas. Esto puede ser extensiones de archivo, como .jpg, .json, .docx, o tipos Mime, por ejemplo, image/_, application/_

También puedes combinar filtros, por ejemplo, `image/*`, `.docx`.
Usar el filtro `*/*` permite subir cualquier archivo.
<br>

![Mantenimiento de almacenamiento de archivos](../assets/images/user-interface/file-storage-maintenance.png)