# Extract collection

![](../../assets/images/app-development/extract-collection.png)

## General information
The “Extract Collection” step is used to convert an array field to a flat list. This field can be obtained either from an external source or from a field (property) of an array component.

On this step, the array is parsed and the processing of each array element (entry or object) is started as a separate internal dataflow. Each such thread is executed independently of each other. Data flows parsed using the “Extract Collection” step can be reassembled via the “Group by” step.

## Parameters
**Step Settings:**

| Setting Field | Value Options | Purpose |
|----------------|-------------------|------------|
| Step name      | -                 | Name of the step |
| Source step    | -                 | Selecting the previous step |
| Model path     | -                 | Path to an array field in the data model |

## Cases
- **Data Array Processing**: Used to extract and process each element of the data array independently.
- **Splitting and Subsequent Grouping**: Suitable for scenarios where you need to split complex data structures into simpler elements for further processing and analysis.

## Exceptions
- **Need to specify the exact source and path**: Incorrect indication of the source or path to the array field can lead to errors in data processing.

## Application scenario

This component allows processing client warehouse data by adding new records using **extract collection** and **execute script** steps. After the data flow execution, each record receives additional field data. 

- You can download the component configuration [here](https://drive.google.com/file/d/1Q1czyILIGHc7tVwPYpkgHIFfI87p5WvQ/view?usp=sharing).

