# Publicações

Para criar uma versão de componente, localização, extensão ou outra personalização apropriada via a plataforma, você deve publicá-la. E para que uma versão de componente seja publicada, ela deve ser marcada como pronta para publicação.

O processo de publicação é controlado através da máquina de estados, que permite controlar efetivamente todas as etapas e, em caso de erros, retornar o sistema ao estado anterior. Um recurso de bloqueio global foi introduzido para evitar que várias publicações sejam iniciadas ao mesmo tempo. Os usuários veem o status das publicações ativas e, após cada publicação ser concluída, os status dos objetos que estão prontos para serem publicados são atualizados automaticamente.

**Etapas para publicar um componente:**

- **Botão “Salvar”**: Usado para salvar as alterações atuais no componente.
- **“Pronto para Publicar”**: Marca um componente como pronto para publicação após todas as alterações terem sido salvas.

**Etapas para publicar localizações e integrações:**
- Tornam-se automaticamente disponíveis para publicação após você fazer alterações.

**Processo de Publicação:**
1. **Ir para Publicações**: Localizado em ‘Estúdio→Aplicações→Publicação.’
2. **Selecionando Itens para Publicar**: 
   - Componentes, localizações, integrações e módulos Python são selecionados para serem publicados.
3. **Publicação final**: 
   - O procedimento é concluído clicando no botão de publicar.
   - Uma notificação aparece quando a publicação é bem-sucedida.

![Publicações](../assets/images/app-development/publication-example.png)