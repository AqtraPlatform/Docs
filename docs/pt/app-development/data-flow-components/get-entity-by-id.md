# Obter entidade por id

![](../../assets/images/app-development/get-entity-by-id.png)

## Informações gerais
A etapa “Obter Entidade por ID” é usada para obter um item de componente pelo seu identificador único (ID). Esta etapa é geralmente utilizada em combinação com outras etapas, como “Lookup” ou “Atualizar Entrada”, que retornam um ID que é adequado para esta etapa.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Selecionando a etapa anterior |
| Campo de origem       | -                | Campo contendo o ID a ser pesquisado |
| Nome do campo de destino | -             | Campo onde o resultado será registrado |
| Componente            | -                | Componente que está sendo pesquisado |

## Casos
- **Pesquisa de Dados por ID**: Usado para recuperar com precisão uma entrada específica utilizando o ID do componente.

## Exceções
- **Dependência da Precisão do ID**: O ID exato deve ser especificado e estar disponível nos dados de origem para que a consulta seja bem-sucedida.
- **Tratamento de Inconsistências**: Se não houver entrada com o ID especificado, a etapa pode retornar um resultado vazio.

## Cenário de aplicação

Este componente permite adicionar um campo do tipo catálogo e criar um fluxo de dados para recuperar uma entidade pelo seu identificador. O campo do tipo catálogo é colocado na página para selecionar o valor correspondente do catálogo. O fluxo de dados inclui uma etapa 'Obter modelo de ação' para inicialização, uma etapa 'Obter entidade por id' para recuperar a entidade pelo identificador usando o valor selecionado do catálogo, e uma etapa 'Escrever resposta' para output do resultado.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1eCxoYHKg0Zl8APxnUMRA9qmpqNkrtfuW/view?usp=sharing).