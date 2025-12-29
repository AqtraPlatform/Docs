# Armazenamento de entrada sobre o barramento

![](../../assets/images/app-development/store-entry-over-bus.png)

## Informações gerais

A etapa “Armazenamento de Entrada sobre o Barramento” é projetada para armazenar o modelo nos dados do componente (campos) via o barramento. Esta etapa sempre cria uma nova instância do componente especificado e é usada para trabalhar dinamicamente com os dados no sistema. A etapa é chamada de forma assíncrona.

## Parâmetros

**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor       | Propósito                                                                             |
| --------------------- | --------------------- | ------------------------------------------------------------------------------------- |
| Nome da etapa         | -                     | Nome da etapa                                                                        |
| Etapa de origem       | -                     | Seleção da etapa anterior                                                             |
| Componente            | -                     | Seleção entre os componentes disponíveis para salvar a entrada                       |
| Nome                  | String                | Nome do sistema da entrada a ser exibida usando links do tipo Catálogo              |
| Chaves                | ADICIONAR CHAVE       | Para componentes com a flag Restringir acesso, especificando as chaves para mapear os campos |
| Campo de chave        | Multiseleção de Catálogo | Campos contendo as chaves primárias do componente selecionado                        |
| Mapeamento de campos  | -                     | Configurando dinamicamente o mapeamento dos modelos de componente para o modelo de fluxo de dados |

## Casos

- **Criando Novas Instâncias de Componentes**: Usado para criar automaticamente novas entradas em componentes com base nos dados no fluxo de dados.

## Exceções

- **Dependência da Disponibilidade de Chaves Primárias no Componente**: A eficácia da etapa depende da disponibilidade e correção das chaves primárias no componente de destino, especialmente se o componente tiver a flag Restringir acesso.
- **Requisito de Processamento Assíncrono**: A etapa é realizada de forma assíncrona, o que pode afetar a sequência e o tempo de processamento do sistema.

## Cenário de aplicação

Este componente permite recuperar dados da integração selecionada e armazená-los nos campos correspondentes dos modelos de dados criados. Os dados recuperados podem então ser usados em outras partes do sistema para processamento ou exibição adicional.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1jFuXBG8v-YuICBozvoCPAm0FfBQhApvG/view?usp=sharing)