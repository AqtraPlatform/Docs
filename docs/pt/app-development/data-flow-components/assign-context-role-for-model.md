# Atribuir função de contexto para o modelo

![](../../assets/images/app-development/assign-context-role-for-model.png)

## Informações gerais
A etapa “Atribuir Função de Contexto para o Modelo” é usada para vincular um usuário ou grupo de usuários a uma função e contexto específicos. Este processo requer que pelo menos uma função esteja configurada na seção “Funções” do menu “Acesso”. Esta etapa permite estabelecer relações entre usuários e funções no contexto de um modelo de dados específico, proporcionando assim controle sobre o acesso e permissões dos usuários.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Selecionando a etapa anterior |
| Campo UserId          | -                | Campo de ID do usuário |
| Campo ContextId       | -                | Campo de ID do contexto |
| Selecionar contextos  | -                | Selecionando os contextos aos quais a função será vinculada |

## Casos
- **Gerenciamento de Acesso do Usuário**: Usado para atribuir funções a usuários, determinando seu acesso e permissões dentro do sistema.
- **Gerenciamento dinâmico de funções ao interagir com a UI**: Esta etapa é efetivamente usada para alterar ou atualizar as funções dos usuários em tempo real com base em suas ações e interações com elementos da interface do usuário. Isso torna possível adaptar o acesso e as permissões dos usuários dependendo de ações ou cenários específicos de uso do sistema.

## Exceções
- **Requisito para funções configuradas**: Para um vínculo bem-sucedido, o sistema deve ter as funções apropriadas pré-configuradas.
- **Dependência da precisão do ID**: A identificação precisa dos IDs de usuários e contextos é crítica para que a etapa funcione corretamente.