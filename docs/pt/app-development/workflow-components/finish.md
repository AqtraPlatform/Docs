# Finalizar

![](../../assets/images/app-development/finish.png)

## Informações gerais
A etapa “Finalizar” dentro de um fluxo de trabalho é projetada para concluir a execução do Fluxo de Trabalho atual. Esta etapa é tipicamente usada para especificar explicitamente o ponto de conclusão de um fluxo de trabalho, especialmente nos scripts alternativos definidos no bloco de Condições.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Propósito |
|-----------------------|-----------|
| Nome da etapa         | Nome da etapa “Finalizar” |

## Casos
- **Conclusão Controlada do Fluxo de Trabalho**: Usada para especificar explicitamente o ponto de conclusão de um fluxo de trabalho, o que é especialmente importante em processos complexos com muitas condições e ramificações.
- **Caminhos de Execução Alternativos**: Adequada para scripts onde um fluxo de trabalho precisa ser encerrado sob certas condições que diferem do fluxo principal de execução.

## Exceções
- **Necessidade de Configuração Adequada**: É importante garantir que a etapa “Finalizar” esteja devidamente incorporada na lógica do fluxo de trabalho para que não interrompa o processo prematuramente ou pule etapas importantes.