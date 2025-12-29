# Número de Telefone

![](../../assets/images/app-development/phone-number.png)

## Informações gerais

O Número de Telefone é um componente de UI projetado para inserir e exibir números de telefone. Este componente facilita a entrada de números de telefone, garantindo a formatação correta e a validação dos dados inseridos.

## Parâmetros

**Propriedades do componente**

| Grupo de configurações | Campo de configuração | Opções de valor          | Propósito                                                                               |
| ---------------------- | --------------------- | ------------------------ | --------------------------------------------------------------------------------------- |
|                        | Nome                  | -                        | Nome do Componente de UI no sistema                                                    |
| Comum                  | Desativado            | true, false              | A propriedade permite desativar um elemento no formulário                              |
|                        | Obrigatório           | true, false              | A propriedade torna o elemento obrigatório para ser preenchido antes de enviar o formulário |
|                        | Rótulo                | -                        | Contém a tabela de conteúdos do contêiner de texto                                    |
|                        | Vínculo               | Multiseleção de Catálogo | Contém um campo “String” relacionado do modelo                                         |
| Eventos                | Ao valor alterado     | -                        | Permite executar o script especificado após a alteração do valor do campo              |

**Propriedades CSS**

| Grupo de configurações | Campo de configuração | Opções de valor | Propósito                                                                                                                   |
| ---------------------- | --------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------- | --- | ------------ |
| Layout                 | Largura               | -                | Largura do componente                                                                                                      |
|                        | Altura                | -                | Altura do componente                                                                                                       |
|                        | Crescer               | true, false      | A propriedade determina o quanto um elemento crescerá em relação aos outros elementos flex dentro do mesmo contêiner       |
|                        | Margem                | -                | A propriedade define os preenchimentos externos em todos os quatro lados do elemento                                       |
|                        | Preenchimento         | -                | A propriedade define os preenchimentos internos em todos os lados do elemento                                             |
| Aparência              | Raio do Canto         | -                | A propriedade é usada para arredondar os cantos de um elemento                                                             |
|                        | Espessura da Borda    | -                | A propriedade permite definir os limites para o elemento                                                                   |
| Pincel                 | Fundo                 | -                | A propriedade define a cor de fundo do elemento                                                                           |
|                        | Pincel da Borda       | -                | A propriedade define a cor da borda do elemento                                                                           |     | Cor da borda |

## Casos

- **Validação de Formato de Número:** Usado para validar o número de telefone inserido para garantir que siga um formato nacional ou internacional específico.

## Exceções

- **Opções de Formatação Limitadas:** O recurso pode não suportar todos os formatos possíveis de números de telefone, especialmente variantes não padronizadas ou regionais.
- **Sensibilidade a Erros de Entrada:** A entrada inválida do usuário pode resultar em erros no processamento do número de telefone.