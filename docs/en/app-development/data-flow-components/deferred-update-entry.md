# Deferred update entry

![](../../assets/images/app-development/deferred-update-entry.png)

## General information
The “Deferred Update Entry” step is used to organize the deferred update of entries in a specific component. This step allows you to accumulate actions to create, update, or delete entries, which are then executed after the “Apply Deferred Update Operations” step is enabled. In this way, multiple update operations can be collected.

## Parameters
**Step Settings:**

| Setting Field      | Value Options | Purpose |
|---------------------|-------------------|------------|
| Step name           | -                 | Name of the step |
| Source step         | -                 | Selecting the previous step |
| Component           | -                 | Component to be updated |
| Field component key | -                 | Field with the component key to update |
| Mark entry for deletion | true, false             | Entry deletion mark |
| Name field          | -                 | Name of the field to be updated |
| Fields mapping      | -                 | Mapping fields between data flow and component |

## Cases
- **Data Batch Processing**: Used to collect multiple data update operations and then execute them in a single transaction, improving performance and reducing the load on the system.
- **Complex data management**: Suitable for scenarios that require complex data update logic, including creating, modifying, and deleting entries within a single workflow.

## Exceptions
- **Need for Subsequent Updates**: All update operations accumulated by this step need to be enabled via the “Apply Deferred Update Operations” step in order to perform them.

## Application scenario

The component with a custom definition configures a data flow for updating records. Users start by extracting the action model using the "Get action model" step. Then, the "Deferred update entry" step is used for deferred updates of records, where users can specify the component, component ID, and field mappings. The "Apply deferred update" step allows configuring batch processing and parallel execution parameters. After completing these steps, the component is ready for updating, creating, or deleting records, which occurs on the frontend when interacting with the corresponding interface elements.

- You can download the component configuration [here](https://drive.google.com/file/d/16uo9P5IWDv-QnT749fYDISyyWEbKrDVR/view?usp=sharing)
