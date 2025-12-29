# Executar chamada de API

![](../../assets/images/app-development/execute-api-call.png)

## Informações gerais
A etapa “Executar Chamada de API” é usada para interagir com sistemas externos via API. Esta etapa pode ser configurada para vários tipos de solicitações, incluindo receber dados (GET), enviar dados (POST/PUT) ou excluir dados (DELETE) em um sistema externo. Dependendo do contexto de uso, esta etapa pode ser uma das primeiras etapas no Dataflow para obter dados ou uma das últimas etapas para atualizar dados em sistemas externos.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Selecionando a etapa anterior |
| Campo de armazenamento de resultado | - | Um campo para armazenar o ID de uma entrada criada ou processada |
| Sistema               | -                | Escolhendo um sistema de integração |
| Conector              | -                | Selecionando um conector no sistema de integração |
| Caminho da consulta    | -                | EndPoint para a solicitação |
| Nome do método        | Get, Post, Put, Delete | Tipo de solicitação a ser completada |
| Mapeamento de parâmetros | -              | Configuração dinâmica para filtragem de consultas |

## Casos
- **Obtenção de dados de fontes externas**: É usado para baixar dados de sistemas externos, o que pode ser especialmente útil ao integrar com serviços ou bancos de dados externos.
- **Envio ou atualização de dados**: Adequado para enviar dados para sistemas externos ou atualizar dados existentes, por exemplo, ao sincronizar alterações feitas no dataflow.
- **Exclusão de dados**: Pode ser usado para excluir dados de sistemas externos, o que ajuda a manter a relevância e a integridade dos dados em sistemas integrados.

## Exceções
- **Necessidade de processamento assíncrono**: A etapa é realizada de forma assíncrona, o que requer levar em conta o tempo de resposta dos sistemas externos e o impacto potencial na sequência de processamento de dados.
- **Requisito de configuração do conector**: A eficácia da etapa depende de sistemas de integração e conectores configurados corretamente, bem como da precisão na determinação do EndPoint e dos parâmetros da solicitação.

## Cenário de aplicação

O componente cria uma integração simples para recuperar dados, como clima, através de uma API. No fluxo de dados, etapas são usadas para configurar a solicitação da API, incluindo a execução de um script para criar variáveis da API, chamando a API e salvando os resultados. Em seguida, a integração é selecionada e configurada no sistema, e os resultados são exibidos no frontend usando um formulário vinculado à execução do script. A função no componente processa os dados recuperados para exibição ao usuário.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/119_NZiqzENXCaqdmiZ7qj4ZmeHcje7je/view?usp=sharing).