# Inscrever-se no conector

![](../../assets/images/app-development/subscribe-to-connector.png)

## Informações gerais

A etapa “Inscrever-se no conector” é para se inscrever para receber mensagens de vários sistemas de mensagens, como RabbitMQ ou Kafka.

## Parâmetros

**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor          | Propósito                                                      |
| --------------------- | ------------------------ | -------------------------------------------------------------- |
| Nome da etapa         | -                        | Nome da etapa                                                 |
| Sistema               | Multiseleção de Catálogo | Contém sistemas de integração pré-configurados                |
| Conector              | Multiseleção de Catálogo | Contém conectores pré-configurados no sistema de integração   |
| Caminho da Consulta   | Multiseleção de Catálogo | Contém o “EndPoint” a ser acessado                           |
| Nome do Método        | Get, Post, Put, Delete   | Tipo de solicitação a ser executada                           |

## Casos

- **Resposta a Eventos**: Recebimento automático de notificações sobre eventos ou mudanças nos dados de fontes externas.
- **Integração com Sistemas de Mensagens**: Interação com várias plataformas de mensagens para garantir um fluxo contínuo de dados.

## Exceções

- **Funcionalidade Limitada**: A etapa é limitada a se inscrever para mensagens e não suporta outros tipos de interações com sistemas externos.
- **Dependência de Sistemas Externos**: Requer configuração e suporte confiáveis dos sistemas de mensagens utilizados.

## Cenário de Aplicação

O componente é configurado para **inscrever-se em uma fila RabbitMQ** e salvar as mensagens recebidas em um **banco de dados**. Etapas como "**Inscrever-se no conector**", "**Executar script**" para processamento de dados e "**Atualizar entrada**" para salvar mensagens são utilizadas nesse processo.

- A configuração do componente estará disponível posteriormente.