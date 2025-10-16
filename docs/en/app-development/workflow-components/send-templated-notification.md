# Send templated notification

![](../../assets/images/app-development/send-templated-notification-workflow.png)

## General information
The “Send Templated Notification” step within the workflow is used to send notifications to users or groups of users using preconfigured templates. This allows you to create standardized yet personalized messages, which improves communication and ensures consistency of messages.

## Parameters
**Step Settings:**

| Setting Field    | Value Options        | Purpose |
|-------------------|--------------------------|------------|
| Step name         | -                        | Name of the step |
| Notification type | Smtp, Mail, SignalR      | Type of notification delivery channel |
| User info field   | Multiselect of Catalog | Field with information about a user or group of users |
| User group        | Multiselect of Catalog | (Outdated parameter, not used) |
| User routing      | Multiselect of Catalog | Configuration of notification routing |
| User name         | Multiselect of Catalog | Specific user to be notified |
| Template          | Multiselect of Catalog | Choosing a notification template |
| Render type       | Text, Html, Docx, Xlsx   | Template rendering format |

## Cases
- **Automated Notifications**: Used to send standardized notifications, such as reminders, action confirmations, or informational messages.
- **Effective Communication**: Suitable for creating professionally designed messages for external or internal communications.

## Exceptions
- **Template Customization Requirements**: Notification templates must be prepared and configured in advance to ensure that messages are relevant to communication purposes.
- **Manage Notification Recipients**: It is important to pinpoint message recipients using the User info field and User name to ensure that notifications reach the right recipients.

