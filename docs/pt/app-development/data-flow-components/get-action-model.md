# Obter Modelo de Ação

![](../../assets/images/app-development/get-action-model.png)

## Informações gerais
A etapa “Obter Modelo de Ação” é projetada para extrair um modelo de ação de uma fonte ou sistema específico. Esta etapa pode ser usada para obter dados sobre ações ou processos específicos que são necessários para processamento ou análise adicional dentro do fluxo de dados.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor            | Propósito |
|-----------------------|----------------------------|-----------|
| Nome da etapa         | -                          | Nome da etapa |
| Validar valores de entrada | true, false            | Especifica se os valores de entrada devem ser verificados quanto à correção antes do processamento |

## Casos
- **Integração de UI**: Frequentemente usada como uma etapa inicial no fluxo de dados, especialmente quando o fluxo de dados é ativado a partir da UI, por exemplo, ao pressionar um botão. Permite obter o estado atual dos dados do componente no momento da ativação.
- **Transferência Automática de Dados da UI**: Quando a transferência de dados é ativada a partir de elementos da UI, como botões, a plataforma transmite automaticamente os dados atuais do componente, incluindo as alterações feitas pelo usuário.

## Exceções
- **Limitações na Recuperação de Dados**: A etapa recupera apenas os dados dos campos (propriedades) do componente. Para obter as variáveis definidas no Script do Componente, você precisa usar outras etapas, como “Obter modelo bruto”.

## Cenário de aplicação

O componente é um sistema para adicionar e exibir dados usando vários tipos de campos. Ele inclui a capacidade de adicionar campos de diferentes tipos na **definição** e fornece uma interface de front-end para inserção de valores, além de exibir dados em um **datagrid** com a capacidade de atualizar a página. Este componente utiliza as seguintes **etapas do fluxo de dados**: **Obter modelo de ação**, **Atualizar entrada**, **Escrever resposta**.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/15M_FvmlFmkJXunTeeT6jtFolPvE5jCfk/view?usp=sharing)