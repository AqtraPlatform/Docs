# Reset user password request

![](../../assets/images/app-development/reset-user-password-request.png)

## General information
The “Reset User Password Request” step is designed for generating a new password for the user. The step works in conjunction with the “Send Templated Notification” to ensure that users receive a new password. The step only works if you have an application domain with a configured public URI.

## Parameters
**Step Settings:**

| Setting Field   | Value Options | Purpose |
|------------------|-------------------|------------|
| Step name        | -                 | Name of the step |
| Source step      | -                 | Selecting the previous step |
| User info field  | -                 | A field that contains information about the user |
| User name        | -                 | Username for whom the password is being reset |
| Client for request | -               | Client or application that initiates the authentication request |

## Cases
- **User Access Recovery**: Used in scripts where a user has forgotten their password and needs to reset it to re-access the system.

## Exceptions
- **Requirement for an Application Domain with a Public URI**: The step requires a configured application domain with a public URI for it to work correctly.
- **Dependency on User Notification Method**: The effectiveness of the step depends on the reliability and availability of the user notification method, such as email, used for sending a new password.
