# Flujo de Datos

## ¿Qué es el flujo de datos? {: #dataflow }

El flujo de datos, o data flow, en la plataforma es un componente clave que permite a los usuarios procesar y transformar datos dentro de una aplicación. Esta es una herramienta poderosa para integrar datos, procesar eventos y automatizar procesos de negocio.

El flujo de datos se construye en la plataforma utilizando un 'editor visual' del flujo de datos:

El editor visual de flujo de datos es un diseñador intuitivo para crear y gestionar flujos de datos. Esta herramienta permite a los usuarios crear secuencialmente un conjunto de Etapas y Pasos para implementar scripts de procesamiento de datos complejos.

- **Agregar Etapa**: Esto se hace presionando el ícono "+" en el panel de control del flujo de datos. Puedes agregar un número ilimitado de etapas según las necesidades de tu script.
- **Eliminar Etapa**: Para eliminar una etapa, utiliza el botón "X" en el bloque de etapa seleccionado.
- **Editar Etapa**: Solo puedes editar el nombre de la etapa seleccionada.
- **Agregar Paso**: Un nuevo paso se agrega presionando el botón "AGREGAR PASO" en la etapa correspondiente. Los usuarios pueden elegir tipos de paso de los grupos de actividad propuestos.
- **Eliminar Paso**: Para eliminar un paso, haz clic en el ícono "X" en el bloque de paso seleccionado.

## Grupo de Entrada

Componentes para recuperar e importar datos:

- [Pasos de Entrada](input-steps.md) - Visión general de los pasos de entrada
- [Obtener Valores del Conector](get-values-from-connector.md) - Recuperar datos de conectores
- [Suscribirse al Conector](subscribe-to-connector.md) - Suscribirse a actualizaciones de datos
- [Obtener Modelo de Acción](get-action-model.md) - Recuperar modelo de acción
- [Obtener Modelo de Flujo de Trabajo](get-workflow-model.md) - Recuperar modelo de flujo de trabajo
- [Obtener Modelo Vacío](get-empty-model.md) - Crear modelo de datos vacío
- [Proxy Obtener Entrada](proxy-get-entry.md) - Recuperación de entrada proxy
- [Proxy Consultar Entrada](proxy-query-entry.md) - Ejecución de consulta proxy
- [Obtener Modelo Crudo](get-raw-model.md) - Recuperar modelo de datos crudos
- [Importar Archivo](import-file.md) - Importar datos de archivos

## Grupo de Transformación de Modelos

Componentes para la transformación y procesamiento de datos:

- [Pasos de Transformación de Modelos](model-transformation-steps.md) - Visión general de los pasos de transformación
- [Transformar Modelo](transform-model.md) - Transformar modelos de datos
- [Unir Modelos](join-modes.md) - Unir múltiples modelos de datos
- [Extraer Colecciones](extract-collections.md) - Extraer datos de colecciones
- [Filtrar Fuente](filter-source.md) - Filtrar fuentes de datos
- [Buscar Referencia](lookup-reference.md) - Búsqueda de referencia
- [Ejecutar Script](execute-script.md) - Ejecutar scripts personalizados
- [Consultar Entidad por Filtro](query-entity-by-filter.md) - Consultas basadas en filtros
- [Seleccionar Muchos](select-many.md) - Selección múltiple
- [Obtener Entidad por ID](get-entity-by-id.md) - Recuperar por identificador
- [Cargar Catálogos por Clave](load-catalogs-by-key.md) - Cargar datos de catálogo
- [Distinto](distinct.md) - Obtener valores distintos
- [Agrupar Por](group-by.md) - Agrupar datos
- [Calcular Array](calculate-array.md) - Cálculos de array
- [Matemáticas Simples](simple-math.md) - Operaciones matemáticas
- [Ejecutar Flujo de Datos](execute-dataflow.md) - Ejecutar flujo de datos anidado
- [Obtener Información del Archivo](get-file-info.md) - Recuperar información del archivo

## Grupo de Contextos de Usuario

Componentes para la gestión y autenticación de usuarios:

- [Pasos de Contextos de Usuario](user-contexts-steps.md) - Visión general de los pasos de contexto de usuario
- [Registrar Contexto para Modelo](register-context-for-model.md) - Registrar contexto de modelo
- [Registrar Usuario Externo](register-external-user.md) - Registro de usuario externo
- [Preparar Claves Externas](prepare-external-keys.md) - Preparar claves de autenticación
- [Asignar Rol de Contexto para Modelo](assign-context-role-for-model.md) - Asignar roles
- [Obtener Código de Un Solo Uso para Usuario](get-one-time-code-for-user.md) - Generar OTP
- [Confirmar Código de Un Solo Uso para Usuario](confirm-one-time-code-for-user.md) - Verificar OTP
- [Actualizar o Crear Información de Usuario](update-or-create-user-info.md) - Gestión de información de usuario
- [Obtener Información de Usuario](get-user-info.md) - Recuperar datos de usuario
- [Iniciar Sesión con Contraseña](login-with-password.md) - Autenticación por contraseña
- [Solicitar Restablecimiento de Contraseña de Usuario](reset-user-password-request.md) - Restablecimiento de contraseña
- [Confirmar Solicitud de Correo Electrónico de Usuario](confirm-user-email-request.md) - Verificación de correo electrónico
- [Enviar Notificación con Plantilla](send-templated-notification.md) - Notificaciones basadas en plantillas
- [Enviar Notificación](send-notification.md) - Enviar notificaciones
- [Eliminar Roles Asignados para Usuario](remove-assigned-roles-for-user.md) - Eliminar roles de usuario

## Grupo de Salida

Componentes para la salida de datos y acciones:

- [Pasos de Salida](output-steps.md) - Visión general de los pasos de salida
- [Almacenar Entrada a través de Bus](store-entry-over-bus.md) - Almacenar datos a través de un bus de mensajes
- [Actualizar Entrada](update-entry.md) - Actualizar entradas de datos
- [Actualizar Entrada Diferida](deferred-update-entry.md) - Actualizaciones diferidas
- [Aplicar Operaciones de Actualización Diferida](apply-deferred-update-operations.md) - Aplicar operaciones diferidas
- [Ejecutar Llamada a API](execute-api-call.md) - Llamadas a API externas
- [Escribir Respuesta](write-response.md) - Escribir datos de respuesta
- [Acción de Formulario](form-action.md) - Acciones de envío de formularios
- [Ejecutar Flujo de Trabajo](execute-workflow.md) - Ejecutar flujo de trabajo
- [Exportar a Archivo](export-to-file.md) - Exportar datos a archivos
- [Renderizar Plantilla](render-template.md) - Renderización de plantillas