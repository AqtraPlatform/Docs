# Register context for model

![](../../assets/images/app-development/register-context-for-model.png)

## General information
The “Register context for model” step is used in the context of LDAP integration to register the security context of users registered in an external system. This step ensures that data about users and their roles are synchronized between the external system and the current system, using keys to identify and register the context.

## Parameters
**Step Settings:**

| Setting Field | Value Options | Purpose |
|----------------|-------------------|------------|
| Step name      | -                 | Name of the step |
| Source step    | -                 | Selecting the previous step |
| Component      | -                 | Component for which the context is being registered |
| Name field     | -                 | Field that indicates the entity's name or identifier |
| Keys           | -                 | Keys used to uniquely identify an entity |

## Cases
- **LDAP Integration**: Used to synchronize and register user data from LDAP in the current system.
- **Role and Access Management**: Suitable for scripts that require accurate matching and tracking of the roles of users registered in external systems.

## Exceptions
- **Key Accuracy Requirements**: The keys must be accurately matched to correctly identify and register users in the system.
- **Managing Changes in External Systems**: Changes in user roles or statuses in an external system require an appropriate update in the current system, which can be a challenge in the face of dynamically changing data.
