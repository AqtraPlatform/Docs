# Release descriptions

!!! note "The Aqtra Platform is constantly evolving!"
New versions are normally released once a month for:

    - Kubernetes cluster
    - Docker mini-image

<br>

## Version 0.13.x

> **Functionality Added**

- **New Component Module**: Within the component, the \*\*Web parts\*\* module has been added, which consists of two blocks: “Styles” and “JavaScript”. This module is similar to the “Component Script” module, but instead of interacting with Python, you can describe CSS styles in the “Styles” block and interact in JavaScript in the “JavaScript” block;
- **Setting up Global Modules in the Aplication domain**: Setting up global CSS and JavaScript modules have been added in the **Main settings\*\* of **Application domain\*\*. More details \*\*here\*\*;
- **New Tools in the Maintenance Menu**: A setting has been added for the **File storage\*\* section. More details **here\*\*;
- **New Object Model Settings for File Type Data**: Now you can set validation by file type and limit on file size in bytes;
- **XSRF/CSRF Support**: The file upload component now eliminates binary data transfer via JS and adds XSRF sending. Requests for downloading files are now targeted and direct access to file-storage is excluded. Improvements have also been made to the work-place to receive an XSRF token when loading a page, and the OData controller has been improved to load files. Sending requests from work-place to download files is now also targeted, and direct access to file-storage is impossible.
  <br>

> **Design Updated**

- **Export/Import Section**: The design of the export/import section of the \*\*Applications\*\* menu has been updated.
  <br>

## Version 0.12.x

> **Functionality Added**

- **Send Notification**: A new step in Dataflow “Send notification” has been added. This step allows you to send simple notifications to the user, which enhances the way you interact with the user via the notification system. More details here: \*\*Send notification\*\*
- **Pivot Grid**: A new UI element “Pivot Grid” has been added for data analysis and visualization. More details here: \*\*Pivot grid\*\*
- **Changes to **List view\*\*\*\*:
  - Ability to expand the component horizontally or vertically.
  - The ability to enable Drag & Drop has been added for all groups of a component or by choice.
  - Enabling function has been added to Events after using Drag & Drop.
- **Changes to **Data grid\*\*\*\*:
  - The multiselect mechanism has been changed. In the Data grid settings there is now a “Selection Mode” option with a choice: `None`, `Single`, `Multiple`, `Checkbox`.
  - New events: `On Table Changed`, `On Header Changed`, `On Row Changed`, `On Cell Changed`.
  - Ability to select the number of lines in the paginator at the front.
- **Changes in **Chart View\*\*\*\*:
  - Color Scheme setting has been removed.
  - Min/Max settings have been added.
- **SIP Client Integration**:
  - Ability to make calls from Workplace thanks to SIP client integration. More details \*\*here\*\*.
- **Placeholder images for missing images in the settings of application domains and the UI "Image" element**: More details in [User Interface documentation](user-interface/index.md) and [Image component](app-development/ui-components/image.md).
- **New methods for managing the state of UI elements**. More details in \*\*documentation\*\*.
- **Bulk Upload of Images Via http.client and File Storage in Dataflow scripts**: A function for bulk upload of images has been added. More details in \*\*documentation\*\*.
- **Optimization of the Publishing Mechanism**: The publishing mechanism has been improved using a state machine, providing a stable process with the ability to roll back in case of errors. More details in \*\*documentation\*\*.

<br>

## Version 0.10.x

> **Functionality Added**

- A new dataflow step “Get file info” has been created, allowing you to obtain information about a file by its identifier. More details in the documentation: \*\*Get file info\*\*
- Added a filter for the “Component” field inside the “Get entity by id” dataflow step. More details here: \*\*Get entity by id\*\*  
  <br>

> **Design Update**

- “Dashboard” main page. More details here: \*\*Dashboard\*\*
- “Navigation menu” has been removed from the “Applications” menu and is now located on the main page. More details here: \*\*Navigation menu\*\*
- Dataflow steps design has been updated. More details here: \*\*Available Dataflow steps\*\*
- “File storage” design has been updated. More details here: \*\*File storage\*\*
- The “System maintenance” design has been updated. More details here: \*\*System maintenance\*\*
  <br>

## Version 0.9.x

> **Functionality Added**

- System-specific (Platform-specific) features
  - User interface uploading: optimization of UI component compilation.
  - Refactoring of the \*\*Maintenance menu\*\*. Moving control buttons to the “System maintenance” tab, and displaying logs with their settings in the “System logs” tab.
  - Job queue storage generator in Redis.
  - IronPython has been updated from version 2.7.12 to 3.4.1 on Workplace.
- User-specific (Studio-specific) features - Copy/paste elements in \*\*interface builder\*\* on the component page. - Adding files to the root of the [file storage](user-interface/file-storage.md). - Ability to use the Data Model of the reference components (Catalog) in the component element ribbon bar for: `DataGrid`, `ListView`, `TreeView`.
  <br>

> **Interface Changes**

- Refactoring of the studio main menu:
  - moving the following elements to the right corner of the top ribbon bar: localization switch and button to log out of the current account (logout),
  - the Profile item of the main menu has been removed.
- The icon for the Python Modulesmenu item has been redesigned.
- Online help icons have been added in many sections of the Studio: dataflow steps, buttons for user interface elements (Toolbox UI), main application parameters, as well as in many other locations in the studio to ensure a faster access to online help on the documentation site.  
  <br>

> **Key bugs fixed**

- Correction of the `Cron` task scheduler operation during import/export of components.
- Elimination of the `changeAuthor` duplicate from the component data model.
- Stabilization of workflow step selection.
- Correction of the `Number` UI element from the component elements panel.
- Fixing the operation of the On focusevent for some of the UI elements: Day, Time, Signature.
  <br>

## Version 0.8.x

> **Important and Improved Functionality Added**

- In the dataflow Form Action step, the Open Sidebar and Open Modal parameters have been added, which allow you to open a sidebar & modal window, respectively, similar to how this can be done via Python script.
- Transferring the required attributes for parameters transferred in the Get Action Model step.
- “Remove assigned roles for user” dataflow step has been added, which removes all current roles assigned to the user, allowing you to create a new set of roles from scratch.
- \*\*Python modules\*\* menu has been added to manage the shared library of Python modules.
- Background setting for UI controls has been added, which allows you to set an image in standard formats (for example, png, svg, jpeg, etc.) as a background for all controls that have a Brush settings section.
- Data model view icon on the dataflow step has been changed to the eye icon.
- “Skip from Synchronize” parameter has been replaced with Virtual Property. Fields marked “Virtual Property” are not saved to the database when the component is recorded.
- Settings for Power Web Application (PWA) in the Edit manifest section have been added.
- Additional Application Domain settings have been added - show breadcrumps, login, locale.
  <br>

> **Important Fixed Errors**

- The work of dynamic filters for Data Grid control has been fixed.
- The “First line to ignore field” in the Import File step is not reset to 0 after saving.
- The default color for the application domain applies to controls of the button type that do not have a default color set.
- Permissions for a multicomponent are not set in restrict access mode.
  <br>

## Version 0.7.0

> **Important and Improved Functionality Added**

- When selecting a Default component for an application domain in the Main Settings section, you can select the page that will be opened for this component in the Default page field. If no page is selected, the first page of the component (main page) will be opened by default.
- A new “Execute Dataflow” step has been added to dataflow, which allows you to launch new dataflows, including dataflows from other components, within the current dataflow.
- The outdated “Get Audience” dataflow step has been removed, and the “Form Action” step has been moved to the “Model Transformation” group. The “Other” group has been removed completely.
- Search for configuring “Field mapping” has been added for the “Apply Deferred update operations” step.
- For the UI control \*\*Text Area\*\*, an Auto-size option has been added, which allows you to expand the size of the field if you need to enter a larger amount of text.
- The “Query Entity by Filter” dataflow step has been optimized via automatic creation of indexes and database normalization.
- Notice of imminent license expiration has been added. The message appears 10 days before the expiration date of the current license.
- Swagger APIs generated for Dataflow now show the Dataflow name as the API name.
- The ability to request user geolocation from Component Script via the context.PlatformServices.GeolocationPosition function has been added.
- The ability to set the default locale setting for application domain has been added in the Main Settings section.
- The ability to set a favicon for the application domain has been added in the settings of the Home Menu: Domain: Main Settings.
  <br>

> **Important Fixed Errors**

- The work of dynamic filters for Data Grid control has been fixed.
- An issue where an error occurred when sorting fields retrieved from Catalog type links has been fixed.
- Data grid stability, including phantom errors when navigating through the Data grid, has been improved.
- An issue with the search form being cut off in the Data Grid when clicking on a filter has been fixed.
- Output of string values ​​for Enum has been added.
- Incorrect system operation with remote logout has been fixed.
- Incorrect operation of the timer in the “Apply deferred update operations” step has been fixed.
- For UI controls of the Label type, bound to a field of the Catalog type, the Color setting is now processed correctly.
  <br>

## Version 0.6.x

> **Important and Improved Functionality Added**

- Advanced features for managing the main application menu - building hierarchical menus and setting menu icons.
- Improved work with Python scripts - highlight for Python syntax, auto-complete for Python system methods, as well as auto-complete and tips for methods of built-in platform libraries have been added (available via Ctrl-Space under Win10/11, and Option-Space under MacOS).
- The ability to build additional sidebar windows via Component Script has been added.
- The ability to build complex modal windows via Component Script with data transfer from modal windows to the calling script has been added.
- The Component Script call has been moved to the main menu.
- Localization of Studio into Russian has been completed.
- In the DataGrid control, it is now possible to select arbitrary fields of an external component when displaying reference fields of the Catalog type.
- Import-export now includes export and subsequent import of permissions and roles (exporting files created using version 0.6.x to previous versions will work, but will not import included roles and permissions).
- Import-export now checks for related components and warns the user if any related components were not included in the export list.
- At the platform level, the ability to mark entries (component instances) as available for physical deletion has been added via a flag in the dataflow “Update Entry” step.
- The ability for the Studio admin to get a list of entries marked for deletion and remove those that do not have links to entries that are not marked ready for deletion has been added.
  <br>

## Version 0.5.24

> **Important and Improved Functionality Added**

- Advanced capabilities for dynamic and static filters in advanced controls such as Data Grid, List View, Tree View, allowing on-the-fly filtering of data before display to the user (parameters have been added for filters of the contains type, etc.).
- Expanding the concept of utilizing Dataflow & Workflow - now both can be created and used separately from UI controls such as buttons, which allows for a more flexible application structure and simplifies development.
- Many new methods available via [Using Python](app-development/using-python.md) in Component Script have been added, such as calling modal windows, checking screen resolution and device type to create a responsive UI layout.
- The ability to work with message queue systems (for example, RabbitMQ) from dataflow with a new step [Subscribe to Connector](app-development/data-flow-components/subscribe-to-connector.md) has been added.
- The ability to batch data processing in Dataflow via new steps [Deferred Update Entry](app-development/data-flow-components/deferred-update-entry.md) & [Apply Deferred Update Operations](app-development/data-flow-components/apply-deferred-update-operations.md) has been added.
  <br>

## Version 0.4.4

> **Important and Improved Functionality Added**

- New system storage field “Name” has been added, used to display items from Catalogs.
  - When showing a single element from Catalog (for example, using a UI control Select that references Catalog), the contents of the Name field will now always be shown. If the Name field is empty, the system Catalog name/sequence number of the Catalog entry will be shown.
- Default sorting settings for Datagrid and Listview have been added.
- Automatic replacement of Unicode special characters in Component Script for link generation has been added.
  <br>

> **Mistakes Corrected**

- Incorrect operation of the paginator concerning switching several tables on one page has been fixed.
- Not working Scrolling function in some parts of the Studio has been fixed.
  <br>

## Version 0.3.223

_Kubernetes cluster 0.3.223 | Docker mini-image 0.2.118_

> **Important and Improved Functionality Added**

- New data-flow step “Send templated notification” has been added, which allows you to send a notification by email using a specified template.
- Transparency property for UI components.
- Support for OAuth2 authorization for HTTP requests has been added. You can now configure automatic token generation via OAuth to connect to the API.
- The “Store response as file” parameter has been added in the “Execute API call” step to allow you to download a file via the API upon request.
- The steps no longer generate a newsletter, they now generate a field in the model for later use, such as “Send templated notification”.
  <br>

> **Mistakes Corrected**

- Errors when working with the Datetime type in the calendar have been fixed.
- UI in the Studio and Workplace has been fixed.
- The Disabled state for the Radiobutton UI component has been fixed.
- Localization errors have been fixed.
- Search in Dropdown is now case insensitive.
- Authorization operation including log-out issues has been fixed. <br>
