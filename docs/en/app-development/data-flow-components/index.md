# Dataflow

## What is dataflow? {: #dataflow }

Dataflow, or data flow, in the platform is a key component that allows users to process and transform data within an application. This is a powerful tool for integrating data, processing events and automating business processes.

Dataflow is built on the platform using a 'visual editor' of the data flow:

The visual data flow editor is an intuitive designer for creating and managing data flows. This tool allows users to sequentially create a set of Stages and Steps to implement complex data processing scripts.

- **Add Stage**: This is done by pressing the "+" icon on the data flow control panel. You can add an unlimited number of stages depending on the needs of your script.
- **Delete Stage**: To delete a stage, use the "X" button on the selected stage block.
- **Edit Stage**: You can only edit the name of the selected stage.
- **Add Step**: A new step is added by pressing the "ADD STEP" button at the appropriate stage. Users can choose step types from the proposed activity groups.
- **Delete Step**: To delete a step, click on the "X" icon on the selected step block.

## Input Group

Components for retrieving and importing data:

- [Input Steps](input-steps.md) - Overview of input steps
- [Get Values from Connector](get-values-from-connector.md) - Retrieve data from connectors
- [Subscribe to Connector](subscribe-to-connector.md) - Subscribe to data updates
- [Get Action Model](get-action-model.md) - Retrieve action model
- [Get Workflow Model](get-workflow-model.md) - Retrieve workflow model
- [Get Empty Model](get-empty-model.md) - Create empty data model
- [Proxy Get Entry](proxy-get-entry.md) - Proxy entry retrieval
- [Proxy Query Entry](proxy-query-entry.md) - Proxy query execution
- [Get Raw Model](get-raw-model.md) - Retrieve raw data model
- [Import File](import-file.md) - Import data from files

## Model Transformation Group

Components for data transformation and processing:

- [Model Transformation Steps](model-transformation-steps.md) - Overview of transformation steps
- [Transform Model](transform-model.md) - Transform data models
- [Join Models](join-modes.md) - Join multiple data models
- [Extract Collections](extract-collections.md) - Extract collection data
- [Filter Source](filter-source.md) - Filter data sources
- [Lookup Reference](lookup-reference.md) - Reference lookup
- [Execute Script](execute-script.md) - Run custom scripts
- [Query Entity by Filter](query-entity-by-filter.md) - Filter-based queries
- [Select Many](select-many.md) - Multiple selection
- [Get Entity by ID](get-entity-by-id.md) - Retrieve by identifier
- [Load Catalogs by Key](load-catalogs-by-key.md) - Load catalog data
- [Distinct](distinct.md) - Get distinct values
- [Group By](group-by.md) - Group data
- [Calculate Array](calculate-array.md) - Array calculations
- [Simple Math](simple-math.md) - Mathematical operations
- [Execute Dataflow](execute-dataflow.md) - Execute nested dataflow
- [Get File Info](get-file-info.md) - Retrieve file information

## User Contexts Group

Components for user management and authentication:

- [User Contexts Steps](user-contexts-steps.md) - Overview of user context steps
- [Register Context for Model](register-context-for-model.md) - Register model context
- [Register External User](register-external-user.md) - External user registration
- [Prepare External Keys](prepare-external-keys.md) - Prepare authentication keys
- [Assign Context Role for Model](assign-context-role-for-model.md) - Assign roles
- [Get One-Time Code for User](get-one-time-code-for-user.md) - Generate OTP
- [Confirm One-Time Code for User](confirm-one-time-code-for-user.md) - Verify OTP
- [Update or Create User Info](update-or-create-user-info.md) - User information management
- [Get User Info](get-user-info.md) - Retrieve user data
- [Login with Password](login-with-password.md) - Password authentication
- [Reset User Password Request](reset-user-password-request.md) - Password reset
- [Confirm User Email Request](confirm-user-email-request.md) - Email verification
- [Send Templated Notification](send-templated-notification.md) - Template-based notifications
- [Send Notification](send-notification.md) - Send notifications
- [Remove Assigned Roles for User](remove-assigned-roles-for-user.md) - Remove user roles

## Output Group

Components for data output and actions:

- [Output Steps](output-steps.md) - Overview of output steps
- [Store Entry over Bus](store-entry-over-bus.md) - Store data via message bus
- [Update Entry](update-entry.md) - Update data entries
- [Deferred Update Entry](deferred-update-entry.md) - Deferred updates
- [Apply Deferred Update Operations](apply-deferred-update-operations.md) - Apply deferred operations
- [Execute API Call](execute-api-call.md) - External API calls
- [Write Response](write-response.md) - Write response data
- [Form Action](form-action.md) - Form submission actions
- [Execute Workflow](execute-workflow.md) - Execute workflow
- [Export to File](export-to-file.md) - Export data to files
- [Render Template](render-template.md) - Template rendering
