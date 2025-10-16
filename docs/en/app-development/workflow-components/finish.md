# Finish

![](../../assets/images/app-development/finish.png)

## General information
The “Finish” step within a workflow is designed for completing the execution of the current Workflow. This step is typically used to explicitly specify the completion point of a workflow, especially in the alternative scripts defined in the Conditions block.

## Parameters
**Step Settings:**

| Setting Field | Purpose |
|----------------|------------|
| Step name      | “Finish” step name |

## Cases
- **Controlled Workflow Completion**: Used to explicitly specify the completion point of a workflow, which is especially important in complex processes with many conditions and branches.
- **Alternative Execution Paths**: Suitable for scripts where a workflow needs to terminate under certain conditions that differ from the main flow of execution.

## Exceptions
- **Need for Proper Configuration**: It's important to make sure that the “Finish” step is properly embedded in the workflow logic so that it doesn't interrupt the process prematurely or skip important steps.

