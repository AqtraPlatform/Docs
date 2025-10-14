# Write response

![](../../assets/images/app-development/write-response.png)

## General information
The “Write Response” step plays a key role in Dataflow, as it is designed for returning the final result to the caller. This step is usually the last step in any Dataflow, summarizing and sending the received data back to the requesting source.

## Parameters
**Step Settings:**

| Setting Field  | Value Options | Purpose |
|-----------------|-------------------|------------|
| Step name       | -                 | Name of the step |
| Source step     | -                 | Selecting the previous step |

## Cases
- **Returning Dataflow Results**: Used to send the results of the Dataflow process data back to the caller, which can be critical in data analytics and error management.
- **Pre-Response Data Transformation**: Can be combined with the “Transform Model” step to transform or filter data before it is sent, allowing you to optimize and customize the content of the response to meet the caller's requirements.

## Application scenario

The component contains custom data definitions (definitions) and provides the ability to create and manage data using data flows. It implements steps to retrieve data models (Get action model) and write responses (Write response), allowing users to interact with data through the user interface and interact with it on the frontend of the application.

- You can download the component configuration [here](https://drive.google.com/file/d/1qNTgk1uYrMO3uUkDRmTO3i4En5mbG22i/view?usp=sharing).