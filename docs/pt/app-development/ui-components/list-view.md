# Visualização em lista

![](../../assets/images/app-development/list-view.png)

## Informações gerais
“Visualização em Lista” é um componente de UI utilizado para exibir e configurar a apresentação de dados em “cartões”.

## Parâmetros
**Propriedades do componente**

| Grupo de configurações | Campo de configuração | Opções de valor          | Propósito                         |
|------------------------|-----------------------|--------------------------|------------------------------------|
|                        | Nome                  | -                        | Nome do Componente de UI no sistema |
| Comum                  | Componente            | Multiselecionar do Catálogo | Contém uma lista de todos os Componentes |
|                        | Número de colunas     | -                        | Número de colunas do contêiner      |
|                        | Número de linhas      | -                        | Número de linhas do contêiner       |
|                        | Espaçamento de colunas| -                        | Espaçamento entre colunas          |
|                        | Espaçamento de linhas  | -                        | Espaçamento entre linhas           |
|                        | Tamanho da página     | -                        | Tamanho do contêiner               |
|                        | Recarregamento manual  | true, false              | Capacidade de recarregar dados manualmente |
|                        | Ocultar seletor de página | true, false            | Ocultar seletor de página          |
|                        | Habilitar arrastar e soltar | true, false          | Habilitar recurso de arrastar e soltar |
|                        | Grupo de arrastar e soltar | -                    | Grupo de arrastar e soltar (se houver) |
|                        | ID de automação       | -                        | ID para automação                  |
| Eventos                | Ao carregar fonte de dados | -                    | Evento de carregamento da fonte de dados |
|                        | Ao carregar           | -                        | Evento de carregamento do componente |
|                        | Ao soltar            | -                        | Evento de arrastar e soltar       |

**Propriedades CSS**

| Grupo de configurações | Campo de configuração | Opções de valor          | Propósito                         |
|------------------------|-----------------------|--------------------------|------------------------------------|
| Layout                 | Largura               | -                        | Largura do componente              |
|                        | Altura                | -                        | Altura do componente               |
|                        | Margem                | -                        | Preenchimento externo do componente |
|                        | Preenchimento         | -                        | Preenchimento interno do componente  |
|                        | Visível               | true, false              | Visibilidade do componente          |
|                        | Oculto                | true, false              | Ocultação do componente            |
|                        | Orientação            | Horizontal, Vertical      | Orientação do componente           |
| Aparência              | Raio de canto         | -                        | Raio de arredondamento dos cantos  |
|                        | Espessura da borda    | -                        | Espessura da borda do componente   |
|                        | Opacidade             | -                        | Transparência do componente        |
| Pincel                 | Fundo                 | -                        | Cor de fundo do componente         |
|                        | Cor da borda         | -                        | Cor da borda do componente        |

## Usando o recurso de arrastar e soltar
Primeiro, no grupo de configurações “Comum”, você precisa selecionar a seguinte opção:

![](../../assets/images/app-development/enable-drag-and-drop.png)

Após salvar e publicar, o recurso de arrastar e soltar já estará disponível para esta visualização em lista no local de trabalho. Para o funcionamento correto subsequente, você precisa acessar o script do componente e preparar a função para lidar com o evento de arrastar e soltar (ao soltar).

Aqui está um exemplo da função aplicada a um quadro kanban que consiste em uma visualização em lista principal e uma visualização em lista aninhada. A principal desempenha a função das etapas do funil de vendas e está em uma posição horizontal, enquanto a aninhada contém os próprios negócios e está em uma posição vertical. A função recebe o ID do objeto sendo arrastado (neste caso, o negócio) e a etapa para a qual o negócio é transferido, em seguida, chama o fluxo de dados e, se concluído com sucesso, atualiza a visualização em lista, movendo o negócio para uma nova etapa:

```python
def OnMove(dstList, srcList, dataObject, oldIdx, newIdx):
    context.Logger.Info("Callback on move")
    # The new Busy(boolean) method puts the UIElement into a loading status,
    # showing or hiding the loader
    srcList.Busy(True)
    dstList.Busy(True)
    
    # The new GetDynamicFilterValue(string) method computes the value of a Dynamic filter.
    # If there are two filters on one field, the first in the list is computed
    stage = dstList.GetDynamicFilterValue("data.Stage")
    
    # Creating a model to call the data-flow
    flowModel = {"Stage": stage, "OrderId": dataObject.Id}
    # Calling the data-flow with a new overload for onComplete and onError
    context.ExecuteDataflow("783cf3e3-d8f8-4551-8447-13be4f738e41", flowModel, 
    lambda res: OnDataflowComplete(res, dstList, srcList), 
    lambda ex: OnDataflowError(ex, dstList, srcList))

def OnDataflowComplete(dataResult, dstList, srcList):
    # The new Busy(boolean) method puts the UIElement into a loading status,
    # showing or hiding the loader
    srcList.Busy(False)
    dstList.Busy(False)
    # Refreshing the lists
    srcList.Refresh()
    dstList.Refresh()

def OnDataflowError(exception, dstList, srcList):
    # The new Error(boolean, string) method puts the UIElement into an error status,
    # displaying the error message
    srcList.Error(True, "An error occurred")
    dstList.Error(True)
    context.Logger.Error(exception, "An error occurred during the data-flow call")
```

## Casos
- **Exibição de Dados**: Eficaz para apresentar dados na forma de cartões ou listas.
- **Interface do Usuário**: Adequado para interfaces que requerem representação de informações na forma de cartões ou listas.

## Exceções
- **Flexibilidade Limitada**: Não é adequado para exibir dados além do formato de cartão ou lista, pois se especializa em uma representação visual específica.
- **Limitações Visuais**: O estilo e o design podem ser limitados pelas configurações de CSS, que podem não atender a todos os requisitos de design.