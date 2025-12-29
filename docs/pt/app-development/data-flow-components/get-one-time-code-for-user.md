# Obter código de uso único para o usuário

![](../../assets/images/app-development/get-one-time-code-for-user.png)

## Informações gerais
A etapa “Obter Código de Uso Único para o Usuário” é utilizada para gerar e enviar um código de uso único para login como parte da autenticação de dois fatores. Esta etapa funciona em conjunto com a etapa “Confirmar Código de Uso Único para o Usuário” e geralmente é aplicada usando a funcionalidade “Enviar Notificação Modelada”.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Selecionar a etapa anterior |
| Nome do usuário       | -                | Nome ou ID do usuário para o qual o código é gerado |
| Cliente para solicitação | -             | Cliente ou aplicativo que inicia a solicitação de confirmação |
| Tempo de vida do código | -              | O tempo de vida de um código |

## Casos
- **Autenticação de Dois Fatores**: Usado para fornecer uma camada extra de segurança ao fazer login, gerando um código temporário que o usuário deve confirmar.
- **Segurança de Login Aprimorada**: Adequado para cenários onde medidas de segurança aprimoradas são necessárias para evitar acesso não autorizado ao sistema.

## Exceções
- **Dependência da Precisão dos Dados do Usuário**: A precisão e relevância das informações do usuário são críticas para a geração e envio bem-sucedidos de um código de uso único.
- **Gerenciamento do Tempo de Vida do Código**: Você deve configurar corretamente o tempo de vida do código para garantir que seu código esteja atualizado e evitar problemas de acesso do usuário.

## Cenário de aplicação 

O componente adiciona uma nova definição de string ForTestCode. Um fluxo de dados é criado onde um código de uso único para o usuário é obtido através do modelo de ação Get e das etapas Get user info. A etapa Execute script é usada para passar esse código para a variável new_code, que é então armazenada na definição ForTestCode do componente e exibida em uma janela modal.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1_uPyqNOuOddurvwz-KteaoIIRQjgEzBH/view?usp=sharing)