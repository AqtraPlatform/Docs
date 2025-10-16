# Export to File

![](../../assets/images/app-development/export-to-file.png)

## General information
The “Export to File” step is used to export data from the internal Dataflow model to a structured file. This step supports the creation of files in CSV, Excel and JSON formats, allowing you to efficiently transfer and distribute processed data.

## Parameters
**Step Settings:**

| Setting Field       | Value Options | Purpose |
|----------------------|-------------------|------------|
| Step name            | -                 | Name of the step |
| Source Step          | - | Selecting from previous steps for data source |
| Output file type     | Csv, Excel, JSON  | Export file format |
| File name            | -                 | Export file name |
| Column separator     | ; (default)       | CSV file separator (default ";") |
| Worksheet name (If Iput file type = Excel)       | -                 | Sheet name in Excel file |
| Fields mapping       | -                 | Mapping Dataflow model fields and file structure |

## Cases
- **Data Distribution**: Ideal for creating reports, distributing information to clients or partners, and transferring data between different systems or departments.
- **Data Archiving**: Can be used to store important information in a structured and easily accessible format.
- **Integration with other systems**: Allows you to prepare data for subsequent integration or processing by other systems that support CSV, Excel or JSON formats.

## Exceptions
- **File format compatibility**: It is important to fine-tune export settings to ensure that the generated files are compatible with the expectations and requirements of end users or systems.
- **Optimizing performance for large volumes of data**: When exporting large volumes of data, you need to consider performance and possible file size restrictions (default 1 MB).

## Application scenario

The created component serves as a tool for exporting data from the system. It includes several steps such as fetching the data model, filtering, and exporting to an Excel file. The user can customize data filtering before exporting and download the results in a convenient format using the button on the user interface.

- You can download the component configuration [here](https://drive.google.com/file/d/1haTgN7Qyu6rD3GSYcDKPEMu3V_KcOdVt/view?usp=sharing).