# Registrar contexto para o modelo

![](../../assets/images/app-development/register-context-for-model.png)

## Informações gerais
A etapa “Registrar contexto para o modelo” é utilizada no contexto da integração LDAP para registrar o contexto de segurança dos usuários registrados em um sistema externo. Esta etapa garante que os dados sobre os usuários e seus papéis sejam sincronizados entre o sistema externo e o sistema atual, utilizando chaves para identificar e registrar o contexto.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Selecionando a etapa anterior |
| Componente            | -                | Componente para o qual o contexto está sendo registrado |
| Campo de nome         | -                | Campo que indica o nome ou identificador da entidade |
| Chaves                | -                | Chaves usadas para identificar de forma única uma entidade |

## Casos
- **Integração LDAP**: Usado para sincronizar e registrar dados de usuários do LDAP no sistema atual.
- **Gerenciamento de Papéis e Acesso**: Adequado para scripts que requerem correspondência e rastreamento precisos dos papéis dos usuários registrados em sistemas externos.

## Exceções
- **Requisitos de Precisão das Chaves**: As chaves devem ser correspondidas com precisão para identificar e registrar corretamente os usuários no sistema.
- **Gerenciamento de Mudanças em Sistemas Externos**: Mudanças nos papéis ou status dos usuários em um sistema externo requerem uma atualização apropriada no sistema atual, o que pode ser um desafio diante de dados que mudam dinamicamente.