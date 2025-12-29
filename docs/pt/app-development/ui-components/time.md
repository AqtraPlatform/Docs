# Tempo

![](../../assets/images/app-development/time.png)

## Informações gerais
O Tempo é um componente de UI projetado para inserir e exibir o tempo. Este elemento é tipicamente usado para definir o horário de eventos ou tarefas e para exibir o tempo nas interfaces de aplicação.

## Parâmetros
**Propriedades do componente**

| Grupo de configurações | Campo de configuração | Opções de valor | Propósito |
| --- | --- | --- | --- |
|  | Nome | - | Nome do Componente de UI no sistema |
| Comum | Desativado | true, false | A propriedade permite desativar um elemento no formulário |
|  | Obrigatório | true, false | A propriedade torna o elemento obrigatório para ser preenchido antes de enviar o formulário |
|  | Rótulo | - | Contém a tabela de conteúdos do contêiner de texto |
|  | Vínculo | Multiseleção de Catálogo | Contém um campo “Tempo” relacionado do modelo |
| Eventos | Ao valor alterado | - | Permite executar o script especificado após a alteração do valor do campo |

**Propriedades CSS**

| Grupo de configurações | Campo de configuração | Opções de valor | Propósito |
| --- | --- | --- | --- |
| Layout | Largura | - | Largura do componente |
|  | Altura | - | Altura do componente |
|  | Crescer | true, false | A propriedade determina quanto um elemento irá crescer em relação aos outros elementos flex dentro do mesmo contêiner |
|  | Margem | - | A propriedade define os preenchimentos externos em todos os quatro lados do elemento |
|  | Preenchimento | - | A propriedade define os preenchimentos internos em todos os lados do elemento |
| Aparência | Raio de Canto | - | A propriedade é usada para arredondar os cantos de um elemento |
|  | Espessura da Borda | - | A propriedade permite definir os limites para o elemento |
| Pincel | Fundo | - | A propriedade define a cor de fundo do elemento |
|  | Cor da Borda | - | A propriedade define a cor da borda do elemento |

## Casos
- **Configuração de Tempo**: Usado para definir um horário específico em agendadores e calendários.
- **Entrada de Tempo**: Fornece uma interface para o usuário inserir o tempo para vários propósitos.

## Exceções
- **Formatação de Tempo**: Você deve estar ciente das restrições de formato de tempo definidas nas configurações do componente.
- **Apenas Tempo**: O componente Tempo é limitado a exibir e inserir apenas o tempo, sem datas.