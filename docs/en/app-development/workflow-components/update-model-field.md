# Update model field

![](../../assets/images/app-development/update-model-field.png)

## General information
The “Update Model Field” step within workflow is used to update a specific field in the model. This step allows you to change the values of individual fields in the data model, which is particularly useful for dynamic data management during workflow execution.

## Parameters
**Step Settings:**

| Setting Field | Purpose |
|----------------|------------|
| Step name      | “Update Model Field” step name  |
| Model field    | Model field you want to update |
| Value          | Value to which the field will be updated |
| Source field   | Source field whose value will be used for updating |

## Cases
- **Dynamic Data Updating**: Used to change values in the model based on data generated during workflow, such as updating the status of a task or changing configuration options.

## Exceptions
- **Accuracy and Relevance of Data**: Ensure that updated data are accurate and up-to-date to avoid undesirable consequences.
- **Understanding the Impact of Changes**: It is important to understand the impact of updating a field on the overall workflow model and logic, especially in complex systems with interlocking dependencies.
