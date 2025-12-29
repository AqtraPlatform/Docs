# Comenzando

> Un punto de entrada estructurado para los recién llegados a Aqtra. Tono técnico. Esta página enlaza documentación, tutoriales, videos (con transcripciones) y un ejemplo ejecutable para formar una hoja de ruta de aprendizaje progresivo.

---

## ¿Qué es Aqtra?

Aqtra es una **plataforma de bajo código** para construir aplicaciones empresariales principalmente a través de una interfaz visual, con **scripting en Python** opcional para lógica avanzada. Este modelo híbrido acelera la entrega para principiantes y permite a los desarrolladores extender y personalizar cuando sea necesario.

**Aprenderás a:**

- Instalar y ejecutar Aqtra (en la nube o localmente a través de Docker).
- Construir una primera característica de principio a fin (modelo de datos → componente de UI → flujo de datos → publicar).
- Usar scripts de Python donde sea apropiado.
- Integrar con servicios externos y APIs.

> **Público objetivo:** desarrolladores ciudadanos, desarrolladores junior de front‑/back‑end, analistas, arquitectos, líderes de equipo.

**CTAs principales:**

- **Comienza en 60 minutos →** Recorrido de la primera característica (ver [4) Primera victoria](#4-first-win-in-60-minutes))
- **Documentación →** [https://docs.aqtra.io/](https://docs.aqtra.io/es/)
- **Ruta de video →** [https://www.youtube.com/@Aqtra.Academy](https://www.youtube.com/@Aqtra.Academy)

**Enlaces rápidos (tarjetas):**

- **Instalar** → [5) Instalar y Acceder](#5-install--access) (Nube / Docker)
- **Construir tu primera pantalla (Factura)** → [4) Primera victoria](#4-first-win-in-60-minutes)
- **Fundamentos de DataFlow** → [2) Ruta de aprendizaje paso a paso](#2-stepbystep-learning-path-single-track)
- **Publicar en la web** → [2) Ruta de aprendizaje paso a paso](#2-stepbystep-learning-path-single-track)

**En esta página**

- [1) Metodología — cómo usar esta guía](#1-methodology--how-to-use-this-guide)
- [2) Ruta de aprendizaje paso a paso](#2-stepbystep-learning-path-single-track)
- [3) Tutoriales y enlaces cruzados de documentación](#tutorials-documentation-cross-links)
- [4) Primera victoria en ~60 minutos](#4-first-win-in-60-minutes)
- [5) Instalar y Acceder](#5-install--access)
- [6) Conceptos básicos (Glosario de Aqtra)](#6-core-concepts-aqtra-glossary)
- [7) Ruta de Video](#7-video-track-with-transcripts--timecodes)
- [8) Biblioteca de Pasos de DataFlow](#8-dataflow-step-library-quick-reference)
- [9) FAQ](#9-faq-short-practical)

---

## 1) Metodología — cómo usar esta guía {: #1-methodology--how-to-use-this-guide }

- **Progresión de una sola pista**: un camino unificado para todos los roles, conceptos nuevos mínimos por paso.
- **Enlace de primera mención**: cada concepto/elemento de UI está vinculado una vez en la primera aparición; los pasos posteriores asumen esto.
- **Profundidad justo a tiempo**: cada paso hace referencia a documentos enfocados y un video corto con marcas de tiempo clicables.
- **Resultados visibles**: cada paso termina en un resultado concreto y comprobable en Workplace.
- **Mentalidad de error primero**: el Paso 10 enseña depuración sistemática/análisis de logs.
- **Evaluación**: el **Capstone** (Paso 11) valida CRUD, integración, plantillas, navegación y roles/permisos.

### Alcance y requisitos previos

- Acceso a **Aqtra Studio/Workplace** (inquilino en la nube) _o_ una configuración local de **Docker** (≥ 4 vCPU / 8 GB RAM).
- Navegador moderno y la capacidad de ver la pestaña **Red** de devtools.
- (Opcional) Familiaridad básica con JSON y APIs HTTP para el Paso 6.

### Resultados de aprendizaje (por paso)

- **Paso 1**: puedes acceder a Studio/Workplace.
- **Paso 2**: puedes modelar una entidad (Factura) y mostrarla en un Componente visible en Workplace.
- **Paso 3**: puedes construir un DataFlow y vincularlo a un Botón.
- **Paso 4**: puedes completar CRUD y validación básica.
- **Paso 5**: puedes agregar lógica de Python en un flujo.
- **Paso 6**: puedes llamar a una API HTTP externa y mapear resultados.
- **Paso 7**: puedes componer una página MultiComponent con contexto de datos.
- **Paso 8**: puedes navegar entre páginas con parámetros de acción.
- **Paso 9**: puedes renderizar y descargar un documento de una plantilla.
- **Paso 10**: puedes diagnosticar errores usando logs/devtools y republicar.
- **Paso 11**: puedes entregar una pequeña característica con roles/permisos y una integración.

### Bucle de retroalimentación

- Después de **Primera victoria** y **Capstone**, captura retroalimentación: qué fue poco claro, dónde aparecieron errores y qué enlaces/videos ayudaron más; retroalimenta esto en la documentación.

### Rubrica de evaluación (Capstone)

- [ ] CRUD funciona con validación y mensajes claros para el usuario.
- [ ] Llamada a API externa mapeada; fallos manejados (timeouts/4xx/5xx).
- [ ] Plantilla de documento renderizada; archivo es descargable.
- [ ] Navegación a través de parámetros de acción abre el registro/página correcta.
- [ ] Al menos **2 roles** configurados con diferentes accesos.
- [ ] Todos los componentes **Publicados** sin advertencias bloqueantes.

---

## 2) Ruta de aprendizaje paso a paso (pista única)

Un camino unificado para todos los roles. Sigue los pasos en orden; cada paso enlaza a documentos y (opcionalmente) a un video corto.

**Paso 1 — Acceder a Aqtra (nube o Docker)**
Obtén una instancia en funcionamiento (ver Sección 4). Verifica que puedes abrir **Studio** y **Workplace**.

**Paso 2 — Primer esqueleto de aplicación**
Crea un **DataModel** mínimo (por ejemplo, `Invoice(number, title, totalAmount, dueDate)`) y un **Componente** para mostrar/editarlo. Publica y añade a la navegación para que aparezca en Workplace.

**Docs**: Componente → [https://docs.aqtra.io/app-development/component.html](https://docs.aqtra.io/es/app-development/component.html) ; Catálogo de UI → [https://docs.aqtra.io/app-development/ui-components/index.html](https://docs.aqtra.io/es/app-development/ui-components/index.html)
**Video**: Tutorial #1 → [https://youtu.be/GaUr5ET4dfQ](https://youtu.be/GaUr5ET4dfQ) ; Tutorial #2 → [https://youtu.be/UEG2pmct74s](https://youtu.be/UEG2pmct74s)

**Paso 3 — Fundamentos de DataFlow**
Agrega un **DataFlow** con etapas/pasos: `Get Action Model → Update Entry → Write Response`. Vincúlalo a un **Botón** y prueba crear/actualizar.

**Docs**: Visión general de Dataflow → [https://docs.aqtra.io/app-development/data-flow-components/index.html](https://docs.aqtra.io/es/app-development/data-flow-components/index.html) ; Actualizar entrada → [https://docs.aqtra.io/app-development/data-flow-components/update-entry.html](https://docs.aqtra.io/es/app-development/data-flow-components/update-entry.html) ; Ejecutar dataflow → [https://docs.aqtra.io/app-development/data-flow-components/execute-dataflow.html](https://docs.aqtra.io/es/app-development/data-flow-components/execute-dataflow.html)
**Video**: Tutorial #3 — ([05:16](https://youtu.be/UEG2pmct74s?t=316)–[07:30](https://youtu.be/UEG2pmct74s?t=450))

**Paso 4 — Finalización de CRUD**
Agrega vistas de lista/detalle, termina los flujos de crear/actualizar/eliminar y validaciones.

**Docs**: Data Grid → [https://docs.aqtra.io/app-development/ui-components/data-grid.html](https://docs.aqtra.io/es/app-development/ui-components/data-grid.html)
**Video**: Tutorial #4 — eliminar a través de Actualizar Entrada ([05:18](https://youtu.be/oLoYMSAlLVo?t=318)–[06:20](https://youtu.be/oLoYMSAlLVo?t=380)); Tutorial #5 — filtros dinámicos ([00:13](https://youtu.be/YuU_YomoNaw?t=13)–[03:00](https://youtu.be/YuU_YomoNaw?t=180))

**Paso 5 — Scripting en Python para lógica empresarial**
Inserta un paso de **Script de Python** para calcular campos derivados y validar entradas.

**Docs**: Ejecutar script → [https://docs.aqtra.io/app-development/data-flow-components/execute-script.html](https://docs.aqtra.io/es/app-development/data-flow-components/execute-script.html)
**Video**: Tutorial #6 — Ejecutar Script ([04:10](https://youtu.be/bOR2nOk_S0c?t=250)–[06:10](https://youtu.be/bOR2nOk_S0c?t=370))

**Paso 6 — Integraciones externas**
Llama a una API HTTP externa desde un script de Python; mapea la respuesta a tu DataModel.

**Docs**: Ejecutar llamada a API → [https://docs.aqtra.io/app-development/data-flow-components/execute-api-call.html](https://docs.aqtra.io/es/app-development/data-flow-components/execute-api-call.html)
**Video**: (Opcional) Tutorial #10 — diagnosticando desajustes de carga/tipo ([01:46](https://youtu.be/qJcpIQQEqbo?t=106)–[05:00](https://youtu.be/qJcpIQQEqbo?t=300))

!!! tip "Solución de problemas"
_ **Timeout/5xx**: verifica URL/método/cabeceras; añade reintentos/retrasos; registra el cuerpo de la respuesta.
_ **401/403**: proporciona/renueva el token de autenticación (almacena secretos de forma segura).
_ **406/422 (desajuste de tipo)**: corrige el mapeo de campos y tipos; transforma en **Ejecutar Script** (por ejemplo, cadena → número/fecha) antes de `Update Entry`.
_ Usa `context.Logger` para registrar IDs de correlación y fragmentos de carga.

**Paso 7 — Páginas MultiComponent**
Compón una página a partir de varios componentes (filtros + cuadrícula + formulario). Configura **contexto de datos** y cableado.

**Docs**: Vista de Lista → [https://docs.aqtra.io/app-development/ui-components/list-view.html](https://docs.aqtra.io/es/app-development/ui-components/list-view.html) ; Control de Pestañas → [https://docs.aqtra.io/app-development/ui-components/tab-control.html](https://docs.aqtra.io/es/app-development/ui-components/tab-control.html) ; Gráficos → [https://docs.aqtra.io/app-development/ui-components/charts.html](https://docs.aqtra.io/es/app-development/ui-components/charts.html)
**Video**: Tutorial #6 — diálogo modal + cuadrícula de auto‑actualización ([10:45](https://youtu.be/bOR2nOk_S0c?t=645)–[17:00](https://youtu.be/bOR2nOk_S0c?t=1020)); Tutorial #7 — Vista de Lista ([00:59](https://youtu.be/PtAJwn07sWI?t=59)–[03:00](https://youtu.be/PtAJwn07sWI?t=180))

> **Consejo de diseño (opcional)**: agrupa entradas relacionadas en paneles, mantén un ritmo vertical consistente (múltiplos de 8–12px), evita el uso excesivo de gráficos—añádelos solo cuando aclaren tendencias.

**Paso 8 — Navegación y cableado entre páginas**
Agrega elementos de menú y abre páginas con **parámetros de acción** (pasa el registro `id` de la cuadrícula al formulario).

**Docs**: Acciones de botón → [https://docs.aqtra.io/app-development/ui-components/button.html](https://docs.aqtra.io/es/app-development/ui-components/button.html)
**Video**: Tutorial #12 — abrir página + mapeo de parámetros ([06:18](https://youtu.be/k36-qpZa9bU?t=378)–[07:00](https://youtu.be/k36-qpZa9bU?t=420)); Tutorial #5 — Abrir aplicación desde la cuadrícula ([10:53](https://youtu.be/YuU_YomoNaw?t=653)–[11:20](https://youtu.be/YuU_YomoNaw?t=680))

**Paso 9 — Plantillas y generación de documentos (PDF)**
Renderiza y descarga un documento de una plantilla a través de DataFlow.

**Docs**: Componentes de dataflow (Renderizar Plantilla) → [https://docs.aqtra.io/app-development/data-flow-components/index.html](https://docs.aqtra.io/es/app-development/data-flow-components/index.html)
**Video**: Tutorial #12 — renderizar plantilla + descargar ([01:37](https://youtu.be/k36-qpZa9bU?t=97)–[02:45](https://youtu.be/k36-qpZa9bU?t=165); [05:20](https://youtu.be/k36-qpZa9bU?t=320)–[07:00](https://youtu.be/k36-qpZa9bU?t=420))

**Paso 10 — Manejo de errores y depuración**
Usa la pestaña de Red y los logs de Studio para diagnosticar 4xx/5xx; corrige tipos; republica.

**Docs**: Publicación de aplicaciones → [https://docs.aqtra.io/app-development/publishing-applications.html](https://docs.aqtra.io/es/app-development/publishing-applications.html)
**Video**: Tutorial #10 — encontrar y corregir errores ([01:46](https://youtu.be/qJcpIQQEqbo?t=106)–[05:00](https://youtu.be/qJcpIQQEqbo?t=300))

!!! tip "Solución de problemas"

- Sigue la secuencia: **Compilar → Guardar → Listo para publicar → Publicar**; verifica que el componente esté listado como _Publicado_.
- Usa devtools del navegador **Red** para comparar solicitud/respuesta con el esquema esperado; corrige mapeo/tipos.
  _ Si el comportamiento difiere entre páginas, verifica que **todos los componentes dependientes** se hayan republicado juntos.
  _ En configuraciones de Docker, inspecciona los logs del contenedor para rastros de pila y conflictos de puertos.

**Paso 11 — Capstone**
Extiende tu aplicación a una pequeña característica (por ejemplo, Mini‑CRM): roles/permisos, panel de control MultiComponent, una integración, una plantilla de documento. Documenta los criterios de aceptación y haz un video corto de demostración.

[Volver al inicio](#getting-started)

---

## 3) Tutoriales y enlaces cruzados de documentación {: #tutorials-documentation-cross-links }

**Instalar / Plataforma**

- Configuraciones básicas, autenticación, logs, métricas → [https://docs.aqtra.io/install1/basic-settings.html](https://docs.aqtra.io/es/install1/basic-settings.html)

**Construcción básica**

- Componente (creación, configuraciones básicas) → [https://docs.aqtra.io/app-development/component.html](https://docs.aqtra.io/es/app-development/component.html)
- Catálogo de componentes de UI (primera mención) → [https://docs.aqtra.io/app-development/ui-components/index.html](https://docs.aqtra.io/es/app-development/ui-components/index.html)
- Data Grid (primera mención) → [https://docs.aqtra.io/app-development/ui-components/data-grid.html](https://docs.aqtra.io/es/app-development/ui-components/data-grid.html)
- Vista de Lista / Control de Pestañas / Gráficos (primera mención) → [https://docs.aqtra.io/app-development/ui-components/list-view.html](https://docs.aqtra.io/es/app-development/ui-components/list-view.html), [https://docs.aqtra.io/app-development/ui-components/tab-control.html](https://docs.aqtra.io/es/app-development/ui-components/tab-control.html), [https://docs.aqtra.io/app-development/ui-components/charts.html](https://docs.aqtra.io/es/app-development/ui-components/charts.html)

**Flujos / Lógica**

- Visión general de Dataflow → [https://docs.aqtra.io/app-development/data-flow-components/index.html](https://docs.aqtra.io/es/app-development/data-flow-components/index.html)
- Actualizar Entrada (CRUD) → [https://docs.aqtra.io/app-development/data-flow-components/update-entry.html](https://docs.aqtra.io/es/app-development/data-flow-components/update-entry.html)
- Ejecutar dataflow → [https://docs.aqtra.io/app-development/data-flow-components/execute-dataflow.html](https://docs.aqtra.io/es/app-development/data-flow-components/execute-dataflow.html)
- Ejecutar script (Python) → [https://docs.aqtra.io/app-development/data-flow-components/execute-script.html](https://docs.aqtra.io/es/app-development/data-flow-components/execute-script.html)
- Ejecutar llamada a API → [https://docs.aqtra.io/app-development/data-flow-components/execute-api-call.html](https://docs.aqtra.io/es/app-development/data-flow-components/execute-api-call.html)

**Publicación**

- Publicación de aplicaciones → [https://docs.aqtra.io/app-development/publishing-applications.html](https://docs.aqtra.io/es/app-development/publishing-applications.html)

**Tutoriales (docs)**

- Tutorial #1 → [https://docs.aqtra.io/tutorials/tutorial1.html](https://docs.aqtra.io/es/tutorials/tutorial1.html)
- Tutorial #2 → [https://docs.aqtra.io/tutorials/tutorial2.html](https://docs.aqtra.io/es/tutorials/tutorial2.html)
- Tutorial #3 → [https://docs.aqtra.io/tutorials/tutorial3.html](https://docs.aqtra.io/es/tutorials/tutorial3.html)

**Índice de videos (marcas de tiempo clicables)**

- T#3 — Fundamentos de DataFlow ([05:16](https://youtu.be/UEG2pmct74s?t=316)–[07:30](https://youtu.be/UEG2pmct74s?t=450)).
- T#4 — Eliminar a través de Actualizar Entrada ([05:18](https://youtu.be/oLoYMSAlLVo?t=318)–[06:20](https://youtu.be/oLoYMSAlLVo?t=380)).
- T#5 — Filtros de Data Grid; Abrir aplicación ([00:13](https://youtu.be/YuU_YomoNaw?t=13)–[03:00](https://youtu.be/YuU_YomoNaw?t=180)), ([10:53](https://youtu.be/YuU_YomoNaw?t=653)–[11:20](https://youtu.be/YuU_YomoNaw?t=680)).
- T#6 — Ejecutar Script; diálogo modal; cuadrícula de auto‑actualización ([04:10](https://youtu.be/bOR2nOk_S0c?t=250)–[06:10](https://youtu.be/bOR2nOk_S0c?t=370)), ([10:45](https://youtu.be/bOR2nOk_S0c?t=645)–[17:00](https://youtu.be/bOR2nOk_S0c?t=1020)).
- T#10 — Depurar 500→406; corregir tipos; republicar ([01:46](https://youtu.be/qJcpIQQEqbo?t=106)–[05:00](https://youtu.be/qJcpIQQEqbo?t=300)).
- T#12 — Renderizar plantilla; Descargar; Abrir página + mapeo ([01:37](https://youtu.be/k36-qpZa9bU?t=97)–[02:45](https://youtu.be/k36-qpZa9bU?t=165)), ([06:18](https://youtu.be/k36-qpZa9bU?t=378)–[07:00](https://youtu.be/k36-qpZa9bU?t=420)).

---

## 4) Primera victoria en ~60 minutos

> Construye la mini‑característica **Inventario de Facturas** de principio a fin.

1. **Accede a Aqtra** (nube o Docker) y abre **Studio**.
2. **Crea DataModel** `Invoice(number, title, totalAmount, dueDate)`.
3. **Agrega un Componente** para crear/listar facturas (primer uso de Data Grid).
4. **Cablea un DataFlow** — `Get Action Model → Update Entry → Write Response` (opcional **Ejecutar Script** para validar totalAmount).
5. **Publica** y verifica en **Workplace**: crea dos facturas, edita una.

**Docs**: Tutoriales → Construye tu primera aplicación — [https://docs.aqtra.io/tutorials/index.html](https://docs.aqtra.io/es/tutorials/index.html)

---

## 5) Instalar y Acceder {: #5-install--access }

Elige una de las siguientes opciones. Mantén las credenciales y claves de licencia seguras.

### Opción 1 — Nube (Alojada)

- Obtén acceso a través de un socio de alojamiento o compra directamente.
- Precios y adquisición: [https://aqtra.io/#price](https://aqtra.io/#price).
- Recibe una URL de organización/inquilino y credenciales.
- Configura SSO (opcional), usuarios y roles.

### Opción 2 — Local (Docker)

**Requisitos previos**: Docker Engine/Compose último; host Linux/Windows/macOS con **4 vCPU / 8 GB RAM** mínimo.

**Lista de verificación**

- [ ] Instala Docker/Compose y verifica que `docker ps` funcione.
- [ ] Prepara `docker-compose.yml` y `.env` con los secretos requeridos.
- [ ] Inicia DB → `docker compose up -d db` y espera a que esté listo.
- [ ] Inicia la aplicación → `docker compose up -d app`.
- [ ] Accede a **Workplace** en `http://<host>:8080/` y **Studio** en `http://<host>:8080/studio/`.

**Docs**: Configuraciones básicas (arquitectura, puertos, autenticación, logs, métricas) → [https://docs.aqtra.io/install1/basic-settings.html](https://docs.aqtra.io/es/install1/basic-settings.html)

[Volver al inicio](#getting-started)

---

## 6) Conceptos básicos (Glosario de Aqtra)

Definiciones cortas y accionables.

- **Componente** — un bloque de construcción de UI que renderiza datos y acciones para los usuarios (formulario, lista, detalle, etc.). [https://docs.aqtra.io/app-development/component.html](https://docs.aqtra.io/es/app-development/component.html)
- **DataFlow** — un flujo dirigido de operaciones (por ejemplo, validar → transformar → persistir → notificar) que se ejecuta en eventos de usuario o del sistema. Pasos típicos: **Obtener Modelo de Acción**, **Actualizar Entrada**, **Escribir Respuesta**, **Ejecutar Script**, **Ejecutar llamada a API**. [https://docs.aqtra.io/app-development/data-flow-components/index.html](https://docs.aqtra.io/es/app-development/data-flow-components/index.html)
- **DataModel** — la definición estructurada de entidades/atributos que la aplicación persiste y manipula.
- **MultiComponent** — una vista compuesta que ensambla varios Componentes (por ejemplo, lista + detalles + filtros) en una página cohesiva; los elementos utilizan **contexto de datos** para vincularse a un componente fuente.
- **Script de Python** — paso de lógica personalizada incrustado en un flujo para transformar datos, llamar a servicios o implementar reglas. [https://docs.aqtra.io/app-development/data-flow-components/execute-script.html](https://docs.aqtra.io/es/app-development/data-flow-components/execute-script.html)

---

## 7) Ruta de Video (con transcripciones y códigos de tiempo) {: #7-video-track-with-transcripts--timecodes }

Lista de videos centralizada con enlaces profundos y marcas de tiempo. Usa estos para saltar directamente a los momentos de demostración relevantes.

- **Tutorial #1** — [https://youtu.be/GaUr5ET4dfQ](https://youtu.be/GaUr5ET4dfQ)
- **Tutorial #2** — [https://youtu.be/UEG2pmct74s](https://youtu.be/UEG2pmct74s)
- **Tutorial #3** — Fundamentos de DataFlow ([05:16](https://youtu.be/UEG2pmct74s?t=316)–[07:30](https://youtu.be/UEG2pmct74s?t=450))
- **Tutorial #4** — Eliminar a través de Actualizar Entrada ([05:18](https://youtu.be/oLoYMSAlLVo?t=318)–[06:20](https://youtu.be/oLoYMSAlLVo?t=380))
- **Tutorial #5** — Filtros de Data Grid; Abrir aplicación ([00:13](https://youtu.be/YuU_YomoNaw?t=13)–[03:00](https://youtu.be/YuU_YomoNaw?t=180)), ([10:53](https://youtu.be/YuU_YomoNaw?t=653)–[11:20](https://youtu.be/YuU_YomoNaw?t=680))
- **Tutorial #6** — Ejecutar Script; diálogo modal; cuadrícula de auto‑actualización ([04:10](https://youtu.be/bOR2nOk_S0c?t=250)–[06:10](https://youtu.be/bOR2nOk_S0c?t=370)), ([10:45](https://youtu.be/bOR2nOk_S0c?t=645)–[17:00](https://youtu.be/bOR2nOk_S0c?t=1020))
- **Tutorial #7** — [https://youtu.be/PtAJwn07sWI](https://youtu.be/PtAJwn07sWI)
- **Tutorial #8** — [https://youtu.be/YfqfdJpDm-k](https://youtu.be/YfqfdJpDm-k)
- **Tutorial #9/10** — Depuración y diagnósticos ([01:46](https://youtu.be/qJcpIQQEqbo?t=106)–[05:00](https://youtu.be/qJcpIQQEqbo?t=300))
- **Tutorial #11** — [https://youtu.be/d-FD1ARn0h0](https://youtu.be/d-FD1ARn0h0)
- **Tutorial #12** — Renderizar plantilla; Descargar; Abrir página + mapeo ([01:37](https://youtu.be/k36-qpZa9bU?t=97)–[02:45](https://youtu.be/k36-qpZa9bU?t=165)), ([06:18](https://youtu.be/k36-qpZa9bU?t=378)–[07:00](https://youtu.be/k36-qpZa9bU?t=420))

!!! note "Mantente actualizado"
Suscríbete a **Aqtra Academy** en YouTube y revisa regularmente la raíz de la documentación para actualizaciones. Nuevos episodios se enlazarán aquí a medida que lleguen.

[Volver al inicio](#getting-started)

---

## 8) Biblioteca de Pasos de DataFlow (referencia rápida)

Algunos pasos útiles que probablemente usarás más allá de CRUD:

- **Actualizar Entrada** — [https://docs.aqtra.io/app-development/data-flow-components/update-entry.html](https://docs.aqtra.io/es/app-development/data-flow-components/update-entry.html)
- **Ejecutar dataflow** — llama a otro dataflow y fusiona resultados.
  [https://docs.aqtra.io/app-development/data-flow-components/execute-dataflow.html](https://docs.aqtra.io/es/app-development/data-flow-components/execute-dataflow.html)
- **Ejecutar llamada a API** — configura y ejecuta solicitud HTTP, vincula resultados.
  [https://docs.aqtra.io/app-development/data-flow-components/execute-api-call.html](https://docs.aqtra.io/es/app-development/data-flow-components/execute-api-call.html)
- **Obtener entidad por id** — busca entidad por identificador a través de campo de catálogo.
  [https://docs.aqtra.io/app-development/data-flow-components/get-entity-by-id.html](https://docs.aqtra.io/es/app-development/data-flow-components/get-entity-by-id.html)
- **Actualizar campo de modelo** — establece/deriva un solo campo dentro del modelo.
  [https://docs.aqtra.io/workflow-components/update-model-field.html](https://docs.aqtra.io/es/workflow-components/update-model-field.html)
- **Matemáticas simples** — suma/resta/multiplica y escribe en un campo objetivo.
  [https://docs.aqtra.io/app-development/data-flow-components/simple-math.html](https://docs.aqtra.io/es/app-development/data-flow-components/simple-math.html)
- **Almacenar entrada sobre bus** — crea/almacena instancia de componente de forma asíncrona.
  [https://docs.aqtra.io/app-development/data-flow-components/store-entry-over-bus.html](https://docs.aqtra.io/es/app-development/data-flow-components/store-entry-over-bus.html)
- **Suscribirse a conector** — por ejemplo, suscripción a RabbitMQ → procesar → guardar.
  [https://docs.aqtra.io/app-development/data-flow-components/subscribe-to-connector.html](https://docs.aqtra.io/es/app-development/data-flow-components/subscribe-to-connector.html)

[Volver al inicio](#getting-started)

---

## 9) FAQ (corto, práctico)

**P: ¿Nube vs local?**
R: Nube para la incorporación más rápida/acceso del equipo; Docker local para entornos fuera de línea/PoCs/restringidos.

**P: Docker no inicia o es lento.**
R: Asegúrate de tener 4 vCPU/8 GB RAM+, libera los puertos de destino y verifica los logs del contenedor. Reinicia Docker y vuelve a intentar componer.

**P: ¿Dónde poner lógica personalizada?**
R: Agrega un paso de **Script de Python** dentro de un **DataFlow** para validar, transformar o llamar a APIs externas.

**P: ¿Cómo llamar a servicios externos?**
R: Usa `http.client` desde un script de Python; mapea la respuesta a tu DataModel.

**P: ¿Principales bloques de construcción?**
R: **DataModel**, **Componente**, **DataFlow**, **MultiComponent**, **Script de Python**.

**P: ¿Errores y excepciones?**
R: Usa el inspector de red y los logs de Studio; corrige desajustes de tipo, republica y vuelve a probar. Consulta el video en la Sección 8.

**P: ¿Cómo comprar o obtener una prueba?**
R: Consulta precios: [https://aqtra.io/#price](https://aqtra.io/#price). Compra a través de un proveedor o directamente; para implementaciones alojadas, sigue la incorporación del socio.

---

## 10) ¿Qué sigue?

- Patrones y mejores prácticas (nomenclatura, versionado, pruebas de flujos).
- Integraciones avanzadas (SSO, bases de datos, colas de mensajes).
- Flujos de trabajo en equipo (revisiones de código para scripts, promoción de entornos).
- Enlaces a la comunidad y soporte (Slack/Telegram/Foro) — _agregar cuando esté disponible_.