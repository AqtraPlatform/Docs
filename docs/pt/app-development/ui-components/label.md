# Rótulo

![](../../assets/images/app-development/label.png)

## Informações gerais
O rótulo é um componente básico da interface do usuário projetado para exibir campos de texto não editáveis em capturas de tela. Este componente é amplamente utilizado para adicionar texto descritivo, títulos ou simplesmente exibir informações que o usuário não pode alterar.

## Parâmetros
**Propriedades do Componente:**

| Grupo de configurações | Campo de Configuração | Opções de Valor         | Propósito |
|-----------------------|-----------------------|-------------------------|-----------|
| (Configurações globais) | Nome                  | -                       | Nome do Componente da UI no sistema |
| Texto                 | Tamanho da fonte      | -                       | Tamanho da fonte |
|                       | Cor                   | -                       | Cor do texto (CSS) |
|                       | Negrito               | true, false             | Fonte em negrito |
|                       | Itálico               | true, false             | Fonte em itálico |
|                       | Alinhamento de texto  | Esquerda, Direita, Centro, Justificar | Alinhamento do texto |
| Comum                 | Vinculação            | Multiseleção de Catálogo | Vinculação a Dados |
|                       | Valor                 | -                       | Valor do campo estático |
|                       | Formato               | -                       | Formato de entrada/saída de dados (Para DataHora) |

**Propriedades CSS:**

| Grupo de configurações | Campo de Configuração | Opções de Valor         | Propósito |
|-----------------------|-----------------------|-------------------------|-----------|
| Layout                | Alinhar itens         | Nenhum, Centro, Fim, Início, Esticar | Alinhamento de elementos em um contêiner flexível |
|                       | Largura               | -                       | Largura do componente |
|                       | Altura                | -                       | Altura do componente |
|                       | Crescer               | true, false             | Esticar um componente em um contêiner |
|                       | Margem                | -                       | Preenchimento externo |
|                       | Preenchimento         | -                       | Preenchimento interno |
| Aparência             | Raio de Canto         | -                       | Raio do canto |
|                       | Espessura da Borda    | -                       | Espessura da borda |
| Pincel                | Fundo                 | -                       | Cor de fundo |
|                       | Pincel da Borda       | -                       | Cor da borda |

## Casos
- **Dicas de Informação**: Usar um rótulo para fornecer informações de apoio ao lado de outros elementos da interface do usuário, como explicar as funções de botões ou dados de entrada.
- **Títulos de Seção**: Rótulos podem servir como títulos para diferentes seções da interface, delineando claramente o conteúdo para melhorar a experiência do usuário.
- **Exibição de Status**: Em casos onde é necessário exibir o status ou resultado de uma operação, um rótulo pode ser usado para mostrar as mensagens correspondentes (por exemplo, “Carregando...”, “Concluído com sucesso”).

## Exceções
- **Não Editabilidade**: O rótulo não é destinado à entrada do usuário ou edição de texto. Tentar usá-lo para esses fins resultará em um design de interface ineficaz.
- **Restrições de Formato**: Embora o rótulo permita um certo nível de personalização de texto, ele não pode conter elementos de texto complexos, como hyperlinks ou imagens inline.