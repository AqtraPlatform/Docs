# Switch

![](../../assets/images/app-development/switch.png)

## General information
The “Switch” component is an interface element that allows the user to enable or disable a specific function, option, or state. This component is often used to provide the ability to quickly switch between two states (True/False).

## Parameters
**Component properties**

| Settings group | Setting field | Value Options | Purpose |
| --- | --- | --- | --- |
|  | Name | - | Name of the UI Component in the system |
| Common | Disabled | true, false | The property allows you to disable an element on the form |
|  | Required | true, false | The property makes the element required to be filled out prior to submitting the form |
|  | Label | - | Contains the table of contents of the text container |
|  | Binding | Multiselect of Catalog | Contains a related “Catalog” field from the model |
| Events | On value changed | - | Allows you to run the specified script after changing the value of the field |

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
|  | BorderBrush | - | The property sets the color of the element's border |.

## Cases 
- **Binary Selection:** Switch is used for binary selections such as on/off sound, notifications, and other options.
- **State Management:** You can use Switch to manage the state of a particular interface element.

## Exceptions
- **Unclear Status:** If it is not obvious what the enabled and disabled status means, users may be confused.

