# Get Action Model

![](../../assets/images/app-development/get-action-model.png)

## General information
The “Get Action Model” step is designed to extract an action model from a specific source or system. This step can be used to obtain data about specific actions or processes that are required for further processing or analysis within the dataflow.

## Parameters
**Step Settings:**

| Setting Field        | Value Options             | Purpose |
|-----------------------|-------------------------------|------------|
| Step name             | -                             | Name of the step |
| Validate input values | true, false                   | Specifies whether the input values should be checked for correctness before processing |

## Cases
- **UI Integration**: Often used as an initial step in dataflow, especially when dataflow is enabled from the UI, e.g. via pressing a button. Allows you to get the current state of the component data at the time of enabling.
- **Automatic Data Transfer from UI**: When data transfer enabled from UI elements such as buttons, the platform automatically transmits the current data of the component, including changes made by the user.

## Exceptions
- **Data Retrieval Limitations**: The step retrieves only the fields (properties) data of the component. To get the variables set in the Component Script, you need to use other steps, such as “Get raw model”.

## Application scenario

The component is a system for adding and displaying data using various field types. It includes the capability to add fields of different types in the **definition** and provides a front-end interface for inputting values, as well as displaying data in a **datagrid** with the ability to refresh the page. This component utilizes the following **data flow steps**: **Get action model**, **Update entry**, **Write response**.

- You can download the component configuration [here](https://drive.google.com/file/d/15M_FvmlFmkJXunTeeT6jtFolPvE5jCfk/view?usp=sharing)