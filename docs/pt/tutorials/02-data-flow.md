# Tutorial №2 
<br>

## Criando uma Aplicação Simples para uma Concessionária de Carros
<br>

**Descrição da Aplicação:**

Vamos criar uma aplicação composta por vários componentes que permite rastrear carros disponíveis para venda, atribuir um gerente para a assinatura do contrato e permitir que os gerentes fechem o negócio.

**Vamos criar os seguintes componentes:**

<br>

### Componente "Especialistas em Transações"

O primeiro componente será um formulário simples para adicionar novos gerentes e consistirá em uma única propriedade personalizada:

<br>

![Tutorial 2.2](../assets/images/tutorials/tut2.1.png)

<br>

Em seguida, passamos para a configuração do nosso espaço de trabalho, adicionando um elemento de painel onde realizaremos nosso trabalho.

Depois, nas configurações do painel, sob o grupo de configurações "Layout", altere a orientação do painel para vertical e comece a adicionar os seguintes elementos: precisaremos do manager_name que criamos e de um botão. Deve ficar assim:

<br>

![Tutorial 2.2](../assets/images/tutorials/tut2.2.png)

<br>

Em seguida, crie um fluxo de dados, nomeie-o como "Adicionar um gerente" e adicione os seguintes passos: `get action model`, `update entry`, `write response`. Deve ficar assim:

<br>

![Tutorial 2.3](../assets/images/tutorials/tut2.3.png)

<br>

Configure o passo `Update entry` da seguinte forma:

<br>

![Tutorial 2.4](../assets/images/tutorials/tut2.4.png)

<br>

**Não se esqueça** de definir o `source step` para o passo `update entry`!

Após configurar o fluxo de dados, vincule-o ao botão da seguinte forma: vá para as configurações do botão, clique no grupo de configurações "ações", defina o "tipo de comando" como "executar fluxo de dados" e selecione o fluxo de dados que criamos "Adicionar um gerente".

Clique em "Salvar", "Pronto para publicar". Publique o componente e, em seguida, adicione-o ao local de trabalho usando o "menu de navegação" do domínio onde você está implantando sua aplicação (neste caso, este é o domínio "digital-workplace").

<br>

![Tutorial 2.5](../assets/images/tutorials/tut2.5.png)

<br>

Clique em "ADICIONAR ITEM DE MENU" e adicione nosso componente:
<br>

![Tutorial 2.6](../assets/images/tutorials/tut2.6.png)

<br>

Vá para o `workplace` e adicione alguns gerentes para trabalhar com eles.

<br>

### Componente "Frota de Carros"

<br>

Com este componente, configuraremos a exibição de todos os carros e informações gerais sobre eles, adicionaremos um formulário para criar registros de novos carros, um formulário para atribuir um gerente de transação a um carro e um formulário para confirmar que o negócio foi concluído com subsequente arquivamento do registro do carro.

Neste componente, criaremos várias propriedades personalizadas:

- `car_vin`: tipo de propriedade - `string`, título - `VIN`, configurações - `required`, `primary key`, `query`;
- `car_brand`: tipo de propriedade - `string`, título - `Car Brand`, configurações - `required`, `query`;
- `car_model`: tipo de propriedade - `string`, título - `Car Model`, configurações - `required`, `query`;
- `year_of_manufacture`: tipo de propriedade - `integer`, título - `Year of manufacture`, configurações - `required`, `query`;
- `color`: tipo de propriedade - `string`, título - `Color`, configurações - `required`, `query`;
- `price`: tipo de propriedade - `number`, título - `Price of the car`, configurações - `required`, `query`;
- `is_manager_exists`: tipo de propriedade - `boolean`, título - `Is manager exists`, configurações - `query`;
- `choosen_manager`: tipo de propriedade - `catalog`, componente - `Transaction Specialists` título - `Chosen Manager`, configurações - `query`;
- `is_archieved`: tipo de propriedade - `string`, configurações - `query`.

O componente consistirá nas seguintes partes (páginas):

<br>

1. **Página Principal**

Para adicionar uma página, você precisa encontrar o grupo `Layout` no `Toolbox` e arrastar o elemento `Page` para o espaço de trabalho.
Esta página apresentará uma grade de dados com todos os carros disponíveis para venda e informações gerais sobre eles para os gerentes de vendas. Além disso, adicionaremos um botão à página que redirecionará para um formulário para adicionar carros à lista, mas faremos isso mais tarde.

Adicione um painel ao espaço de trabalho, mude a configuração de orientação para vertical e, em seguida, adicione mais dois painéis. No painel inferior, coloque o elemento da grade de dados e, no painel superior, adicione mais dois painéis. No painel esquerdo, coloque um rótulo e escreva "Frota de carros" nas configurações de "valor de tradução". No painel direito, adicione um botão e escreva "Adicionar um novo carro" em seu "valor de tradução". Mais tarde, mudaremos a configuração de "Ações", mas por enquanto, você pode alterar o tamanho do botão nas configurações de "Layout".

<br>

![Tutorial 2.7](../assets/images/tutorials/tuto2.7.png)

<br>

Você pode experimentar outras configurações.

Em seguida, prossiga para configurar o `data grid`: clique no ícone de engrenagem e selecione o componente para a grade de dados "Frota de carros". Então, ao lado de colunas, clique em `+`, isso adicionará uma coluna à nossa grade de dados, faça isso 5 vezes.

Clique na primeira coluna, depois em "Adicionar campo" e selecione a propriedade `car_brand`. A configuração posterior deve parecer assim:

<br>

![Tutorial 2.8](../assets/images/tutorials/tut2.8.png)

<br>

Você deve configurar as seguintes colunas de maneira semelhante nesta ordem: 2ª coluna - `car_model`, 3ª coluna - `year_of_manufacture`, 4ª coluna - `color`, 5ª coluna - `price`.

Além disso, nas configurações da grade de dados, defina `Static filters`. Como vamos exibir carros que ainda não foram atribuídos a um gerente, defina a seguinte configuração:

<br>

![Tutorial 2.12](../assets/images/tutorials/tut2.12.png)

<br>

O resultado final em nosso espaço de trabalho deve parecer assim:

<br>

![Tutorial 2.9](../assets/images/tutorials/tut2.9.png)

<br>

2. **Adicionar um novo carro**

Esta página será acessada pelo usuário clicando no botão "Adicionar um novo carro" da nossa página anterior. Vamos começar a configurar nosso espaço de trabalho.

Adicione um painel à página. Nas suas configurações, mude a orientação da página para vertical. Em seguida, adicione mais dois painéis. No primeiro painel, também mude a orientação para vertical e transfira nossas propriedades para parecer assim:

<br>

![Tutorial 2.10](../assets/images/tutorials/tut2.10.png)

<br>

No painel inferior, adicione dois botões, defina seu preenchimento como no botão "Adicionar um novo carro" e nomeie-os de acordo: "Adicionar um novo carro" e "Voltar para todos os carros".

Nas configurações do botão "Voltar para todos os carros", defina as "Ações" para "Abrir página" "Página principal". Clicar neste botão redirecionará o usuário para a página com a grade de dados. Para o botão "Adicionar um novo carro", crie um fluxo de dados, que vincularemos a ele mais tarde.

O fluxo de dados consistirá nas seguintes etapas: `get action model`, `execute script`, `update entry`, `write response`. Vamos configurá-las.

Na etapa `execute script`, crie variáveis que serão usadas para as propriedades `is_manager_exists` e `is_archieved`:

```
item["_is_manager_exists@boolean"] = False
item["_is_archieved@boolean"] = False
```

Em seguida, configure a etapa `Update entry`:

<br>

![Tutorial 2.13](../assets/images/tutorials/tut2.13.png)

<br>

Em seguida, precisamos mapear nossos campos. **Lembre-se** de que os campos nas configurações da etapa são mapeados com o prefixo data.`property_name`. Para as propriedades `is_archieved` e `is_manager_exists`, use os valores de variável definidos na etapa de script de execução, deixe o campo `chosen_manager` vazio:

<br>

![Tutorial 2.14](../assets/images/tutorials/tut2.14.png)

<br>

**Sempre defina a etapa de origem para cada etapa, exceto a primeira. Isso não será mencionado mais adiante na descrição do tutorial.**

Agora que nosso fluxo de dados está completo, podemos vinculá-lo ao botão "Adicionar um novo carro" e salvar nosso componente. O resultado final da nossa página é mostrado abaixo:

<br>

![Tutorial 2.15](../assets/images/tutorials/tut2.15.png)

<br>

3. **Designar um gerente**

Esta página será chamada como uma janela modal ao clicar em uma entrada específica na grade de dados. É projetada para uma única função - atribuir um gerente a um carro específico. Vamos prosseguir para a configuração do espaço de trabalho.
A página em si se parecerá com a página "Adicionar um novo carro", com a única diferença sendo que adicionaremos a propriedade `chosen_manager` ao espaço de trabalho, que será a única propriedade disponível para modificação. Isso permite que o gerente selecione um colega para quem transferirá o carro e o negócio. Além disso, adicione dois botões, um para fechar a janela modal chamado "Voltar para todos os carros" e o outro chamado "Designar um gerente", que será vinculado a um fluxo de dados que criaremos mais tarde.

**Não se esqueça de habilitar a configuração Desativado nas configurações do TextBox para cada propriedade, exceto `chosen_manager`.**

<br>

![Tutorial 2.16](../assets/images/tutorials/tut2.16.png)

<br>

O resultado final nesta página deve se parecer com o mostrado abaixo:

<br>

![Tutorial 2.17](../assets/images/tutorials/tut2.17.png)

<br>

**Vamos passar para a configuração do fluxo de dados**.

Precisamos adicionar os seguintes passos: `get action model`, `execute script`, `lookup reference`, `update entry`, `write response`.

No passo `execute script`, criaremos uma variável que mudará a propriedade `is_manager_exists` para True, fazendo com que a entrada recém-criada desapareça da grade de dados na página Principal, onde configuramos filtros estáticos.

```
item["_is_manager_exists@boolean"] = True
```

Em seguida, usamos o passo `Lookup reference`. Recomendo que você leia sobre este passo na seção de Fluxo de Dados da nossa documentação técnica. O passo deve ser configurado como mostrado abaixo.

<br>

![Tutorial 2.18](../assets/images/tutorials/tut2.18.png)

<br>

Em seguida, configuramos o passo `Update entry`, no campo chave do componente especifique o nome do campo do passo `Lookup reference`:

<br>

![Tutorial 2.19](../assets/images/tutorials/tut2.19.png)

<br>

Em 'Mapeamento de campos', deixe os campos vazios, exceto para `chosen_manager` e `is_manager_exists`, estes são os campos que queremos alterar no registro encontrado usando o passo `Lookup reference`.

<br>

![Tutorial 2.20](../assets/images/tutorials/tut2.20.png)

<br>

No passo `write response`, precisamos definir o passo de origem.

Atribua este fluxo de dados para ser executado quando o botão "Designar um gerente" for pressionado. Em seguida, salve o componente.

<br>

**Prossiga para o script do componente para construir a janela modal**.

Para criar uma janela modal, você pode usar o script abaixo. Para trabalhar com o **script do componente**, recomendo fortemente que você leia a seção de documentação `Using Python`:

```
def show_model_info(model):
    context.Logger.Error("updated")

def open_custom_modal(sender, model):
    # Creating a modal window template using the GUID of a specific component
    dialog_builder = context.PlatformServices.DialogBuilder('component guid')
    # Setting the title for the modal window and selecting a specific page from the component's settings
    # Also setting the component instance ID to 1, so the first saved instance of component data will be used
    dialog_builder.WithEntryId(int(model[0].Id)).WithTitle("Appoint a manager").WithPageId('page id')
    # Setting the size of the modal window
    dialog_builder.WithVSize("650px").WithHSize("820px")
    dialog_builder.OnComplete(lambda model: show_model_info(model))
    dialog_builder.OnCancel(update_cars_success)
    # Opening the created modal window
    dialog_builder.OpenDialog()
    
def get_datagrid_cars(sender, *args):
    global datagrid_cars
    datagrid_cars = sender
    
def update_cars_success():
    datagrid_cars.Refresh()
```

As funções `get_datagrid_cars` e `update_cars_success` são usadas para atualizar automaticamente a grade de dados após alguma ação. Se você não as usar, a grade de dados só será atualizada após atualizar a página no navegador. Após copiar, você precisa salvar o componente e retornar ao espaço de trabalho na "Página Principal".

Você precisa ir para as configurações da grade de dados no grupo de configurações `Events` e atribuir a execução de funções a certas ações na grade de dados.

<br>

![Tutorial 2.21](../assets/images/tutorials/tut2.21.png)

<br>

Salve o componente, em seguida, prossiga para configurar a próxima página.

4. **Entrar em um contrato**

Esta página é um formulário que permite ao gerente arquivar um determinado negócio de carro, alterando o campo `is_archieved` para `True`.

A página é uma cópia da página `Appoint a manager`, a única diferença é que todos os campos têm a configuração `Disabled` -> `True`. Na parte inferior, adicionaremos dois botões, um dos quais iniciará o fluxo de dados, e o outro redirecionará o usuário para a página do componente que ainda não criamos.

A página em si deve se parecer com isto:

<br>

![Tutorial 2.22](../assets/images/tutorials/tut2.22.png)

<br>

Vamos passar para a criação e configuração do fluxo de dados. Precisaremos de 5 passos: `get action model`, `execute script`, `update entry`, `form action`, `write response`.

No passo `execute script`, criaremos uma variável que definirá o valor `True` na propriedade `is_archieved`.

```
item["_is_archieved@boolean"] = True
```

A configuração do passo `update entry` deve se parecer com isto:

<br>

![Tutorial 2.23](../assets/images/tutorials/tut2.23.png)

<br>
No campo da chave do componente, forneceremos uma referência ao registro que queremos editar, e então prosseguiremos para "Mapeamento de campos". Aqui deixamos todos os campos vazios, exceto para `is_archieved`. Aqui colocamos a variável que definimos na etapa `execute script`.

A próxima é a etapa `Form action`, à qual retornaremos após criar o componente final. Por enquanto, salve o componente para evitar perder seu trabalho.

### Componente "Grade de gerentes"

Este componente consistirá em uma única página e não criaremos propriedades personalizadas para ele. Este componente será usado apenas por gerentes que têm acesso a ele, permitindo que vejam todos os carros que foram movidos para a fase de negociação e atribuídos a um gerente específico.

Crie uma grade de dados, vincule-a ao componente `Car fleet` e adicione uma coluna para cada uma de suas propriedades. O resultado deve ser parecido com isto:

<br>

![Tutorial 2.24](../assets/images/tutorials/tut2.24.png)

<br>

Em seguida, vá para o grupo de configurações `Actions`, defina o tipo de comando como `Open application`, componente como `Car fleet`, página do componente como `Enter into a contract`, uma página que criamos como a última página do componente `Car fleet`.

Em seguida, clique no botão `Action parameters` e mapeie Id -> Id, conforme mostrado abaixo.

<br>

![Tutorial 2.25](../assets/images/tutorials/tut2.25.png)

<br>

Vamos salvar o componente e ir para suas configurações. Além de nomear e selecionar o domínio necessário, precisamos marcar a caixa `Restrict access` para que possamos definir permissões de segurança especiais para este componente.

Vamos salvar novamente, marcar o componente como pronto para publicação e adicioná-lo ao `Navigation menu` do domínio que estamos usando.

<br>

**Retorne ao componente `Car fleet` na página `Enter into a contract`**

Ainda há um botão não utilizado, `Back to all contracts`, vamos definir seu `Command type` no grupo de configurações `Actions` como `Navigation back`.

Em seguida, precisamos retornar ao fluxo de dados "Negócio concluído" e terminar de configurar a etapa `Form action`. A configuração final da etapa deve ser parecida com isto:

<br>

![Tutorial 2.26](../assets/images/tutorials/tut2.26.png)

<br>

**Não se esqueça de selecionar o `source step` na etapa `update entry`**.

Salve, publique o componente, adicione-o ao local de trabalho usando o `Navigation menu` e assegure-se de que todos os componentes estejam no lugar.

<br>

### Configurando acesso ao componente `Managers grid`

Você precisa ir ao menu "Acesso" na seção "Permissões" e clicar no botão "Adicionar" no canto superior direito.

Uma janela de configurações de permissão será aberta na sua tela, onde você precisa especificar o domínio e dar um nome para a permissão. Para conceder acesso para manipular o componente `Managers grid`, vá para `Permissions`, entre na seção `Components`, encontre nosso componente `Managers grid` e selecione direitos de acesso total para ele. Clique no botão "Salvar" e prossiga para a próxima seção "Funções".

Aqui você também precisa clicar no botão "ADICIONAR", selecionar o domínio necessário, nomeá-lo e selecionar a "Permissão" que você criou anteriormente. Em seguida, prossiga para a seção `Users`.

Na seção `Users`, todos os usuários registrados em seu sistema estão listados. Clique no usuário ao qual você deseja conceder direitos para usar este componente, em "Selecionar contextos" escolha "Plataforma" -> "Sistema" e em "Selecionar funções" encontre a função que você criou anteriormente, em seguida, clique na caixa de seleção e clique em "Salvar".

<br>

### Conclusão

Você criou um aplicativo pequeno e simples no qual trabalhou com vários componentes e aprendeu como vinculá-los. Você aprendeu a criar janelas modais e começou a explorar a interação entre linguagens de programação e as ferramentas da nossa plataforma.

Tente criar vários gerentes, adicionar novos carros à venda, atribuir gerentes a eles e tentar fechar negócios.
Claro, esta aplicação é um teste; pode ser melhorada e tornada mais complexa infinitamente. Após criá-la, você pode usar outras ferramentas por conta própria, construir lógica diferente e personalizar o design ao seu gosto. A plataforma oferece ferramentas flexíveis que tornam o desenvolvimento mais empolgante e fácil!

As descrições das ferramentas usadas no tutorial podem ser encontradas na seção "Desenvolvimento de Aplicações".