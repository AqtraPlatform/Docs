# Descrições de lançamento

!!! note "A Plataforma Aqtra está em constante evolução!"
Novas versões são normalmente lançadas uma vez por mês para:

    - Cluster Kubernetes
    - Mini-imagem Docker

<br>

## Versão 0.13.x

> **Funcionalidade Adicionada**

- **Novo Módulo de Componente**: Dentro do componente, o módulo **Web parts** foi adicionado, que consiste em dois blocos: “Estilos” e “JavaScript”. Este módulo é semelhante ao módulo “Component Script”, mas em vez de interagir com Python, você pode descrever estilos CSS no bloco “Estilos” e interagir em JavaScript no bloco “JavaScript”;
- **Configuração de Módulos Globais no domínio da Aplicação**: A configuração de módulos CSS e JavaScript globais foi adicionada nas **Configurações principais** do **domínio da Aplicação**. Mais detalhes **aqui**;
- **Novas Ferramentas no Menu de Manutenção**: Uma configuração foi adicionada para a seção **Armazenamento de arquivos**. Mais detalhes **aqui**;
- **Novas Configurações do Modelo de Objeto para Dados de Tipo de Arquivo**: Agora você pode definir validação por tipo de arquivo e limite de tamanho de arquivo em bytes;
- **Suporte a XSRF/CSRF**: O componente de upload de arquivos agora elimina a transferência de dados binários via JS e adiciona o envio de XSRF. As solicitações para download de arquivos agora são direcionadas e o acesso direto ao armazenamento de arquivos é excluído. Melhorias também foram feitas no local de trabalho para receber um token XSRF ao carregar uma página, e o controlador OData foi aprimorado para carregar arquivos. O envio de solicitações do local de trabalho para baixar arquivos agora também é direcionado, e o acesso direto ao armazenamento de arquivos é impossível.
  <br>

> **Design Atualizado**

- **Seção Exportar/Importar**: O design da seção de exportação/importação do menu **Aplicações** foi atualizado.
  <br>

## Versão 0.12.x

> **Funcionalidade Adicionada**

- **Enviar Notificação**: Um novo passo no Dataflow “Enviar notificação” foi adicionado. Este passo permite enviar notificações simples ao usuário, o que melhora a forma como você interage com o usuário através do sistema de notificações. Mais detalhes aqui: **Enviar notificação**
- **Pivot Grid**: Um novo elemento de UI “Pivot Grid” foi adicionado para análise e visualização de dados. Mais detalhes aqui: **Pivot grid**
- **Mudanças na **Visualização de Lista**:
  - Capacidade de expandir o componente horizontal ou verticalmente.
  - A capacidade de habilitar Drag & Drop foi adicionada para todos os grupos de um componente ou por escolha.
  - A função de habilitação foi adicionada a Eventos após o uso de Drag & Drop.
- **Mudanças na **Grade de Dados**:
  - O mecanismo de multiseleção foi alterado. Nas configurações da Grade de Dados agora há uma opção “Modo de Seleção” com a escolha: `None`, `Single`, `Multiple`, `Checkbox`.
  - Novos eventos: `On Table Changed`, `On Header Changed`, `On Row Changed`, `On Cell Changed`.
  - Capacidade de selecionar o número de linhas no paginador na frente.
- **Mudanças na **Visualização de Gráfico**:
  - A configuração do Esquema de Cores foi removida.
  - Configurações de Min/Max foram adicionadas.
- **Integração do Cliente SIP**:
  - Capacidade de fazer chamadas do Local de Trabalho graças à integração do cliente SIP. Mais detalhes **aqui**.
- **Imagens de espaço reservado para imagens ausentes nas configurações de domínios de aplicação e no elemento de UI "Imagem"**: Mais detalhes na [documentação da Interface do Usuário](user-interface/index.md) e [componente de Imagem](app-development/ui-components/image.md).
- **Novos métodos para gerenciar o estado dos elementos de UI**. Mais detalhes na **documentação**.
- **Upload em Massa de Imagens Via http.client e Armazenamento de Arquivos em scripts de Dataflow**: Uma função para upload em massa de imagens foi adicionada. Mais detalhes na **documentação**.
- **Otimização do Mecanismo de Publicação**: O mecanismo de publicação foi aprimorado usando uma máquina de estados, proporcionando um processo estável com a capacidade de reverter em caso de erros. Mais detalhes na **documentação**.

<br>

## Versão 0.10.x

> **Funcionalidade Adicionada**

- Um novo passo de dataflow “Obter informações do arquivo” foi criado, permitindo que você obtenha informações sobre um arquivo pelo seu identificador. Mais detalhes na documentação: **Obter informações do arquivo**
- Adicionado um filtro para o campo “Componente” dentro do passo de dataflow “Obter entidade por id”. Mais detalhes aqui: **Obter entidade por id**  
  <br>

> **Atualização de Design**

- Página principal “Dashboard”. Mais detalhes aqui: **Dashboard**
- O “menu de navegação” foi removido do menu “Aplicações” e agora está localizado na página principal. Mais detalhes aqui: **Menu de navegação**
- O design dos passos de dataflow foi atualizado. Mais detalhes aqui: **Passos de Dataflow disponíveis**
- O design do “armazenamento de arquivos” foi atualizado. Mais detalhes aqui: **Armazenamento de arquivos**
- O design da “manutenção do sistema” foi atualizado. Mais detalhes aqui: **Manutenção do sistema**
  <br>

## Versão 0.9.x

> **Funcionalidade Adicionada**

- Recursos específicos do sistema (específicos da plataforma)
  - Carregamento da interface do usuário: otimização da compilação de componentes de UI.
  - Refatoração do **Menu de Manutenção**. Movendo botões de controle para a aba “Manutenção do Sistema” e exibindo logs com suas configurações na aba “Logs do Sistema”.
  - Gerador de armazenamento de fila de trabalho no Redis.
  - IronPython foi atualizado da versão 2.7.12 para 3.4.1 no Local de Trabalho.
- Recursos específicos do usuário (específicos do estúdio) - Copiar/colar elementos no **construtor de interface** na página do componente. - Adicionando arquivos à raiz do [armazenamento de arquivos](user-interface/file-storage.md). - Capacidade de usar o Modelo de Dados dos componentes de referência (Catálogo) na barra de ferramentas do elemento do componente para: `DataGrid`, `ListView`, `TreeView`.
  <br>

> **Mudanças na Interface**

- Refatoração do menu principal do estúdio:
  - movendo os seguintes elementos para o canto direito da barra de ferramentas superior: switch de localização e botão para sair da conta atual (logout),
  - o item Perfil do menu principal foi removido.
- O ícone do item de menu Módulos Python foi redesenhado.
- Ícones de ajuda online foram adicionados em muitas seções do Estúdio: passos de dataflow, botões para elementos da interface do usuário (Toolbox UI), principais parâmetros da aplicação, bem como em muitos outros locais no estúdio para garantir um acesso mais rápido à ajuda online no site de documentação.  
  <br>

> **Correções de bugs principais**

- Correção do `Cron` operação do agendador de tarefas durante a importação/exportação de componentes.
- Eliminação do `changeAuthor` duplicado do modelo de dados do componente.
- Estabilização da seleção de passos de workflow.
- Correção do `Number` elemento de UI do painel de elementos do componente.
- Correção da operação do evento On focus para alguns dos elementos de UI: Dia, Hora, Assinatura.
  <br>

## Versão 0.8.x

> **Funcionalidade Importante e Melhorada Adicionada**

- No passo de Ação de Formulário do dataflow, os parâmetros Open Sidebar e Open Modal foram adicionados, que permitem abrir uma barra lateral e uma janela modal, respectivamente, semelhante ao que pode ser feito via script Python.
- Transferência dos atributos necessários para parâmetros transferidos no passo Get Action Model.
- O passo de dataflow “Remover funções atribuídas ao usuário” foi adicionado, que remove todas as funções atuais atribuídas ao usuário, permitindo que você crie um novo conjunto de funções do zero.
- O menu **Módulos Python** foi adicionado para gerenciar a biblioteca compartilhada de módulos Python.
- Configuração de fundo para controles de UI foi adicionada, que permite definir uma imagem em formatos padrão (por exemplo, png, svg, jpeg, etc.) como fundo para todos os controles que têm uma seção de configurações de Brush.
- O ícone de visualização do modelo de dados no passo de dataflow foi alterado para o ícone de olho.
- O parâmetro “Pular da Sincronização” foi substituído por Propriedade Virtual. Campos marcados como “Propriedade Virtual” não são salvos no banco de dados quando o componente é gravado.
- Configurações para Aplicação Web Progressiva (PWA) na seção Editar manifesto foram adicionadas.
- Configurações adicionais do Domínio da Aplicação foram adicionadas - mostrar breadcrumbs, login, localidade.
  <br>

> **Erros Importantes Corrigidos**

- O funcionamento de filtros dinâmicos para o controle de Grade de Dados foi corrigido.
- O “Campo da primeira linha a ignorar” no passo de Importar Arquivo não é redefinido para 0 após a gravação.
- A cor padrão para o domínio da aplicação se aplica a controles do tipo botão que não têm uma cor padrão definida.
- Permissões para um multicomponente não são definidas no modo de acesso restrito.
  <br>

## Versão 0.7.0

> **Funcionalidade Importante e Melhorada Adicionada**

- Ao selecionar um componente padrão para um domínio de aplicação na seção Configurações Principais, você pode selecionar a página que será aberta para este componente no campo Página Padrão. Se nenhuma página for selecionada, a primeira página do componente (página principal) será aberta por padrão.
- Um novo passo “Executar Dataflow” foi adicionado ao dataflow, que permite lançar novos dataflows, incluindo dataflows de outros componentes, dentro do dataflow atual.
- O desatualizado passo de dataflow “Obter Público” foi removido, e o passo “Ação de Formulário” foi movido para o grupo “Transformação de Modelo”. O grupo “Outros” foi removido completamente.
- A busca para configurar “Mapeamento de Campos” foi adicionada para o passo “Aplicar operações de atualização diferida”.
- Para o controle de UI **Área de Texto**, uma opção de Auto-tamanho foi adicionada, que permite expandir o tamanho do campo se você precisar inserir uma quantidade maior de texto.
- O passo de dataflow “Consultar Entidade por Filtro” foi otimizado através da criação automática de índices e normalização do banco de dados.
- Aviso de expiração iminente da licença foi adicionado. A mensagem aparece 10 dias antes da data de expiração da licença atual.
- APIs Swagger geradas para Dataflow agora mostram o nome do Dataflow como o nome da API.
- A capacidade de solicitar a geolocalização do usuário a partir do Script do Componente através da função context.PlatformServices.GeolocationPosition foi adicionada.
- A capacidade de definir a configuração de localidade padrão para o domínio da aplicação foi adicionada na seção Configurações Principais.
- A capacidade de definir um favicon para o domínio da aplicação foi adicionada nas configurações do Menu Inicial: Domínio: Configurações Principais.
  <br>

> **Erros Importantes Corrigidos**

- O funcionamento de filtros dinâmicos para o controle de Grade de Dados foi corrigido.
- Um problema onde um erro ocorreu ao classificar campos recuperados de links do tipo Catálogo foi corrigido.
- A estabilidade da grade de dados, incluindo erros fantasmas ao navegar pela Grade de Dados, foi melhorada.
- Um problema com o formulário de busca sendo cortado na Grade de Dados ao clicar em um filtro foi corrigido.
- A saída de valores de string para Enum foi adicionada.
- O funcionamento incorreto do sistema com logout remoto foi corrigido.
- O funcionamento incorreto do temporizador no passo “Aplicar operações de atualização diferida” foi corrigido.
- Para controles de UI do tipo Rótulo, vinculados a um campo do tipo Catálogo, a configuração de Cor agora é processada corretamente.
  <br>

## Versão 0.6.x

> **Funcionalidade Importante e Melhorada Adicionada**

- Recursos avançados para gerenciar o menu principal da aplicação - construção de menus hierárquicos e configuração de ícones de menu.
- Melhor trabalho com scripts Python - destaque para a sintaxe Python, autocompletar para métodos de sistema Python, bem como autocompletar e dicas para métodos de bibliotecas integradas da plataforma foram adicionados (disponíveis via Ctrl-Space no Win10/11, e Option-Space no MacOS).
- A capacidade de construir janelas laterais adicionais via Script do Componente foi adicionada.
- A capacidade de construir janelas modais complexas via Script do Componente com transferência de dados de janelas modais para o script chamador foi adicionada.
- A chamada do Script do Componente foi movida para o menu principal.
- A localização do Estúdio para o russo foi concluída.
- No controle DataGrid, agora é possível selecionar campos arbitrários de um componente externo ao exibir campos de referência do tipo Catálogo.
- A importação-exportação agora inclui a exportação e subsequente importação de permissões e funções (exportar arquivos criados usando a versão 0.6.x para versões anteriores funcionará, mas não importará funções e permissões incluídas).
- A importação-exportação agora verifica componentes relacionados e avisa o usuário se algum componente relacionado não foi incluído na lista de exportação.
- No nível da plataforma, a capacidade de marcar entradas (instâncias de componente) como disponíveis para exclusão física foi adicionada via uma flag no passo de dataflow “Atualizar Entrada”.
- A capacidade do administrador do Estúdio de obter uma lista de entradas marcadas para exclusão e remover aquelas que não têm links para entradas que não estão marcadas como prontas para exclusão foi adicionada.
  <br>

## Versão 0.5.24

> **Funcionalidade Importante e Melhorada Adicionada**

- Capacidades avançadas para filtros dinâmicos e estáticos em controles avançados como Grade de Dados, Visualização de Lista, Visualização em Árvore, permitindo filtragem de dados em tempo real antes da exibição ao usuário (parâmetros foram adicionados para filtros do tipo contém, etc.).
- Expansão do conceito de utilização de Dataflow & Workflow - agora ambos podem ser criados e usados separadamente de controles de UI como botões, o que permite uma estrutura de aplicação mais flexível e simplifica o desenvolvimento.
- Muitos novos métodos disponíveis via [Usando Python](app-development/using-python.md) no Script do Componente foram adicionados, como chamar janelas modais, verificar a resolução da tela e o tipo de dispositivo para criar um layout de UI responsivo.
- A capacidade de trabalhar com sistemas de filas de mensagens (por exemplo, RabbitMQ) a partir do dataflow com um novo passo [Inscrever-se no Conector](app-development/data-flow-components/subscribe-to-connector.md) foi adicionada.
- A capacidade de processamento em lote de dados no Dataflow via novos passos [Atualização Diferida de Entrada](app-development/data-flow-components/deferred-update-entry.md) & [Aplicar Operações de Atualização Diferida](app-development/data-flow-components/apply-deferred-update-operations.md) foi adicionada.
  <br>

## Versão 0.4.4

> **Funcionalidade Importante e Melhorada Adicionada**

- Novo campo de armazenamento do sistema “Nome” foi adicionado, usado para exibir itens de Catálogos.
  - Ao mostrar um único elemento do Catálogo (por exemplo, usando um controle de UI Selecionar que referencia o Catálogo), o conteúdo do campo Nome agora será sempre exibido. Se o campo Nome estiver vazio, o nome do Catálogo/s número de sequência da entrada do Catálogo será exibido.
- Configurações de ordenação padrão para Datagrid e Visualização de Lista foram adicionadas.
- Substituição automática de caracteres especiais Unicode no Script do Componente para geração de links foi adicionada.
  <br>

> **Erros Corrigidos**

- Funcionamento incorreto do paginador em relação à troca de várias tabelas em uma página foi corrigido.
- Função de Rolagem não funcionando em algumas partes do Estúdio foi corrigida.
  <br>

## Versão 0.3.223

_Cluster Kubernetes 0.3.223 | Mini-imagem Docker 0.2.118_

> **Funcionalidade Importante e Melhorada Adicionada**

- Novo passo de fluxo de dados “Enviar notificação com template” foi adicionado, que permite enviar uma notificação por e-mail usando um template especificado.
- Propriedade de transparência para componentes de UI.
- Suporte para autorização OAuth2 para solicitações HTTP foi adicionado. Agora você pode configurar a geração automática de tokens via OAuth para se conectar à API.
- O parâmetro “Armazenar resposta como arquivo” foi adicionado no passo “Executar chamada API” para permitir que você baixe um arquivo via API mediante solicitação.
- Os passos não geram mais um boletim informativo, agora geram um campo no modelo para uso posterior, como “Enviar notificação com template”.
  <br>

> **Erros Corrigidos**

- Erros ao trabalhar com o tipo Datetime no calendário foram corrigidos.
- UI no Estúdio e no Local de Trabalho foi corrigida.
- O estado Desativado para o componente de UI Radiobutton foi corrigido.
- Erros de localização foram corrigidos.
- A busca em Dropdown agora é insensível a maiúsculas e minúsculas.
- A operação de autorização, incluindo problemas de logout, foi corrigida. <br>