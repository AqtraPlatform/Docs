# Text Field

![](../../assets/images/app-development/text-field.png)

## General information
“Text Field” is a UI component designed to display and configure text input and output.

## Parameters
**Component properties**

| Settings group | Setting field | Value Options | Purpose |
| --- | --- | --- | --- |
|  | Name | - | Name of the UI Component in the system |
| Common | Disabled | true, false | The property allows you to disable an element on the form |
|  | Required | true, false | The property makes the element required to be filled out prior to submitting the form |
|  | Label | - | Contains the table of contents of the text container |
|  | Binding | Multiselect of Catalog | Contains a related “String” field from the model |
| Events | On value changed | - | Allows you to run the specified script after changing the value of the field |
| Tab index |  | Positive integer starting from zero | Sets the order in which active (editable) fields are toggled via the keyboard (for example, using the Tab key) |

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
- **Data Entry Forms**: Used to collect text information from users.
- **Interface Settings**: Provides a user interface for entering or modifying text.

## Exceptions
- **Limited Functionality**: Suitable for text input only.
