# Get raw model

![](../../assets/images/app-development/get-raw-model.png)

## General information
The “Get Raw Model” step is used in a dataflow, which requires processing a custom data model that does not correspond to the standard component model, workflow, or other standard options. Typical use cases include dataflow called from a Component Script with variables defined within the script, as well as processing form data within a multi-component structure.

## Parameters
**Step Settings:**

| Setting Field        | Value Options | Purpose |
|-----------------------|-------------------|------------|
| Step name             | -                 | Name of the step |
| Validate input values | true, false       | Indicates that input values should be checked for correctness prior to processing |

## Cases
- **Integration with Component Script**: Used for dataflow called from Component Script when specific variables or data are required.
- **Processing of Multi-Component Form Data**: Suitable for scripts where dataflows work with data obtained from forms in a multi-component structure.

## Exceptions
- **Model Configuration Requirement**: You must preconfigure the data model in JSON format.
- **Model Format Features**: Improper model configuration may result in incorrect data processing or dataflow errors.
