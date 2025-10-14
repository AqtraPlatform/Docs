# Date / Time

![](../../assets/images/app-development/date-time.png)

## General information
Date/Time is a UI component for entering and displaying date and time. It is designed to provide a user-friendly interface for selecting the date/time, as well as to display this data in a specific format.

## Parameters
**Component Properties:**

| Settings group | Setting Field   | Value Options         | Purpose                 |
|----------------|------------------|---------------------------|----------------------------|
| (Global settings)        | Name             | -                         | Name of the UI Component in the system |
| Date Time      | Format           | Date, Time, Date & Time | Display Format         |
|                | Default value    | -                         | Default value      |
|                | Min date         | -                         | Minimum Date           |
|                | Max date         | -                         | Maximum Date          |
| Common         | Binding          | -                         | Binding to Data          |
|                | Required         | true, false               | Required to fill out  |

**CSS Properties:**

| Settings group | Setting Field   | Value Options         | Purpose                 |
|----------------|------------------|---------------------------|----------------------------|
| Layout         | Width            | -                         | Component width          |
|                | Height           | -                         | Component height          |
|                | Margin           | -                         | Outer padding             |
|                | Padding          | -                         | Inner padding          |
| Appearance     | CornerRadius     | -                         | Corner radius          |
|                | BorderThickness  | -                         | Border thickness              |
| Brush          | Background       | -                         | Background color                  |
|                | BorderBrush      | -                         | Border color                 |

## Cases
- **Event Date Selection**: Used to select a date in the calendar or to set the time of the event.
- **Filter by Date**: Can be used in filters to filter data by date/time.
- **Display Time Intervals**: Suitable for tasks that involve displaying time intervals, such as in job schedulers.

## Exceptions
- **Formatting**: Date/Time is not intended for free text input, but is used strictly for working with dates and time.
