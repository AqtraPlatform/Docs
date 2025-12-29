# Editor WYSIWYG

![](../../assets/images/app-development/wysiwyg-editor.png)

## Informações gerais
O editor WYSIWYG é um componente de interface do usuário projetado para inserir e editar texto rico no formato WYSIWYG. Ele fornece funcionalidade semelhante a editores como o Wordpad, permitindo que os usuários formatem facilmente o texto e insiram vários elementos de mídia.

## Parâmetros
**Propriedades do Componente:**

| Grupo de Configurações | Campo de Configuração | Opções de Valor          | Propósito |
|------------------------|-----------------------|--------------------------|-----------|
| (Configurações globais)        | Nome                  | -                        | Nome do Componente de UI no sistema |
| Comum                  | Desativado            | true, false              | Desativar um elemento |
|                        | Obrigatório           | true, false              | Campo obrigatório a ser preenchido |
|                        | Plugins               | -                        | Habilitar plugins |
|                        | Rótulo                | -                        | Descrição do campo |
|                        | Vinculação            | Multiseleção de Catálogo | Vinculação de dados |
| Eventos                | Ao valor alterado     | -                        | Evento de alteração de valor |
|                        | Ao pressionar tecla   | -                        | Evento de pressionar tecla |
|                        | Ao soltar tecla       | -                        | Evento de soltar tecla |
|                        | Ao focar              | -                        | Evento ao focar em um elemento |
| Índice de guia        | -                     | Inteiro                  | Ordem de troca de campo |

**Propriedades CSS:**

| Grupo de Configurações | Campo de Configuração | Opções de Valor          | Propósito |
|------------------------|-----------------------|--------------------------|-----------|
| Layout                 | Largura               | -                        | Largura do componente |
|                        | Altura                | -                        | Altura do componente |
|                        | Crescer               | true, false              | Estiramento do componente |
|                        | Margem                | -                        | Preenchimento externo |
|                        | Preenchimento         | -                        | Preenchimento interno |
| Aparência              | Raio de Canto         | -                        | Raio dos cantos |
|                        | Espessura da Borda    | -                        | Espessura da borda |
| Pincel                 | Fundo                 | -                        | Cor de fundo |
|                        | Pincel da Borda       | -                        | Cor da borda |

## Casos
- **Formatação de Texto**: Usado para criar documentos e conteúdos ricamente formatados.
- **Edição de Conteúdo**: Usado em sistemas de gerenciamento de conteúdo para facilitar a edição de artigos, blogs e outros conteúdos textuais.

## Exceções
- **Complexidade da Interface**: Pode ser difícil de usar para usuários sem experiência com editores semelhantes.
- **Limitações Técnicas**: Dependendo da implementação, pode não suportar todos os recursos de editores de texto avançados.