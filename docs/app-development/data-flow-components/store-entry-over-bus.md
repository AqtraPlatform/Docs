# Store entry over bus

![](../../assets/images/app-development/store-entry-over-bus.png)

## General information

The “Store Entry Over Bus” step is designed for storing the model in the component data (fields) via the bus. This step always creates a new instance of the specified component and is used to work dynamically with the data in the system. The step is called asynchronously.

## Parameters

**Step Settings:**

| Setting Field  | Value Options          | Purpose                                                                             |
| -------------- | ---------------------- | ----------------------------------------------------------------------------------- |
| Step name      | -                      | Name of the step                                                                    |
| Source step    | -                      | Selection of the previous step                                                      |
| Component      | -                      | Selection from the available components to save the entry                           |
| Name           | String                 | System name of the entry to be displayed using links of the Catalog type            |
| Keys           | ADD KEY                | For components with the Restrict access flag, specifying the keys to map the fields |
| Key field      | Multiselect of Catalog | Fields containing the primary keys of the selected component                        |
| Fields mapping | -                      | Dynamically configuring the mapping of component models to the data flow model      |

## Cases

- **Creating New Component Instances**: Used to automatically create new entries in components based on data in data flow.

## Exceptions

- **Dependency on the Availability of Primary Keys in the Component**: The effectiveness of the step depends on the availability and correctness of primary keys in the target component, especially if the component has the Restrict access flag.
- **Asynchronous Processing Requirement**: The step is performed asynchronously, which can affect the sequence and processing time of the system.

## Application scenario

This component allows retrieving data from the selected integration and storing it in the corresponding fields of created data models. The retrieved data can then be used in other parts of the system for further processing or display.

- You can download the component configuration [here](https://drive.google.com/file/d/1jFuXBG8v-YuICBozvoCPAm0FfBQhApvG/view?usp=sharing)
