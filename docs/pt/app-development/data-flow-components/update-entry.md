# Atualização de entrada

![](../../assets/images/app-development/update-entry.png)

## Informações gerais

A etapa “Atualização de Entrada” é usada para criar, atualizar ou excluir uma entrada existente no sistema. Esta etapa é executada diretamente, e o sistema aguarda sua conclusão. Se um erro ocorrer durante a execução, a execução do fluxo de dados será interrompida.

## Parâmetros

**Configurações da Etapa:**

| Campo de Configuração   | Opções de Valor | Propósito                                      |
| ----------------------- | --------------- | ---------------------------------------------- |
| Nome da etapa           | -               | Nome da etapa                                 |
| Etapa de origem         | -               | Selecionando a etapa anterior                  |
| Componente              | -               | Componente a ser atualizado                    |
| Chave do campo componente| -              | Campo com a chave do componente a ser atualizado |
| Marcar entrada para exclusão | true, false | Marca de exclusão da entrada                   |
| Campo de nome           | -               | Nome do campo a ser atualizado                 |
| Campo de armazenamento do resultado | -     | Campo para salvar o resultado da operação      |
| Mapeamento de campos    | -               | Mapeamento de campos entre o fluxo de dados e o componente |

## Casos

- **Atualização de Dados**: Usado para atualizar informações nas entradas existentes dos componentes do sistema para garantir que os dados sejam precisos e atualizados.
- **Exclusão de uma Entrada**: A etapa “Atualização de Entrada” pode ser usada para excluir entradas existentes no sistema. Isso é especialmente relevante em scripts onde você precisa remover informações desatualizadas ou incorretas para manter os dados no sistema precisos e atualizados. Por exemplo, isso pode incluir a exclusão da conta de um usuário que deixou a organização ou a remoção de itens indisponíveis do inventário. É importante notar que a etapa pode ser configurada para marcar a entrada para exclusão, o que permite gerenciar o processo de exclusão de forma mais flexível.

## Exceções

- **Dependência da Presença de um ID de Instância**: Para atualizar dados com sucesso, o ID da instância do componente deve ser recebido e transmitido primeiro.
- **Gerenciamento de Erros em Tempo de Execução**: Qualquer erro durante o processo de atualização de dados interromperá o fluxo de dados, o que requer monitoramento cuidadoso do tratamento de erros e exceções.

## Cenário de aplicação

O componente apresenta um cenário para adicionar, editar e excluir registros de componentes usando a etapa "Atualização de entrada".

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1k1oMpI2YSF-P3zgsd2cORfRjFs3l7w0o/view?usp=sharing)