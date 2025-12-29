# Render template

![](../../assets/images/app-development/render-template.png)

## Informações gerais
A etapa “Render Template” é utilizada para criar documentos, especialmente em formato PDF, utilizando dados do Dataflow e templates disponíveis no sistema. A etapa permite converter dados em documentos profissionalmente projetados, amplamente utilizados na geração de relatórios, contratos, faturas e outros documentos oficiais.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor  | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Selecionar de etapas anteriores para a fonte de dados |
| Template              | -                | Seleção entre os templates disponíveis para criar um documento |
| Tipo de renderização   | text, HTML, Docx, Xlsx, PDF | Formato do documento a ser gerado |
| Nome do arquivo       | -                | Nome do arquivo gerado |
| Mapeamento de campos  | -                | Mapeamento de campos entre um template e um modelo de dados |

## Casos
- **Geração de Documentos Formalizados**: Especialmente útil para a geração automatizada de documentos oficiais, como relatórios, faturas e contratos, aplicando templates predefinidos.
- **Personalização de Conteúdo**: Permite criar documentos personalizados para clientes ou usuários utilizando dados específicos de cada caso, como ofertas personalizadas ou relatórios customizados.
- **Preparação para Distribuição de Documentos**: Usado para criar documentos que podem ser disponibilizados para os usuários para download ou enviados por e-mail.

## Exceções
- **Exigência de Qualidade e Precisão dos Templates**: A qualidade dos documentos resultantes está diretamente relacionada à precisão e profissionalismo dos templates utilizados.
- **Necessidade de Acompanhamento para Distribuir Documentos**: Uma vez que um documento é gerado, uma etapa de acompanhamento, como “Form Action” com a opção “Download file”, é frequentemente necessária para tornar o documento disponível para os usuários.

## Cenário de aplicação

Este componente utiliza várias etapas para criar e baixar um arquivo PDF. Primeiro, o modelo de dados é recuperado, em seguida, o template PDF é renderizado. A etapa de ação do formulário é configurada para baixar o arquivo, especificando o campo de dados que contém as informações do arquivo. Após a etapa Write Response, o arquivo gerado é enviado para o frontend para download.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1Omst72osc9qf1FtxQcIohdARDzqwDKHT/view?usp=sharing).