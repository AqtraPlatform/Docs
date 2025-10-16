# Register external user

![](../../assets/images/app-development/register-external-user.png)

## General information
The “Register External User” step is intended for registering individual users or groups of users. This step is designed in the context of LDAP integration and is used for integration with external systems, facilitating the process of swapping out of users from those systems and then logging them into the current system.

## Parameters
**Step Settings:**

| Setting Field | Value Options | Purpose |
|----------------|-------------------|------------|
| Step name      | -                 | Name of the step |
| Source step    | -                 | Selecting the previous step |
| User name      | -                 | Registration name or user ID |
| Key field      | -                 | Field containing key information to identify the user |
| Auth provider  | -                 | Authentication provider used to register the user |

## Cases
- **Integration of Users from External Systems**: Used to swap out and register users from LDAP or other external systems, ensuring their correct integration into the current system.
- **Automation of the Registration Process**: Suitable for scripts where it is necessary to automate the registration process of a large number of users, minimizing manual labor and possible errors.

## Exceptions
- **Dependency on the Accuracy of the Input Data**: The effectiveness of the step depends on the accuracy and completeness of the data received from the external system.

