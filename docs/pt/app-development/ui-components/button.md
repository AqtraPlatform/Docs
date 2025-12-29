# Botão

![](../../assets/images/app-development/button.png)

## Informações gerais
Um Botão é o principal componente de interface do usuário usado para executar comandos ou iniciar ações em uma aplicação. Ele pode ser configurado para executar processos, confirmar ações do usuário ou servir como uma ferramenta de navegação.

## Parâmetros
**Propriedades do Componente:**

| Grupo de configurações | Campo de Configuração | Opções de Valor         | Propósito |
|-----------------------|-----------------------|-------------------------|-----------|
| (Configurações globais) | Nome                  | -                       | Nome do Componente de UI no sistema |
| Comum                 | Ícone                 | -                       | Carregamento de ícone (.svg) |
|                       | Desativado            | true, false             | Desativando um elemento |
|                       | Rótulo                | -                       | Texto do botão |
| Texto                 | Tamanho da fonte      | -                       | Tamanho da fonte |
|                       | Cor                   | -                       | Cor do texto (CSS) |
|                       | Negrito               | true, false             | Fonte em negrito |
|                       | Itálico               | true, false             | Fonte em itálico |
|                       | Alinhamento do texto  | Esquerda, Direita, Centro, Justificado | Alinhamento do texto |
| Ações                 | Tipo de comando       | Vários comandos         | Ação ao clicar no botão |
|                       | Restringir acesso     | true, false             | Limitação de acesso |

**Propriedades CSS:**

| Grupo de configurações | Campo de Configuração | Opções de Valor         | Propósito |
|-----------------------|-----------------------|-------------------------|-----------|
| Layout                | Largura               | -                       | Largura do componente |
|                       | Altura                | -                       | Altura do componente |
|                       | Crescer               | true, false             | Estiramento do componente |
|                       | Margem                | -                       | Preenchimento externo |
|                       | Preenchimento         | -                       | Preenchimento interno |
| Aparência             | Raio de Canto         | -                       | Raio dos cantos |
|                       | Espessura da Borda    | -                       | Espessura da borda |
| Pincel                | Fundo                 | -                       | Cor de fundo |
|                       | Pincel da Borda       | -                       | Cor da borda |

## Casos
- **Envio de Formulário**: Usando um botão para enviar dados de formulário para o servidor ou para iniciar o processamento de dados de formulário na aplicação.
- **Navegação**: Atribuição de um botão para navegar entre diferentes telas ou seções da aplicação.
- **Elementos Interativos**: Criação de botões para controlar elementos interativos, como mudar o conteúdo em uma página.

## Exceções
- **Limitações no Número de Ações**: Apenas uma ação pode ser atribuída a um botão (executar fluxo de dados, executar script, etc.).