# Get workflow model

![](../../assets/images/app-development/get-workflow-model.png)

## General information
The “Get Workflow Model” step is used exclusively in dataflows that are called from a workflow. It allows you to get the model and data from the calling workflow within the current dataflow.

## Parameters
**Step Settings:**

| Setting Field        | Value Options | Purpose |
|-----------------------|-------------------|------------|
| Step name             | -                 | Name of the step |
| Validate input values | true, false       | Indicates that input values should be checked for correctness before processing |

## Cases
- **Dataflow and Workflow Integration**: Allows you to integrate dataflow with workflow providing access to the model and data of the calling workflow.

## Exceptions
- **Limited Use**: The step is not intended for use in Input dataflow.

## Application scenario

The component allows you to create a data flow for updating a record in the source data component. It includes steps such as Get workflow model to obtain the workflow model, Update entry to update the record with the appropriate parameters set, and Write response to output the result. This component can be used to update data in the source component using workflows and UI elements.

- You can download the component configuration [here](https://drive.google.com/file/d/1F2ZFQlyMf6ZaxABcoOWib4T8AD8w-75Q/view?usp=sharing)