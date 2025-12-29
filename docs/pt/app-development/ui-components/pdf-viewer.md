# Visualizador de PDF

![](../../assets/images/app-development/pdf-viewer.png)

## Informações gerais
O componente Visualizador de PDF permite que você visualize e interaja com documentos PDF diretamente na interface do usuário. Este componente é útil para exibir arquivos PDF, como relatórios, instruções e outros documentos.

## Parâmetros
**Propriedades do componente**

| Grupo de configurações | Campo de configuração | Opções de valor | Propósito |
| --- | --- | --- | --- |
|  | Nome | - | Nome do Componente de UI no sistema |
| Comum | Vínculo | Multiseleção de Catálogo | Contém um campo “Arquivo” relacionado do modelo |
|  | Arquivo | Botão | Permite que você faça o upload de um arquivo com extensão .pdf |

**Propriedades CSS**

| Grupo de configurações | Campo de configuração | Opções de valor | Propósito |
| --- | --- | --- | --- |
| Layout | Largura | - | Largura do componente |
|  | Altura | - | Altura do componente |
|  | Crescer | true, false | A propriedade determina o quanto um elemento irá crescer em relação aos outros elementos flex dentro do mesmo contêiner |
|  | Margem | - | A propriedade define os preenchimentos externos em todos os quatro lados do elemento |
|  | Preenchimento | - | A propriedade define os preenchimentos internos em todos os lados do elemento |
| Aparência | RaioDeCanto | - | A propriedade é usada para arredondar os cantos de um elemento |
|  | EspessuraDaBorda | - | A propriedade permite que você defina os limites para o elemento |
| Pincel | Fundo | - | A propriedade define a cor de fundo do elemento |
|  | CorDaBorda | - | A propriedade define a cor da borda do elemento |

## Casos
- **Visualização de Relatórios:** Permite que os usuários visualizem relatórios e documentação em formato PDF.

## Exceções
- **Limitações de Formato:** O Visualizador de PDF suporta documentos PDF padrão, mas pode não exibir corretamente formatos complexos ou documentos protegidos.
- **Desempenho:** O uso de documentos PDF grandes ou um grande número de elementos interativos pode afetar o desempenho.