# Get user confirmation

![](../../assets/images/app-development/get-user-confirmation.png)

## General information
The “Get User Confirmation” step in the workflow is used to request confirmation or perform an action from the user. The step sends a notification to the user with a request to perform a specific action on the object, where the object is the state of the current model.

## Parameters
**Step Settings:**

| Setting Field      | Value Options     | Purpose |
|---------------------|-----------------------|------------|
| Step name           | -                     | “Get User Confirmation” step name |
| Confirmation field  | -                     | Field with options to be requested from the user |
| User info field     | Multiselect of Catalog | Field with information about a user or group of users |
| User routing        | Multiselect of Catalog | Object that is a security context |

## Cases
- **Request for User Confirmation**: Ideal for scripts that require confirmation or choice of action from the user, such as confirming a transaction, agreeing to data processing, or choosing an answer option.
- **Interactive User Participation in the Process**: Suitable for a workflow, where it is important to take into account the user's decisions or choices to continue or change the process.

## Exceptions
- **Ensuring the Request Is Clear**: It is important to clearly formulate the confirmation request so that the user understands what action is expected from him.
- **Managing User Responses**: User responses should be adequately processed and taken into account, especially in situations where they determine the course of further actions in the workflow.
- **Taking into Account the Security Context and Permissions**: When using the User routing parameter, it is important to consider the security context and the corresponding user permissions.
