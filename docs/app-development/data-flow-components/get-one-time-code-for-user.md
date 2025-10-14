# Get one-time code for user

![](../../assets/images/app-development/get-one-time-code-for-user.png)

## General information
The “Get One-Time Code for User” step is used to generate and send a one-time code for logging in as part of two-factor authentication. This step works in conjunction with the “Confirm One-Time Code for User” step and is usually applied using the “Send Templated Notification” functionality.

## Parameters
**Step Settings:**

| Setting Field   | Value Options | Purpose |
|------------------|-------------------|------------|
| Step name        | -                 | Name of the step |
| Source step      | -                 | Selecting the previous step |
| User name        | -                 | Name or ID of the user for whom the code is generated |
| Client for request | -               | Client or application that initiates the confirmation request |
| Code life time   | -                 | The lifetime of a code |

## Cases
- **Two-Factor Authentication**: Used to provide an extra layer of security when logging in by generating a temporary code that the user must confirm.
- **Enhanced Login Security**: Suitable for scenarios where enhanced security measures are required to prevent unauthorized access to the system.

## Exceptions
- **Dependency on Accuracy of User Data**: The accuracy and relevance of user information is critical for the successful generation and sending of a one-time code.
- **Code Lifetime Management**: You must configure the code lifetime correctly to ensure that your code is up-to-date and avoid user access issues.

## Application scenario 

The component adds a new string definition ForTestCode. A dataflow is created where a one-time code for the user is obtained through Get action model and Get user info steps. The Execute script step is used to pass this code into the new_code variable, which is then stored in the ForTestCode definition of the component and displayed in a modal window.

- You can download the component configuration [here](https://drive.google.com/file/d/1_uPyqNOuOddurvwz-KteaoIIRQjgEzBH/view?usp=sharing)
