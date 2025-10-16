# Render template

![](../../assets/images/app-development/render-template.png)

## General information
The “Render Template” step is used to create documents, especially in PDF format, using data from Dataflow and templates available in the system. The step allows you to convert data into professionally designed documents, which is widely used in the generation of reports, contracts, invoices, and other official documents.

## Parameters
**Step Settings:**

| Setting Field  | Value Options  | Purpose |
|-----------------|--------------------|------------|
| Step name       | -                  | Name of the step |
| Source step     | - | Selecting from previous steps for data source |
| Template        | - | Selection from the available templates to create a document |
| Render type     | text, HTML, Docx, Xlsx, PDF | Format of the document to be generated |
| File name       | -                  | Name of the generated file |
| Fields mapping  | -                  | Mapping fields between a template and a data model |

## Cases
- **Generation of Formalized Documents**: Especially useful for automated generation of official documents such as reports, invoices, and contracts, by applying preset templates.
- **Content Personalization**: Allows you to create personalized documents for customers or users using data specific to each case, such as personalized offers or customized reports.
- **Preparation for Document Distribution**: Used to create documents that can then be made available to users for downloading or sent via email.

## Exceptions
- **Requirement for the Quality and Accuracy of Templates**: The quality of the resulting documents is directly related to the accuracy and professionalism of the templates used.
- **Need for Follow-Up to Distribute Documents**: Once a document is generated, a follow-up step, such as “Form Action” with “Download file” option, is often required to make the document available to users.

## Application scenario

This component utilizes several steps to create and download a PDF file. First, the data model is fetched, then the PDF template is rendered. The Form action step is configured to download the file, specifying the data field containing file information. After the Write Response step, the generated file is sent to the frontend for downloading.

- You can download the component configuration [here](https://drive.google.com/file/d/1Omst72osc9qf1FtxQcIohdARDzqwDKHT/view?usp=sharing).