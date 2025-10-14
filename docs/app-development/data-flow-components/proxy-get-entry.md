# Proxy get entry

![](../../assets/images/app-development/proxy-get-entry.png)

## General information
The “Proxy Get Entry” step is used to generate a model of a proxy request in order to obtain a single entry. This step is closely related to the “Proxy mode” setting, which can be found in the “Settings” section.

## Parameters
**Step Settings:**

| Setting Field        | Value Options | Purpose |
|-----------------------|-------------------|------------|
| Step name             | -                 | Name of the step |
| Validate input values | true, false       | Indicates that input values should be checked for correctness prior to processing |

## Cases
- **Single Entry Retrieval**: Used to generate and send requests for a specific entry via a proxy server.
- **Integration with external systems**: Provides communication with external systems and services to obtain data using query proxying.

## Exceptions
- **Proxy Settings Dependency**: The correct operation of the step depends on the correct “Proxy mode” setting in the “Settings” section.
- **Limited Functionality**: The step is specialized in retrieving single records and is not designed to handle multiple queries or data.
