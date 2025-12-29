# Atualizar ou criar informações do usuário

![](../../assets/images/app-development/update-or-create-user-info.png)

## Informações gerais
A etapa “Atualizar ou Criar Informações do Usuário” é usada para atualizar informações de usuários existentes ou criar um novo usuário. Esta etapa funciona exclusivamente com o componente “Informações do Usuário”. Quando as informações do usuário são atualizadas, se a senha não for especificada, ela permanecerá inalterada.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Selecionando a etapa anterior |
| Campo de informações do usuário | -        | Um campo que contém informações sobre o usuário |
| Nome do usuário       | -                | Nome do usuário |
| Senha do usuário      | -                | Senha do usuário (obrigatória) |
| Usuário desativado    | true, false      | Status de atividade do usuário |
| Atualizar campos      | name, email, lastName, userName, firstName, middleName | Campos para atualizar ou criar informações do usuário |

## Casos
- **Atualizando Informações do Usuário**: Usado para alterar dados sobre usuários existentes, incluindo suas informações de contato, nome de usuário e outras informações pessoais.
- **Criando Novos Usuários**: Adequado para adicionar novos usuários ao sistema, permitindo que você expanda rapidamente e de forma eficiente o banco de dados de usuários.

## Exceções
- **Necessidade de Precisão dos Dados**: A etapa requer entrada de dados precisa e atualizada, especialmente ao criar novos usuários.
- **Gerenciamento de Senhas**: Quando as informações do usuário são atualizadas, se a senha não for especificada, ela permanecerá inalterada. Ao criar um usuário, especificar uma senha é obrigatório.

## Cenário de aplicação

O componente é projetado para gerenciar informações do usuário. Envolve a recuperação de informações do usuário, atualização de seus dados e criação de um novo registro de usuário com parâmetros especificados.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1zrn1vRmP3BtXAp-FBsoc5OHj96JuGKvF/view?usp=sharing)