# Password

![](../../assets/images/app-development/password.png)

## General information
Password is a basic UI component designed for entering passwords in a secure form. This component is used to create password entry fields, ensuring the confidentiality and protection of the entered data.

## Parameters
**Component properties**

| Settings group | Setting field | Value Options | Purpose |
| --- | --- | --- | --- |
|  | Name | - | Name of the UI Component in the system |
| Common | Disabled | true, false | The property allows you to disable an element on the form |
|  | Required | true, false | The property makes the element required to be filled out prior to submitting the form |
|  | Show clear | true, false | Shows the clear (reset) icon of the field value |
|  | Auto complete |  | Field for setting the value of the autocomplete HTML attribute. As a rule, use username for the name input field, and password, new-password, or current-password for the corresponding input fields for different password types. Works in conjunction with the Provide Root Form parameter for Page UI control. |
|  | Label | - | Contains the table of contents of the text container |
|  | Binding | Multiselect of Catalog | Contains a related “String” field from the model |
| Events | On value changed | - | Allows you to run the specified script after changing the value of the field |
|  | On key down |  | Allows you to run the specified script after moving to the next page element (tab) |
|  | On key up |  | Allows you to run the specified script after moving to the previous page element (tab) |
|  | On focus |  | Allows you to run a script the moment an element is focused on |
| Tab index |  | Positive integer starting from zero | Sets the order in which active (editable) fields are toggled via the keyboard (for example, using the Tab key) |
| Automation ID |  |  | Control ID for automated tests and for transferring CSS settings |

**CSS properties**

| Settings group | Setting field | Value Options | Purpose |
| --- | --- | --- | --- |
| Layout | Width | - | Component width |
|  | Height | - | Component height |
|  | Grow | true, false | The property determines how much an element will grow relative to the rest of the flex elements within the same container |
|  | Margin | - | The property defines the outer paddings on all four sides of the element |
|  | Padding | - | The property sets the inner paddings on all sides of the element |
| Appearance | CornerRadius | - | The property is used to round the corners of an element |
|  | BorderThickness | - | The property allows you to set the boundaries for the element |
| Brush | Background | - | The property sets the background color of the element |
|  | BorderBrush | - | The property sets the color of the element's border |

## Cases
- **Authentication Forms**: Used in login and registration forms for securely entering passwords.
- **Interactive Forms**: Enabling interactive forms that require confidential data entry.

## Exceptions
- **Formatting Limitations**: Does not support complex text formats such as hyperlinks or embedded images.