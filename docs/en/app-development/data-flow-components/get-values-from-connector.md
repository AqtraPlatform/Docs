# Get values from connector

![](../../assets/images/app-development/get-values-from-connector.png)

## General information
The “Get values from the connector” step allows you to retrieve data via a query to external systems using the configured connectors. The step can be called by schedule or on behalf of the user.

## Parameters
**Step Settings:**

| Setting Field        | Value Options             | Purpose |
|-----------------------|-------------------------------|------------|
| Step name             | -                             | Name of the step |
| System                | Multiselect of Catalog   | Contains preconfigured integration systems |
| Connector             | Multiselect of Catalog   | Contains pre-configured connectors in the integration system |
| Query path            | Multiselect of Catalog   | Contains the “EndPoint” to be accessed |
| Method name           | Get, Post, Put, Delete        | Type of request to be executed |
| Parameters mapping    | -                             | A dynamic entity that allows you to filter a request via a selected API |

## Cases
- **Scheduled Updating of Data**: The step is used to automatically update data in the Input dataflow on a scheduled basis via cron ensuring getting timely and up-to-date information.
- **Individual Query Customization**: The step is configured to send specific queries to different external systems, allowing for flexible integration and processing of data from multiple sources.
- **Dataflow Optimization**: The step is efficiently used to extract data from external systems minimizing the need for manual processing and improving dataflow performance.

## Exceptions
- **Query Methods**: Although various query methods (Get, Post, Put, Delete) are supported, careful customization is required on a case-by-case basis, taking into account the specific features of the external system and data type.
- **Automation with Limitations**: The ability to automatically call a scheduled step provides convenience, but requires fine-tuning of parameters and checking the accessibility of external systems.

## Application scenario

This component handles character data. We create five data models for their attributes: character_id, character_name, character_species, character_status, and gender. Then, we select an integration, for example, Rick and Morty, and add the following steps: Get values from connector, Extract collection, Store entry over bus, and Write response.

- You can download the component configuration [here](https://drive.google.com/file/d/1zWIWzpqccbocpDCfVUNIkGW2grrWJ5Yn/view?usp=sharing)