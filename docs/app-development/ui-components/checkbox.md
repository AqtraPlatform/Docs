# Checkbox

![](../../assets/images/app-development/checkbox.png)

## General information
A “Checkbox” is an interface element that allows users to select or deselect a specific parameter or option. This component is widely used to create parameter lists, manage settings, or select multiple options at once.

## Parameters
**Component properties**

| Settings group | Setting field | Value Options | Purpose |
| --- | --- | --- | --- |
|  | Name | - | Name of the UI Component in the system |
| Common | Disabled | true, false | The property allows you to disable an element on the form |
|  | Required | true, false | The property makes the element required to be filled out prior to submitting the form |
|  | Label | - | Contains the table of contents of the text container |
|  | Binding | Multiselect of Catalog | Contains a related “Boolean” field from the model |
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
|  | BorderBrush | - | The property sets the color of the element's border |

## Cases
- **Option Selection**: Users can select or deselect certain parameters or options.
- **Settings Management**: Checkbox is used to enable or disable certain settings or features.
- **Multiple Selection**: In the Checkbox group, users can select multiple options at the same time.

## Exceptions
- **Unintuitive Interface:** With a large number of checkboxes on a page or in complex forms, users may have difficulty choosing options.
- **Unclear Formulations:** If Checkbox formulations are not informative or unclear, users may not understand what they are choosing.

