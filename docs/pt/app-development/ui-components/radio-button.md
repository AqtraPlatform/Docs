# Botão de Rádio

![](../../assets/images/app-development/radio-button.png)

## Informações gerais
O componente “Botão de Rádio” é um elemento de interface que permite ao usuário selecionar uma das opções fornecidas. Este componente é utilizado para implementar a seleção de um único elemento entre várias opções mutuamente exclusivas.

## Parâmetros
**Propriedades do componente**

| Grupo de configurações | Campo de configuração | Opções de valor | Propósito |
| --- | --- | --- | --- |
|  | Nome | - | Nome do Componente de UI no sistema |
| Comum | Desativado | true, false | A propriedade permite desativar um elemento no formulário |
|  | Obrigatório | true, false | A propriedade torna o elemento obrigatório para ser preenchido antes de enviar o formulário |
|  | Rótulo | - | Contém a tabela de conteúdos do contêiner de texto |
|  | Vínculo | Multiseleção de Catálogo | Contém um campo “Catálogo” relacionado do modelo |
| Eventos | Ao valor alterado | - | Permite executar o script especificado após a alteração do valor do campo |
|  | Ao foco |  | Permite executar o script especificado quando em foco |

**Propriedades CSS**

| Grupo de configurações | Campo de configuração | Opções de valor | Propósito |
| --- | --- | --- | --- |
| Layout | Largura | - | Largura do componente |
|  | Altura | - | Altura do componente |
|  | Crescer | true, false | A propriedade determina quanto um elemento crescerá em relação aos outros elementos flex dentro do mesmo contêiner |
|  | Margem | - | A propriedade define os preenchimentos externos em todos os quatro lados do elemento |
|  | Preenchimento | - | A propriedade define os preenchimentos internos em todos os lados do elemento |
| Aparência | Raio de Canto | - | A propriedade é usada para arredondar os cantos de um elemento |
|  | Espessura da Borda | - | A propriedade permite definir os limites para o elemento |
| Pincel | Fundo | - | A propriedade define a cor de fundo do elemento |
|  | Pincel da Borda | - | A propriedade define a cor da borda do elemento |

## Casos
- **Seleção de Opção Única:** Os usuários podem selecionar apenas uma opção da lista.
- **Opções Mutuamente Exclusivas:** O componente Botão de Rádio é utilizado para criar um conjunto de opções mutuamente exclusivas das quais apenas uma pode ser selecionada.

## Exceções
- **Informações Insuficientes:** Se os rótulos dos botões de rádio não forem suficientemente informativos, os usuários podem ter dificuldade em selecionar opções.
- **Escolha Difícil:** Com um grande número de botões de rádio ou organização pouco clara, a escolha pode ser difícil para os usuários.