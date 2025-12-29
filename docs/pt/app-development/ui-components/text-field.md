# Campo de Texto

![](../../assets/images/app-development/text-field.png)

## Informações gerais
“O Campo de Texto” é um componente de UI projetado para exibir e configurar a entrada e saída de texto.

## Parâmetros
**Propriedades do componente**

| Grupo de configurações | Campo de configuração | Opções de valor | Propósito |
| --- | --- | --- | --- |
|  | Nome | - | Nome do Componente de UI no sistema |
| Comum | Desativado | true, false | A propriedade permite desativar um elemento no formulário |
|  | Obrigatório | true, false | A propriedade torna o elemento obrigatório para ser preenchido antes de enviar o formulário |
|  | Rótulo | - | Contém a tabela de conteúdos do contêiner de texto |
|  | Vínculo | Multiseleção de Catálogo | Contém um campo “String” relacionado do modelo |
| Eventos | Ao valor alterado | - | Permite executar o script especificado após alterar o valor do campo |
| Índice de guia |  | Inteiro positivo começando do zero | Define a ordem em que os campos ativos (editáveis) são alternados via teclado (por exemplo, usando a tecla Tab) |

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
- **Formulários de Entrada de Dados**: Usado para coletar informações de texto dos usuários.
- **Configurações de Interface**: Fornece uma interface de usuário para inserir ou modificar texto.

## Exceções
- **Funcionalidade Limitada**: Adequado apenas para entrada de texto.