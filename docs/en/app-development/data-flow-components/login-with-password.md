# Login with password

![](../../assets/images/app-development/login-with-password.png)

## General information
The “Login with Password” step is used to create a user session based on his username and password. This step allows the user to be authorized into the system by verifying the provided credentials and, if verified successfully, creating a user session.

## Parameters
**Step Settings:**

| Setting Field   | Value Options | Purpose |
|------------------|-------------------|------------|
| Step name        | -                 | Name of the step |
| Source step      | -                 | Selecting the previous step |
| User name        | -                 | Login username |
| User password    | -                 | User password |
| Client for request | -               | Client or application that initiates the authentication request |

## Cases
- **User Authentication**: Step used in authentication processes where users enter their credentials to access the system or its features.
- **Access Control**: Suitable for systems that require user credentials to be verified before granting access to certain resources or functionality.

## Exceptions
- **Need for Accuracy of Credentials**: The effectiveness of the step depends on the accuracy of the credentials entered (username and password).
- **Handling Failed Login Attempts**: It is important to properly handle failed login attempts to avoid potential security risks such as brute-force attacks. This requires implementing mechanisms to limit the number of login attempts or temporarily block access after several unsuccessful attempts.

## Application scenario

The scenario implements user login to the system using a username and password. After initiating the dataflow and entering the login and password into the corresponding fields of the user interface, the "Login with password" step authenticates the user. Then, using the "Form action" step, the selected component is opened.

- You can download the component configuration [here](https://drive.google.com/file/d/1Kb9QNcCHXqetQmXGvBHScQSiRlA-542s/view?usp=sharing)