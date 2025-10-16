# Text area

![](../../assets/images/app-development/text-area.png)

## General information
Text area is a basic UI component designed to input and display multi-line text. It is ideal for typing large amounts of text, such as comments or descriptions, and provides enough room for easy typing.

## Parameters
**Component Properties:**

| Settings group | Setting Field   | Value Options         | Purpose |
|----------------|------------------|---------------------------|------------|
| (Global settings)        | Name             | -                         | Name of the UI Component in the system |
| Common         | Disabled         | true, false               | Disabling an element |
|                | Auto size        | true, false               | Automatic dimension control |
|                | Required         | true, false               | Required field to fill out |
|                | Label            | -                         | Input field description |
|                | Binding          | Multiselect of Catalog | Data binding |
| Events         | On value changed | -                         | Value change event |
| Tab index      | -                | Integer               | Field switching order |

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
- **Multi-Line Input**: Ideal for forms that require large amounts of text.
- **Comments & Descriptions**: Used to write comments, descriptions, or any other script where multi-line input is required.

## Exceptions
- **Limited Formatting**: Like most text input fields, the text area restricts the use of complex formatting, such as hyperlinks or embedded images.
