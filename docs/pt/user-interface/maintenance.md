# Menu de Manutenção

<br>

O menu “Manutenção” é uma ferramenta poderosa para gerenciar dados e manter o sistema, especialmente após grandes atualizações, migrações de dados ou alterações no banco de dados.
<br>

## Descrição geral

- **Propósito**: Gerenciar dados do PostgreSQL via ODATA, remover dados excluídos, analisar e gerenciar logs do sistema.
- **Recursos**: A ferramenta é utilizada principalmente após atualizações de versão da plataforma, importações de componentes ou alterações massivas de dados.
  <br>

## Abas do menu de manutenção

<br>

### Logs do sistema

<br>

! [Logs do sistema] (system-logs.png)
<br>

- **Funcionalidade**: Visualizar logs do sistema atuais e ajustar níveis de log (Trace, Debug, Information, Warning, Critical, Error, None).
  <br>

### Manutenção do sistema

<br>

! [Manutenção do sistema] (system-maintenance.png)
<br>

1. **Reconstruir Referências do Banco de Dados**: Verificar e reconstruir referências cruzadas entre componentes ou dentro de componentes (fluxo de dados/fluxo de trabalho).
2. **Reconstruir Regras RLS**: Reconstruir regras de Segurança em Nível de Linha para personalizar o acesso aos dados.
3. **Reconstruir Cache**: Reconstruir o cache interno da plataforma, resolvendo problemas com atualizações.
4. **Análise marcada para exclusão**: Visualizar e gerenciar registros marcados para exclusão usando a flag ‘Marcar entrada para exclusão’ na etapa ‘Atualizar entrada’. Após clicar no botão “Análise marcada para exclusão”, todas as entradas marcadas são exibidas. As entradas são selecionadas e excluídas via “Excluir itens selecionados”. O sistema impedirá que entradas sejam excluídas se houver entradas relacionadas não marcadas.
5. **Redefinir publicação atual**: Redefine o processo de publicação se ele falhar.
   <br>

### Armazenamento de arquivos

Esta seção adiciona a capacidade de configurar as seguintes configurações para Armazenamento de arquivos:

| Tipos de arquivo aceitáveis | Limite de tamanho do arquivo em bytes |
| --------------------------- | ------------------------------------- |
| .\* (todos os tipos de arquivo)  | tamanho selecionado                   |

<br>

Você pode especificar tipos de filtro, separando-os com vírgulas. Isso pode ser extensões de arquivo, como .jpg, .json, .docx, ou tipos Mime, por exemplo, image/_, application/_

Você também pode combinar filtros, por exemplo, `image/*`, `.docx`.
Usar o filtro `*/*` permite que você faça upload de quaisquer arquivos.
<br>

![Manutenção de armazenamento de arquivos](../assets/images/user-interface/file-storage-maintenance.png)