# Selecionar

![](../../assets/images/app-development/select.png)

## Informações gerais
“Selecionar” é um elemento de interface que permite ao usuário escolher uma opção da lista apresentada. Este componente é amplamente utilizado para criar listas suspensas com uma escolha de opção ou categoria.

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

**Propriedades CSS**

| Grupo de configurações | Campo de configuração | Opções de valor | Propósito |
| --- | --- | --- | --- |
| Layout | Largura | - | Largura do componente |
|  | Altura | - | Altura do componente |
|  | Crescer | true, false | A propriedade determina o quanto um elemento irá crescer em relação aos outros elementos flex dentro do mesmo contêiner |
|  | Margem | - | A propriedade define os preenchimentos externos em todos os quatro lados do elemento |
|  | Preenchimento | - | A propriedade define os preenchimentos internos em todos os lados do elemento |
| Aparência | Raio de Canto | - | A propriedade é usada para arredondar os cantos de um elemento |
|  | Espessura da Borda | - | A propriedade permite definir os limites para o elemento |
| Pincel | Fundo | - | A propriedade define a cor de fundo do elemento |
|  | Cor da Borda | - | A propriedade define a cor da borda do elemento |

## Casos
- **Seleção da Lista:** Os usuários podem selecionar uma opção de uma lista de opções sugeridas.

## Exceções
- **Interface Não Intuitiva:** Se a lista não for intuitiva ou compreensível para o usuário, pode causar dificuldades na seleção de uma opção.
- **Velocidade de Download:** Se a lista for muito longa, carregar os itens selecionados exigirá uma espera adicional.