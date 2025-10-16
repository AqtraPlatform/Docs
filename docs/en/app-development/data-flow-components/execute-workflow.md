# Execute Workflow

![](../../assets/images/app-development/execute-workflow.png)

## General information
The “Execute Workflow” step is used to activate and execute a specific workflow in the system.

## Parameters
**Step Settings:**

| Setting Field      | Value Options | Purpose |
|---------------------|-------------------|------------|
| Step name           | -                 | Name of the step |
| Source step         | -                 | Selecting the previous step |
| Component           | -                 | The component within which the workflow is performed |
| Workflow            | -                 | Name of the workflow to be completed |
| Component entry field | -               | The field in the component used to transfer data to workflow |

## Cases
- **Dynamic data flow control**: It can be used to launch specific workflows based on data obtained from previous Dataflow steps, which allows you to create flexible and adaptive data management systems.

## Exceptions
- **Dependency on data correctness**: To avoid errors in workflow execution, it is necessary to ensure that the data sent to the workflow is accurate and complete.
- **Coordination between Dataflow and Workflow**: It is important to carefully configure the interaction between Dataflow and Workflow to ensure a smooth and correct transfer of data and commands between them.

## Application scenario

The created component serves as an interface for interacting with the data model containing a field "user_name" of type string. This component includes functionality for updating the data model using the Update model step within the Workflow. To interact with the component, the user can input their name, click a button, after which the data will be sent, and the name will be displayed in the data grid after refreshing the page.

- You can download the component configuration [here](https://drive.google.com/file/d/1AgjjrOW-z2LPMj7sFWg_PKjHjFfVtxub/view?usp=sharing).