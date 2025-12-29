# Obter valores do conector

![](../../assets/images/app-development/get-values-from-connector.png)

## Informações gerais
A etapa “Obter valores do conector” permite recuperar dados por meio de uma consulta a sistemas externos usando os conectores configurados. A etapa pode ser chamada por agendamento ou em nome do usuário.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor            | Propósito |
|-----------------------|----------------------------|-----------|
| Nome da etapa         | -                          | Nome da etapa |
| Sistema               | Multiseleção de Catálogo   | Contém sistemas de integração pré-configurados |
| Conector              | Multiseleção de Catálogo   | Contém conectores pré-configurados no sistema de integração |
| Caminho da consulta    | Multiseleção de Catálogo   | Contém o “EndPoint” a ser acessado |
| Nome do método        | Get, Post, Put, Delete     | Tipo de solicitação a ser executada |
| Mapeamento de parâmetros | -                        | Uma entidade dinâmica que permite filtrar uma solicitação via uma API selecionada |

## Casos
- **Atualização Programada de Dados**: A etapa é usada para atualizar automaticamente os dados no fluxo de dados de entrada em uma base programada via cron, garantindo a obtenção de informações oportunas e atualizadas.
- **Personalização de Consulta Individual**: A etapa é configurada para enviar consultas específicas a diferentes sistemas externos, permitindo uma integração flexível e o processamento de dados de múltiplas fontes.
- **Otimização do Fluxo de Dados**: A etapa é utilizada de forma eficiente para extrair dados de sistemas externos, minimizando a necessidade de processamento manual e melhorando o desempenho do fluxo de dados.

## Exceções
- **Métodos de Consulta**: Embora vários métodos de consulta (Get, Post, Put, Delete) sejam suportados, uma personalização cuidadosa é necessária caso a caso, levando em consideração as características específicas do sistema externo e do tipo de dado.
- **Automação com Limitações**: A capacidade de chamar automaticamente uma etapa programada oferece conveniência, mas requer um ajuste fino dos parâmetros e verificação da acessibilidade dos sistemas externos.

## Cenário de aplicação

Este componente lida com dados de personagens. Criamos cinco modelos de dados para seus atributos: character_id, character_name, character_species, character_status e gender. Em seguida, selecionamos uma integração, por exemplo, Rick and Morty, e adicionamos as seguintes etapas: Obter valores do conector, Extrair coleção, Armazenar entrada sobre o barramento e Escrever resposta.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1zWIWzpqccbocpDCfVUNIkGW2grrWJ5Yn/view?usp=sharing)