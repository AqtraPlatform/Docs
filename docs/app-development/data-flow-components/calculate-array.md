# Calculate array

![](../../assets/images/app-development/calculate-array.png)

## General information
The “Calculate Array” step is designed to perform simple mathematical operations on arrays. This step is often used in conjunction with the “Group By” step or to process data presented as arrays.

This step allows you to perform various mathematical operations, such as minimum (min), maximum (max), sum, and average, on one or more fields in an array.

## Parameters
**Step Settings:**

| Setting Field     | Value Options       | Purpose |
|--------------------|-------------------------|------------|
| Step name          | -                       | Name of the step |
| Source step        | -                       | Selecting the previous step |
| Add operation      | min, max, sum, average  | The type of mathematical operation to perform on an array |

## Cases
- **Mathematical processing of arrays**: It is used to calculate key statistical indicators of a data array.
- **Data analysis and processing**: Suitable for scenarios where data arrays need to be aggregated or summarized.

## Exceptions
- **Dependency on the type of data in the array**: Requires that the data in the array be suitable for performing the selected mathematical operation.
- **Restrictions on processing complex data**: May not be suitable for complex operations that require advanced data analysis or processing.
