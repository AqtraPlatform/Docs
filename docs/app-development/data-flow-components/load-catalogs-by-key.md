# Load catalogs by key

![](../../assets/images/app-development/load-catalogs-by-key.png)

## General information
The “Load Catalogs by Key” step works similar to the “Get Entity by ID” step, but instead of requiring a specific component ID, it automatically identifies any Catalog type field in the data model. Depending on the user's choice, the step retrieves the full entry linked with the selected Catalog type field. Thus, it allows you to get complete information from any link in the data without having to specify a specific ID.

## Parameters
**Step Settings:**

| Setting Field | Value Options | Purpose |
|----------------|-------------------|------------|
| Step name      | -                 | Name of the step |
| Source step    | -                 | Selecting the previous step |

## Cases
- **Automatic Identification and Downloading of the Linked Data**: Used to identify and automatically load data linked with Catalog fields.
- **Flexible Data Extraction**: Suitable for scripts that require flexibility in selecting and extracting data from various related components.

## Exceptions
- **Excessive Load When Working with a Large Number of Catalogs**: If there is a large number of catalogs being opened, it may take additional time to process them.
- **Unjustified Replacement of the “Get entity by ID” step with the “Load catalogs by key” step:** If the number of linked catalogs does not exceed a few, it is better to use the “Get entity by ID” step for better performance.

## Application scenario

This component allows you to create a data flow starting from obtaining an empty data model. Then, it is used to retrieve the record identifier with catalogs, after which it loads these catalogs and outputs their data on the frontend.

- You can download the component configuration [here](https://drive.google.com/file/d/1_GImBJ3UCDo-T1dL6c85-wWgcUfpJIz3/view?usp=sharing).