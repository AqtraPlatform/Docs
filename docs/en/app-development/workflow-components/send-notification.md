# Send notification

![](../../assets/images/app-development/send-notification-workflow.png)

## General information
The “Send Notification” step within workflow is used to send simple notifications to a user or group of users using a bell icon. This allows you to communicate effectively with system users by transmitting important information or notifications.

## Parameters
**Step Settings:**

| Setting Field    | Value Options   | Purpose |
|-------------------|---------------------|------------|
| Step name         | -                   | Name of the step |
| Notification type | Smtp, Mail, SignalR | Type of notification delivery channel |
| User info field   | Multiselect of Catalog | Field containing user or list of users |
| User name         | Multiselect of Catalog | Specific user to be notified |
| Message           | -                   | Notification text |

## Cases
- **User Information**: Used to inform users about important events, system changes, alarms or other messages that need attention.
- **Personalized Notifications**: Allows notifications to be sent to specific users or groups, making communication more targeted and effective.

## Exceptions
- **Need for Up-to-Date User Information**: Effective notification delivery requires up-to-date user information, including user contact details.
- **Selecting the Correct Delivery Channel**: You must carefully choose the type of delivery channel (Smtp, Mail, SignalR) depending on users’ preferences and technical capabilities of the system.
