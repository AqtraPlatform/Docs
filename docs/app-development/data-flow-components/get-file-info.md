# Get file info

![](../../assets/images/app-development/get-file-info.png)

## General information
The “Get File Info” step in Dataflow is used to retrieve information about a file by its ID. This step provides access to various properties of the file, including its name, extension (type), size, date of updating, creation, author of the initial and updated file.

## Parameters
**Step Settings:**

| Setting Field | Value Options | Purpose |
|----------------|-------------------|------------|
| Step name      | -                 | Name of the step |
| Source step    | -                 | Selecting the previous step |
| Src field      | -                 | Field containing the file ID |
| Dst field name | -                 | Field where the information about the file will be recorded |

## Cases
- **File Information Extraction**: Used to obtain detailed information about a file, which can be useful for subsequent data processing or analysis.
- **Preparing Data for Additional Processing**: The obtained information about the file can be used in subsequent steps, such as “Execute Script” or “Filter Source”, to perform specific operations depending on the properties of the file.

## Exceptions
- **Dependency on the Accuracy of the Data Source**: The accuracy of the information obtained depends on the accuracy and relevance of the data in the source.
- **Limited Information**: The step provides only basic information about the file, and may not include some specific or additional data.
