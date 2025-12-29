# Exportar para Arquivo

![](../../assets/images/app-development/export-to-file.png)

## Informações gerais
A etapa “Exportar para Arquivo” é utilizada para exportar dados do modelo interno Dataflow para um arquivo estruturado. Esta etapa suporta a criação de arquivos nos formatos CSV, Excel e JSON, permitindo transferir e distribuir dados processados de forma eficiente.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de Origem       | -                | Selecionar de etapas anteriores para a fonte de dados |
| Tipo de arquivo de saída | Csv, Excel, JSON | Formato do arquivo de exportação |
| Nome do arquivo       | -                | Nome do arquivo de exportação |
| Separador de coluna   | ; (padrão)       | Separador de arquivo CSV (padrão ";") |
| Nome da planilha (Se o tipo de arquivo de entrada = Excel) | - | Nome da planilha no arquivo Excel |
| Mapeamento de campos   | -                | Mapeamento dos campos do modelo Dataflow e da estrutura do arquivo |

## Casos
- **Distribuição de Dados**: Ideal para criar relatórios, distribuir informações para clientes ou parceiros e transferir dados entre diferentes sistemas ou departamentos.
- **Arquivamento de Dados**: Pode ser utilizado para armazenar informações importantes em um formato estruturado e facilmente acessível.
- **Integração com outros sistemas**: Permite preparar dados para integração ou processamento subsequente por outros sistemas que suportam os formatos CSV, Excel ou JSON.

## Exceções
- **Compatibilidade de formato de arquivo**: É importante ajustar as configurações de exportação para garantir que os arquivos gerados sejam compatíveis com as expectativas e requisitos dos usuários finais ou sistemas.
- **Otimização de desempenho para grandes volumes de dados**: Ao exportar grandes volumes de dados, é necessário considerar o desempenho e possíveis restrições de tamanho de arquivo (padrão 1 MB).

## Cenário de aplicação

O componente criado serve como uma ferramenta para exportar dados do sistema. Ele inclui várias etapas, como buscar o modelo de dados, filtrar e exportar para um arquivo Excel. O usuário pode personalizar a filtragem de dados antes da exportação e baixar os resultados em um formato conveniente usando o botão na interface do usuário.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1haTgN7Qyu6rD3GSYcDKPEMu3V_KcOdVt/view?usp=sharing).