# Selecionar muitos

![](../../assets/images/app-development/select-many.png)

## Informações gerais
A etapa “Selecionar Muitos” é usada para converter um campo do tipo array em uma lista plana. Ao contrário da etapa “Extrair Coleção”, “Selecionar Muitos” preserva os dados do modelo da etapa anterior e adiciona valores “pai” com um prefixo `$parent` para cada elemento do array. Isso não apenas expande o array, mas também preserva o contexto da entrada pai.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Selecionando a etapa anterior |
| Caminho do modelo     | -                | Caminho para um campo array no modelo de dados |

## Casos
- **Expansão e Preservação de Contexto**: Usado para converter arrays de dados em uma lista plana enquanto preserva a relação com os dados pai.
- **Processamento de Estruturas Hierárquicas**: Adequado para scripts onde é necessário processar dados de arrays sem perder a conexão com os elementos de dados “pai”.

## Exceções
- **Processamento de Arrays Grandes**: O processamento de arrays grandes pode ser mais intensivo em recursos devido à necessidade de preservar o contexto dos dados pai.

## Cenário de aplicação

Este componente é uma ferramenta para criar e gerenciar fluxos de dados dentro da aplicação. A etapa 'Selecionar muitos' neste componente é usada para escolher vários itens de um array de dados obtidos na etapa anterior do fluxo de dados. O componente permite que os usuários definam condições de seleção e processamento de dados de acordo com suas necessidades.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1T9k35m8cg56vmM68LCT0brMeYQ2JIJ6U/view?usp=sharing).