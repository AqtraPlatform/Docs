# Send templated notification

![](../../assets/images/app-development/send-templated-notification.png)

## General information
The “Send Templated Notification” step is designed to send notifications to users or groups of users using pre-configured templates. This step provides flexibility in choosing the delivery method and the recipients of the notification.

## Parameters
**Step Settings:**

| Setting Field  | Value Options   | Purpose |
|-----------------|---------------------|------------|
| Step name       | -                   | Name of the step |
| Source step     | -                   | Selecting the previous step | 
| Notification type | Smtp, Mail, SignalR| Type of notification delivery channel |
| User info field | - | List of users to be notified |
| User routing    | - | Routing the user to deliver the notification |
| User name       | - | Specific user to be notified |
| Template        | - | Selection from pre-configured notification templates |
| Render type     | Text, Html, Docx, Xlsx, Pdf | Type of notification template rendering  |
| Message theme   | Text                 | Subject line for email notifications |

## Cases
- **Automated Notifications**: Used to send notifications to users using preset templates to ensure consistent and accurate messages.
- **Flexibility of Message Delivery**: Allows you to choose between different delivery channels (e.g., SMTP, Mail, SignalR) which increases the coverage and efficiency of communications.
- **Notification Personalization**: Supports customizing notifications for specific users or groups, as well as various content formats (text, HTML, Docx, Xlsx).

## Exceptions
- **Requirement of a Configured Delivery Channel**: In order for notifications to be sent successfully, you must have a functioning delivery channel, such as an SMTP server for email notifications.
