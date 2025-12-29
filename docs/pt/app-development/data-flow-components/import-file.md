# Importar arquivo

![](../../assets/images/app-development/import-file.png)

## Informações gerais
A etapa “Importar Arquivo” é usada para importar dados de arquivos .csv, Excel ou JSON. Os dados são importados linha por linha, mapeando para o formato descrito em “Mapeamento de Campos”. Para importar um arquivo, você deve carregar o arquivo no campo do tipo Arquivo e especificar este campo no parâmetro "Campo de Informações do Arquivo".

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Selecionando a etapa anterior |
| Campo de informações do arquivo | -       | Campo contendo o arquivo a ser importado |
| Tipo de arquivo de entrada | .csv, .xlsx, .json | Formato do arquivo para importação |
| Separador de colunas  | ;                | Separador de colunas para arquivo CSV |
| Primeiras linhas a ignorar | 0           | Número de primeiras linhas a ignorar no arquivo |
| Mapeamento de campos   | -               | Mapeamento dos campos do componente para as colunas do arquivo |

## Casos
- **Importar Dados Tabulares**: Usado para carregar dados de arquivos CSV ou Excel, personalizando o mapeamento entre as colunas do arquivo e os campos do componente.
- **Importar Dados Estruturados**: Adequado para importar arquivos JSON contendo dados estruturados.

## Exceções
- **Mapeamento de Campos Incorreto**: Erros na configuração de “Mapeamento de Campos” podem resultar em importação de dados incorretos.
- **Ignorar Linhas Não Informativas**: Você deve especificar exatamente o número de linhas a serem ignoradas antes de começar a importar dados.

## Cenário de aplicação

Este componente é uma interface para upload de arquivos nos formatos **CSV** e **XLSX**. Ele inclui campos para três campos do modelo de dados **CSV** e três campos do modelo de dados **XLSX**, além de um campo para upload de arquivo. Dois fluxos de dados são usados para importação de arquivos, execução de scripts e armazenamento de dados.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/10P0-XqSZOKV7wZzg8uH6NR1VnxZ0-8RB/view?usp=sharing)