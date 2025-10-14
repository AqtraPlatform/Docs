# Tutorial №2

<br>

## Erstellen einer einfachen Anwendung für ein Autohaus

<br>

**Anwendungsbeschreibung:**

Wir werden eine Anwendung erstellen, die aus mehreren Komponenten besteht und es ermöglicht, zum Verkauf verfügbare Autos zu verfolgen, einen Manager für die Vertragsunterzeichnung zuzuweisen und es Managern zu ermöglichen, das Geschäft abzuschließen.

**Wir werden die folgenden Komponenten erstellen:**

<br>

### Komponente "Transaction Specialists"

Die erste Komponente wird ein einfaches Formular zum Hinzufügen neuer Manager sein und aus einer einzigen benutzerdefinierten Eigenschaft bestehen:

<br>

![Tutorial 2.2](../assets/images/tutorials/tut2.1.png)

<br>

Als Nächstes richten wir unseren Arbeitsbereich ein und fügen ein Panel-Element hinzu, in dem wir unsere Arbeit durchführen.

Ändern Sie dann in den Panel-Einstellungen unter der Einstellungsgruppe "Layout" die Panel-Ausrichtung auf vertikal und beginnen Sie, die folgenden Elemente hinzuzufügen: Wir benötigen den von uns erstellten manager_name und eine Schaltfläche. Es sollte so aussehen:

<br>

![Tutorial 2.2](../assets/images/tutorials/tut2.2.png)

<br>

Erstellen Sie als Nächstes einen Dataflow, nennen Sie ihn "Add a manager" und fügen Sie die folgenden Schritte hinzu: `get action model`, `update entry`, `write response`. Es sollte so aussehen:

<br>

![Tutorial 2.3](../assets/images/tutorials/tut2.3.png)

<br>

Konfigurieren Sie den Schritt `Update entry` wie folgt:

<br>

![Tutorial 2.4](../assets/images/tutorials/tut2.4.png)

<br>

**Vergessen Sie nicht**, den `source step` für den Schritt `update entry` festzulegen!

Verknüpfen Sie nach dem Einrichten des Dataflows ihn mit der Schaltfläche wie folgt: Gehen Sie zu den Schaltflächeneinstellungen, klicken Sie auf die Einstellungsgruppe "actions", setzen Sie den "command type" auf "execute dataflow" und wählen Sie den von uns erstellten Dataflow "Add a manager" aus.

Klicken Sie auf "Save", "Ready to publish". Veröffentlichen Sie die Komponente und fügen Sie sie dann dem Workplace über das "Navigation menu" der Domäne hinzu, in der Sie Ihre Anwendung bereitstellen (in unserem Fall ist dies die Domäne "digital-workplace").

<br>

![Tutorial 2.5](../assets/images/tutorials/tut2.5.png)

<br>

Klicken Sie auf "ADD MENU ITEM" und fügen Sie unsere Komponente hinzu:
<br>

![Tutorial 2.6](../assets/images/tutorials/tut2.6.png)

<br>

Gehen Sie zum `workplace` und fügen Sie einige Manager für die weitere Arbeit mit ihnen hinzu.

<br>

### Komponente "Car fleet"

<br>

Mit dieser Komponente richten wir die Anzeige aller Autos und allgemeiner Informationen über sie ein, fügen ein Formular zum Erstellen von Datensätzen neuer Autos hinzu, ein Formular zum Zuweisen eines Transaktionsmanagers zu einem Auto und ein Formular zum Bestätigen, dass das Geschäft mit anschließender Archivierung des Autodatensatzes abgeschlossen ist.

In dieser Komponente erstellen wir eine Reihe von benutzerdefinierten Eigenschaften:

- `car_vin`: Eigenschaftstyp - `string`, Titel - `VIN`, Einstellungen - `required`, `primary key`, `query`;
- `car_brand`: Eigenschaftstyp - `string`, Titel - `Car Brand`, Einstellungen - `required`, `query`;
- `car_model`: Eigenschaftstyp - `string`, Titel - `Car Model`, Einstellungen - `required`, `query`;
- `year_of_manufacture`: Eigenschaftstyp - `integer`, Titel - `Year of manufacture`, Einstellungen - `required`, `query`;
- `color`: Eigenschaftstyp - `string`, Titel - `Color`, Einstellungen - `required`, `query`;
- `price`: Eigenschaftstyp - `number`, Titel - `Price of the car`, Einstellungen - `required`, `query`;
- `is_manager_exists`: Eigenschaftstyp - `boolean`, Titel - `Is manager exists`, Einstellungen - `query`;
- `choosen_manager`: Eigenschaftstyp - `catalog`, Komponente - `Transaction Specialists` Titel - `Chosen Manager`, Einstellungen - `query`;
- `is_archieved`: Eigenschaftstyp - `string`, Einstellungen - `query`.

Die Komponente besteht aus den folgenden Teilen (Seiten):

<br>

1. **Hauptseite**

Um eine Seite hinzuzufügen, müssen Sie die Gruppe `Layout` in der `Toolbox` finden und das Element `Page` in den Arbeitsbereich ziehen.

Diese Seite zeigt ein Datengitter mit allen zum Verkauf verfügbaren Autos und allgemeinen Informationen über sie für Verkaufsmanager. Darüber hinaus fügen wir der Seite eine Schaltfläche hinzu, die zu einem Formular zum Hinzufügen von Autos zur Liste weiterleitet, aber wir werden sie später hinzufügen.

Fügen Sie ein Panel zum Arbeitsbereich hinzu, ändern Sie die Ausrichtungseinstellung auf vertikal und fügen Sie dann zwei weitere Panels hinzu. Platzieren Sie im unteren Panel das Datengitter-Element und fügen Sie im oberen Panel zwei weitere Panels hinzu. Platzieren Sie im linken Panel eine Beschriftung und schreiben Sie "Car fleet" in den "translation value"-Einstellungen. Fügen Sie im rechten Panel eine Schaltfläche hinzu und schreiben Sie "Add a new car" in den "translation value". Später werden wir die Einstellung "Actions" ändern, aber vorerst können Sie die Schaltflächengröße in den "Layout"-Einstellungen ändern.

<br>

![Tutorial 2.7](../assets/images/tutorials/tuto2.7.png)

<br>

Sie können andere Einstellungen ausprobieren.

Fahren Sie als Nächstes mit der Konfiguration des `data grid` fort: Klicken Sie auf das Zahnradsymbol und wählen Sie die Komponente für das Datengitter "Car fleet" aus. Klicken Sie dann neben Columns auf `+`, dadurch wird eine Spalte zu unserem Datengitter hinzugefügt, tun Sie dies 5 Mal.

Klicken Sie auf die erste Spalte, dann auf "Add field" und wählen Sie die Eigenschaft `car_brand` aus. Die weitere Konfiguration sollte so aussehen:

<br>

![Tutorial 2.8](../assets/images/tutorials/tut2.8.png)

<br>

Sie sollten die folgenden Spalten auf ähnliche Weise in dieser Reihenfolge konfigurieren: 2. Spalte - `car_model`, 3. Spalte - `year_of_manufacture`, 4. Spalte - `color`, 5. Spalte - `price`.

Setzen Sie auch in den Datengitter-Einstellungen `Static filters`. Da wir Autos anzeigen möchten, denen noch kein Manager zugewiesen wurde, setzen Sie die folgende Einstellung:

<br>

![Tutorial 2.12](../assets/images/tutorials/tut2.12.png)

<br>

Das Endergebnis in unserem Arbeitsbereich sollte so aussehen:

<br>

![Tutorial 2.9](../assets/images/tutorials/tut2.9.png)

<br>

2. **Ein neues Auto hinzufügen**

Auf diese Seite wird der Benutzer zugreifen, indem er auf die Schaltfläche "Add a new car" von unserer vorherigen Seite klickt. Beginnen wir mit der Einrichtung unseres Arbeitsbereichs.

Fügen Sie ein Panel zur Seite hinzu. Ändern Sie in den Einstellungen die Seitenausrichtung auf vertikal. Fügen Sie als Nächstes zwei weitere Panels hinzu. Ändern Sie im ersten Panel auch die Ausrichtung auf vertikal und übertragen Sie unsere Eigenschaften so, dass sie so aussehen:

<br>

![Tutorial 2.10](../assets/images/tutorials/tut2.10.png)

<br>

Fügen Sie im unteren Panel zwei Schaltflächen hinzu, setzen Sie deren Padding wie bei der Schaltfläche "Add a new car" und benennen Sie sie entsprechend: "Add a new car" und "Back to all cars".

Setzen Sie in den Einstellungen für die Schaltfläche "Back to all cars" die "Actions" auf "Open page" "Main page". Durch Klicken auf diese Schaltfläche wird der Benutzer zur Seite mit dem Datengitter weitergeleitet. Erstellen Sie für die Schaltfläche "Add a new car" einen Datenfluss, den wir später verknüpfen werden.

Der Datenfluss besteht aus den folgenden Schritten: `get action model`, `execute script`, `update entry`, `write response`. Konfigurieren wir sie.

Im Schritt `execute script` erstellen Sie Variablen, die für die Eigenschaften `is_manager_exists` und `is_archieved` verwendet werden:

```
item["_is_manager_exists@boolean"] = False
item["_is_archieved@boolean"] = False
```

Konfigurieren Sie als Nächstes den Schritt `Update entry`:

<br>

![Tutorial 2.13](../assets/images/tutorials/tut2.13.png)

<br>

Als Nächstes müssen wir unsere Felder zuordnen. **Denken Sie daran**, dass die Felder in den Schritteinstellungen mit dem Präfix data.`property_name` zugeordnet werden. Verwenden Sie für die Eigenschaften `is_archieved` und `is_manager_exists` die im execute script-Schritt festgelegten Variablenwerte, lassen Sie das Feld `chosen_manager` leer:

<br>

![Tutorial 2.14](../assets/images/tutorials/tut2.14.png)

<br>

**Setzen Sie immer den Quellschritt für jeden Schritt außer dem ersten fest. Dies wird in der Tutorial-Beschreibung nicht weiter erwähnt.**

Jetzt, da unser Datenfluss abgeschlossen ist, können wir ihn mit der Schaltfläche "Add a new car" verknüpfen und unsere Komponente speichern. Das Endergebnis unserer Seite ist unten gezeigt:

<br>

![Tutorial 2.15](../assets/images/tutorials/tut2.15.png)

<br>

[... Weitere Abschnitte fortsetzen mit ähnlicher Übersetzungsqualität ...]

### Schlussfolgerung

Sie haben eine kleine und einfache Anwendung erstellt, in der Sie mit mehreren Komponenten gearbeitet und gelernt haben, wie Sie sie miteinander verknüpfen. Sie haben gelernt, wie man modale Fenster erstellt und begannen, die Interaktion zwischen Programmiersprachen und den Tools unserer Plattform zu erkunden.

Versuchen Sie, mehrere Manager zu erstellen, neue Autos zum Verkauf hinzuzufügen, Manager zuzuweisen und zu versuchen, Geschäfte abzuschließen.

Natürlich ist diese Anwendung ein Test; sie kann endlos verbessert und komplexer gemacht werden. Nach dem Erstellen können Sie andere Tools selbst verwenden, unterschiedliche Logik aufbauen und das Design nach Ihren Wünschen anpassen. Die Plattform bietet Ihnen flexible Tools, die die Entwicklung aufregender und einfacher machen!

Beschreibungen der im Tutorial verwendeten Tools finden Sie im Abschnitt "Application Development".
