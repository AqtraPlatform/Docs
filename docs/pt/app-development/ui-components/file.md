# Arquivo

![](../../assets/images/app-development/file.png)

## Informações gerais
O componente “Arquivo” fornece a capacidade de carregar e exibir arquivos na interface do usuário. Este componente é útil para fazer upload e visualizar diferentes tipos de arquivos, como imagens, documentos, arquivos compactados, etc.

## Parâmetros
**Propriedades do componente**

| Grupo de configurações | Campo de configuração | Opções de valor | Propósito |
| --- | --- | --- | --- |
|  | Nome | - | Nome do Componente de UI no sistema |
| Comum | Tamanho máximo do arquivo em bytes | - | A propriedade permite especificar o tamanho máximo do arquivo carregado em bytes |
|  | Aceitar arquivos |  | A propriedade permite especificar os arquivos que estão disponíveis para download |
|  | Somente leitura | true, false | Esta propriedade permite desabilitar o upload de arquivos para formulários |
|  | Desabilitado | true, false | A propriedade permite desabilitar um elemento no formulário |
|  | Obrigatório | true, false | A propriedade torna o elemento obrigatório para ser preenchido antes de enviar o formulário |
|  | Rótulo | - | Contém a tabela de conteúdos do contêiner de texto |
|  | Valor | - | - |
|  | Vínculo | Múltipla Escolha: Catálogo | Referência ao Catálogo do tipo de Arquivo |
| Eventos | Ao valor alterado | - | Permite executar o script especificado após a alteração do valor do campo |

**Propriedades CSS**

| Grupo de configurações | Campo de configuração | Opções de valor | Propósito |
| --- | --- | --- | --- |
| Layout | Largura | - | Largura do componente |
|  | Altura | - | Altura do componente |
|  | Crescer | true, false | A propriedade determina quanto um elemento crescerá em relação aos outros elementos flex dentro do mesmo contêiner |
|  | Margem | - | A propriedade define os preenchimentos externos em todos os quatro lados do elemento |
|  | Preenchimento | - | A propriedade define os preenchimentos internos em todos os lados do elemento |
| Aparência | Raio de Canto | - | A propriedade é usada para arredondar os cantos de um elemento |
|  | Espessura da Borda | - | A propriedade permite definir os limites para o elemento |
| Pincel | Fundo | - | A propriedade define a cor de fundo do elemento |
|  | Pincel da Borda | - | A propriedade define a cor da borda do elemento |

## Casos
- **Upload de Documentos**: Permite que os usuários façam upload de documentos, imagens e outros arquivos.
- **Visualizar Informações do Arquivo:** Exibe informações sobre o arquivo carregado, como seu nome e tamanho.

## Exceções
- **Desempenho**: O download de arquivos grandes ou de um grande número de arquivos pode afetar o desempenho.