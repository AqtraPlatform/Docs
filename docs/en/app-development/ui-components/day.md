# Day

![](../../assets/images/app-development/day.png)

## General information
Day is a UI component designed to display or select individual days. This element is commonly used in calendars or date sensors, allowing the user to select specific days to complete tasks or set reminders.

## Parameters
**Component properties**

| Settings group | Setting field | Value Options | Purpose |
| --- | --- | --- | --- |
|  | Name | - | Name of the UI Component in the system |
| Common | Format | - | The property allows you to [configure](https://docs.microsoft.com/ru-ru/dotnet/standard/base-types/custom-date-and-time-format-strings) the date and time display |
|  | Disabled | true, false | The property allows you to disable an element on the form |
|  | Required | true, false | The property makes the element required to be filled out prior to submitting the form |
|  | Label | - | Contains the table of contents of the text container |
|  | Binding | Multiselect of Catalog | Contains a related “Date” field from the model |
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
- **Date Picker**: Used to select specific days in interfaces where precise date selection is required.
- **Event Display**: Can be used to display events or reminders scheduled for specific days.

## Exceptions
- **Limited Functionality**: The Day component is limited to displaying and selecting days, and is not suitable for displaying wider time intervals.
