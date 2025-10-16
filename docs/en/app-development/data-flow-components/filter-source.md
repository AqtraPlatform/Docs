# Filter source

![](../../assets/images/app-development/filter-source.png)

## General information
The “Filter Source” step is used to filter the data stream in dataflow. It allows you to branch data streams based on the value of the selected field and the specified test operator, such as equal, not equal, greater, and less.

## Parameters
**Step Settings:**

| Setting Field     | Value Options   | Purpose |
|--------------------|---------------------|------------|
| Step name          | -                   | Name of the step |
| Source step        | -                   | Selecting the previous step |
| Src field          | -                   | Field to be filtered |
| Operator           | equal, not equal, greater, less | Operator for comparing field values |
| Compare with null  | true, false         | Indicates whether to compare with null |
| Filter value       | -                   | Value to be filtered |

## Cases
- **Data Stream Branching**: Used to split a data stream based on specific conditions defined in the filter.
- **Data Segmentation**: Suitable for situations where you need to treat different segments of data differently depending on specified criteria.

## Exceptions
- **Filter Setting Accuracy**: An incorrectly set filter can result in the loss of important data or the inclusion of unnecessary data in processing.
- **Dependency on the selected field**: The effectiveness of filtering depends on the correct choice of field and the appropriate comparison operator.

## Application scenario

This component is an interface with three buttons: `ExecuteFilterSource`, `ExecuteFilterSourceNotEqual`, and `ExecuteFilterSourceGreat`, each of which triggers a data flow depending on the input in the `First` field. Different test scenarios include checking conditions for equality, inequality, and greater/less than the specified value.

- You can download the component configuration [here](https://drive.google.com/file/d/1OO5SymRdhmv3oED2EPG4twG5mypsqqs9/view?usp=sharing).
