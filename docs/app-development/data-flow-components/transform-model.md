# Transform model

![](../../assets/images/app-development/transform-model.png)

## General information
The “Transform Model” step is used for mapping and transforming fields in the data model. This involves changing field names and removing unnecessary fields from the model. The step creates a new copy of the dataflow model, allowing you to modify its structure, which is often used to minimize the response as a data model. It can also be used to optimize the data model after performing multiple grouping operations (Group by).

## Parameters
**Step Settings:**

| Setting Field   | Value Options | Purpose |
|------------------|-------------------|------------|
| Step name        | -                 | Name of the step |
| Source step      | -                 | Selecting the previous step |
| Fields mapping   | -                 | Mapping and changing fields in the data model |

## Cases
- **Data Model Optimization**: Used to change the structure of the data model, including renaming or deleting fields.

## Exceptions
- **Importance of Accurate Mapping**: Errors in the “Fields Mapping” setting may result in unwanted changes to the data model.
- **Dependency on the Source Data**: Correct application of the step requires an accurate understanding of the structure of the source data.

## Application scenario

This component contains a data flow used for data transformation according to specified rules. The data flow includes steps such as Extract Collection and Execute Script, which allow adding new records to client data arrays.

- You can download the component configuration [here](https://drive.google.com/file/d/1buQNdkjcnY8wgIUM9TjjI7KoikEcSmv3/view?usp=sharing)