# Update entry

![](../../assets/images/app-development/update-entry.png)

## General information

The “Update Entry” step is used to create, update or delete an existing entry in the system. This step is executed directly, and the system waits for it to be completed. If an error occurs during execution, further execution of the data flow will be stopped.

## Parameters

**Step Settings:**

| Setting Field           | Value Options | Purpose                                        |
| ----------------------- | ------------- | ---------------------------------------------- |
| Step name               | -             | Name of the step                               |
| Source step             | -             | Selecting the previous step                    |
| Component               | -             | Component to be updated                        |
| Field component key     | -             | Field with the component key to update         |
| Mark entry for deletion | true, false   | Entry deletion mark                            |
| Name field              | -             | Name of the field to be updated                |
| Result store field      | -             | Field for saving the result of the operation   |
| Fields mapping          | -             | Mapping fields between data flow and component |

## Cases

- **Data Update**: Used to update information in the existing entries of the system components to ensure data is accurate and up-to-date.
- **Deleting an Entry**: The “Update Entry” step can be used to delete existing entries in the system. This is especially relevant in scripts where you need to remove outdated or incorrect information to keep the data in the system accurate and up-to-date. For example, this can be deleting the account of a user who has left the organization or removing unavailable items from inventory. It is important to note that the step can be configured to mark entry for deletion, which allows you to manage the deletion process more flexibly.

## Exceptions

- **Dependency on the Presence of an Instance ID**: To successfully update data, the component instance ID must first be received and transmitted.
- **Managing Runtime Errors**: Any error during the data update process will stop the data flow, which requires the careful monitoring of error and exception handling.

## Application scenario

The component presents a scenario for adding, editing, and deleting component records using the "Update entry" step.

- You can download the component configuration [here](https://drive.google.com/file/d/1k1oMpI2YSF-P3zgsd2cORfRjFs3l7w0o/view?usp=sharing)
