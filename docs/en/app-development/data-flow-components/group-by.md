# Group By

![](../../assets/images/app-development/group-by.png)

## General information
The “Group By” step is used to collect and group data split in previous steps, for example, using the “Extract Collection”. The main function of this step is to group data by specific keys specified by the user. The step collects the split data and combines only the entries that match the specified keys.

## Parameters
**Step Settings:**

| Setting Field | Value Options | Purpose |
|----------------|-------------------|------------|
| Step name      | -                 | Name of the step |
| Source step    | -                 | Selecting the previous step |
| Keys           | -                 | Keys used to group data |

## Cases
- **Combining Split Data**: Used to combine data split in the previous steps, such as the “Extract Collection”, using specific keys.
- **Data Segmentation and Analysis**: Suitable for cases where it is necessary to analyze data according to specific categories or criteria.

## Exceptions
- **Dependency on Grouping Keys**: The accuracy and relevance of the keys are critical to properly grouping the data.
- **Difficulty in Data Processing and Analysis**: Grouping can be difficult if the data structure is varied or the keys do not identify groups uniquely.

## Application scenario

This component checks the availability of fields in the Group By step. In the dataflow, first, a Get action model step and Group By step are added. Then, on the frontend, the imported component is opened, and the "Network" tab in the browser developer tools is opened. After that, the "Group by" button is clicked on the frontend. If the step works correctly, a "execute" line with a preview of the HTTP response should appear in the Network tab, containing data with the key "ETO test123" and their aggregation.

- You can download the component configuration [here](https://drive.google.com/file/d/1fKeJh3a0HHcG7VuFs-Tx5YdS7H6C7mI0/view?usp=sharing).
