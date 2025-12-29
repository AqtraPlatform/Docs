# Checkbox

![](../../assets/images/app-development/checkbox.png)

## Informações gerais
Uma “Checkbox” é um elemento de interface que permite aos usuários selecionar ou desmarcar um parâmetro ou opção específica. Este componente é amplamente utilizado para criar listas de parâmetros, gerenciar configurações ou selecionar várias opções ao mesmo tempo.

## Parâmetros
**Propriedades do componente**

| Grupo de configurações | Campo de configuração | Opções de valor | Propósito |
| --- | --- | --- | --- |
|  | Nome | - | Nome do Componente de UI no sistema |
| Comum | Desativado | true, false | A propriedade permite desativar um elemento no formulário |
|  | Obrigatório | true, false | A propriedade torna o elemento obrigatório para ser preenchido antes de enviar o formulário |
|  | Rótulo | - | Contém a tabela de conteúdos do contêiner de texto |
|  | Vínculo | Multiseleção de Catálogo | Contém um campo “Booleano” relacionado do modelo |
| Eventos | Ao valor alterado | - | Permite executar o script especificado após a alteração do valor do campo |

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
- **Seleção de Opção**: Os usuários podem selecionar ou desmarcar certos parâmetros ou opções.
- **Gerenciamento de Configurações**: A Checkbox é usada para habilitar ou desabilitar certas configurações ou recursos.
- **Seleção Múltipla**: No grupo de Checkbox, os usuários podem selecionar várias opções ao mesmo tempo.

## Exceções
- **Interface Não Intuitiva:** Com um grande número de checkboxes em uma página ou em formulários complexos, os usuários podem ter dificuldade em escolher opções.
- **Formulações Pouco Claras:** Se as formulações da Checkbox não forem informativas ou forem confusas, os usuários podem não entender o que estão escolhendo.