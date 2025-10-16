# Prepare external keys

![](../../assets/images/app-development/prepare-external-keys.png)

## General information
The “Prepare External Keys” step is used to convert the internal identifiers of the component into external system keys. This step is widely used to prepare and send data to external systems, including integration with LDAP. It facilitates the process of transferring user information to an external system, including the relevant context.

In the course of the step, the internal IDs of the component are replaced with the primary keys that are specified for this component, which ensures the correct mapping of data between the internal and external systems.

## Parameters
**Step Settings:**

| Setting Field | Value Options | Purpose |
|----------------|-------------------|------------|
| Step name      | -                 | Name of the step |
| Source step    | -                 | Key conversion data source |

## Cases
- **Integration with External Systems**: Used to adapt internal data for their proper integration and sending to external systems such as LDAP.
- **Prepare Data for Export**: Suitable for scripts where internal IDs need to be transformed to meet the standards and requirements of external systems.

## Exceptions
- **Data Relevance and Accuracy Requirement**: The effectiveness of the step depends on the accuracy and relevance of the internal data and their compliance with the structure of the external system.
- **Data Mapping Management**: You need to ensure that all internal IDs are correctly mapped to the primary keys of the external system to avoid integration errors.
