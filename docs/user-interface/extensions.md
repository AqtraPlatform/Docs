# Extensions menu
<br>

The menu consists of 2 blocks:
- **Templates**
- **SMTP settings**
<br>

## Templates

Templates are used for mailing and user notifications and can only be used in the ‘Send Templated Notification’ step. Templates are configured in the ‘Application/Templates’ section.
<br>

### Adding/Removing Templates

- To **add a new template**, click the ‘ADD’ button. 
- To **delete a template**, click on the cross in the common list of all templates.
<br>

### Setting up the template component model

When adding or editing a Template, you must define an Object Model structure that will interact with Dataflow and/or Workflow. This is done by setting a set of properties for each of them, similar to configuring any component.
<br>

### Customizing Template Layout and Content

The platform uses ‘DevExpress Report Designer’ to create templates. These templates can be used to send notifications or create documents.

- After creating a new template, the editing window opens. This is where you can add and customize visual elements to your template, and make links to your template properties.
<br>

## SMTP settings

The mailing service is used to send notifications via SMTP.

Recommendations for using an SMTP server:

- **During Development**: It is recommended to use a corporate SMTP server or shareware services such as [sendinblue.com] (http://www.sendinblue.com/). Avoid using a personal server to avoid getting into spam.
- **For Industrial Use**: It is preferable to use a corporate or paid commercial SMTP service.

Configure the following settings for the mailing service:

| Setting Field | Value Options | Purpose |
| -------------- | ----------------- | ---------- |
| `Sender`       | -                 | Default sender name, e.g. `sender@company.com` |
| `User name`    | -                 | Login for the SMTP server, usually in the `user@company.com` format. |
| `Password`     | -                 | SMTP server password |
| `Host`         | -                 | SMTP server address, e.g. `http://smtp-relay.sendinblue.com/` |
| `Port`         | -                 | Port for the SMTP server depends on the provider, for example 587 for sendinblue.com |
| `Enable SSL`   | `true`, `false`   | Using SSL to encrypt data. ‘True’ is usually used for modern SMTP servers. |

<br>

### Example of using Template and SMTP

1. Create and customize a template.
2. Set up SMTP to send email.
3. In your workflow, add the ‘Send Templated Notification’ step.
4. Select the SMTP notification type and set the parameters for sending e-mail.
5. Choose your template and set the render type in HTML.

After you complete these steps, your workflow will send an email using the customized template.
