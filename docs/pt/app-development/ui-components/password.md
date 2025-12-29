# Senha

![](../../assets/images/app-development/password.png)

## Informações gerais
Senha é um componente básico de UI projetado para a entrada de senhas de forma segura. Este componente é utilizado para criar campos de entrada de senha, garantindo a confidencialidade e proteção dos dados inseridos.

## Parâmetros
**Propriedades do componente**

| Grupo de configurações | Campo de configuração | Opções de valor | Propósito |
| --- | --- | --- | --- |
|  | Nome | - | Nome do Componente de UI no sistema |
| Comum | Desativado | true, false | A propriedade permite desativar um elemento no formulário |
|  | Obrigatório | true, false | A propriedade torna o elemento obrigatório para ser preenchido antes de enviar o formulário |
|  | Mostrar limpar | true, false | Mostra o ícone de limpar (resetar) o valor do campo |
|  | Autocompletar |  | Campo para definir o valor do atributo HTML de autocompletar. Como regra, use username para o campo de entrada de nome, e password, new-password ou current-password para os campos de entrada correspondentes para diferentes tipos de senha. Funciona em conjunto com o parâmetro Fornecer Formulário Raiz para controle de UI da Página. |
|  | Rótulo | - | Contém a tabela de conteúdos do contêiner de texto |
|  | Vinculação | Multiseleção de Catálogo | Contém um campo “String” relacionado do modelo |
| Eventos | Ao valor alterado | - | Permite executar o script especificado após a alteração do valor do campo |
|  | Ao pressionar tecla |  | Permite executar o script especificado após mover para o próximo elemento da página (aba) |
|  | Ao soltar tecla |  | Permite executar o script especificado após mover para o elemento anterior da página (aba) |
|  | Ao focar |  | Permite executar um script no momento em que um elemento é focado |
| Índice da aba |  | Inteiro positivo começando do zero | Define a ordem em que os campos ativos (editáveis) são alternados via teclado (por exemplo, usando a tecla Tab) |
| ID de Automação |  |  | ID de controle para testes automatizados e para transferência de configurações CSS |

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
- **Formulários de Autenticação**: Usado em formulários de login e registro para a entrada segura de senhas.
- **Formulários Interativos**: Habilitando formulários interativos que requerem a entrada de dados confidenciais.

## Exceções
- **Limitações de Formatação**: Não suporta formatos de texto complexos, como hyperlinks ou imagens incorporadas.