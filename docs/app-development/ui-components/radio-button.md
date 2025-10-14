# Radio button

![](../../assets/images/app-development/radio-button.png)

## General information
The “Radio Button” component is an interface element that allows the user to select one of the provided options. This component is used to implement the selection of a single element from several mutually exclusive options.

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
|  | On focus |  | Allows you to run the specified script when focused |

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
- **Single Option Selection:** Users can only select one option from the list.
- **Mutually Exclusive Options:** The Radio Button component is used to create a set of mutually exclusive options from which only one can be selected.

## Exceptions
- **Not Enough Information:** If the radio button labels are not sufficiently informative, users may have difficulty selecting options.
- **Difficult Choice:** With a large number of radio buttons or unclear organization, the choice can be difficult for users.

