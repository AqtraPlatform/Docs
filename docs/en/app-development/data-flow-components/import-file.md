# Import file

![](../../assets/images/app-development/import-file.png)

## General information
The “Import File” step is used to import data from .csv, Excel or JSON files. The data is imported line by line, mapping to the format described in “Fields Mapping”. To import a file, you should load the file into the File type field and specify this field in the "File Info Field" parameter.

## Parameters
**Step Settings:**

| Setting Field       | Value Options | Purpose |
|----------------------|-------------------|------------|
| Step name            | -                 | Name of the step |
| Source step          | -                 | Selecting the previous step |
| File info field      | -                 | Field containing the file to import |
| Input file type      | .csv, .xlsx, .json| File format for import |
| Column separator     | ;                 | Column separator for CSV file |
| First lines to ignore| 0                 | Number of first lines to ignore in the file |
| Fields mapping       | -                 | Mapping component fields to file columns |

## Cases
- **Import Tabular Data**: Used to load data from CSV or Excel files, customizing the mapping between file columns and component fields.
- **Import Structured Data**: Suitable for importing JSON files containing structured data.

## Exceptions
- **Incorrect Fields Mapping**: Errors in the “Fields Mapping” setting may result in incorrect data import.
- **Ignore Uninformative Rows**: You must specify exactly the number of rows to ignore before you start importing data.

## Application scenario

This component is an interface for uploading files in **CSV** and **XLSX** formats. It includes fields for three **CSV** data model fields and three **XLSX** data model fields, as well as one field for file upload. Two data flows are used for file import, script execution, and data storage.

- You can download the component configuration [here](https://drive.google.com/file/d/10P0-XqSZOKV7wZzg8uH6NR1VnxZ0-8RB/view?usp=sharing)
