# Select many

![](../../assets/images/app-development/select-many.png)

## General information
The “Select Many” step is used to convert an array type field into a flat list. Unlike the “Extract Collection” step, “Select Many” preserves the model data from the previous step and adds “parent” values with a `$parent` prefix for each array element. This does not only expand the array, but also preserves the context of the parent entry.

## Parameters
**Step Settings:**

| Setting Field | Value Options | Purpose |
|----------------|-------------------|------------|
| Step name      | -                 | Name of the step |
| Source step    | -                 | Selecting the previous step |
| Model path     | -                 | Path to an array field in the data model |

## Cases
- **Context Expansion and Preservation**: Used to convert arrays of data into a flat list while preserving the relationship with the parent data.
- **Processing of Hierarchical Structures**: Suitable for scripts where you need to process data from arrays without losing connection with “parent” data elements.

## Exceptions
- **Processing Large Arrays**: Processing large arrays can be more resource intensive due to the need to preserve the context of the parent data.

## Application scenario

This component is a tool for creating and managing data flows within the application. The 'Select many' step in this component is used to choose multiple items from an array of data obtained in the previous stage of the data flow. The component enables users to define selection and data processing conditions according to their requirements.

- You can download the component configuration [here](https://drive.google.com/file/d/1T9k35m8cg56vmM68LCT0brMeYQ2JIJ6U/view?usp=sharing).

