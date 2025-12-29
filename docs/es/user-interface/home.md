# Menú de Inicio

<br>

La página proporciona información sobre su licencia y los dominios de aplicación que han sido desplegados. Tendrá acceso a las siguientes características e información:

- **Tipo de Plan**: Esto muestra el tipo de su plan actual y la fecha de expiración o renovación de su suscripción.
- **Dominios de Aplicación**: Esta sección le permite crear componentes de aplicación, conectar usuarios a través de URLs específicas y navegar a la sección "Menú de Navegación".
- **Estadísticas de Uso**: Muestra información sobre el número actual de aplicaciones en comparación con el límite total, así como el número actual y total de usuarios, flujos de trabajo y flujos de datos.
  <br>

![Panel principal](../assets/images/user-interface/main-dashboard.png)
<br>

## Aprenda más sobre la configuración de dominios de aplicaciones

Los dominios de aplicación son espacios externos con una URL específica (HTTP/HTTPS://<su-nombre-de-dominio>) donde puede desplegar sus componentes.

**Por defecto, hay una aplicación disponible** llamada ‘digital-workplace’. Puede agregar más aplicaciones utilizando el botón ‘Agregar aplicación’ en la esquina superior derecha de la barra de herramientas. Cada aplicación que agregue aparece en la lista de aplicaciones bajo la descripción de su plan.

En el dominio de aplicación, los siguientes parámetros se pueden establecer en la ‘configuración principal’:

| Grupo de configuración | Campo de configuración  | Opciones de valor                                 | Propósito                                               |
| ---------------------- | ---------------------- | ------------------------------------------------- | ------------------------------------------------------ |
| Configuración principal | Título                 | -                                                 | Título de la pestaña del navegador                     |
|                        | Ocultar barra superior  | true, false                                       | Ocultar el menú superior para el lugar de trabajo      |
|                        | Menú estático          | true, false                                       | Visualización constante de menús o visualización al pasar el mouse |
|                        | Ocultar migas de pan    | true, false                                       | Mostrar/ocultar navegación jerárquica                  |
|                        | Ocultar inicio de sesión | true, false                                       | Mostrar/ocultar inicio de sesión del usuario           |
|                        | Ocultar localización    | true, false                                       | Mostrar/ocultar selección de ubicación                  |
|                        | Elegir logo            | Logo, Logo pequeño, favicon, "Sin imagen"        | Elegir un logo para WorkPlace (diferentes tipos)      |
|                        | Almacenamiento de sesión de usuario | local/session                                     | Guardar parámetros de autorización en una sesión o localmente |
|                        | Proveedor Idp predeterminado | Multiselección de Catálogo                          | Elegir un Método de Autorización                       |
|                        | Localización predeterminada | Multiselección de Catálogo                          | Localización predeterminada                             |
|                        | Aplicación de información de usuario predeterminada | Multiselección de Catálogo                          | Aplicación principal para gestionar datos de usuario    |
|                        | Componente predeterminado | Multiselección de Catálogo                          | Componente predeterminado                               |
|                        | Página predeterminada   | -                                                 | Página de componente predeterminada                    |
|                        | Componente de inicio de sesión | Multiselección de Catálogo                          | Componente del formulario de autorización               |
|                        | Habilitar SIP          | True, False                                       | Construir integración con SIP                           |

<br>
En este grupo, puedes configurar los ajustes de los módulos globales a través de JavaScript y CSS, lo que te permite convertir la plataforma en un sistema de gestión de contenido (CMS), así como cargar y utilizar cualquier biblioteca de terceros.

Ejemplo de JS para JavaScript global:

```javascript
loadScript([
  'https://code.jquery.com/jquery-3.7.1.min.js?integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo=&crossorigin="anonymous"',
])
  .then((res) => {
    return loadScript([
      'https://code.jquery.com/ui/1.13.2/jquery-ui.min.js?integrity="sha256-lSjKY0/srUM9BE3dPm+c4fBo1dky2v27Gdjm2uoZaL0="&crossorigin="anonymous"',
    ]);
  })
  .subcribe({
    complete: () => {
      console.log("Load scripts complete");
    },
    error: (err) => {
      console.log("Load scripts err:" + err);
    },
  });
```

<br>

Además, hay un grupo de ajustes de ‘configuración de estilo’:

| Grupo de ajustes | Campo de ajuste        | Propósito              |
| ---------------- | ---------------------- | ---------------------- |
| Fuente principal  | Fuente                 | Fuente principal de la app |
| Esquema de color | Tema predeterminado    | Esquema de color predeterminado |
|                  | Color claro primario   | Color claro principal  |
|                  | Color primario         | Color principal        |
|                  | Color oscuro primario   | Color oscuro principal |
|                  | Color más oscuro primario | Color más oscuro principal |
|                  | Color de texto primario | Color de texto predeterminado |

<br>

Grupo de ajustes ‘Editar manifiesto’:

| Campo de ajuste         | Propósito                         |
| ----------------------- | --------------------------------- |
| Nombre                  | Nombre de la app en el manifiesto |
| Nombre corto            | Nombre corto de la app           |
| Elegir ícono (192x192) | Elegir un ícono de app de 192x192px |
| Elegir ícono (512x512) | Elegir un ícono de app de 512x512px |

<br>

## Integración SIP

Si la opción ‘Habilitar SIP’ dentro de los ‘Ajustes principales’ está habilitada, se requieren varios ajustes subsiguientes para que las llamadas desde el lugar de trabajo funcionen correctamente.

**Del lado del estudio:**

| Campo de ajuste        | Propósito                                                               |
| ---------------------- | ----------------------------------------------------------------------- |
| Servidor SIP WebSocket | Dirección del servidor SIP WebSocket (por ejemplo, 'wss://test-pbx.aqtra.ru:8089/ws') |
| Dominio SIP            | Dominio SIP (realm)                                                    |

<br>

**Del lado del lugar de trabajo:**

| Campo de ajuste        | Propósito                                                               |
| ---------------------- | ----------------------------------------------------------------------- |
| Nombre de usuario SIP   | Nombre del usuario SIP                                                  |
| Contraseña de usuario SIP | Contraseña del usuario SIP                                            |
| Servidor SIP WebSocket | Dirección del servidor SIP WebSocket (por ejemplo, 'wss://test-pbx.aqtra.ru:8089/ws') |
| Dominio SIP            | Dominio SIP (realm)                                                    |

<br>

Si todos los parámetros están configurados correctamente, podrás realizar llamadas desde el lugar de trabajo. Puedes leer sobre el trabajo con SIP dentro del script del componente aquí: [Usando Python](../app-development/using-python.md).