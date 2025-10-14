# Join models

![](../../assets/images/app-development/join-models.png)

## General information
The “Join Models” step is designed to merge data from two different sources. It adds data from the “Right step” source to data from a “Left step” source if matching entries are found in both sources.

The step creates a new data model by merging the data flows defined in the “Left step” and “Right step” parameters. The step waits for both flows to finish processing, and then sorts and merges the data.

## Parameters
**Step Settings:**

| Setting Field | Value Options | Purpose |
|----------------|-------------------|------------|
| Step name      | -                 | Name of the step |
| Left step      | -                 | Data source for the left side of the merged flows |
| Right step     | -                 | Data source for the right side of the merged flows |
| Left key       | -                 | Key to merging data from the left source |
| Right key      | -                 | Key to merging data from the right source |
| Map            | -                 | Mapping fields between left and right sources |

## Cases
- **Merging Data Flows**: Used to merge two different data flows into one model, allowing you to analyze and process the merged data.
- **Data Enrichment**: It is used to add additional information from one data set to another, thereby improving the completeness of the information.

## Exceptions
- **Need for an Exact Merging Key**: Errors in defining the “Left key” and “Right key” can lead to incorrect or inefficient data merging.

## Application scenario

This component allows **testing** and **verifying** the functionality of a data flow where data is **merged** from different sources. It provides **field mapping** and **data merge verification** on the **frontend** and in the **HTTP** response preview. 

- You can download the component configuration [here](https://drive.google.com/file/d/1YRpXJwNSTp_jOPxP-j0M9SvocZw1W6Tt/view?usp=sharing).

