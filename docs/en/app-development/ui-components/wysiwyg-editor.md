# WYSIWYG editor

![](../../assets/images/app-development/wysiwyg-editor.png)

## General information
WYSIWYG editor is a UI component designed for entering and editing rich text in WYSIWYG format. It provides functionality similar to editors like Wordpad, allowing users to easily format text and insert various media elements.

## Parameters
**Component Properties:**

| Settings group | Setting Field   | Value Options          | Purpose |
|----------------|------------------|----------------------------|------------|
| (Global settings)        | Name             | -                          | Name of the UI Component in the system |
| Common         | Disabled         | true, false                | Disabling an element |
|                | Required         | true, false                | Required field to fill out |
|                | Plugins          | -                          | Enabling plugins |
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
- **Text Formatting**: Used to create richly formatted documents and content.
- **Content Editing**: Used in content management systems to facilitate editing articles, blogs, and other text content.

## Exceptions
- **Interface Complexity**: May be difficult to use for users without experience with similar editors.
- **Technical Limitations**: Depending on implementation, may not support all features of advanced text editors.
