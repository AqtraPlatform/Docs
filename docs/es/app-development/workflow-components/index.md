# Flujo de trabajo

## ¿Qué es un flujo de trabajo? {: #workflow }

El flujo de trabajo es un mecanismo para gestionar estados y tareas en varios scripts de componentes en la plataforma. Permite organizar la ejecución secuencial de tareas, manteniendo estados y proporcionando la capacidad de reiniciar en caso de fallo.

### ¿Cómo creo un flujo de trabajo?

1. **Abrir Toolbox**: Abre el menú Toolbox en la ventana de componentes y ve a la pestaña Flujos.
2. **Agregar Flujo de Trabajo**: Haz clic en el ícono de Flujo de Trabajo y arrástralo al área de trabajo. Aparecerá un nuevo flujo de trabajo para ser configurado.

Usando el constructor visual de Flujo de Trabajo, puedes configurar un script de flujo de trabajo:

- **Agregar Etapas y Pasos**: El editor te permite agregar Etapas y Pasos que forman la lógica del flujo de trabajo.
- **Configuración de Secuencia**: Los scripts se ejecutan de arriba hacia abajo y de izquierda a derecha, permitiéndote crear un flujo de tareas consistente.

### Parámetros del Flujo de Trabajo

- **Nombre del flujo de trabajo**: El nombre utilizado para identificar el flujo de trabajo en el componente.
- **Restringir Acceso**: Cuando se establece en "Sí", crea un contexto de seguridad para el flujo de trabajo.

### Editar Etapas y Pasos del Flujo de Trabajo

- **Agregar Etapas**: Usando el botón "+", puedes agregar nuevas etapas.
- **Eliminar Etapas**: El botón "X" te permite eliminar etapas innecesarias.
- **Editar Etapas**: Solo se puede cambiar el nombre de la etapa.
- **Agregar y Eliminar Pasos**: Los pasos se pueden agregar y eliminar dentro de las etapas, definiendo acciones específicas del flujo de trabajo.

## Grupo de Notificaciones

Componentes para enviar notificaciones y confirmaciones:

- [Pasos de Notificaciones](notifications-steps.md) - Visión general de los pasos de notificación
- [Enviar Notificación](send-notification.md) - Enviar notificaciones a los usuarios
- [Enviar Notificación Plantillada](send-templated-notification.md) - Enviar notificaciones basadas en plantillas
- [Obtener Confirmación del Usuario](get-user-confirmation.md) - Solicitar confirmación del usuario

## Grupo de Integraciones

Componentes para integrarse con otros sistemas:

- [Pasos de Integraciones](integrations-steps.md) - Visión general de los pasos de integración
- [Ejecutar Flujo de Datos](execute-data-flow.md) - Ejecutar flujo de datos desde el flujo de trabajo

## Grupo Común

Operaciones comunes del flujo de trabajo:

- [Pasos Comunes](common-steps.md) - Visión general de los pasos comunes
- [Actualizar Modelo](update-model.md) - Actualizar el modelo de datos
- [Finalizar](finish.md) - Completar la ejecución del flujo de trabajo
- [Actualizar Campo del Modelo](update-model-field.md) - Actualizar un campo específico del modelo
- [Restablecer a Borrador](reset-to-draft.md) - Restablecer el flujo de trabajo al estado de borrador

## Grupo de Condiciones

Lógica condicional y ramificación:

- [Pasos de Condiciones](conditions-steps.md) - Visión general de los pasos de condición
- [Caso Switch](switch-case.md) - Ramificación de caso switch
- [Condición If](if-condition.md) - Ramificación condicional