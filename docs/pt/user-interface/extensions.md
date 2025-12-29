# Menu de Extensões
<br>

O menu consiste em 2 blocos:
- **Modelos**
- **Configurações SMTP**
<br>

## Modelos

Modelos são usados para envio de e-mails e notificações de usuários e podem ser utilizados apenas na etapa ‘Enviar Notificação Modelada’. Os modelos são configurados na seção ‘Aplicativo/Modelos’.
<br>

### Adicionando/Removendo Modelos

- Para **adicionar um novo modelo**, clique no botão ‘ADICIONAR’. 
- Para **excluir um modelo**, clique na cruz na lista comum de todos os modelos.
<br>

### Configurando o modelo de componente do template

Ao adicionar ou editar um Modelo, você deve definir uma estrutura de Modelo de Objeto que interaja com Dataflow e/ou Workflow. Isso é feito definindo um conjunto de propriedades para cada um deles, semelhante à configuração de qualquer componente.
<br>

### Personalizando o Layout e Conteúdo do Modelo

A plataforma utiliza o ‘DevExpress Report Designer’ para criar modelos. Esses modelos podem ser usados para enviar notificações ou criar documentos.

- Após criar um novo modelo, a janela de edição se abre. É aqui que você pode adicionar e personalizar elementos visuais ao seu modelo e fazer links para as propriedades do seu modelo.
<br>

## Configurações SMTP

O serviço de envio é utilizado para enviar notificações via SMTP.

Recomendações para uso de um servidor SMTP:

- **Durante o Desenvolvimento**: Recomenda-se usar um servidor SMTP corporativo ou serviços shareware como [sendinblue.com](http://www.sendinblue.com/). Evite usar um servidor pessoal para não cair em spam.
- **Para Uso Industrial**: É preferível usar um serviço SMTP corporativo ou comercial pago.

Configure as seguintes configurações para o serviço de envio:

| Campo de Configuração | Opções de Valor | Propósito |
| --------------------- | ---------------- | --------- |
| `Sender`     | -                | Nome do remetente padrão, por exemplo `sender@company.com` |
| `User name`     | -                | Login para o servidor SMTP, geralmente no formato `user@company.com`. |
| `Password`     | -                | Senha do servidor SMTP |
| `Host`     | -                | Endereço do servidor SMTP, por exemplo `http://smtp-relay.sendinblue.com/` |
| `Port`     | -                | A porta para o servidor SMTP depende do provedor, por exemplo 587 para sendinblue.com |
| `Enable SSL`     | `true`, `false` | Usando SSL para criptografar dados. ‘True’ é geralmente usado para servidores SMTP modernos. |

<br>

### Exemplo de uso de Modelo e SMTP

1. Crie e personalize um modelo.
2. Configure o SMTP para enviar e-mails.
3. No seu fluxo de trabalho, adicione a etapa ‘Enviar Notificação Modelada’.
4. Selecione o tipo de notificação SMTP e defina os parâmetros para envio de e-mail.
5. Escolha seu modelo e defina o tipo de renderização em HTML.

Após concluir essas etapas, seu fluxo de trabalho enviará um e-mail usando o modelo personalizado.