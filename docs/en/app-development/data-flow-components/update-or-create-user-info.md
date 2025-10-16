# Update or create user info

![](../../assets/images/app-development/update-or-create-user-info.png)

## General information
The “Update or Create User Info” step is used to update existing user information or create a new user. This step works exclusively with the “User Info” component. When user information is updated, if the password is not specified, it will remain unchanged.

## Parameters
**Step Settings:**

| Setting Field  | Value Options  | Purpose |
|-----------------|--------------------|------------|
| Step name       | -                  | Name of the step |
| Source step     | -                  | Selecting the previous step |
| User info field | -                  | A field that contains information about the user |
| User name       | -                  | Name of the user |
| User password   | -                  | User password (required) |
| User disabled   | true, false                 | User activity status |
| Update fields   | name, email, lastName, userName, firstName, middleName | Fields for updating or creating user information |

## Cases
- **Updating User Information**: Used to change data about existing users, including their contact information, username, and other personal information.
- **Creating New Users**: Suitable for adding new users to the system, allowing you to quickly and efficiently expand the user database.

## Exceptions
- **Need for Data Accuracy**: The step requires accurate and up-to-date data entry, especially when creating new users.
- **Password Management**: When user information is updated, if the password is not specified, it will remain unchanged. When creating a user, specifying a password is mandatory.

## Application scenario

The component is designed to manage user information. It involves retrieving user information, updating their data, and creating a new user record with specified parameters.

- You can download the component configuration [here](https://drive.google.com/file/d/1zrn1vRmP3BtXAp-FBsoc5OHj96JuGKvF/view?usp=sharing)