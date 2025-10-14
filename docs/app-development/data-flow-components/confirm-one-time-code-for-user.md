# Confirm one-time code for user

![](../../assets/images/app-development/confirm-one-time-code-for-user.png)

## General information
The “Confirm One-Time Code for User” step is used to confirm the one-time code that was generated for the user in the previous “Get One-Time Code for User” step. This step is the key one in the two-factor authentication process, allowing you to verify the correctness of the code entered by the user to access the system.

## Parameters
**Step Settings:**

| Setting Field   | Value Options | Purpose |
|------------------|-------------------|------------|
| Step name        | -                 | Name of the step |
| Source step      | -                 | Selecting the previous step |
| User code field  | -                 | The field in which the user enters the received code for confirmation |

## Cases
- **Two-Factor Authentication Confirmation**: Applied to complete the two-factor authentication process by requiring the users to enter the code that was sent to them in the previous step.
- **Enhancing Access Security**: Used in scenarios where enhanced system access control is required to prevent unauthorized logins.

## Exceptions
- **Dependency on the correctness of the code entered**: The effectiveness of the step depends on the accuracy of entering the code by the user.
- **Limited Code Validity**: If the code expires, it must be re-issued, which may result in delays in authentication.

## Application scenario

The component creates a dataflow to confirm the user's one-time code. The Get action model step is used to retrieve the model data. Then, the code from the ForTestCode variable is cleaned of unnecessary characters and stored in the _code variable using the Execute script step. The Confirm one-time code for user step is utilized to confirm the one-time code using the _code value as the user's code. Finally, the result is passed through the Write response step.

- You can download the component configuration [here](https://drive.google.com/file/d/1_uPyqNOuOddurvwz-KteaoIIRQjgEzBH/view?usp=sharing)