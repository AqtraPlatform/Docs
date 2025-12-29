# Publicaciones

Para crear una versión de componente, localización, extensión u otra personalización adecuada a través de la plataforma, debes publicarla. Y para que una versión de componente sea publicada, debe estar marcada como lista para publicar.

El proceso de publicación se controla a través de la máquina de estados, que te permite controlar efectivamente todas las etapas y, en caso de errores, devolver el sistema al estado anterior. Se ha introducido una función de bloqueo global para evitar que se inicien múltiples publicaciones al mismo tiempo. Los usuarios ven el estado de las publicaciones activas, y después de que cada publicación se complete, los estados de los objetos que están listos para ser publicados se actualizan automáticamente.

**Pasos para publicar un componente:**

- **Botón “Guardar”**: Se utiliza para guardar los cambios actuales en el componente.
- **“Listo para Publicar”**: Marca un componente como listo para publicar después de que se hayan guardado todos los cambios.

**Pasos para publicar localizaciones e integraciones:**
- Se vuelven automáticamente disponibles para publicación después de que realices cambios.

**Proceso de Publicación:**
1. **Ir a Publicaciones**: Ubicado en ‘Estudio→Aplicaciones→Publicación.’
2. **Seleccionar Elementos para Publicar**: 
   - Se seleccionan componentes, localizaciones, integraciones y módulos de Python para ser publicados.
3. **Publicación final**: 
   - El procedimiento se completa haciendo clic en el botón de publicar.
   - Aparece una notificación cuando la publicación es exitosa.

![Publicaciones](../assets/images/app-development/publication-example.png)