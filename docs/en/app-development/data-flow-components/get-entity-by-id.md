# Get entity by id

![](../../assets/images/app-development/get-entity-by-id.png)

## General information
The “Get Entity by ID” step is used to get a component item by its unique identifier (ID). This step is usually used in combination with other steps, such as “Lookup” or “Update Entry”, which return an ID that is suitable for this step.

## Parameters
**Step Settings:**

| Setting Field  | Value Options | Purpose |
|-----------------|-------------------|------------|
| Step name       | -                 | Name of the step |
| Source step     | -                 | Selecting the previous step |
| Src field       | -                 | Field containing the ID to be searched |
| Dst field name  | -                 | Field where the result will be recorded |
| Component       | -                 | Component that is being searched |

## Cases
- **Data Search by ID**: Used to accurately retrieve a specific entry by using the ID from the component.

## Exceptions
- **Dependency on ID Accuracy**: The exact ID must be specified and available in the source data in order for the query to be successful.
- **Handling Inconsistencies**: If there is no entry with the specified ID, the step may return an empty result.

## Application scenario

This component allows adding a catalog-type field and creating a data flow to retrieve an entity by its identifier. The catalog-type field is placed on the page for selecting the corresponding value from the catalog. The data flow includes a 'Get action model' step for initialization, a 'Get entity by id' step for retrieving the entity by identifier using the selected value from the catalog, and a 'Write response' step for outputting the result.

- You can download the component configuration [here](https://drive.google.com/file/d/1eCxoYHKg0Zl8APxnUMRA9qmpqNkrtfuW/view?usp=sharing).
