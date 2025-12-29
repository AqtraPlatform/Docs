# Confirmar código único para o usuário

![](../../assets/images/app-development/confirm-one-time-code-for-user.png)

## Informações gerais
A etapa “Confirmar Código Único para o Usuário” é utilizada para confirmar o código único que foi gerado para o usuário na etapa anterior “Obter Código Único para o Usuário”. Esta etapa é a chave no processo de autenticação de dois fatores, permitindo que você verifique a correção do código inserido pelo usuário para acessar o sistema.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Selecionar a etapa anterior |
| Campo de código do usuário | -          | O campo no qual o usuário insere o código recebido para confirmação |

## Casos
- **Confirmação de Autenticação de Dois Fatores**: Aplicado para completar o processo de autenticação de dois fatores, exigindo que os usuários insiram o código que foi enviado a eles na etapa anterior.
- **Aprimoramento da Segurança de Acesso**: Usado em cenários onde um controle de acesso ao sistema aprimorado é necessário para prevenir logins não autorizados.

## Exceções
- **Dependência da correção do código inserido**: A eficácia da etapa depende da precisão na inserção do código pelo usuário.
- **Validade Limitada do Código**: Se o código expirar, ele deve ser reemitido, o que pode resultar em atrasos na autenticação.

## Cenário de aplicação

O componente cria um fluxo de dados para confirmar o código único do usuário. A etapa do modelo de ação Get é utilizada para recuperar os dados do modelo. Em seguida, o código da variável ForTestCode é limpo de caracteres desnecessários e armazenado na variável _code usando a etapa Execute script. A etapa Confirmar código único para o usuário é utilizada para confirmar o código único usando o valor _code como o código do usuário. Finalmente, o resultado é passado pela etapa Write response.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1_uPyqNOuOddurvwz-KteaoIIRQjgEzBH/view?usp=sharing)