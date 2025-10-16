# Data Grid

![](../../assets/images/app-development/data-grid.png)

## General information
Data Grid is a powerful UI component designed to display and interact with large amounts of data in tabular form. This component is ideal for presenting data as rows and columns, as well as providing sorting and filtering functionality.

## Parameters
**Component Properties:**

| Settings group | Setting Field      | Value Options        | Purpose                          |
|----------------|---------------------|--------------------------|-------------------------------------|
| (Global settings)        | Name                | -                        | Name of the UI Component in the system   |
|                | Columns             | -                        | Defining columns and their properties   |
|                | Component           | Multiselect of Catalog | Contains a list of all Components |
|                | Static filters      | Button                  | Used to specify static filters |
|                | Dynamic filters     | Button                  | The property is used to specify dynamic filters |
|                | Page size           | -                        | Size of the page                     |
|                | Manual reload       | -                        | Manual data reload          |
|                | Selection mode      | none, single, multiple, checkbox | Item selection mode          |
|                | Automation id       | -                        | ID for automation     |
| Events         | On datasource loaded | - | Data source load event|
|                | On rows selected    | -             | Row selection event|
|                | On loaded           | -      | Component load event|
|                | On table changed    | -        | Table change event|
|                | On header changed   | -      | Header change event|
|                | On row changed      | -         |Row change event |
|                | On cell changed     | -         | Cell change event|

**CSS Properties:**

| Settings group | Setting Field      | Value Options        | Purpose                          |
|----------------|---------------------|--------------------------|-------------------------------------|
| Layout         | Width               | -                        | Component width                   |
|                | Height              | -                        | Component height                   |
|                | Margin              | -                        | Outer padding                      |
|                | Padding             | -                        | Inner padding                   |
|                | Visible             | -                        | Component Visibility                |
|                | Hidden              | -                        | Hiding a Component                  |
| Appearance     | CornerRadius        | -                        | Corner radius                   |
|                | BorderThickness     | -                        | Border thickness                       |
| Brush          | Background          | -                        | Background color                           |
|                | BorderBrush         | -                        | Border color                          |

**DataGrid Configuration Model**

The following settings are used to modify the columns of the DataGrid UI component: 

| Setting Field   | Value Options                           | Purpose                                              |
|-------------------|--------------------------------------------|---------------------------------------------------------|
| Translation value | -                                          | Column header                                       |
| Show header       | true, false                                | This property allows you to customize the display of the column header |
| Sortable          | true, false                                | The property allows you to configure the ability to sort the table by the selected column |
| Filterable        | true, false                                | This property allows you to configure the ability to filter the table by the selected column |
| Visible           | true, false                                | The property determines the visibility of the column                   |
| Plain text        | true, false                                | Property to display a column as plain text    |
| Width             | -                                          | Column width in the table                                |
| Display format    | -                                          | Column data display format                       |
| Icon              | Available only for Edit record, Open application | A property that contains a selection of available icons         |
| Command type      | Open application, Edit record             | The property allows you to select the action that will be performed by clicking on the column |
| Add field         | Button                                     | The property allows you to add fields for output in the column   |

## Cases
- **Data Display**: Ideal for displaying data in an easy-to-understand tabular form.
- **Administrative Panels**: Widely used in management interfaces for viewing and editing data.
- **Analytics Applications**: Allows you to analyze and sort large amounts of information.

## Exceptions
- **Limited Visualization**: Data Grid is not suitable for complex data visualizations such as graphs or charts.
- **Data Processing**: The component is designed to display data, not to process or compute data.
