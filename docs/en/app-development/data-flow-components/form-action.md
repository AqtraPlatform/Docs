# Form action

![](../../assets/images/app-development/form-action.png)

## General information
The “Form Action” step is used for performing various actions in the user interface (UI) in the frontend of the application, such as opening pages, executing scripts, opening modal windows, etc. The step is the link between the server logic and the user interface allowing you to dynamically control the behavior of the UI.

## Parameters
**Step Settings:**

| Setting Field | Value Options | Purpose |
|----------------|-------------------|------------|
| Step name      | -                 | Name of the step |
| Source step    | Multiselect of Catalog | Selection from the previous steps |
| Form action    | Execute script, Open page, Open component, Open Sidebar, Open Modal, Open file in new tab | UI command type |
| Method name    | (If ‘Execute script’ is selected) | Name of the script function to execute |
| Open page      | (If ‘Open page’ is selected) | List of pages to open |
| File info field | (If ‘Open file’ in new tab is selected) | File information field to open |
| Open sidebar   | Settings for the sidebar | Configuring to open the sidebar |
| Open modal     | Settings for modal windows | Configuring to open a modal window |

## Cases
- **Dynamic UI Element Management**: Using an “Open Sidebar” or “Open Modal” allows you to dynamically display sidebars or modals with additional information, forms, or other content, which increases the interactivity and usability of the interface.
- **Data Grid Update**: In a script where the user loads some new data, you can add a refresh function to the form and the datagrid will be updated without refreshing the page.

## Exceptions
- **Write Response Step Required**: After performing actions such as opening a page or file, you need to add a “Write Response” step to complete the Dataflow correctly.
- **Dependency on Previous Steps**: When using certain actions, such as “Open file in new tab”, you need to have an appropriate file prepared by the previous steps.

## Application scenario

This component employs various methods in the Form action step to interact with the user interface on the frontend. Users can perform different actions such as executing a script (Execute Script), opening a page (Open page) or a component (Open component), downloading a file (Download file), and opening a file in a new tab (Open file in new tab). After these actions are executed, the data is processed and sent back to the frontend using the Write response step.

- You can download the component configuration [here](https://drive.google.com/file/d/1AgjjrOW-z2LPMj7sFWg_PKjHjFfVtxub/view?usp=sharing)