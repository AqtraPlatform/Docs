# Progress Bar

![](../../assets/images/app-development/progress-bar.png)

## General information
This UI Component is used to display and configure the progress bar.

## Parameters
**Component properties**

| Settings group | Setting Field | Value Options | Purpose  |
| --- | --- | --- | --- |
|  | Name | - | Name of the UI Component in the system |
| Common | Show value | true, false | The property is used to display the progress bar values |
|  | Determinate | true, false | The property allows you to make the progress bar an animation |
|  | Invert | true, false | The property allows you to invert the progress bar |
|  | Format | - | The property allows you to specify the data output format |
|  | Value | - | The property allows you to set a value |
|  | Binding | Multiselect of Catalog | Contains the associated “Integer” field from the model |
|  | Min value | - | The property allows you to specify a minimum value |
|  | Binding | Multiselect of Catalog | Contains the associated “Integer” field from the model for the minimal value  |
|  | Max value | - | The property allows you to specify a maximum value |
|  | Binding | Multiselect of Catalog | Contains the associated “Integer” field from the model for the maximal value  |

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
|  | Progress | - | The property sets the color of the element's bar |

## Use Cases
- Displaying the progress of tasks, downloads, or other processes.

## Exceptions
- Limited to use for progress presentation and not suitable for other types of visualizations.
