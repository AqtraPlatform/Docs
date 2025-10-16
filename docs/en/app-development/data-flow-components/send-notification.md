# Send notification

![](../../assets/images/app-development/send-notification.png)

## General information
The “Send Notification” step is designed to send customized notifications to users or groups of users. This step offers a high degree of flexibility, allowing you to directly set the text and subject of each notification, making it ideal for situations that require personalized messages.

## Parameters
**Step Settings:**

| Setting Field   | Value Options | Purpose |
|------------------|-------------------|------------|
| Step name        | -                 | Name of the step |
| Source step      | -                 | Source of the data for sending the notification |
| User info field  | -                 | Field that contains information about the recipients of the notification |
| User name        | -                 | Name of the user to whom the notification will be sent |
| Message body field | -               | Field for the body of the message |
| Message theme    | Text                | Notification subject |
| Message body     | Text                 | Customizable text of the notification  |
| Notification type| Smtp, Mail, SignalR                 | Notification type |

## Cases
- **Personalized Notifications**: Used to create unique messages for each user or situation ensuring maximum relevance and engagement of recipients.
- **Flexible Communication**: Suitable for scripts where special messages are required, such as special offers, individual reminders or personalized newsletters.
 
## Exceptions
- **Message Detail Requirement: Attention to detail and precision should be paid when formulating the text of each notification.
- **Need for Careful Notification Management**: Because each message is individually customizable, it's important to carefully manage the process of creating and sending notifications to avoid errors and inconsistencies.
