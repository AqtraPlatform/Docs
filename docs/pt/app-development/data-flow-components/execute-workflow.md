# Executar Fluxo de Trabalho

![](../../assets/images/app-development/execute-workflow.png)

## Informações gerais
A etapa “Executar Fluxo de Trabalho” é usada para ativar e executar um fluxo de trabalho específico no sistema.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Selecionando a etapa anterior |
| Componente            | -                | O componente dentro do qual o fluxo de trabalho é realizado |
| Fluxo de trabalho     | -                | Nome do fluxo de trabalho a ser concluído |
| Campo de entrada do componente | -       | O campo no componente usado para transferir dados para o fluxo de trabalho |

## Casos
- **Controle dinâmico do fluxo de dados**: Pode ser usado para iniciar fluxos de trabalho específicos com base em dados obtidos de etapas anteriores do Dataflow, o que permite criar sistemas de gerenciamento de dados flexíveis e adaptáveis.

## Exceções
- **Dependência da correção dos dados**: Para evitar erros na execução do fluxo de trabalho, é necessário garantir que os dados enviados para o fluxo de trabalho sejam precisos e completos.
- **Coordenação entre Dataflow e Fluxo de Trabalho**: É importante configurar cuidadosamente a interação entre Dataflow e Fluxo de Trabalho para garantir uma transferência suave e correta de dados e comandos entre eles.

## Cenário de aplicação

O componente criado serve como uma interface para interagir com o modelo de dados que contém um campo "user_name" do tipo string. Este componente inclui funcionalidade para atualizar o modelo de dados usando a etapa Atualizar modelo dentro do Fluxo de Trabalho. Para interagir com o componente, o usuário pode inserir seu nome, clicar em um botão, após o qual os dados serão enviados e o nome será exibido na grade de dados após atualizar a página.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1AgjjrOW-z2LPMj7sFWg_PKjHjFfVtxub/view?usp=sharing).