# Assign context role for model

![](../../assets/images/app-development/assign-context-role-for-model.png)

## General information
The “Assign Context Role for Model” step is used to link a user or group of users to a specific role and context. This process requires that at least one role should be configured in the “Roles” section of the “Access” menu. This step allows you to establish relations between users and roles in the context of a specific data model, thereby providing control over user access and permissions.

## Parameters
**Step Settings:**

| Setting Field  | Value Options | Purpose |
|-----------------|-------------------|------------|
| Step name       | -                 | Name of the step |
| Source step     | -                 | Selecting the previous step |
| UserId field    | -                 | User ID field |
| ContextId field | -                 | Context ID field |
| Select contexts | -                 | Selecting the contexts to which the role will be linked |

## Cases
- **User Access Management**: Used to assign roles to users determining their access and permissions within the system.
- **Dynamic role management when interacting with UI**: This step is effectively used to change or update users’ roles in real time based on their actions and interactions with user interface elements. This makes it possible to adapt user access and permissions depending on specific actions or scenarios of using the system.

## Exceptions
- **Requirement for configured roles**: For successful linking, the system must have the appropriate roles pre-configured.
- **Dependence on ID accuracy**: Accurate identification of user IDs and contexts is critical for the step to work correctly.
