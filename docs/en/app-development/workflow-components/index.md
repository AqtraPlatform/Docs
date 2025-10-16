# Workflow

## What is workflow? {: #workflow }

Workflow is a mechanism for managing states and tasks in various component scripts on the platform. It allows you to organize the sequential execution of tasks, maintaining states and providing the ability to restart in case of failure.

### How do I create a workflow?

1. **Open Toolbox**: Open the Toolbox menu in the components window and go to the Flows tab.
2. **Add Workflow**: Click on the Workflow icon and drag it to the workspace. A new workflow will appear to be configured.

Using Visual builder of Workflow, you can configure a workflow script:

- **Adding Stages and Steps**: The editor allows you to add Stages and Steps that form the workflow logic.
- **Sequence Configuring**: Scripts are run from top to bottom and left to right, allowing you to create a consistent flow of tasks.

### Workflow Parameters

- **Workflow name**: The name used to identify the workflow in the component.
- **Restrict Access**: When set to "Yes", creates a security context for workflow.

### Editing Workflow Stages and Steps

- **Add Stages**: Using the "+" button, you can add new stages.
- **Delete Stages**: The "X" button allows you to delete unnecessary stages.
- **Edit Stages**: Only the stage name can be changed.
- **Add and Delete Steps**: Steps can be added and removed within stages, defining specific workflow actions.

## Notifications Group

Components for sending notifications and confirmations:

- [Notifications Steps](notifications-steps.md) - Overview of notification steps
- [Send Notification](send-notification.md) - Send notifications to users
- [Send Templated Notification](send-templated-notification.md) - Send template-based notifications
- [Get User Confirmation](get-user-confirmation.md) - Request user confirmation

## Integrations Group

Components for integrating with other systems:

- [Integrations Steps](integrations-steps.md) - Overview of integration steps
- [Execute Dataflow](execute-data-flow.md) - Execute dataflow from workflow

## Common Group

Common workflow operations:

- [Common Steps](common-steps.md) - Overview of common steps
- [Update Model](update-model.md) - Update data model
- [Finish](finish.md) - Complete workflow execution
- [Update Model Field](update-model-field.md) - Update specific model field
- [Reset to Draft](reset-to-draft.md) - Reset workflow to draft state

## Conditions Group

Conditional logic and branching:

- [Conditions Steps](conditions-steps.md) - Overview of condition steps
- [Switch Case](switch-case.md) - Switch-case branching
- [If Condition](if-condition.md) - Conditional branching
