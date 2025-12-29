# Obter informações do usuário

![](../../assets/images/app-development/get-user-info.png)

## Informações gerais
A etapa “Obter Informações do Usuário” é utilizada para obter dados sobre o usuário da plataforma, como e-mail, nome e sobrenome, para processamento posterior no fluxo de dados atual. Esta etapa é necessária para a maioria das operações do usuário, exceto para criar um novo usuário.

**Obtendo Informações do Usuário**
1. **Usando a flag ‘Obter informações do usuário da solicitação’**: A etapa tentará recuperar dados sobre o usuário atual. Para que funcione corretamente, é necessário que o fluxo de dados seja chamado em nome de um usuário específico (por exemplo, a partir de um formulário de solicitação ou via uma solicitação Proxy). Se chamado em nome da plataforma (por exemplo, no fluxo de dados de entrada), o resultado será nulo.
2. **Sem a flag ‘Obter informações do usuário da solicitação’**: O usuário pode ser definido:
   - Via o nome do sistema, usando um parâmetro String do modelo de fluxo de dados atual.
   - Via um link para o diretório de informações do usuário, por exemplo, campos creatorSubject ou changeAuthor.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração     | Opções de Valor | Propósito |
|---------------------------|------------------|-----------|
| Nome da etapa             | -                | Nome da etapa |
| Etapa de origem           | -                | Selecionando a etapa anterior |
| Obter informações do usuário da solicitação | - | Flag para obter informações sobre o usuário atual |
| Campo de informações do usuário | -         | Campo de identificação do usuário |
| Nome do usuário           | -                | Nome do usuário |
| Campo de armazenamento do resultado | -      | Campo para salvar as informações obtidas sobre o usuário |

## Casos
- **Recuperando Dados do Usuário para Processamento**: Usado para extrair informações do usuário para uso subsequente no fluxo de dados.
- **Enviar Notificações Personalizadas**: Em casos onde é necessário enviar notificações por e-mail personalizadas aos usuários, a etapa “Obter Informações do Usuário” é utilizada para obter seus endereços de e-mail. Essas informações são então passadas para a etapa projetada para enviar notificações.

## Exceções
- **Tratamento de Usuário Não Encontrado**: Em casos em que o usuário não pode ser identificado, o resultado será nulo, o que requer processamento adicional no fluxo de dados.

## Cenário de aplicação

O componente "Obter informações do usuário" é projetado para recuperar informações sobre um usuário. Dentro de um fluxo de dados, esta etapa é usada para consultar dados do usuário com base em critérios especificados, como um nome de usuário ou outras informações identificadoras. Por exemplo, dentro de um fluxo de dados, você pode especificar o nome de um usuário para recuperar informações sobre ele e, em seguida, usar essas informações para ações posteriores, como exibi-las em uma tela ou atualizar um banco de dados.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/16keZXK_MXlWLmcSA4a-nLvhx-GPP3RPy/view?usp=sharing)