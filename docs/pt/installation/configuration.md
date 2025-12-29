# Configurações Básicas da Plataforma

<br>

## Arquitetura da Plataforma

A plataforma é construída sobre uma arquitetura de microserviços que proporciona modularidade, escalabilidade e flexibilidade. As principais características da arquitetura incluem:

- **Arquitetura de Microserviços**: O sistema é dividido em microserviços separados, cada um dos quais desempenha uma função específica e opera de forma independente.
- **Processamento Distribuído**: Os microserviços podem ser distribuídos entre diferentes nós, proporcionando balanceamento de carga e maior resiliência do sistema.
- **Containerização e Orquestração**: O uso do Docker para containerizar microserviços e do Kubernetes para orquestrá-los facilita a implantação, escalabilidade e gerenciamento da aplicação.
- **Modularidade e Interoperabilidade dos Microserviços**: A modularidade é alcançada pela delimitação clara das funções entre os microserviços, e a comunicação entre eles ocorre por meio de APIs específicas e protocolos de interoperabilidade.

O sistema é composto por onze imagens de contêiner Docker:

| Serviço          | Propósito                                                        |
| ---------------- | ---------------------------------------------------------------- |
| catalogs         | Armazenamento e processamento de dados do usuário; suporte a RLS |
| data-flow        | Processamento e armazenamento de scripts de dados personalizados  |
| file-storage     | Armazenamento de dados binários                                   |
| identity         | Gerenciamento e autenticação de usuários                          |
| notification     | Envio de notificações                                            |
| scheduler        | Agendador de eventos no sistema; todos os eventos são chamados via o bus |
| template-service | Trabalho com templates                                            |
| view-service     | Armazenamento de metadados do sistema; orquestração de processos de atualização de metadados |
| workflow         | Scripting via a Máquina de Estados                                |
| web-studio       | Parte web para desenvolvimento de aplicações                      |
| web-workplace    | Parte web para execução de aplicações                             |

<br>

## Stack Tecnológico

- **Fundação**: A plataforma é construída sobre o Net Core 8.0, uma plataforma de desenvolvimento de software modular e de código aberto.
- **Linguagem de Desenvolvimento**: C# é utilizada como a principal linguagem de programação.
  <br>

## Infraestrutura Adicional

- **PostgreSQL** (versão ≥13.0): Sistema de gerenciamento de banco de dados objeto-relacional para armazenamento de dados primários.
- **Redis** (versão ≥5.0): Um banco de dados não relacional usado para cache de dados.
- **RabbitMQ** (versão ≥3.0): Um software de broker de mensagens para gerenciamento de eventos e filas do sistema.
  <br>

## Partes Web

- Utiliza o framework web front-end **Blazor**, parte do Net Core, para criar componentes web.
- As Partes Web são executadas como **WebAssembly** (WASM) do lado do cliente.
  <br>

## Requisitos de Instalação

- **Kubernetes**: Um cluster Kubernetes é necessário para que a versão agrupada do produto funcione.
  - **Configuração Mínima**:
    - 1 x Master (2 vCPU, 4GB RAM, 20GB SSD) - recomenda-se 3 nós com o papel de Master.
    - 1 x Ingress (4 vCPU, 8GB RAM, 20GB SSD)
    - 3 x Worker (16 vCPU, 32GB RAM, 60GB SSD)
- **Sistema Operacional**: Ubuntu Server 22.04 LTS
  <br>

## Rede e Portas

- Todo o tráfego de rede utiliza o protocolo **TCP/IP**.
- Por padrão, cada microserviço (exceto web-studio) fornece duas portas:
  - **80**: API pública (HTTP/1.1).
  - **5001**: API privada (HTTP/2).
- **Web-studio**: Fornece apenas a porta 80 para servir recursos estáticos.
- Todos os microserviços, com exceção do web-studio, devem ter acesso ao PostgreSQL, Redis e RabbitMQ.
  <br>

## Protocolos Utilizados

- **HTTP/1.1**: Para API pública.
- **GRPC**: Para API privada.
- **WebSocket**: Para o serviço de Notificação.
- **SIP sobre WebSocket**: Opcional, para integração com SIP em um web-workplace.
- **RTC/RTCP**: Opcional, para integração com SIP em um web-workplace.
  <br>

## Armazenamento de Dados

Cada microserviço gerencia seu próprio esquema no banco de dados, sem sobreposição com os outros.

| Serviço          | Esquema                    |
| ---------------- | -------------------------- |
| catalogs         | catalogs                   |
| data-flow        | dataflow                   |
| file-storage     | file_storage               |
| identity         | identity                   |
| notification     | notification               |
| scheduler        | scheduler                  |
| template-service | template                   |
| view-service     | view_service, maintenance  |
| workflow         | workflow, wfc_persistence  |
| web-workplace    | workplace-host             |

<br>

Cada microserviço é responsável por criar e migrar os metadados de seus esquemas.

O serviço de catalogs, que é responsável por armazenar dados do usuário, cria uma partição adicional em seu esquema para cada tipo de dado, herdada da tabela primária, bem como partições adicionais para implementar RLS, se necessário. Quando essas partições são formadas, todos os índices adicionais e chaves externas são gerados.

A composição de índices e chaves externas depende da configuração da aplicação que você está construindo na plataforma.
<br>

## Gerenciamento de Autorização e Permissões

- Autorização local usando **tokens JWT**.
- Capacidade de conectar sistemas de autorização externos (oAuth, OpenId Connect, autorização do Windows, SAML).
- **RBAC** (Controle de Acesso Baseado em Funções) para controle de acesso.
  <br>

## Coleta de Métricas e Rastros

Todos os serviços, exceto web-studio, fornecem métricas no formato ‘Prometheus’. As métricas estão disponíveis pelo caminho relativo /metrics. Para verificar a disponibilidade do serviço, dois caminhos são fornecidos /hc e /liveness:

- hc - informações detalhadas sobre todas as verificações;
- liveness - uma resposta curta sobre a disponibilidade do serviço.

Os logs são coletados pelo próprio sistema, todos os logs são escritos no esquema de manutenção, e a visualização de logs está disponível no web-studio.
O nível de log para cada serviço é configurado separadamente através do web-studio, na seção "Manutenção".
Dois sistemas Zipkin ou Jaeger podem ser conectados para coletar rastros. A coleta de rastros é configurada no nível de parâmetro do serviço. Se você quiser exportar rastros para o Jaeger, precisa de pelo menos a versão 1.35.