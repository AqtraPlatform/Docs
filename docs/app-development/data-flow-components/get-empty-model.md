# Get Empty Model

![](../../assets/images/app-development/get-empty-model.png)

## General information
The “Get Empty Model” step is used in dataflow scripts that do not require data model retrieval at the input. It is often used when dataflow is called to run regular operations, such as generating reports, especially if they are scheduled (for example, by cron).

## Parameters
**Step Settings:**

| Setting Field        | Value Options | Purpose |
|-----------------------|-------------------|------------|
| Step name             | -                 | Name of the step |
| Validate input values | true, false       | Indicates that input values should be checked for correctness before processing |

## Cases
- **Regular Operations**: Ideal for dataflow scheduled to run regularly without the need for input data.
- **Dataflow Initial State**: Used to initialize dataflow without pre-set data, allowing developers to create and populate the data model themselves using subsequent steps.

## Exceptions
- **No Input Data**: When using this step, the input data are not provided in the dataflow. It means that the developer has to initialize and populate the data model in subsequent steps.

## Application scenario

This component is an interface for adding a new name via an **input field** on the front end, then updating the data model and displaying the result in a **datagrid**. The data flow in the component allows adding a new name to the model and updating the record in the **datagrid**.

- You can download the component configuration [here](https://drive.google.com/file/d/1G3v4cZiteFdONpIjxPAf78a8gBTrh0w_/view?usp=sharing)