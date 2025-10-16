# Pdf viewer

![](../../assets/images/app-development/pdf-viewer.png)

## General information
The PDF Viewer component allows you to view and interact with PDF documents directly in the user interface. This component is useful for displaying PDF files such as reports, instructions, and other documents.

## Parameters
**Component properties**

| Settings group | Setting field | Value Options | Purpose |
| --- | --- | --- | --- |
|  | Name | - | Name of the UI Component in the system |
| Common | Binding | Multiselect of Catalog | Contains a related “File” field from the model |
|  | File | Button | Allows you to upload a file with a .pdf extension |

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
- **Viewing Reports:** Allows users to view reports and documentation in PDF format.

## Exceptions
- **Format Limitations:** PDF Viewer supports standard PDF documents but may not correctly display complex formats or protected documents.
- **Performance:** Using large PDF documents or a large number of interactive elements can affect performance.

