# Switch

![](../../assets/images/app-development/switch.png)

## Informações gerais
O componente “Switch” é um elemento de interface que permite ao usuário ativar ou desativar uma função, opção ou estado específico. Este componente é frequentemente utilizado para fornecer a capacidade de alternar rapidamente entre dois estados (Verdadeiro/Falso).

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
|  | Crescer | true, false | A propriedade determina quanto um elemento crescerá em relação aos outros elementos flex dentro do mesmo contêiner |
|  | Margem | - | A propriedade define os preenchimentos externos em todos os quatro lados do elemento |
|  | Preenchimento | - | A propriedade define os preenchimentos internos em todos os lados do elemento |
| Aparência | Raio de Canto | - | A propriedade é usada para arredondar os cantos de um elemento |
|  | Espessura da Borda | - | A propriedade permite definir os limites para o elemento |
| Pincel | Fundo | - | A propriedade define a cor de fundo do elemento |
|  | Pincel da Borda | - | A propriedade define a cor da borda do elemento |

## Casos 
- **Seleção Binária:** O Switch é utilizado para seleções binárias, como ativar/desativar som, notificações e outras opções.
- **Gerenciamento de Estado:** Você pode usar o Switch para gerenciar o estado de um elemento de interface específico.

## Exceções
- **Status Incerto:** Se não estiver claro o que os status ativado e desativado significam, os usuários podem ficar confusos.