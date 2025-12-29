# Dia

![](../../assets/images/app-development/day.png)

## Informações gerais
O Dia é um componente de UI projetado para exibir ou selecionar dias individuais. Este elemento é comumente utilizado em calendários ou sensores de data, permitindo que o usuário selecione dias específicos para completar tarefas ou definir lembretes.

## Parâmetros
**Propriedades do componente**

| Grupo de configurações | Campo de configuração | Opções de valor | Propósito |
| --- | --- | --- | --- |
|  | Nome | - | Nome do Componente de UI no sistema |
| Comum | Formato | - | A propriedade permite [configurar](https://docs.microsoft.com/ru-ru/dotnet/standard/base-types/custom-date-and-time-format-strings) a exibição de data e hora |
|  | Desativado | true, false | A propriedade permite desativar um elemento no formulário |
|  | Obrigatório | true, false | A propriedade torna o elemento obrigatório para ser preenchido antes de enviar o formulário |
|  | Rótulo | - | Contém a tabela de conteúdos do contêiner de texto |
|  | Vínculo | Multiseleção de Catálogo | Contém um campo “Data” relacionado do modelo |
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
- **Seletor de Data**: Usado para selecionar dias específicos em interfaces onde a seleção precisa de data é necessária.
- **Exibição de Eventos**: Pode ser usado para exibir eventos ou lembretes agendados para dias específicos.

## Exceções
- **Funcionalidade Limitada**: O componente Dia é limitado a exibir e selecionar dias, e não é adequado para exibir intervalos de tempo mais amplos.