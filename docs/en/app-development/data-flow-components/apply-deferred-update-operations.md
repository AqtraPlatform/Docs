# Apply deferred update operations

![](../../assets/images/app-development/apply-deferred-update-operations.png)

## General information
The “Apply Deferred Update Operations” step is used for the bulk application of updates that have been prepared using the “Deferred Update Entry” series of steps. This step allows you to perform the accumulated update operations in an efficient manner by applying them all at once.

## Parameters
**Step Settings:**

| Setting Field       | Value Options | Purpose |
|----------------------|-------------------|------------|
| Step name            | -                 | Name of the step |
| Batch chunk size     | 1000              | Size of the data batch to be processed |
| Batch idle timeout in ms | -             | Idle timeout in milliseconds between batches |
| Parallel number of batches | 0           | Number of data batches processed in parallel |

## Cases
- **Bulk Update Application**: Ideal for scenarios where you need to update data in bulk, such as when you synchronize a large amount of data or when you need to quickly make changes to multiple system components.
- **Performance Optimization**: Improves performance for bulk updates via parallel processing and efficient management of data batches.

## Exceptions
- **Update Sequence Management**: It is important to ensure that updates are sequenced correctly, especially if the data in the different steps of the “Deferred Update Entry” are interrelated.
- **Configuring Batch Processing Parameters**: Parameters such as batch size and number of parallel batches must be carefully configured to avoid overloading the system and ensure that updates are performed efficiently.

## Application scenario

The component with a custom definition configures a data flow for updating records. Users start by extracting the action model using the "Get action model" step. Then, the "Deferred update entry" step is used for deferred updates of records, where users can specify the component, component ID, and field mappings. The "Apply deferred update" step allows configuring batch processing and parallel execution parameters. After completing these steps, the component is ready for updating, creating, or deleting records, which occurs on the frontend when interacting with the corresponding interface elements.

- You can download the component configuration [here](https://drive.google.com/file/d/16uo9P5IWDv-QnT749fYDISyyWEbKrDVR/view?usp=sharing)