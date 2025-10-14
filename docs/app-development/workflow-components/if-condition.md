# If condition

![](../../assets/images/app-development/if-condition.png)

## General information

The “If Condition” step within the workflow is used to check the value of a field against the specified condition. This step allows you to implement conditional branching in a process where performing certain actions or moving to an alternative script depends on the result of a condition check. An alternative script must contain the “Finish” step.

## Parameters

**Step Settings:**

| Setting Field     | Value Options                 | Purpose                                 |
| ----------------- | ----------------------------- | --------------------------------------- |
| Step name         | -                             | “If Condition” step name                |
| Condition field   | Multiselect of Catalog        | Condition validation field              |
| Operator          | Equal, Not equal, Great, Less | Type of operator to check the condition |
| Compare with null | true, false                   | Checking for comparison with null       |
| Value             | -                             | Value to compare with the field         |

## Cases

- **Conditional Execution of Actions**: Used to activate different parts of the workflow based on the values of certain fields, for example, to start different processes based on the status of the request.
- **Logical Branching in Processes**: Suitable for creating complex logical chains where different execution steps depend on the satisfaction of specific conditions.

## Exceptions

- **Condition Definition Accuracy**: It is important to accurately define conditions and properly configure the fields to validate them to avoid incorrect branching or errors in the workflow logic.
- **Handling Different Scripts**: You need to plan clearly how different scripts will be handled depending on the result of the condition check, especially in multi-step or complex workflows.
