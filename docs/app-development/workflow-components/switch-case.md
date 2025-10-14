# Switch case

![](../../assets/images/app-development/switch-case.png)

## General information
The “Switch Case” step within a workflow is used as an unconditional switch operator that allows you to choose between different script options. This step is ideal for controlling process logic based on certain conditions, usually specified by Boolean or Enum fields. When used, the main script is always disabled and the process goes to one of the alternative branches.
![](../../assets/images/app-development/switch-case-example.png)

## Parameters
**Step Settings:**

| Setting Field     | Purpose |
|--------------------|------------|
| Step name          | “Switch Case” step name |
| Switch source field| Field based on the value of which the script is selected |

## Cases
- **Process Logic Branching**: Used to create conditional paths in a workflow where the next direction is determined based on a certain condition or value.
- **Management of Different Execution Scripts**: Suitable for scripts where a process requires different execution depending on predefined conditions or user selection.

## Exceptions
- **Accuracy of Transition Conditions**: It is necessary to accurately define the switch conditions for each case to ensure that the correct execution path is selected.
- **Complexity of Multiple Path Management**: Complex workflows with many possible paths require clear understanding and management of each of them to avoid errors in the process logic.
