# Get user info

![](../../assets/images/app-development/get-user-info.png)

## General information
The “Get User Info” step is used to obtain data about the platform user, such as email, first and last name, for further processing in the current dataflow. This step is required for most user operations except creating a new user.

**Obtaining User Information**
1. **Using the ‘Get user info from request’ flag**: The step will attempt to retrieve data about the current user. For it to work correctly, it is necessary that the dataflow is called on behalf of a specific user (for example, from a request form or via a Proxy request). If called on behalf of the platform (e.g. in Input dataflow), the result will be null.
2. **Without the ‘Get user info from request’ flag**: The user can be defined:
   - Via the system name, using a String parameter of the current dataflow model.
   - Via a link to the user info directory, for example, creatorSubject or changeAuthor fields.

## Parameters
**Step Settings:**

| Setting Field            | Value Options | Purpose |
|---------------------------|-------------------|------------|
| Step name                 | -                 | Name of the step |
| Source step               | -                 | Selecting the previous step |
| Get user info from request| -                 | Flag to get information about the current user |
| User info field           | -                 | User identification field |
| User name                 | -                 | Name of the user |
| Result store field        | -                 | Field for saving the obtained information about the user |

## Cases
- **Retrieving User Data for Processing**: Used to extract user information for subsequent use in dataflow.
- **Send Personalized Notifications**: In cases where you need to send personalized email notifications to users, the “Get User Info” step is used to get their email addresses. This information is then passed to the step designed for sending notifications.

## Exceptions
- **User Not Found Handling**: In cases when the user cannot be identified, the result will be null, which requires additional processing in the dataflow.

## Application scenario

The "Get user info" component is designed to retrieve information about a user. Within a dataflow, this step is used to query user data based on specified criteria, such as a username or other identifying information. For example, within a dataflow, you can specify a user's name to retrieve information about them and then use this information for further actions, such as displaying it on a screen or updating a database.

- You can download the component configuration [here](https://drive.google.com/file/d/16keZXK_MXlWLmcSA4a-nLvhx-GPP3RPy/view?usp=sharing)