# Switch case

![](../../assets/images/app-development/switch-case.png)

## Informações gerais
A etapa “Switch Case” dentro de um fluxo de trabalho é usada como um operador de troca incondicional que permite escolher entre diferentes opções de script. Esta etapa é ideal para controlar a lógica do processo com base em certas condições, geralmente especificadas por campos Booleanos ou Enum. Quando utilizada, o script principal é sempre desativado e o processo vai para um dos ramos alternativos.
![](../../assets/images/app-development/switch-case-example.png)

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Propósito |
|-----------------------|-----------|
| Nome da etapa         | Nome da etapa “Switch Case” |
| Campo de origem da troca | Campo com base no valor do qual o script é selecionado |

## Casos
- **Ramificação da Lógica do Processo**: Usado para criar caminhos condicionais em um fluxo de trabalho onde a próxima direção é determinada com base em uma certa condição ou valor.
- **Gerenciamento de Diferentes Scripts de Execução**: Adequado para scripts onde um processo requer diferentes execuções dependendo de condições pré-definidas ou seleção do usuário.

## Exceções
- **Precisão das Condições de Transição**: É necessário definir com precisão as condições de troca para cada caso para garantir que o caminho de execução correto seja selecionado.
- **Complexidade do Gerenciamento de Múltiplos Caminhos**: Fluxos de trabalho complexos com muitos caminhos possíveis requerem uma compreensão clara e gerenciamento de cada um deles para evitar erros na lógica do processo.