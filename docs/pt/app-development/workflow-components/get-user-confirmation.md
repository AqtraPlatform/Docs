# Obter confirmação do usuário

![](../../assets/images/app-development/get-user-confirmation.png)

## Informações gerais
A etapa “Obter Confirmação do Usuário” no fluxo de trabalho é usada para solicitar confirmação ou realizar uma ação do usuário. A etapa envia uma notificação ao usuário com um pedido para realizar uma ação específica sobre o objeto, onde o objeto é o estado do modelo atual.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor       | Propósito |
|-----------------------|-----------------------|-----------|
| Nome da etapa         | -                     | Nome da etapa “Obter Confirmação do Usuário” |
| Campo de confirmação   | -                     | Campo com opções a serem solicitadas ao usuário |
| Campo de informações do usuário | Multiseleção de Catálogo | Campo com informações sobre um usuário ou grupo de usuários |
| Roteamento do usuário  | Multiseleção de Catálogo | Objeto que é um contexto de segurança |

## Casos
- **Solicitação de Confirmação do Usuário**: Ideal para scripts que requerem confirmação ou escolha de ação do usuário, como confirmar uma transação, concordar com o processamento de dados ou escolher uma opção de resposta.
- **Participação Interativa do Usuário no Processo**: Adequado para um fluxo de trabalho, onde é importante levar em conta as decisões ou escolhas do usuário para continuar ou alterar o processo.

## Exceções
- **Garantindo que o Pedido Seja Claro**: É importante formular claramente o pedido de confirmação para que o usuário entenda qual ação é esperada dele.
- **Gerenciando as Respostas do Usuário**: As respostas dos usuários devem ser processadas adequadamente e levadas em conta, especialmente em situações onde elas determinam o curso de ações futuras no fluxo de trabalho.
- **Levando em Conta o Contexto de Segurança e Permissões**: Ao usar o parâmetro de Roteamento do Usuário, é importante considerar o contexto de segurança e as permissões correspondentes do usuário.