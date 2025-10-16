# Lookup reference

![](../../assets/images/app-development/lookup-reference.png)

## General information
The “Lookup Reference” step is used to search for references to component instances by external keys. This process requires that at least one property with the “Primary key” flag be configured in the component to be searched.

The search is performed by this property, and the result of the search in the form of Id (integer) of the found record will be recorded to the variable specified in the “Field name.” If no instance of a component with such a key is found, the variable will be null.

## Parameters
**Step Settings:**

| Setting Field | Value Options | Purpose |
|----------------|-------------------|------------|
| Step name      | -                 | Name of the step |
| Source step    | -                 | Selecting the previous step |
| Component      | -                 | Component that is being searched |
| Field name     | -                 | Name of the field where the search result will be recorded |

## Cases
- **Primary Key Search**: Used to determine the availability and identify instances of components by unique identifiers.
- **Component Data Linking**: Suitable for scripts where you want to link data from different components based on unique keys.

## Exceptions
- **Primary Key Requirement**: The component must have a primary key configured to ensure a successful search.
- **Handling Missing Records**: If there is no instance with the specified key, the value of the variable will be null, which may require additional processing.

## Application scenario

This component utilizes the Lookup Reference step to find the record ID in the "Sorting Task" table based on the entered sorting number. After entering the sorting number and executing the data flow, the corresponding record ID is displayed on the frontend.

- You can download the component configuration [here](https://drive.google.com/file/d/1LZzqHGc7I5IdAVLmK6H1_ItODiiruSAJ/view?usp=sharing)