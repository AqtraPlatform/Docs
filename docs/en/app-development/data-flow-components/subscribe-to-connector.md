# Subscribe to connector

![](../../assets/images/app-development/subscribe-to-connector.png)

## General information

The “Subscribe to connector” step is for subscribing to receive messages from various messaging systems, such as RabbitMQ or Kafka.

## Parameters

**Step Settings:**

| Setting Field | Value Options          | Purpose                                                      |
| ------------- | ---------------------- | ------------------------------------------------------------ |
| Step name     | -                      | Name of the step                                             |
| System        | Multiselect of Catalog | Contains preconfigured integration systems                   |
| Connector     | Multiselect of Catalog | Contains pre-configured connectors in the integration system |
| Query path    | Multiselect of Catalog | Contains the “EndPoint” to be accessed                       |
| Method name   | Get, Post, Put, Delete | Type of request to be executed                               |

## Cases

- **Response to Events**: Automatic receiving of notifications about events or changes in data from external sources.
- **Integration with Messaging Systems**: Interaction with various messaging platforms to ensure a continuous dataflow.

## Exceptions

- **Limited Functionality**: The step is limited to subscribing to messages and does not support other types of interactions with external systems.
- **Dependency on External Systems**: Requires reliable configuration and support from the messaging systems used.

## Application scenario

The component is configured to **subscribe to a RabbitMQ queue** and save the received messages in a **database**. Steps such as "**Subscribe to connector**", "**Execute script**" for data processing, and "**Update entry**" for saving messages are utilized in this process.

- Component configuration will be available later
