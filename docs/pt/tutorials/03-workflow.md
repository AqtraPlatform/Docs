# Tutorial №3

<br>

## Usando Python

### Introdução

<br>

A plataforma oferece a capacidade de usar Python para diversos fins como uma linguagem de script/programação conveniente e amplamente conhecida.

Os scripts Python suportados pela plataforma devem usar a versão 3.0 do Python, conforme descrito aqui: https://docs.python.org/3/. O guia completo para desenvolvedores pode ser encontrado na seção "Usando Python".

A versão do Python utilizada pela plataforma é chamada Iron Python, que fornece uma interface para código C#. Ela oferece duas bibliotecas importantes que precisam ser importadas no início do script — `clr` e `system`. Essas bibliotecas fornecem acesso a entidades da plataforma que podem ser consultadas e controladas a partir do script.
<br>

### Formas de Usar Scripts Python na Plataforma

<br>

Existem várias maneiras de usar Python na plataforma:

- Permite controlar formulários de aplicação projetados e executados usando a plataforma, além de fornecer índices personalizados que podem ser acionados em resposta a um evento, como um cliente pressionando um botão.
  <br>

- Chamando uma Função Dentro de um "Script de Componente", por Exemplo, Quando um Botão é Pressionado:

  - Para fazer isso, você precisa definir uma função dentro do Script de Componente, em seguida, ir a um elemento de controle de UI, como um Botão, acessar a seção "Ações" e definir o parâmetro "Tipo de Comando" como "Executar Script". Depois, você precisa inserir o nome e os parâmetros de chamada (se houver) do seu script nos campos fornecidos.
    <br>

- Usando uma Função Dentro de um Script de Componente para Eventos de Mudança de Valor:
  - Para fazer isso, você precisa definir uma função dentro do script do componente, em seguida, ir a um elemento de controle de UI, como uma caixa de texto, etc., depois acessar a seção "Eventos" e inserir o nome do seu script no campo "Na mudança de valor".
  - Observe que essa função será chamada apenas se os dados no campo tiverem mudado e o foco do elemento de controle de UI no formulário sair desse elemento de controle de UI.

<br>

- Inscrevendo-se em Mudanças de Dados Usando o Método `context.DataModel.Model.Subscribe()`:
  - A maneira mais fácil de fazer isso é definir uma função para interceptar todas as mudanças (por exemplo, `def check_all_changes()`) no seu script de componente e, em seguida, se inscrever nela.
  - Sua função será chamada toda vez que houver uma mudança nos dados atuais do elemento de controle de UI, no momento em que esse elemento de controle de UI perder o foco (por exemplo, quando o usuário mudar para outro elemento de controle de UI ou outra aplicação).

<br>

- Como parte de uma ação DataFlow, execute um script para definir a lógica de tomada de decisão, transformar dados e definir variáveis internas que serão usadas como parte dos scripts DataFlow. Você pode ver exemplos de uso de scripts Python para DataFlow na seção "Usando Python".

<br>

### Usando Python para Acessar Componentes da Plataforma

<br>

Para acessar componentes da plataforma, você primeiro precisa importar as bibliotecas clr do IronPython, conforme mostrado abaixo.

```
#Add IronPython library that imports system CRL (.NET) names into Python
import clr
```

Após a importação, vários objetos podem ser acessados a partir do script Python via a variável de sistema `context`.

<br>

### Usando context.Model & context.DataModel

<br>

`context.Model` & `context.DataModel` fornecem acesso a vários campos de dados do modelo da plataforma.

Para context.Model, os campos de dados incluem tanto os campos de componente padrão fornecidos pela plataforma quanto os campos personalizados adicionados pelo desenvolvedor do componente.

Para context.DataModel, apenas os campos personalizados adicionados pelos desenvolvedores de componentes estão disponíveis.

Recomenda-se que context.DataModel seja usado para acessar todos os campos personalizados, e context.Model seja usado apenas para acessar os campos internos do componente padrão.

Se escrevermos um script de componente que acesse este modelo, as seguintes variáveis de modelo do sistema estarão disponíveis em nosso script através de context.Model:
- `Id` - identificador interno, gerado automaticamente pela plataforma para cada componente. Se Id == 0, isso significa que os dados do componente ainda não foram salvos, indicando que estamos no modo de entrada de dados para esta instância particular dos dados do componente, como adicionar uma nova fatura em nosso Tutorial #1.
- `createDate` - data definida internamente quando a instância de dados deste componente foi criada pela primeira vez
- `name` (String) - nome amigável do sistema que será utilizado por padrão para exibir links através de campos do tipo Catálogo
- `updateDate` - data definida internamente da última atualização da instância de dados deste componente.
- `CreatorSubject` - dados que mostram qual usuário adicionou a instância de dados deste componente particular.
- `changeAuthor` - dados que mostram qual usuário atualizou pela última vez este componente particular

Além disso, os seguintes atributos específicos do componente estarão disponíveis para nosso componente do Tutorial #1 via context.DataModel (recomendado) ou context.Model:

- `InvoiceName` - nome único para nossa nova fatura
- `InvoiceState` - status atual da nossa nova fatura
- `InvoiceNumber` - identificador numérico único para nossa fatura
- `InvoiceDueDate` - data de vencimento da nossa fatura
- `InvoiceTotalValue` - valor total da nossa fatura

Vamos agora escrever um script de exemplo que irá preencher alguns campos para uma nova fatura.

<br>

```python
#Start of the script
#Add IronPython library that imports system CRL (.NET) names into Python
import clr

#Get Component’s DataModel reference
datamodel = context.DataModel.Model
# context.Model.Id shows internal Id for the component data instance
if (context.Model.Id == 0):
# If context.Model.Id is 0, then the instance has not yet been created,
# That means we are creating a new invoice
# We will then set some fields with default values
# Since this is a new Invoice,
# We’ll set it’s status to Under Review and provide default number and name
datamodel.InvoiceNumber = 11111
datamodel.InvoiceName = 'PLEASE_SET_A_UNIQUE_NAME'
datamodel.InvoiceState = 0
#End of the script
```

<br>

Agora, se abrirmos o aplicativo do Tutorial #1 e clicarmos no botão "Adicionar" para adicionar uma nova fatura, a tela ficará assim:

<br>

![Tutorial 3.1](../assets/images/tutorials/tut3.1.png)

<br>

### Usando context.Properties

<br>

`context.Properties` permite acesso a todos os elementos do componente e pode ser usado, por exemplo, para utilizar funções de elementos de controle de UI de formulário para gerenciar um elemento de controle de UI específico.

Para acessar um elemento de controle de UI, use `context.Properties` da seguinte forma:

```
context.Properties.<Internal_UI_Control_Name>.<UIControlProperty> = <Value>
```

Aqui, `<Internal_UI_Control_Name>` deve ser substituído pelo nome do seu elemento de controle de UI que você configurou durante o design. Por exemplo, no caso do Tutorial #1, definimos o nome interno para o elemento de controle de UI InvoiceState conforme mostrado abaixo:

<br>

![Tutorial 3.2](../assets/images/tutorials/tut3.2.png)

<br>

Agora podemos usar esse nome interno para definir a seguinte lógica:

1. Ao criar uma nova fatura, o status é definido como "Em Revisão".
2. A alteração do campo de status é proibida, o que significa que este campo deve estar desabilitado, mas visível.

A maneira de fazer isso é usar a propriedade `Disable` do nosso elemento de controle de UI para defini-lo como `True`. Isso fará com que o campo apareça, mas não pode ser alterado pelo usuário que está criando a nova fatura. Isso é feito adicionando uma linha de código conforme mostrado abaixo:

```
context.Properties.UI_InvoiceStatus.Disabled = True
```

Adicionar isso ao nosso script de componente resultará nas seguintes alterações em nosso formulário de adição de nova fatura.

<br>

![Tutorial 3.3](../assets/images/tutorials/tut3.3.png)

<br>

Como você pode ver, o campo "Status da Fatura" agora está desabilitado.

Outro campo frequentemente usado `context.Properties` para gerenciar elementos de controle de UI é `Visible`. Se definido como `False`, este elemento de controle de UI específico não aparecerá no formulário. Ele pode ser reabilitado definindo-o como `True`. Isso pode ser feito para qualquer elemento de controle de UI, incluindo painéis que contêm vários elementos de controle de UI diferentes.

Um exemplo de como isso pode ser usado no contexto do nosso Tutorial #1 para inicialmente ocultar o campo "Status da Fatura" é mostrado abaixo.

<br>

```python
if (context.Model.Id == 0):
    context.Properties.UI_InvoiceStatus.Visible = False
if (context.Model.Id > 0):
    context.Properties.UI_InvoiceStatus.Visible = True
```

<br>

Há também o campo `Hidden`, que oculta/exibe elementos da interface do usuário, semelhante ao campo `Visible`.

Outro campo frequentemente usado `context.Properties` é `Required`. Se definido como `True`, o elemento de controle de UI específico se torna obrigatório (não pode estar vazio), e se definido como `False`, ele se torna opcional. Observe que isso apenas altera o estado do elemento de controle de UI para a propriedade personalizada na instância atual do formulário, não a propriedade personalizada em si, o modelo de formulário ou elementos de controle de UI para essa propriedade personalizada em outros formulários.

<br>
### Usando context.Form

<br>

`context.Form` pode ser usado para acessar os dados do formulário (por exemplo, para fins de validação durante o processamento do formulário, antes que os dados do formulário sejam salvos no armazenamento interno) ou para gerenciar a representação visual do formulário, como definindo uma mensagem de erro.

Para fazer isso, use `context.Form.Get(<CustomFieldName>)` para obter um objeto representando um campo específico. Em seguida, você pode usar as seguintes funções com este objeto.

- `context.Form.Get(<CustomFieldName>).SetValue(<Value>)` — define o valor para um controle de UI específico no formulário atual.
- `context.Form.Get(<CustomFieldName>).AddError(<StringValue>)` — define uma mensagem de erro exibida sob um controle de UI específico no formulário atual.
- `context.Form.Get(<CustomFieldName>).ClearError()` — limpa a mensagem de erro mostrada sob um controle de UI específico no formulário atual.

A seguinte extensão de script mostra como verificar a situação em que o usuário não alterou o nome padrão da fatura que definimos acima nos exemplos do Tutorial #1.

<br>

```python
if datamodel.InvoiceName == 'PLEASE_SET_A_UNIQUE_NAME':
    context.Form.Get("InvoiceName").AddError("Please set a unique invoice name")
else:
    context.Form.Get("InvoiceName").ClearError()
```

<br>

O resultado será semelhante à seguinte captura de tela se o nome padrão não tiver sido alterado:

<br>

![Tutorial 3.4](../assets/images/tutorials/tut3.4.png)

<br>

### Usando context.Commands

<br>

`context.Commands` pode ser usado para gerenciar a UI do componente atualmente em execução, alterar o conteúdo do formulário atual, abrir diferentes páginas, abrir novos componentes, retornar à página anterior ou até mesmo iniciar novos Workflows, Dataflows ou Scripts.

Esses comandos são tipicamente usados dentro de scripts chamados pela ação ExecuteScript usando botões, e em casos semelhantes. Por exemplo, em nosso Tutorial #1, o botão Voltar para Todas as Faturas pode usar o seguinte script para retornar à página anterior:

<br>

```python
def navigate_back():
    context.Commands.NavigationBack()
```

<br>

Este script deve ser parte do script do componente e ser configurado para o botão Voltar para Todas as Faturas, na seção `Actions` -> `Command Type`: `Execute Script` -> `Method Name`: `navigate back`.

<br>

Outras funções disponíveis de context.Commands:

- `context.Commands.AddItem(GUID)` - adicionar um elemento de controle de UI à página usando o GUID.
- `context.Commands.ChangePageAsync(GUID)` - abrir uma página usando seu GUID
- `context.Commands.ChangePageByName(«PageName»)` - alterar a página do componente atual para uma nova página usando o nome interno
- `context.Commands.OpenComponent(GUID ComponentID, GUID PageID)` - abrir um novo componente e uma página específica dentro do componente
- `context.Commands.EditItem(GUID UI_ControlID, EntityId)` - mudar o foco da UI para um elemento de controle de UI específico e dados específicos (usando seu identificador interno)
- `context.Commands.ExecuteWorkflow(GUID WorkflowID)` - executar um workflow usando seu identificador. Além disso, você pode definir WaitComplete como verdadeiro ou falso, se necessário.
- `context.Commands.ExecuteDataflow(GUID dataflow identifier, ContextID)` - executar um dataflow usando seu GUID e o contexto de dados especificado.
- `context.Commands.ExecuteScript(String ScriptName, StringParams Script)` - executar um script (função) do Script do Componente com alguns parâmetros.