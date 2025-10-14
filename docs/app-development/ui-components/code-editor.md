# Code Editor

![](../../assets/images/app-development/code-editor.png)

## General information
Code Editor is a specialized UI component designed for entering and displaying program code. It supports various programming languages ​​such as JavaScript, Python, etc. and provides functionality for easy code editing, but the element does not support a compiler.

## Parameters
**Component Properties:**

| Settings group | Setting Field   | Value Options          | Purpose |
|----------------|------------------|----------------------------|------------|
| (Global settings)        | Name             | -                          | Name of the UI Component in the system |
| Common         | Disabled         | true, false                | Disabling an element |
|                | Required         | true, false                | Required field to fill out |
|                | Theme            | -                          | Editor visual style |
|                | Mode             | -                          | Programming language |
|                | Label            | -                          | Field description |
|                | Binding          | Multiselect of Catalog | Data binding |
| Events         | On value changed | -                          | Value change event |
|                | On key down      | -                          | Key press event |
|                | On key up        | -                          | Key release event |
|                | On focus         | -                          | Event when focusing on an element |
| Tab index      | -                | Integer                | Field switching order |

**CSS Properties:**

| Settings group | Setting Field   | Value Options          | Purpose |
|----------------|------------------|----------------------------|------------|
| Layout         | Width            | -                          | Component width |
|                | Height           | -                          | Component height |
|                | Grow             | true, false                | Component stretching |
|                | Margin           | -                          | Outer padding |
|                | Padding          | -                          | Inner padding |
| Appearance     | CornerRadius     | -                          | Corner radius |
|                | BorderThickness  | -                          | Border thickness |
| Brush          | Background       | -                          | Background color |
|                | BorderBrush      | -                          | Border color |

## Cases
- **Code Editing**: Used to enter and edit program code in various programming languages.
- **Training and Demonstration**: Used for educational and demonstration purposes to show code examples.

## Exceptions
- **Functionality Limitations**: Depending on implementation, may not support all features of advanced development environments.
