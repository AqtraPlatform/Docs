# Tutorial №1

<br>

## Criando Sua Primeira Aplicação — Inventário de Faturas

<br>

**Descrição da Aplicação: Inventário de Faturas**

Vamos criar uma aplicação simples que permite adicionar, visualizar e editar faturas.

Cada fatura conterá os seguintes dados (veja a tabela abaixo).

| Breve Descrição      | Descrição Detalhada                                         |
| -------------------- | ------------------------------------------------------------ |
| Número da Fatura     | Número atribuído à fatura pelo fornecedor.                   |
| Título da Fatura     | Descrição do item da fatura.                                |
| Valor Total da Fatura| Número indicando o valor em dinheiro cobrado na fatura.    |
| Data de Vencimento   | Data em que a fatura deve ser paga.                         |

<br>

Além disso, iremos acompanhar o status da fatura da seguinte forma (veja a tabela abaixo).

| ID  | Título Legível       | Descrição                                                                          |
| --- | -------------------- | ------------------------------------------------------------------------------------ |
| 0   | Em Revisão          | Atribuído imediatamente após a criação da fatura.                                   |
| 1   | Aceito para Pagamento| Atribuído após a revisão e aprovação da fatura para pagamento.                      |
| 2   | Rejeitado            | Atribuído após a revisão ser concluída, mas a fatura não é aceita para pagamento.   |
| 3   | Pago                 | Atribuído após a fatura ser paga.                                                  |
| 4   | Atrasado             | Indica que a fatura está não paga e a data de vencimento passou.                   |

<br>

A versão básica da aplicação terá 2 telas principais.

- Uma lista de todas as faturas no sistema, que pode ser filtrada e/ou ordenada usando todos os campos de fatura descritos acima. Vamos chamá-la de “Todas as Faturas”.
- Uma tela para adicionar uma nova fatura ou editar uma fatura existente. Vamos chamá-la de “Editar/Visualizar Fatura”.

Após a criação, a aplicação terá a aparência da captura de tela abaixo.

<br>

![Tutorial 1](../assets/images/tutorials/tut1.png)

<br>

## Abrindo o Estúdio

Criar uma aplicação na plataforma começa com a abertura do Estúdio e a adição de um componente.

Você pode abrir o Estúdio usando o link https://<seu_nome_de_hospedagem>/studio/.

Por exemplo, se o nome de domínio onde você implantou sua instância da plataforma é [my.platform.io](http://my.platform.io/), você pode acessar o Estúdio usando a seguinte URL: “[https://my.platform.io/studio/”](https://my.platform.io/studio/%E2%80%9D).

Após fazer login no Estúdio, você verá a seguinte tela com um menu à esquerda listando Início, Aplicações e Acesso. Selecione Aplicações→Componentes.

<br>

![Tutorial 2](../assets/images/tutorials/tut2.png)

<br>

Você verá uma lista de todos os componentes existentes. Clique no botão “Adicionar” e selecione a opção “Componente”, conforme mostrado abaixo.

<br>

![Tutorial 3](../assets/images/tutorials/tut3.png)

<br>

Parabéns, você agora tem seu primeiro componente! Vamos nomeá-lo de “Inventário de Faturas” e definir alguns parâmetros importantes.

Para nomear seu componente, clique no botão “Configurações” e coloque “Inventário de Faturas” no campo “Nome”.

Como nossa aplicação só será acessível a pessoas com as credenciais de login apropriadas, precisamos garantir que o campo “Modo de Acesso” esteja definido como “Privado”.

## Configurando Campos de Dados Necessários

Clique em Salvar para garantir que seu componente seja salvo. Ele mostrará uma mensagem de erro porque ainda não temos dados em nosso componente. Vamos adicionar alguns dados.
Vá para a aba "Definição" e clique no sinal "+" ao lado de "Inventário de Faturas". A plataforma adicionará automaticamente vários campos de sistema que você vê na captura de tela, bem como seu primeiro campo de dados — Property_1.

<br>

![Tutorial 4](../assets/images/tutorials/tut4.png)

<br>

Clique no ícone de edição (lápis) em Property_1. Você verá um novo painel abrir à direita. É aqui que você define como seus campos de dados devem ser interpretados pelo sistema.
Nome — este é o nome interno do sistema para o seu campo de dados (propriedade). Deve conter apenas letras em inglês, sem espaços. Você usará este nome mais tarde, por exemplo, em scripts Python para adicionar alguma lógica avançada à aplicação.

_Nota: a partir da versão 0.4.x, há também uma propriedade do sistema “name” que é adicionada automaticamente quando a primeira propriedade é criada e é usada quando você precisa mostrar aos usuários valores para usuários ao usar propriedades do tipo Catálogo (link para outro componente; usado para relacionamentos 1:1 e M:1) ou Array (link para um array de outros componentes; usado para relacionamentos 1:M e M:M). Ao contrário do Nome interno do sistema, que está presente para cada propriedade dentro do componente, o campo de sistema name é um para todo o componente._

Título — este é o nome que seu campo de dados terá na interface do usuário. Aqui você pode usar quaisquer caracteres que precisar.

Para campos de dados que devem sempre ser não vazios, certifique-se de que a caixa de seleção “Obrigatório” esteja marcada.

O Tipo de Propriedade permite que você selecione um dos tipos de campo de dados disponíveis.

Para começar, adicionaremos o campo de dados Nome da Fatura e definiremos o tipo de propriedade como String. Como os nomes das faturas teoricamente vêm de fornecedores externos, eles podem se repetir, então não definimos a flag de Chave Primária aqui.

<br>

![Tutorial 5](../assets/images/tutorials/tut5.png)

<br>

Uma vez que terminamos de configurar nosso primeiro campo, vamos clicar em Salvar.

Agora vamos adicionar os outros campos que precisaremos em nossa aplicação: número da fatura, data de vencimento da fatura, valor total da fatura e status da fatura.

**Número da Fatura** é o número de conta interno de cada fatura única, que geralmente corresponde ao nome da fatura, mas garantiremos que tenha pelo menos 2 caracteres de comprimento definindo o valor de Comprimento Mínimo como 2, conforme mostrado abaixo. Ele também deve ser único para distinguir diferentes faturas, mesmo que tenham os mesmos nomes, então definimos a flag de Chave Primária. Isso informa à plataforma que não pode haver mais de uma propriedade Número da Fatura com o mesmo valor. Se uma tentativa for feita para criar um valor duplicado, o sistema dará um erro.

<br>

![Tutorial 6](../assets/images/tutorials/tut6.png)

<br>

Para a data de vencimento da fatura esperada, defina o tipo de Propriedade como DateTime.

<br>

![Tutorial 7](../assets/images/tutorials/tut7.png)

<br>

O valor total da fatura deve ser definido como um número. Também definiremos o campo Valor Mínimo como 0 para garantir que não haja faturas negativas (isso pode ser diferente em uma aplicação financeira real onde valores negativos são usados, por exemplo, para representar créditos de fornecedores).

<br>

![Tutorial 8](../assets/images/tutorials/tut8.png)

<br>

Finalmente, adicionaremos o campo “Status da Fatura”. Como declarado na descrição da aplicação, este será um conjunto de status que deve ser conforme segue:

0|Em Revisão  
1|Aceito para Pagamento  
2|Rejeitado  
3|Pago  
4|Atrasado  

Para isso, precisamos definir o tipo de propriedade como Inteiro (a partir da versão 0.5.24 e acima) e marcar a caixa de seleção Enum. Em seguida, precisamos adicionar todos os status disponíveis no formato <Número>|<Nome>, conforme mostrado abaixo.

<br>

![Tutorial 9](../assets/images/tutorials/tut9.png)

<br>

Clique em “Salvar”. Você deve ver o modelo de dados totalmente configurado, conforme mostrado abaixo.

<br>

![Tutorial 10](../assets/images/tutorials/tut10.png)

<br>

## Configurando a Interface para Nossa Aplicação

Agora precisamos configurar a interface do usuário para nossa aplicação. Como descrito acima, precisaremos de 2 telas:

1. Uma tela para adicionar uma nova fatura ou editar uma fatura existente. Vamos chamá-la de “Adicionar/Visualizar Fatura”.
2. Uma lista de todas as faturas no sistema, que pode ser filtrada e/ou ordenada usando todos os campos de fatura descritos acima. Vamos chamá-la de “Todas as Faturas”.

## Configurando a Página Adicionar/Visualizar Fatura

Já temos uma página padrão adicionada automaticamente chamada “Página Principal” acima.

Na versão atual da plataforma, a primeira página do componente por padrão é usada como um formulário para visualizar e editar dados do componente quando não há um formulário explícito para visualização e edição. Por exemplo, no nosso caso, o controle de interface do usuário Data Grid que usaremos para a página Todas as Faturas abrirá por padrão a primeira página do nosso componente.
Usaremos também a primeira página para o formulário de visualização e edição da nossa fatura, e para isso, renomearemos de Página Principal para Adicionar/Visualizar Faturas. Para fazer isso, clique em Página Principal e altere o nome na caixa de diálogo que se abre (campos Nome e Título).

O resultado ficará como mostrado abaixo.

<br>

![Tutorial 11](../assets/images/tutorials/tut11.png)

<br>

Em seguida, para criar a visualização de dados e o formulário de edição, arraste os campos de dados (propriedades) da esquerda para a área do meio na mesma ordem que na grade de dados mostrada acima.

Os resultados devem ficar assim.

<br>

![Tutorial 12](../assets/images/tutorials/tut12.png)

<br>

Clique no botão Salvar. Agora vamos adicionar uma página para visualizar todas as faturas.

## Configurando a Página de Todas as Faturas

Para fazer isso, abra os Componentes de UI no painel direito, selecione Layout, clique em Página e arraste para a área do meio logo acima do nosso formulário de visualização de faturas. Uma página chamada Nova página 1 deve ser adicionada automaticamente, como mostrado abaixo.

<br>

![Tutorial 13](../assets/images/tutorials/tut13.png)

<br>

Vá para a Nova página 1 clicando no botão com o mesmo nome e renomeie para Todas as Faturas.

Clique em Salvar. Na lista de Componentes de UI à direita, selecione Layout, em seguida, selecione Página e arraste para a área do meio. Depois, vá para a seção Avançado e arraste o elemento DataGrid para o painel recém-criado. Você verá o resultado como mostrado abaixo.

<br>

![Tutorial 15](../assets/images/tutorials/tut15.png)

<br>

Clique no ícone de Configurações (engrenagem) no canto superior direito do novo elemento DataGrid e selecione Comum no painel direito. Você verá a seleção do componente para exibir dados nesta grade de dados. Selecione Inventário de Faturas.

<br>

![Tutorial 16](../assets/images/tutorials/tut16.png)

<br>

Em seguida, selecione o ícone “+” ao lado do rótulo “Colunas” 5 vezes (já que temos 5 campos de dados que queremos exibir aqui).

<br>

![Tutorial 17](../assets/images/tutorials/tut17.png)

<br>

Agora, para cada coluna, clique na área da coluna. Uma nova caixa de diálogo aparecerá para configurar a coluna.

Para cada coluna, você precisará definir o cabeçalho com o nome da coluna (por exemplo, “Número da Fatura,” “Nome da Fatura,” etc.).

Você também precisa definir a opção “Mostrar Cabeçalho” como “Ativado.”

Se as opções “Classificável” e/ou “Filtrável” estiverem definidas como “Ativado,” você habilitará a classificação e filtragem dinâmicas (semelhante ao que é feito no Excel, por exemplo).

Finalmente, você precisa clicar no botão “Adicionar campo” e selecionar o campo de dados apropriado para exibir nesta coluna.

O exemplo abaixo mostra a configuração para o campo “Número da Fatura.” As outras colunas são configuradas de forma semelhante.

<br>

![Tutorial 18](../assets/images/tutorials/tut18.png)

<br>

Depois de configurar todas as colunas, vá para Ações no formulário à direita e certifique-se de que a opção “Mostrar botão de adicionar” esteja selecionada. Isso permitirá adicionar novas faturas através deste DataGrid.

Além disso, defina o Tipo de Comando como “Editar Registro” para que possamos visualizar/editar qualquer fatura na lista clicando nela.

Veja a ilustração abaixo para os resultados.

<br>

![Tutorial 19](../assets/images/tutorials/tut19.png)

<br>

Clique no botão Salvar.

## Adicionando Botões de Ação e Fluxo de Dados para Salvar Dados

Depois de criarmos as visualizações de dados e os formulários de edição, precisamos adicionar lógica para salvar os dados do formulário no banco de dados e permitir que os usuários acionem isso.

Para fazer isso, precisamos fazer duas coisas.

1. Adicionar botões que usaremos para salvar os dados do formulário ou cancelar todas as alterações e retornar à lista de Todas as Faturas.
2. Para salvar os dados do formulário, adicionaremos um fluxo de trabalho simples que pegará os dados do formulário e os salvará no banco de dados.

<br>

## Adicionar Botões Salvar e Retornar a todas as faturas

<br>

Clique em “Caixa de Ferramentas”, selecione o campo “Botão” na seção “Básico” e arraste o botão para a área do meio da tela. Defina o título do botão como Salvar. Para fazer isso, vá para a seção Comum e, no campo Valor de Tradução, escreva Salvar.

Adicione outro botão e defina o título como “Voltar para todas as faturas.” O resultado deve ficar como a imagem abaixo.

<br>

![Tutorial 20](../assets/images/tutorials/tut20.png)

<br>
Agora faremos com que o botão “Voltar para todas as faturas” mude a interface para a aba principal “Todas as Faturas”. Para fazer isso, no menu Configurações para o botão inferior, selecione “Ações” e defina o “Tipo de Comando” como “Abrir Página” e a “Página do Componente” como “Todas as Faturas.” Clique em Salvar.

<br>

![Tutorial 21](../assets/images/tutorials/tut21.png)

<br>

## Adicionando Fluxo de Dados para Salvar

Para fazer com que o botão Salvar no aplicativo salve os dados inseridos como uma fatura, precisamos adicionar um fluxo de dados.

Clique em “Caixa de Ferramentas”, selecione o campo “Fluxo de dados” na seção “Fluxo” e arraste-o para a área do meio da tela. Um novo fluxo de dados com o nome padrão “Fluxo de dados 1” aparecerá, acessível através do botão com o mesmo nome no menu de configurações do componente principal, à direita do botão Fluxo de Dados de Entrada. Clique no botão Fluxo de dados 1 e renomeie seu fluxo de dados para Salvar.

O resultado deve ser parecido com isto.

<br>

![Tutorial 22](../assets/images/tutorials/tut22.png)

<br>

Em seguida, clique no botão "+ ADICIONAR ETAPA", depois "Adicionar passo" e selecione o passo "Obter modelo de ação". Adicione outro passo e selecione "Atualizar entrada", depois vá para as configurações deste passo. Você pode ler mais sobre este passo na seção "Fluxo de dados". Configure o passo como mostrado abaixo:

<br>

![Tutorial 23](../assets/images/tutorials/tut23.png)

<br>

![Tutorial 24](../assets/images/tutorials/tut24.png)

<br>

Em seguida, adicione o passo "Escrever resposta", especifique o passo de origem em suas configurações e salve o componente.

Depois disso, no menu Configurações para o botão Salvar, selecione Ações e defina o Tipo de Comando como Executar fluxo de dados, e escolha seu novo Salvar na lista.

Clique no botão Salvar. O resultado deve ser parecido com isto.

<br>

![Tutorial 25](../assets/images/tutorials/tut25.png)

<br>
 
Clique em Salvar e Pronto para publicar. Seu novo componente foi criado e está pronto para ser publicado.

<br>

## Publicando e Testando Seu Aplicativo

Você está agora pronto para publicar e testar seu aplicativo.

Para publicar seu aplicativo, clique no botão Pronto para publicar dentro do seu componente, depois vá para Estúdio→Aplicações→Publicação. Selecione seu componente Inventário de Faturas na lista de componentes disponíveis para publicação e clique no botão Publicar.

Você pode então usar o botão Ver App dentro do seu Estúdio (nem sempre disponível), ou ir para a URL <your-host-name> para ver seu aplicativo em ação.

Preencha os detalhes da fatura e clique em Salvar. Em seguida, clique no botão “Voltar para todas as faturas”. Sua primeira fatura será salva, e você verá a lista de todas as faturas disponíveis.