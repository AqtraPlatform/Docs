# SVG

![](../../assets/images/app-development/svg.png)

## Informações gerais
SVG (Scalable Vector Graphics) é um componente para integrar gráficos vetoriais em interfaces de usuário. Ele permite exibir imagens, tornando-o ideal para ícones, diagramas e ilustrações complexas.

## Parâmetros
**Propriedades do componente**

| Grupo de configurações | Campo de configuração | Opções de valor | Propósito |
| --- | --- | --- | --- |
|  | Nome | - | Nome do Componente de UI no sistema |
| Comum | Vinculação | Multiseleção de Catálogo | Contém um campo “Arquivo” relacionado do modelo |
|  | Arquivo | Botão | Permite fazer o upload de um arquivo com extensão .svg |

**Propriedades CSS**

| Grupo de configurações | Campo de configuração | Opções de valor | Propósito |
| --- | --- | --- | --- |
| Layout | Largura | - | Largura do componente |
|  | Altura | - | Altura do componente |
|  | Crescer | true, false | A propriedade determina quanto um elemento crescerá em relação aos outros elementos flex dentro do mesmo contêiner |
|  | Margem | - | A propriedade define os preenchimentos externos em todos os quatro lados do elemento |
|  | Preenchimento | - | A propriedade define os preenchimentos internos em todos os lados do elemento |
| Aparência | RaioDeCanto | - | A propriedade é usada para arredondar os cantos de um elemento |
|  | EspessuraDaBorda | - | A propriedade permite definir os limites para o elemento |
| Pincel | Fundo | - | A propriedade define a cor de fundo do elemento |
|  | PincelDaBorda | - | A propriedade define a cor da borda do elemento |

## Casos de Uso
- **Ícones e Ilustrações**: Usado para adicionar elementos gráficos claros e escaláveis.

## Exceções
- **Desempenho**: Imagens SVG complexas ou grandes podem afetar o desempenho da página da web.