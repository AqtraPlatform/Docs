# Remove assigned roles for user

![](../../assets/images/app-development/remove-assigned-roles-for-user.png)

## General information
The “Remove Assigned Roles for User” step is used to reset all roles assigned for a particular user. This allows system administrators and process managers to remove user roles simplifying the management of permissions and security controls.

## Parameters
**Step Settings:**

| Field             | Value Options  | Purpose |
|------------------|--------------------|------------|
| Step name        | -                  | Name of the step |
| Source step      | - | Selecting the previous step |
| User id field    | Name of a variable of user info type | Field that contains the user ID for role reset |

## Cases
- **Management of Access and Roles**: This step is ideal for scripts where you want to quickly change or reset user roles, such as when job responsibilities change or when an employee leaves.
- **Ensuring System Security**: Used to prevent unauthorized access to sensitive data or system features by removing roles from users who no longer need such access permissions.

## Exceptions
- **Dependency on the Accuracy of User Identification**: The effectiveness of the step depends on the precise identification of the user whose roles you want to reset.
- **Need to Get User ID First**: The step requires you to first get an internal user id, which can be done via the “Get User Info” step or other authentication methods.
