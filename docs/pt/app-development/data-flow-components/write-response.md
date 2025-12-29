# Escrever resposta

![](../../assets/images/app-development/write-response.png)

## Informações gerais
A etapa “Escrever Resposta” desempenha um papel fundamental no Dataflow, pois é projetada para retornar o resultado final ao chamador. Esta etapa é geralmente a última etapa em qualquer Dataflow, resumindo e enviando os dados recebidos de volta à fonte solicitante.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Selecionando a etapa anterior |

## Casos
- **Retornando Resultados do Dataflow**: Usado para enviar os resultados do processo de dados do Dataflow de volta ao chamador, o que pode ser crítico em análises de dados e gerenciamento de erros.
- **Transformação de Dados Pré-Resposta**: Pode ser combinado com a etapa “Transformar Modelo” para transformar ou filtrar dados antes de serem enviados, permitindo otimizar e personalizar o conteúdo da resposta para atender aos requisitos do chamador.

## Cenário de aplicação

O componente contém definições de dados personalizadas (definições) e fornece a capacidade de criar e gerenciar dados usando fluxos de dados. Ele implementa etapas para recuperar modelos de dados (modelo de ação Get) e escrever respostas (escrever resposta), permitindo que os usuários interajam com os dados através da interface do usuário e interajam com eles no frontend da aplicação.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1qNTgk1uYrMO3uUkDRmTO3i4En5mbG22i/view?usp=sharing).