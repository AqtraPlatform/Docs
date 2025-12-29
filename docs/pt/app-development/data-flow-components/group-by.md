# Agrupar Por

![](../../assets/images/app-development/group-by.png)

## Informações gerais
A etapa “Agrupar Por” é usada para coletar e agrupar dados divididos em etapas anteriores, por exemplo, usando a “Extrair Coleção”. A função principal desta etapa é agrupar dados por chaves específicas especificadas pelo usuário. A etapa coleta os dados divididos e combina apenas as entradas que correspondem às chaves especificadas.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Selecionar a etapa anterior |
| Chaves                | -                | Chaves usadas para agrupar dados |

## Casos
- **Combinando Dados Divididos**: Usado para combinar dados divididos nas etapas anteriores, como a “Extrair Coleção”, usando chaves específicas.
- **Segmentação e Análise de Dados**: Adequado para casos em que é necessário analisar dados de acordo com categorias ou critérios específicos.

## Exceções
- **Dependência das Chaves de Agrupamento**: A precisão e relevância das chaves são críticas para agrupar os dados corretamente.
- **Dificuldade no Processamento e Análise de Dados**: Agrupar pode ser difícil se a estrutura dos dados for variada ou se as chaves não identificarem grupos de forma única.

## Cenário de aplicação

Este componente verifica a disponibilidade de campos na etapa Agrupar Por. No fluxo de dados, primeiro, uma etapa de modelo de ação Get e a etapa Agrupar Por são adicionadas. Em seguida, na interface, o componente importado é aberto, e a aba "Rede" nas ferramentas de desenvolvedor do navegador é aberta. Depois disso, o botão "Agrupar por" é clicado na interface. Se a etapa funcionar corretamente, uma linha "executar" com uma prévia da resposta HTTP deve aparecer na aba Rede, contendo dados com a chave "ETO test123" e sua agregação.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1fKeJh3a0HHcG7VuFs-Tx5YdS7H6C7mI0/view?usp=sharing).