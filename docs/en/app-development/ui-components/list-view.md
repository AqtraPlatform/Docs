# List view

![](../../assets/images/app-development/list-view.png)

## General information
“List View” is a UI component used for displaying and configuring the “card” presentation of data.

## Parameters
**Component properties**

| Settings group | Setting Field   | Value Options          | Purpose                         |
|-----------------|------------------|----------------------------|------------------------------------|
|                 | Name             | -                          | Name of the UI Component in the system |
| Common          | Component        | Multiselect of Catalog| Contains a list of all Components |
|                 | Number of columns| -                          | Number of container columns      |
|                 | Number of rows   | -                          | Number of container rows         |
|                 | Column gap       | -                          | Column spacing          |
|                 | Row gap          | -                          | Line spacing           |
|                 | Page size        | -                          | Container size                   |
|                 | Manual reload    | true, false                | Ability to manually reload data |
|                 | Hide page selector | true, false              | Hide page selector            |
|                 | Enable drag and drop | true, false            | Enable drag-and-drop feature             |
|                 | Drag and drop group | -                        | Drag-and-drop group (if any)           |
|                 | Automation id    | -                          | ID for automation     |
| Events              | On datasource loaded | -                        | Data source load event |
|                     | On loaded          | -                          | Component load event      |
|                     | On drop            | -                          | Drag-and-drop event           |

**CSS properties**

| Settings group | Setting Field   | Value Options          | Purpose                         |
|-----------------|------------------|----------------------------|------------------------------------|
| Layout          | Width            | -                          | Component width                  |
|                 | Height           | -                          | Component height                  |
|                 | Margin           | -                          | Outer padding of the component          |
|                 | Padding          | -                          | Inner padding of the component       |
|                 | Visible          | true, false                | Component Visibility               |
|                 | Hidden           | true, false                | Component concealment               |
|                 | Orientation      | Horizontal, Vertical       | Component orientation              |
| Appearance      | CornerRadius     | -                          | Radius of corner rounding            |
|                 | BorderThickness  | -                          | Component border thickness         |
|                 | Opacity          | -                          | Component transparency            |
| Brush           | Background       | -                          | Component background color               |
|                 | BorderBrush      | -                          | Component border color            |

## Using drag-and-drop feature
First, in the “Common” group of settings, you need to select the following option:

![](../../assets/images/app-development/enable-drag-and-drop.png)

After saving and publishing, drag-and-drop will already be available for this list-view on the work-place. For the subsequent correct operation, you need to go to the component script and prepare the function for handling the drag-and-drop (on drop) event. 

Here's an example of the function applied to a canban board that consists of a main list-view and a nested list-view. The main one performs the function of the stages of the sales funnel and is in a horizontal position, while the nested one contains the deals themselves and is in a vertical position. The function takes the ID of the object being dragged (in this case, the deal) and the stage to which the deal is transferred, then calls the dataflow and, if completed successfully, updates the list-view, moving the deal to a new stage:

```python
def OnMove(dstList, srcList, dataObject, oldIdx, newIdx):
    context.Logger.Info("Callback on move")
    # The new Busy(boolean) method puts the UIElement into a loading status,
    # showing or hiding the loader
    srcList.Busy(True)
    dstList.Busy(True)
    
    # The new GetDynamicFilterValue(string) method computes the value of a Dynamic filter.
    # If there are two filters on one field, the first in the list is computed
    stage = dstList.GetDynamicFilterValue("data.Stage")
    
    # Creating a model to call the data-flow
    flowModel = {"Stage": stage, "OrderId": dataObject.Id}
    # Calling the data-flow with a new overload for onComplete and onError
    context.ExecuteDataflow("783cf3e3-d8f8-4551-8447-13be4f738e41", flowModel, 
    lambda res: OnDataflowComplete(res, dstList, srcList), 
    lambda ex: OnDataflowError(ex, dstList, srcList))

def OnDataflowComplete(dataResult, dstList, srcList):
    # The new Busy(boolean) method puts the UIElement into a loading status,
    # showing or hiding the loader
    srcList.Busy(False)
    dstList.Busy(False)
    # Refreshing the lists
    srcList.Refresh()
    dstList.Refresh()

def OnDataflowError(exception, dstList, srcList):
    # The new Error(boolean, string) method puts the UIElement into an error status,
    # displaying the error message
    srcList.Error(True, "An error occurred")
    dstList.Error(True)
    context.Logger.Error(exception, "An error occurred during the data-flow call")
```

## Cases
- **Data Display**: Effective for presenting data in the form of cards or lists.
- **User Interface**: Suitable for interfaces that require representation of information in the form of cards or lists.

## Exceptions
- **Limited Flexibility**: Not suitable for displaying data beyond the card or list format, as it specializes in a specific visual representation.
- **Visual Limitations**: The style and design may be limited by CSS settings, which may not meet all the design requirements.
