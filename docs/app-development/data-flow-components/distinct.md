# Distinct

![](../../assets/images/app-development/distinct.png)

## General information
The Distinct step is used to eliminate duplicate entries from the data stream, leaving only unique values. This process helps in optimizing data processing by eliminating duplicates and reducing the amount of data analyzed.

## Parameters
**Step Settings:**

| Setting Field | Value Options | Purpose                           |
|----------------|-------------------|--------------------------------------|
| Step name      | -                 | Name of the step in the data flow        |
| Source step    | -                 | Selecting the previous step |
| Keys           | -                 | Keys for checking uniqueness      |

## Cases
- **Data Cleaning**: Removing of duplicate entries to simplify analysis.
- **Preparation for aggregation**: Pre-cleaning of data before performing aggregation operations.

## Exceptions
- **Selection of keys**: Incorrect selection of keys may result in the loss of important data.
- **Loss of information**: Risk of losing part of the data if the step is configured incorrectly.

## Application scenario

This component checks the availability of fields in the Distinct step. The "Distinct" button is clicked on the frontend. If the step works correctly, a "execute" line with a preview of the HTTP response should appear in the Network tab, containing data for three records.

- You can download the component configuration [here](https://drive.google.com/file/d/1dA9EzzJOn9sWBYhdvL__AcI1kJ5qNNLd/view?usp=sharing).