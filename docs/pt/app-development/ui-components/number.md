# Número

![](../../assets/images/app-development/number.png)

## Informações gerais
O componente “Número” é uma interface para a entrada de valores numéricos. Este componente permite que os usuários insiram números e pode ser utilizado para diversos propósitos, como inserir números, quantidades ou outros dados numéricos.

## Parâmetros
**Propriedades do componente**

| Grupo de configurações | Campo de configuração | Opções de valor | Propósito |
| --- | --- | --- | --- |
|  | Nome | - | Nome do Componente de UI no sistema |
| Comum | Desativado | true, false | A propriedade permite desativar um elemento no formulário |
|  | Obrigatório | true, false | A propriedade torna o elemento obrigatório para ser preenchido antes de enviar o formulário |
|  | Rótulo | - | Contém a tabela de conteúdos do contêiner de texto |
|  | Vínculo | Multiseleção de Catálogo | Contém o campo “Inteiro” e “Número” associado do modelo |
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
|  | Cor da Borda | - | A propriedade define a cor da borda do elemento |

## Casos
- **Inserindo Valores Numéricos:** Os usuários podem inserir números no componente Número, como quantidades de produtos ou parâmetros numéricos.
- **Limite de Faixa:** Valores mínimos e máximos permitem limitar os números que você insere a uma faixa específica.
- **Alterar Número Usando Setas:** Os usuários podem aumentar ou diminuir um número usando as setas para cima e para baixo.

## Exceções
- **Entrada de Dados Não Numéricos:** Apenas dados numéricos podem ser inseridos.