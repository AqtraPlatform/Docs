# Execute script

![](../../assets/images/app-development/execute-script.png)

## General information
The “Execute Script” step is designed to execute Python scripts using standard Python libraries. 

This step allows you to execute Python scripts of any complexity while working with the current dataflow model. Using the script, you can change the model by adding new variables or changing the values of existing ones.

Examples of use:
- To get a variable value from the “get action model” step: `item ['data'] ['Property_name'] `
- To create a new variable in the script: `item ['Property_name'] `

## Parameters
**Step Settings:**

| Setting Field | Value Options | Purpose |
|----------------|-------------------|------------|
| Step name      | -                 | Name of the step |
| Source step    | -                 | Selecting the previous step |

## Cases
- **Customization of data processing**: Suitable for complex data processing logic that cannot be implemented with standard dataflow tools.
- **Adding and modifying data**: Suitable for scenarios that require adding new data or modifying existing data in the model.

## Exceptions
- **Need for Python proficiency**: Requires knowledge of Python and an understanding of the logic of working with dataflow.
- **Variable typing**: Strict typing of variables may require additional attention when writing scripts. Supported types: `@number`, `@integer`, `@string`, `@uuid`, `@boolean`, `@uri`, `@date`, `@date-time`, `@time`, `@catalog`, `@array`.

## Application scenario

This component showcases various usage scenarios of the Execute Script step within a data flow, including creating new variables of different types and modifying values of available fields in the data model.

- You can download the component configuration [here](https://drive.google.com/file/d/18fbg2g2rcvXORI7i31zu81NdSKwMqE99/view?usp=sharing)
