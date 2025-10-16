# Maintenance menu

<br>

The “Maintenance” menu is a powerful tool for managing data and maintaining the system, especially after major updates, data migrations, or database changes.
<br>

## General description

- **Purpose**: Managing PostgreSQL data via ODATA, removing deleted data, analyzing and managing system logs.
- **Features**: The tool is mainly used after platform version updates, component imports, or massive data changes.
  <br>

## Maintenance menu tabs

<br>

### System logs

<br>

! [System logs] (system-logs.png)
<br>

- **Functionality**: View current system logs and adjust logging levels (Trace, Debug, Information, Warning, Critical, Error, None).
  <br>

### System maintenance

<br>

! [System maintenance] (system-maintenance.png)
<br>

1. **Rebuild Database References**: Checking and rebuilding cross-references between components or within components (dataflow/workflow).
2. **Rebuild RLS Rules**: Rebuilding Row-Level Security rules to customize data access.
3. **Rebuild Cache**: Rebuilding the platform’s internal cache, solving problems with updates.
4. **Analysis marked for deletion**: Viewing and managing records marked for deletion using the ‘Mark entry for deletion’ flag in the ‘Update entry’ step. After clicking the “Analysis marked for deletion” button, all marked entries are displayed. Entries are selected and deleted via “Delete selected items”. The system will prevent entries from being deleted if there are related untagged entries.
5. **Reset current publication**: Resets the publishing process if it fails.
   <br>

### File storage

This section adds the ability to configure the following settings for File storage:

| Acceptable file types | File size limit in bytes |
| --------------------- | ------------------------ |
| .\* (all file types)  | selected size            |

<br>

You can specify filter types, separating them with commas. This can be file extensions, such as .jpg, .json, .docx, or Mime-types, for example, image/_, application/_

You can also combine filters, for example, `image/*`, `.docx`.
Using the `*/*` filter allows you to upload any files.
<br>

![File storage maintenance](../assets/images/user-interface/file-storage-maintenance.png)
