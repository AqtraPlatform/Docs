# Menu Inicial

<br>

A página fornece informações sobre sua licença e os domínios de aplicação que foram implantados. Você terá acesso aos seguintes recursos e informações:

- **Tipo de Plano**: Isso exibe o tipo do seu plano atual e a data de expiração ou renovação da sua assinatura.
- **Domínios de Aplicação**: Esta seção permite que você crie componentes de aplicação, conecte usuários via URLs específicas e navegue até a seção “Menu de Navegação”.
- **Estatísticas de Uso**: Exibe informações sobre o número atual de aplicações em comparação com o limite total, bem como o número atual e total de usuários, fluxos de trabalho e fluxos de dados.
  <br>

![Painel principal](../assets/images/user-interface/main-dashboard.png)
<br>

## Saiba mais sobre a configuração de domínios de aplicações

Os domínios de aplicação são espaços externos com uma URL específica (HTTP/HTTPS://<seu-nome-de-domínio>) onde você pode implantar seus componentes.

**Por padrão, um aplicativo está disponível** chamado ‘digital-workplace’. Você pode adicionar mais aplicativos usando o botão ‘Adicionar aplicação’ no canto superior direito da barra de ferramentas. Cada aplicativo que você adicionar aparece na lista de aplicativos sob a descrição do seu plano.

No domínio da aplicação, os seguintes parâmetros podem ser configurados nas ‘configurações principais’:

| Grupo de Configurações | Campo de Configuração | Opções de Valor                                   | Propósito                                               |
| ---------------------- | --------------------- | ------------------------------------------------- | ------------------------------------------------------ |
| Configurações principais| Título                | -                                                 | Título da Aba do Navegador                             |
|                        | Ocultar barra superior | true, false                                       | Ocultar o menu superior para o local de trabalho       |
|                        | Menu estático         | true, false                                       | Exibição constante de menus ou exibição ao passar o mouse |
|                        | Ocultar breadcrumbs    | true, false                                       | Mostrar/ocultar navegação hierárquica                  |
|                        | Ocultar login do usuário| true, false                                       | Mostrar/ocultar login do usuário                        |
|                        | Ocultar local         | true, false                                       | Mostrar/ocultar seleção de localização                  |
|                        | Escolher logo         | Logo, Logo pequeno, favicon, "Sem imagem" placeholder | Escolhendo um logo para o WorkPlace (tipos diferentes) |
|                        | Armazenamento de Sessão do Usuário | local/session                             | Salvando parâmetros de autorização em uma sessão ou localmente |
|                        | Provedor Idp padrão   | Multiseleção de Catálogo                          | Escolhendo um Método de Autorização                    |
|                        | Localização padrão    | Multiseleção de Catálogo                          | Localização padrão                                     |
|                        | Aplicativo de informações do usuário padrão | Multiseleção de Catálogo              | Aplicativo principal para gerenciar dados do usuário    |
|                        | Componente padrão     | Multiseleção de Catálogo                          | Componente Padrão                                      |
|                        | Página padrão         | -                                                 | Página do componente padrão                             |
|                        | Componente de login    | Multiseleção de Catálogo                          | Componente do formulário de autorização                 |
|                        | Habilitar SIP         | True, False                                       | Construindo integração com SIP                          |

<br>
Neste grupo, você pode definir as configurações de módulos globais via JavaScript e CSS, o que permite transformar a plataforma em um sistema de gerenciamento de conteúdo (CMS), além de fazer upload e usar quaisquer bibliotecas de terceiros.

Exemplo de JS para JavaScript global:

```javascript
loadScript([
  'https://code.jquery.com/jquery-3.7.1.min.js?integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo=&crossorigin="anonymous"',
])
  .then((res) => {
    return loadScript([
      'https://code.jquery.com/ui/1.13.2/jquery-ui.min.js?integrity="sha256-lSjKY0/srUM9BE3dPm+c4fBo1dky2v27Gdjm2uoZaL0="&crossorigin="anonymous"',
    ]);
  })
  .subcribe({
    complete: () => {
      console.log("Load scripts complete");
    },
    error: (err) => {
      console.log("Load scripts err:" + err);
    },
  });
```

<br>

Além disso, há um grupo de configurações de ‘configurações de estilo’:

| Grupo de configurações | Campo de configuração        | Propósito              |
| ---------------------- | --------------------------- | ---------------------- |
| Fonte principal        | Fonte                       | Fonte principal do app |
| Esquema de cores      | Tema padrão                 | Esquema de cores padrão |
|                        | Cor clara primária          | Cor clara principal    |
|                        | Cor primária                | Cor principal          |
|                        | Cor escura primária         | Cor escura principal   |
|                        | Cor mais escura primária    | Cor mais escura principal |
|                        | Cor do texto primário       | Cor do texto padrão    |

<br>

Grupo de configurações ‘Editar manifesto’:

| Campo de configuração   | Propósito                         |
| ----------------------- | --------------------------------- |
| Nome                    | Nome do app no manifesto          |
| Nome curto              | Nome curto do app                |
| Escolher ícone (192x192)| Escolhendo um ícone de app 192x192px |
| Escolher ícone (512x512)| Escolhendo um ícone de app 512x512px |

<br>

## Integração SIP

Se a opção ‘Habilitar SIP’ dentro das ‘Configurações principais’ estiver habilitada, várias configurações subsequentes são necessárias para que as chamadas do local de trabalho funcionem corretamente.

**Do lado do estúdio:**

| Campo de configuração   | Propósito                                                               |
| ----------------------- | ----------------------------------------------------------------------- |
| Servidor SIP WebSocket  | Endereço do servidor SIP WebSocket (ex.: 'wss://test-pbx.aqtra.ru:8089/ws') |
| Domínio SIP             | Escopo SIP (domínio)                                                   |

<br>

**Do lado do local de trabalho:**

| Campo de configuração   | Propósito                                                               |
| ----------------------- | ----------------------------------------------------------------------- |
| Nome de usuário SIP     | Nome do usuário SIP                                                    |
| Senha do usuário SIP    | Senha do usuário SIP                                                  |
| Servidor SIP WebSocket  | Endereço do servidor SIP WebSocket (ex.: 'wss://test-pbx.aqtra.ru:8089/ws') |
| Domínio SIP             | Escopo SIP (domínio)                                                   |

<br>

Se todos os parâmetros estiverem configurados corretamente, você poderá fazer chamadas do local de trabalho. Você pode ler sobre como trabalhar com SIP dentro do script do componente aqui: [Usando Python](../app-development/using-python.md).