# Gráficos

![](../../assets/images/app-development/charts.png)

## Informações gerais
“Chart View” é um Componente de UI projetado para exibir e personalizar a apresentação gráfica de dados.

## Parâmetros
**Propriedades do componente:**

| Grupo de configurações | Campo de configuração | Opções de valor                          | Propósito                                      |
|------------------------|-----------------------|-----------------------------------------|-------------------------------------------------|
| (Configurações globais) | Componente            | -                                       | Seleção de um componente a ser exibido no gráfico     |
|                        | Tipo de gráfico       | barra, barra horizontal, pizza, rosquinha, linha | Tipo do gráfico                                     |
|                        | Campo de rótulo      | -                                       | Campo para rótulos no gráfico                      |
|                        | Fonte de dados        | -                                       | Fonte de dados para o gráfico                    |
|                        | Mostrar legenda       | verdadeiro, falso                       | Exibição da legenda no gráfico                 |
|                        | Valor máximo do eixo Y | -                                       | Valor máximo no eixo Y                 |
|                        | Valor mínimo do eixo Y | -                                       | Valor mínimo no eixo Y                  |
|                        | Valor máximo do eixo X | -                                       | Valor máximo no eixo X                 |
|                        | Valor mínimo do eixo X | -                                       | Valor mínimo no eixo X                  |
|                        | ID de automação       | -                                       | ID para automação                |

**Propriedades CSS**

| Grupo de configurações | Campo de configuração | Opções de valor | Propósito |
| --- | --- | --- | --- |
| Layout | Largura | - | Largura do componente |
|       | Altura | - | Altura do componente |
|       | Crescer | verdadeiro, falso | A propriedade determina quanto um elemento crescerá em relação aos outros elementos flex dentro do mesmo contêiner |
|       | Margem | - | A propriedade define os preenchimentos externos em todos os quatro lados do elemento |
|       | Preenchimento | - | A propriedade define os preenchimentos internos em todos os lados do elemento |
|       | Visível | verdadeiro, falso | Visibilidade do componente    |
|       | Oculto | verdadeiro, falso | Ocultando um componente      |
| Aparência | Raio do canto | - | A propriedade é usada para arredondar os cantos de um elemento |
|       | Espessura da borda | - | A propriedade permite definir os limites para o elemento |
| Pincel | Fundo | - | A propriedade define a cor de fundo do elemento |
|       | Pincel da borda | - | A propriedade define a cor da borda do elemento |

**Parâmetros da fonte de dados:**

| Campo de configuração | Opções de valor | Propósito |
| --- | --- | --- |
| Título | - | Título da fonte de dados |
| Valor | Escolha múltipla | A propriedade permite selecionar um valor da fonte de dados dos campos Inteiro e Número |
| OK | Botão | Aplicação da personalização |
| Cancelar | Botão | Cancelamento da personalização |

## Casos
- **Visualização de Dados**: Usado para criar gráficos e tabelas, permitindo apresentar dados de forma eficiente.
- **Painéis de Análise**: Adequado para painéis de análise que requerem uma exibição visual de estatísticas e métricas.

## Exceções
- **Uso Especializado**: Limitado à criação de gráficos e não é adequado para outros tipos de visualizações.