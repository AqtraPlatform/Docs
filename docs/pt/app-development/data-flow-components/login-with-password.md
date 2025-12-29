# Login com senha

![](../../assets/images/app-development/login-with-password.png)

## Informações gerais
A etapa “Login com Senha” é usada para criar uma sessão de usuário com base no nome de usuário e na senha. Esta etapa permite que o usuário seja autorizado no sistema, verificando as credenciais fornecidas e, se verificadas com sucesso, criando uma sessão de usuário.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Selecionando a etapa anterior |
| Nome de usuário       | -                | Nome de usuário para login |
| Senha do usuário      | -                | Senha do usuário |
| Cliente para requisição | -              | Cliente ou aplicação que inicia a requisição de autenticação |

## Casos
- **Autenticação de Usuário**: Etapa usada em processos de autenticação onde os usuários inserem suas credenciais para acessar o sistema ou suas funcionalidades.
- **Controle de Acesso**: Adequado para sistemas que exigem que as credenciais do usuário sejam verificadas antes de conceder acesso a certos recursos ou funcionalidades.

## Exceções
- **Necessidade de Precisão das Credenciais**: A eficácia da etapa depende da precisão das credenciais inseridas (nome de usuário e senha).
- **Tratamento de Tentativas de Login Falhadas**: É importante tratar adequadamente as tentativas de login falhadas para evitar riscos de segurança potenciais, como ataques de força bruta. Isso requer a implementação de mecanismos para limitar o número de tentativas de login ou bloquear temporariamente o acesso após várias tentativas malsucedidas.

## Cenário de aplicação

O cenário implementa o login do usuário no sistema usando um nome de usuário e uma senha. Após iniciar o fluxo de dados e inserir o login e a senha nos campos correspondentes da interface do usuário, a etapa "Login com senha" autentica o usuário. Em seguida, usando a etapa "Ação do Formulário", o componente selecionado é aberto.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1Kb9QNcCHXqetQmXGvBHScQSiRlA-542s/view?usp=sharing)