# Ação do Formulário

![](../../assets/images/app-development/form-action.png)

## Informações gerais
A etapa “Ação do Formulário” é utilizada para realizar várias ações na interface do usuário (UI) na parte frontal da aplicação, como abrir páginas, executar scripts, abrir janelas modais, etc. A etapa é o link entre a lógica do servidor e a interface do usuário, permitindo que você controle dinamicamente o comportamento da UI.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | Multiseleção de Catálogo | Seleção das etapas anteriores |
| Ação do formulário    | Executar script, Abrir página, Abrir componente, Abrir Sidebar, Abrir Modal, Abrir arquivo em nova aba | Tipo de comando da UI |
| Nome do método        | (Se ‘Executar script’ for selecionado) | Nome da função de script a ser executada |
| Abrir página          | (Se ‘Abrir página’ for selecionado) | Lista de páginas a serem abertas |
| Campo de informações do arquivo | (Se ‘Abrir arquivo’ em nova aba for selecionado) | Campo de informações do arquivo a ser aberto |
| Abrir sidebar         | Configurações para a sidebar | Configurando para abrir a sidebar |
| Abrir modal           | Configurações para janelas modais | Configurando para abrir uma janela modal |

## Casos
- **Gerenciamento Dinâmico de Elementos da UI**: Usar “Abrir Sidebar” ou “Abrir Modal” permite exibir dinamicamente sidebars ou modais com informações adicionais, formulários ou outros conteúdos, aumentando a interatividade e usabilidade da interface.
- **Atualização da Grade de Dados**: Em um script onde o usuário carrega novos dados, você pode adicionar uma função de atualização ao formulário e a grade de dados será atualizada sem precisar atualizar a página.

## Exceções
- **Etapa de Resposta de Escrita Necessária**: Após realizar ações como abrir uma página ou arquivo, você precisa adicionar uma etapa de “Escrever Resposta” para completar o fluxo de dados corretamente.
- **Dependência de Etapas Anteriores**: Ao usar certas ações, como “Abrir arquivo em nova aba”, você precisa ter um arquivo apropriado preparado pelas etapas anteriores.

## Cenário de Aplicação

Este componente emprega vários métodos na etapa de Ação do Formulário para interagir com a interface do usuário na parte frontal. Os usuários podem realizar diferentes ações, como executar um script (Executar Script), abrir uma página (Abrir página) ou um componente (Abrir componente), baixar um arquivo (Baixar arquivo) e abrir um arquivo em uma nova aba (Abrir arquivo em nova aba). Após a execução dessas ações, os dados são processados e enviados de volta para a parte frontal usando a etapa de Escrever resposta.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1AgjjrOW-z2LPMj7sFWg_PKjHjFfVtxub/view?usp=sharing)