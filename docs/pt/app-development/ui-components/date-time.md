# Data / Hora

![](../../assets/images/app-development/date-time.png)

## Informações gerais
Data/Hora é um componente de UI para inserir e exibir data e hora. Ele é projetado para fornecer uma interface amigável para selecionar a data/hora, bem como para exibir esses dados em um formato específico.

## Parâmetros
**Propriedades do Componente:**

| Grupo de configurações | Campo de Configuração | Opções de Valor         | Propósito                 |
|-----------------------|----------------------|-------------------------|---------------------------|
| (Configurações globais) | Nome                 | -                       | Nome do Componente de UI no sistema |
| Data Hora             | Formato              | Data, Hora, Data & Hora | Formato de Exibição       |
|                       | Valor padrão         | -                       | Valor padrão              |
|                       | Data mínima          | -                       | Data Mínima              |
|                       | Data máxima          | -                       | Data Máxima               |
| Comum                 | Vínculo              | -                       | Vínculo aos Dados         |
|                       | Obrigatório          | true, false             | Obrigatório preencher      |

**Propriedades CSS:**

| Grupo de configurações | Campo de Configuração | Opções de Valor         | Propósito                 |
|-----------------------|----------------------|-------------------------|---------------------------|
| Layout                | Largura              | -                       | Largura do componente     |
|                       | Altura               | -                       | Altura do componente      |
|                       | Margem               | -                       | Preenchimento externo      |
|                       | Preenchimento        | -                       | Preenchimento interno      |
| Aparência             | Raio de Canto        | -                       | Raio do canto             |
|                       | Espessura da Borda   | -                       | Espessura da borda        |
| Pincel                | Fundo                | -                       | Cor de fundo              |
|                       | Pincel da Borda      | -                       | Cor da borda              |

## Casos
- **Seleção de Data do Evento**: Usado para selecionar uma data no calendário ou para definir a hora do evento.
- **Filtrar por Data**: Pode ser usado em filtros para filtrar dados por data/hora.
- **Exibir Intervalos de Tempo**: Adequado para tarefas que envolvem exibir intervalos de tempo, como em agendadores de tarefas.

## Exceções
- **Formatação**: Data/Hora não é destinado à entrada de texto livre, mas é usado estritamente para trabalhar com datas e horas.