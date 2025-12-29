# Componente

Componentes são os principais blocos de construção na plataforma, fornecendo a base para a construção de aplicações. Eles são unidades encapsuladas de funcionalidade que podem incluir dados, interface do usuário, lógica de negócios e automação de processos.

## Tipos de Componente

1. **Componente Único**:

   - Contém o modelo de objeto básico para armazenar dados.
   - Inclui um modelo de UI com formulários e controles.
   - Possui um modelo de automação com fluxos de dados e fluxos de trabalho.
   - Suporta scripts Python para personalização de comportamento adicional.
   - Possui opções de segurança exclusivas.

2. **Multi-Componente**:
   - Combina múltiplos Componentes para criar aplicações complexas.
   - É usado para construir uma única interface de usuário, por exemplo, em aplicações móveis.

## Criando um Novo Componente

1. Abra o Studio ('https://<your-hosting-name>/studio').
2. Vá para o menu Aplicações/Componentes.
3. Clique no botão Adicionar para criar um novo componente ou multi-componente.

## Configurações Básicas do Componente

| Parâmetro         | Descrição                                                          |
| ----------------- | ------------------------------------------------------------------ |
| `Title`           | O nome do componente que é exibido para os usuários.                |
| `Proxy Mode`      | Determina se o componente atuará como um proxy.                    |
| `Restrict Access` | Restringe o acesso ao componente.                                   |
| `Maker`           | Identifica o criador ou proprietário do componente.                  |
| `Cron`            | Configurando o horário de início de um componente usando Cron.      |
| `Run as User`     | Especifica o usuário em nome de quem será executado.              |
| `Access Mode`     | Define o modo de acesso ao componente.                             |
| `Description`     | Uma descrição detalhada do componente, seu propósito e funções.    |
| `Domains`         | Os domínios ou categorias aos quais o componente pertence.          |

## Modelo de Objeto do Componente na Plataforma

Cada componente na plataforma inclui automaticamente os seguintes campos:

- 'Id': Um identificador único do componente.
- 'creatorSubject': O sujeito que criou o objeto.
- 'updateSubject': O sujeito que atualizou o objeto.
- 'createdDate': Data em que o objeto foi criado.
- 'updateDate': Data em que o objeto foi atualizado pela última vez.

Os componentes podem incluir elementos adicionais, que podem pertencer a um dos onze tipos: 'string', 'datetime', 'catalog', 'number', 'integer', 'array', 'file', 'boolean', 'time', 'date', 'uri'. Cada um desses elementos tem suas próprias configurações.

Configurações globais para todos os tipos:

- 'Name': Nome do sistema da propriedade.
- 'Title': Nome da propriedade a ser exibido na interface.
- 'Required': Especifica se o campo é obrigatório.
- 'Primary Key': Determina se um campo é um identificador único.
- 'Query': Determina se o campo pode ser usado em consultas.
- 'Virtual property': Exclui um campo dos processos de sincronização.

## Construtor de Interface

A plataforma oferece uma ferramenta poderosa para personalizar a interface do usuário para cada componente – o Construtor de Interface. É um editor visual que permite criar e personalizar interfaces de usuário multi-componentes usando recursos de arrastar e soltar. O Construtor de Interface é um espaço de trabalho na seção de Definição da Interface de Criação de Componentes.

Nesta seção, você pode:

- Criar uma interface de aplicativo multi-tela usando um editor intuitivo de arrastar e soltar.
- Adicionar elementos de UI das categorias Básica, Avançada e Layout.
- Configurar o modelo de objeto para o Fluxo de Trabalho e Fluxo de Dados da aplicação.
- Personalizar estilos CSS para todos os elementos de UI.

Depois de adicionar elementos de UI ao layout da página do seu aplicativo, você pode realizar as seguintes operações:

- **Copiar:** Copia o elemento atual para a área de transferência.
- **Colar:** Cola o item copiado em um novo local.
- **Mover:** Altera a posição do elemento.
- **Propriedades:** Abre o painel de propriedades para configurar o elemento.
- **Pré-visualização:** Mostra o layout em um formato que se aproxima da aplicação do usuário.
- **Pré-visualização de Marcação:** Exibe a marcação textual da página.
- **Excluir:** Exclui o elemento selecionado.
- **Campo de Dados:** Permite vincular um elemento a um campo de dados (link de banco de dados).

## Módulo de partes da Web: “Estilos” e “JavaScript”

O bloco “Estilos” é projetado para descrever os estilos CSS que são aplicados ao componente, enquanto o bloco “JavaScript” permite estabelecer interação com a interface do usuário e fornecer funcionalidade adicional usando a linguagem JavaScript.

Dessa forma, o módulo de Partes da Web permite que os desenvolvedores criem componentes mais complexos e interativos usando diferentes linguagens de programação para descrever estilos e funcionalidades.<br>

### Usando "JavaScript"

Exemplo de uso do JavaScript para implementar funcionalidade para criar botões, pressionar os quais tira uma captura de tela:

1. Para chamar funções JavaScript do bloco 'Partes da Web', é necessário usar o método context.InvokeInterop(methodName, objects) dentro do script do Componente:

````python
def capturePage1():
    context.InvokeInterop("callScreenshot")

2. Next, we move to the 'JavaScript' section of the 'Web parts' block and prepare function:
```javascript
// Criando um elemento <script> para carregar a biblioteca html2canvas
var script = document.createElement('script');
script.src = "https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js";
document.head.appendChild(script);

// Função para criar e baixar uma captura de tela da página
function takeScreenshot() {
    // Capturing a screenshot of the entire body using html2canvas
    html2canvas(document.body).then(canvas => {
        // Creating a link for downloading the screenshot
        var link = document.createElement('a');
        link.href = canvas.toDataURL("image/png");
        link.download = "screenshot.png";
        // Adding the link to the HTML document and simulating a click to download the screenshot
        document.body.appendChild(link);
        link.click();
        // Removing the link from the document after the screenshot has been downloaded
        document.body.removeChild(link);
    });
}

// Método para chamar a função takeScreenshot
this.callScreenshot = () => {
    takeScreenshot();
}

Este código cria um elemento de script que carrega a biblioteca html2canvas de uma Rede de Distribuição de Conteúdo (CDN). Após carregar a biblioteca, uma função takeScreenshot() é definida, que captura uma captura de tela da página atual usando html2canvas.

Após criar a captura de tela, o código cria um elemento <a> para possibilitar o download, define seu href para a URL da imagem em formato PNG e o atributo de download para screenshot.png. Em seguida, adiciona este link ao corpo do documento, emula um clique neste link para baixar a captura de tela e, finalmente, remove o link do documento.

### Usando "Estilos"

Exemplo de código CSS que define a cor de fundo de todo o seu espaço de trabalho

```css
body {
    background-color: violet; /* Purple background color */
}
```

## Construção de Fluxo de Dados e Fluxo de Trabalho {: #dataflow-workflow }

O modelo de objeto de cada Componente contém dados que são usados tanto dentro do próprio Componente quanto nos processos de sua integração com outros elementos do sistema. Esses dados servem como base para configurar e executar fluxos de dados e fluxos de trabalho.

Para começar a construir um Fluxo de Dados ou Fluxo de Trabalho, você precisa arrastar um dos elementos de "Fluxos" para a área do construtor de interface, após o que você poderá personalizar o editor visual do fluxo de dados e do fluxo de trabalho.

Saiba mais sobre [Componentes de Fluxo de Dados](data-flow-components/index.md) e [Componentes de Fluxo de Trabalho](workflow-components/index.md)

## Publicando um Componente e Transferindo-o para a Interface da Web {: #publication }

- Após terminar de configurar o componente, você deve publicá-lo como parte de uma nova publicação.
- O gerenciamento de publicações é descrito em [Publicando Aplicações](publishing-applications.md).
- Em seguida, você precisa voltar ao menu 'Início' e ir para o 'menu de navegação' do 'domínio de aplicação' desejado, clicar em 'Adicionar item de menu', selecionar o componente desejado, preencher os parâmetros e clicar em 'Salvar'.

![Menu de navegação](../assets/images/app-development/navigation-menu.png)