# Confirm user email request

![](../../assets/images/app-development/confirm-user-email-request.png)

## General information
The “Confirm User Email Request” step is used to enable the user that was originally created with the “Disabled” flag. This process involves verifying the user via email using the “Send Templated Notification” step. The step requires an application domain with a public URI and a configured SMTP server to send email notifications.

## Parameters
**Step Settings:**

| Setting Field   | Value Options | Purpose |
|------------------|-------------------|------------|
| Step name        | -                 | Name of the step |
| Source step      | -                 | Selecting the previous step |
| User info field  | -                 | A field that contains information about the user |
| User name        | -                 | Name of the user whose confirmation is to be obtained |
| Client for request | -               | The client or application that initiates the confirmation request |

## Cases
- **Enabling New Users**: This step is used to enable users who have been registered as disabled by verifying their email. This provides an additional layer of verification and security.
- **User Access Management**: Suitable for systems that require user email verification before full access to system functionality can be granted.

## Exceptions
- **Requirement of a configured SMTP server**: A configured SMTP server is required for confirmation email notifications to be sent successfully.
- **Dependency on application domain and public URI**: This step requires an application domain with a public URI to ensure that the operation is correct and that the verification process is available to the user.
