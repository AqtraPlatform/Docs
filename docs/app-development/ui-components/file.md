# File

![](../../assets/images/app-development/file.png)

## General information
The “File” component provides the ability to load and display files in the user interface. This component is useful for uploading and viewing different types of files, such as images, documents, archives, etc.

## Parameters
**Component properties**

| Settings group | Setting field | Value Options | Purpose |
| --- | --- | --- | --- |
|  | Name | - | Name of the UI Component in the system |
| Common | Max file size in bytes | - | The property allows you to specify the maximum size of the uploaded file in bytes |
|  | Accept files |  | The property allows you to specify the files that are available for download |
|  | Read only | true, false | This property allows you to disable file uploading to forms |
|  | Disabled | true, false | The property allows you to disable an element on the form |
|  | Required | true, false | The property makes the element required to be filled out prior to submitting the form |
|  | Label | - | Contains the table of contents of the text container |
|  | Value | - | - |
|  | Binding | Multiple Choice: Catalog | Reference to the Catalog of File type |
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
- **Document Upload**: Allows users to upload documents, images, and other files.
- **View File Information:** Displays information about the uploaded file, such as its name and size.

## Exceptions
- **Performance**: Downloading large files or a large number of files may affect performance.

