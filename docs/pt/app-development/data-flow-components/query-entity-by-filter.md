# Consultar entidade por filtro

![](../../assets/images/app-development/query-entity-by-filter.png)

## Informações gerais
A etapa “Consultar Entidade por Filtro” é usada para buscar entradas em um componente específico. Ao contrário das etapas, que usam filtros ou identificadores para buscar, esta etapa é projetada para buscar diretamente entradas em um componente.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Selecionando a etapa anterior |
| Componente            | -                | Componente que está sendo pesquisado |
| Nome do campo de destino | -             | Nome do campo no qual o resultado da consulta será salvo |

## Casos
- **Busca Direta no Componente**: Usado para buscar diretamente entradas em um componente específico.

## Exceções
- **Dependência do Componente**: A eficácia da etapa está diretamente relacionada à estrutura e ao conteúdo dos dados no componente selecionado.

## Cenário de aplicação

O fluxo de dados demonstra vários cenários de uso da Consultar Entidade por Filtro para filtragem de dados. Cada cenário inclui a adição de etapas de Modelo de Ação de Obtenção e Consultar Entidade por Filtro, preenchendo campos e aplicando filtros, bem como uma etapa de Escrever Resposta para a saída dos resultados.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1FBXtSNuk7-KmyGofhghsJJiVrV_xebT1/view?usp=sharing)