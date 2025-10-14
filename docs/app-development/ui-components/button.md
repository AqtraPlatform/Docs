# Button

![](../../assets/images/app-development/button.png)

## General information
A Button is the main UI component used to execute commands or initiate actions in an application. It can be configured to run processes, confirm user actions, or serve as a navigation tool.

## Parameters
**Component Properties:**

| Settings group | Setting Field   | Value Options         | Purpose |
|----------------|------------------|---------------------------|------------|
| (Global settings)        | Name             | -                         | Name of the UI Component in the system |
| Common         | Icon             | -                         | Icon loading (.svg) |
|                | Disabled         | true, false               | Disabling an element |
|                | Label            | -                         | Button text |
| Text           | Font size        | -                         | Size of the font |
|                | Color            | -                         | Text color (CSS) |
|                | Bold             | true, false               | Bold font |
|                | Italic           | true, false               | Italic font |
|                | Text alignment   | Left, Right, Center, Justify | Text alignment |
| Actions        | Command type     | Various commands         | Action by button click  |
|                | Restrict access  | true, false               | Access limitation |

**CSS Properties:**

| Settings group | Setting Field   | Value Options         | Purpose |
|----------------|------------------|---------------------------|------------|
| Layout         | Width            | -                         | Component width |
|                | Height           | -                         | Component height |
|                | Grow             | true, false               | Component stretching |
|                | Margin           | -                         | Outer padding |
|                | Padding          | -                         | Inner padding |
| Appearance     | CornerRadius     | -                         | Corner radius |
|                | BorderThickness  | -                         | Border thickness |
| Brush          | Background       | -                         | Background color |
|                | BorderBrush      | -                         | Border color |

## Cases
- **Form Submission**: Using a button to submit form data to the server or to initiate processing of form data in the application.
- **Navigation**: Assignment of a button to navigate between different screens or sections of the application.
- **Interactive Elements**: Creation of buttons to control interactive elements, such as changing content on a page.

## Exceptions
- **Limitations on the Number of Actions**: Only one action can be assigned to a button (execute dataflow, execute script, etc.).

