# Tutorial №2 
<br>

## Erstellung einer einfachen Anwendung für ein Autohaus
<br>

**Anwendungsbeschreibung:**

Wir werden eine Anwendung erstellen, die aus mehreren Komponenten besteht und das Verfolgen von zum Verkauf verfügbaren Autos, die Zuweisung eines Managers für die Vertragsunterzeichnung und die Möglichkeit für Manager, den Deal abzuschließen, ermöglicht.

**Wir werden die folgenden Komponenten erstellen:**

<br>

### Komponente "Transaktionsspezialisten"

Die erste Komponente wird ein einfaches Formular zum Hinzufügen neuer Manager sein und besteht aus einer einzigen benutzerdefinierten Eigenschaft:

<br>

![Tutorial 2.2](../assets/images/tutorials/tut2.1.png)

<br>

Als nächstes gehen wir zur Einrichtung unseres Arbeitsbereichs über und fügen ein Panel-Element hinzu, in dem wir unsere Arbeit durchführen werden.

Dann ändern Sie in den Panel-Einstellungen unter der Gruppe "Layout" die Panel-Ausrichtung auf vertikal und beginnen Sie, die folgenden Elemente hinzuzufügen: Wir benötigen den manager_name, den wir erstellt haben, und einen Button. Es sollte so aussehen:

<br>

![Tutorial 2.2](../assets/images/tutorials/tut2.2.png)

<br>

Erstellen Sie als Nächstes einen Datenfluss, benennen Sie ihn "Manager hinzufügen" und fügen Sie die folgenden Schritte hinzu: `get action model`, `update entry`, `write response`. Es sollte so aussehen:

<br>

![Tutorial 2.3](../assets/images/tutorials/tut2.3.png)

<br>

Konfigurieren Sie den Schritt `Update entry` wie folgt:

<br>

![Tutorial 2.4](../assets/images/tutorials/tut2.4.png)

<br>

**Vergessen Sie nicht**, den `source step` für den `update entry` Schritt festzulegen!

Nachdem Sie den Datenfluss eingerichtet haben, verknüpfen Sie ihn mit dem Button wie folgt: Gehen Sie zu den Button-Einstellungen, klicken Sie auf die Gruppe "Aktionen", setzen Sie den "Befehls-Typ" auf "Datenfluss ausführen" und wählen Sie den von uns erstellten Datenfluss "Manager hinzufügen".

Klicken Sie auf "Speichern", "Bereit zum Veröffentlichen". Veröffentlichen Sie die Komponente und fügen Sie sie dann mit dem "Navigationsmenü" der Domäne hinzu, in der Sie Ihre Anwendung bereitstellen (in unserem Fall ist dies die Domäne "digital-workplace").

<br>

![Tutorial 2.5](../assets/images/tutorials/tut2.5.png)

<br>

Klicken Sie auf "MENÜELEMENT HINZUFÜGEN" und fügen Sie unsere Komponente hinzu:
<br>

![Tutorial 2.6](../assets/images/tutorials/tut2.6.png)

<br>

Gehen Sie zu `workplace` und fügen Sie ein paar Manager für die weitere Arbeit mit ihnen hinzu.

<br>

### Komponente "Fahrzeugflotte"

<br>

Mit dieser Komponente werden wir die Anzeige aller Autos und allgemeine Informationen über sie einrichten, ein Formular zum Erstellen von Aufzeichnungen neuer Autos hinzufügen, ein Formular zur Zuweisung eines Transaktionsmanagers zu einem Auto und ein Formular zur Bestätigung, dass der Deal abgeschlossen ist, mit anschließender Archivierung der Autoaufzeichnung.

In dieser Komponente werden wir eine Reihe von benutzerdefinierten Eigenschaften erstellen:

- `car_vin`: Eigenschaftstyp - `string`, Titel - `VIN`, Einstellungen - `required`, `primary key`, `query`;
- `car_brand`: Eigenschaftstyp - `string`, Titel - `Car Brand`, Einstellungen - `required`, `query`;
- `car_model`: Eigenschaftstyp - `string`, Titel - `Car Model`, Einstellungen - `required`, `query`;
- `year_of_manufacture`: Eigenschaftstyp - `integer`, Titel - `Year of manufacture`, Einstellungen - `required`, `query`;
- `color`: Eigenschaftstyp - `string`, Titel - `Color`, Einstellungen - `required`, `query`;
- `price`: Eigenschaftstyp - `number`, Titel - `Price of the car`, Einstellungen - `required`, `query`;
- `is_manager_exists`: Eigenschaftstyp - `boolean`, Titel - `Is manager exists`, Einstellungen - `query`;
- `choosen_manager`: Eigenschaftstyp - `catalog`, Komponente - `Transaction Specialists` Titel - `Chosen Manager`, Einstellungen - `query`;
- `is_archieved`: Eigenschaftstyp - `string`, Einstellungen - `query`.

Die Komponente wird aus den folgenden Teilen (Seiten) bestehen:

<br>

1. **Hauptseite**

Um eine Seite hinzuzufügen, müssen Sie die Gruppe `Layout` im `Toolbox` finden und das Element `Page` in den Arbeitsbereich ziehen.
Diese Seite wird ein Datenraster mit allen zum Verkauf verfügbaren Autos und allgemeinen Informationen darüber für Verkaufsleiter präsentieren. Darüber hinaus werden wir einen Button zur Seite hinzufügen, der zu einem Formular zum Hinzufügen von Autos zur Liste weiterleitet, aber das werden wir später hinzufügen.

Fügen Sie ein Panel zum Arbeitsbereich hinzu, ändern Sie die Ausrichtungseinstellung auf vertikal und fügen Sie dann zwei weitere Panels hinzu. Im unteren Panel platzieren Sie das Datenrasterelement, und im oberen Panel fügen Sie zwei weitere Panels hinzu. Im linken Panel platzieren Sie ein Label und schreiben "Fahrzeugflotte" in dessen "Übersetzungswert"-Einstellungen. Im rechten Panel fügen Sie einen Button hinzu und schreiben "Neues Auto hinzufügen" in dessen "Übersetzungswert". Später werden wir die Einstellung "Aktionen" ändern, aber vorerst können Sie die Button-Größe in den "Layout"-Einstellungen ändern.

<br>

![Tutorial 2.7](../assets/images/tutorials/tuto2.7.png)

<br>

Sie können andere Einstellungen ausprobieren.

Als Nächstes fahren Sie fort, um die `data grid` zu konfigurieren: Klicken Sie auf das Zahnradsymbol und wählen Sie die Komponente für das Datenraster "Fahrzeugflotte". Klicken Sie dann neben den Spalten auf `+`, dies wird eine Spalte zu unserem Datenraster hinzufügen, tun Sie dies 5 Mal.

Klicken Sie auf die erste Spalte, dann auf "Feld hinzufügen" und wählen Sie die Eigenschaft `car_brand`. Die weitere Konfiguration sollte wie folgt aussehen:

<br>

![Tutorial 2.8](../assets/images/tutorials/tut2.8.png)

<br>

Sie sollten die folgenden Spalten in ähnlicher Weise in dieser Reihenfolge konfigurieren: 2. Spalte - `car_model`, 3. Spalte - `year_of_manufacture`, 4. Spalte - `color`, 5. Spalte - `price`.

Außerdem sollten Sie in den Einstellungen des Datenrasters `Static filters` festlegen. Da wir Autos anzeigen möchten, die noch keinem Manager zugewiesen sind, setzen Sie die folgende Einstellung:

<br>

![Tutorial 2.12](../assets/images/tutorials/tut2.12.png)

<br>

Das Endergebnis in unserem Arbeitsbereich sollte wie folgt aussehen:

<br>

![Tutorial 2.9](../assets/images/tutorials/tut2.9.png)

<br>

2. **Neues Auto hinzufügen**

Diese Seite wird vom Benutzer aufgerufen, indem er auf den Button "Neues Auto hinzufügen" von unserer vorherigen Seite klickt. Lassen Sie uns mit der Einrichtung unseres Arbeitsbereichs beginnen.

Fügen Sie ein Panel zur Seite hinzu. Ändern Sie in seinen Einstellungen die Seitenausrichtung auf vertikal. Fügen Sie als Nächstes zwei weitere Panels hinzu. Im ersten Panel ändern Sie ebenfalls die Ausrichtung auf vertikal und übertragen unsere Eigenschaften, sodass sie wie folgt aussehen:

<br>

![Tutorial 2.10](../assets/images/tutorials/tut2.10.png)

<br>

Im unteren Panel fügen Sie zwei Buttons hinzu, setzen Sie deren Padding wie beim Button "Neues Auto hinzufügen" und benennen Sie sie entsprechend: "Neues Auto hinzufügen" und "Zurück zu allen Autos".

In den Einstellungen für den Button "Zurück zu allen Autos" setzen Sie die "Aktionen" auf "Seite öffnen" "Hauptseite". Ein Klick auf diesen Button leitet den Benutzer zur Seite mit dem Datenraster weiter. Für den Button "Neues Auto hinzufügen" erstellen Sie einen Datenfluss, den wir später damit verknüpfen werden.

Der Datenfluss wird aus den folgenden Schritten bestehen: `get action model`, `execute script`, `update entry`, `write response`. Lassen Sie uns diese konfigurieren.

Im Schritt `execute script` erstellen Sie Variablen, die für die Eigenschaften `is_manager_exists` und `is_archieved` verwendet werden:

```
item["_is_manager_exists@boolean"] = False
item["_is_archieved@boolean"] = False
```

Konfigurieren Sie als Nächstes den Schritt `Update entry`:

<br>

![Tutorial 2.13](../assets/images/tutorials/tut2.13.png)

<br>

Als Nächstes müssen wir unsere Felder zuordnen. **Denken Sie daran**, dass die Felder in den Schritt-Einstellungen mit dem Präfix data.`property_name` zugeordnet sind. Für die Eigenschaften `is_archieved` und `is_manager_exists` verwenden Sie die in dem Ausführungsskript-Schritt festgelegten Variablenwerte und lassen das Feld `chosen_manager` leer:

<br>

![Tutorial 2.14](../assets/images/tutorials/tut2.14.png)

<br>

**Setzen Sie immer den Quellschritt für jeden Schritt außer dem ersten. Dies wird im weiteren Verlauf der Anleitung nicht mehr erwähnt.**

Jetzt, da unser Datenfluss abgeschlossen ist, können wir ihn mit dem Button "Neues Auto hinzufügen" verknüpfen und unsere Komponente speichern. Das Endergebnis unserer Seite ist unten dargestellt:

<br>

![Tutorial 2.15](../assets/images/tutorials/tut2.15.png)

<br>

3. **Einen Manager ernennen**

Diese Seite wird als modales Fenster aufgerufen, wenn auf einen bestimmten Eintrag im Datenraster geklickt wird. Sie ist für eine einzige Funktion konzipiert - die Zuweisung eines Managers zu einem bestimmten Auto. Lassen Sie uns mit der Einrichtung des Arbeitsbereichs fortfahren.
Die Seite selbst wird der Seite "Neues Auto hinzufügen" ähneln, mit dem einzigen Unterschied, dass wir die `chosen_manager`-Eigenschaft zum Arbeitsbereich hinzufügen, die die einzige Eigenschaft sein wird, die geändert werden kann. Dies ermöglicht es dem Manager, einen Kollegen auszuwählen, an den er das Auto und den Deal übertragen wird. Außerdem fügen Sie zwei Schaltflächen hinzu, eine zum Schließen des Modalfensters mit der Bezeichnung "Zurück zu allen Autos" und die andere mit der Bezeichnung "Manager ernennen", die mit einem Datenfluss verknüpft wird, den wir später erstellen werden.

**Vergessen Sie nicht, die Einstellung "Deaktiviert" in den TextBox-Einstellungen für jede Eigenschaft außer `chosen_manager` zu aktivieren.**

<br>

![Tutorial 2.16](../assets/images/tutorials/tut2.16.png)

<br>

Das Endergebnis auf dieser Seite sollte wie unten gezeigt aussehen:

<br>

![Tutorial 2.17](../assets/images/tutorials/tut2.17.png)

<br>

**Lassen Sie uns mit der Konfiguration des Datenflusses fortfahren**.

Wir müssen die folgenden Schritte hinzufügen: `get action model`, `execute script`, `lookup reference`, `update entry`, `write response`.

Im Schritt `execute script` werden wir eine Variable erstellen, die die `is_manager_exists`-Eigenschaft auf True ändert, wodurch der neu erstellte Eintrag aus dem Datenraster auf der Hauptseite verschwindet, wo wir statische Filter gesetzt haben.

```
item["_is_manager_exists@boolean"] = True
```

Als nächstes verwenden wir den Schritt `Lookup reference`. Ich empfehle Ihnen, über diesen Schritt im Abschnitt Datenfluss unserer technischen Dokumentation zu lesen. Der Schritt sollte wie unten gezeigt konfiguriert werden.

<br>

![Tutorial 2.18](../assets/images/tutorials/tut2.18.png)

<br>

Als nächstes konfigurieren wir den Schritt `Update entry`, im Feld "Komponenten-Schlüssel" geben Sie den Feldnamen aus dem Schritt `Lookup reference` an:

<br>

![Tutorial 2.19](../assets/images/tutorials/tut2.19.png)

<br>

In "Feldzuordnung" lassen Sie die Felder leer, außer für `chosen_manager` und `is_manager_exists`, dies sind die Felder, die wir im Datensatz ändern möchten, der mit dem Schritt `Lookup reference` gefunden wurde.

<br>

![Tutorial 2.20](../assets/images/tutorials/tut2.20.png)

<br>

Im Schritt `write response` müssen wir den Quellschritt festlegen.

Weisen Sie diesen Datenfluss zu, damit er ausgeführt wird, wenn die Schaltfläche "Manager ernennen" gedrückt wird. Speichern Sie dann die Komponente.

<br>

**Fahren Sie mit dem Komponentenskript zum Erstellen des Modalfensters fort**.

Um ein Modalfenster zu erstellen, können Sie das folgende Skript verwenden. Für die Arbeit mit dem **Komponentenskript** empfehle ich Ihnen dringend, den Dokumentationsabschnitt `Using Python` zu lesen:

```
def show_model_info(model):
    context.Logger.Error("updated")

def open_custom_modal(sender, model):
    # Creating a modal window template using the GUID of a specific component
    dialog_builder = context.PlatformServices.DialogBuilder('component guid')
    # Setting the title for the modal window and selecting a specific page from the component's settings
    # Also setting the component instance ID to 1, so the first saved instance of component data will be used
    dialog_builder.WithEntryId(int(model[0].Id)).WithTitle("Appoint a manager").WithPageId('page id')
    # Setting the size of the modal window
    dialog_builder.WithVSize("650px").WithHSize("820px")
    dialog_builder.OnComplete(lambda model: show_model_info(model))
    dialog_builder.OnCancel(update_cars_success)
    # Opening the created modal window
    dialog_builder.OpenDialog()
    
def get_datagrid_cars(sender, *args):
    global datagrid_cars
    datagrid_cars = sender
    
def update_cars_success():
    datagrid_cars.Refresh()
```

Die Funktionen `get_datagrid_cars` und `update_cars_success` werden verwendet, um das Datenraster nach einer bestimmten Aktion automatisch zu aktualisieren. Wenn Sie sie nicht verwenden, wird das Datenraster nur nach dem Aktualisieren der Seite im Browser aktualisiert. Nach dem Kopieren müssen Sie die Komponente speichern und zum Arbeitsbereich auf der "Hauptseite" zurückkehren.

Sie müssen zu den Einstellungen des Datenrasters in der Einstellungsgruppe `Events` gehen und die Ausführung von Funktionen bestimmten Aktionen im Datenraster zuweisen.

<br>

![Tutorial 2.21](../assets/images/tutorials/tut2.21.png)

<br>

Speichern Sie die Komponente und fahren Sie dann mit der Einrichtung der nächsten Seite fort.

4. **In einen Vertrag eintreten**

Diese Seite ist ein Formular, das es dem Manager ermöglicht, einen bestimmten Autodeal zu archivieren, indem er das Feld `is_archieved` auf `True` ändert.

Die Seite ist eine Kopie der Seite `Appoint a manager`, der einzige Unterschied besteht darin, dass alle Felder die Einstellung `Disabled` -> `True` haben. Unten fügen wir zwei Schaltflächen hinzu, von denen eine den Datenfluss startet und die andere den Benutzer zur Komponentenseite weiterleitet, die wir noch nicht erstellt haben.

Die Seite selbst sollte so aussehen:

<br>

![Tutorial 2.22](../assets/images/tutorials/tut2.22.png)

<br>

Lassen Sie uns mit der Erstellung und Konfiguration des Datenflusses fortfahren. Wir benötigen 5 Schritte: `get action model`, `execute script`, `update entry`, `form action`, `write response`.

Im Schritt `execute script` werden wir eine Variable erstellen, die den Wert `True` in der `is_archieved`-Eigenschaft festlegt.

```
item["_is_archieved@boolean"] = True
```

Die Konfiguration des Schrittes `update entry` sollte wie folgt aussehen:

<br>

![Tutorial 2.23](../assets/images/tutorials/tut2.23.png)

<br>
Im Feldkomponenten-Schlüssel geben wir einen Verweis auf den Datensatz an, den wir bearbeiten möchten, und fahren dann mit der "Feldzuordnung" fort. Hier lassen wir alle Felder leer, außer für `is_archieved`. Hier setzen wir die Variable, die wir im Schritt `execute script` festgelegt haben.

Als nächstes ist der Schritt `Form action`, zu dem wir zurückkehren werden, nachdem wir die endgültige Komponente erstellt haben. Speichern Sie vorerst die Komponente, um zu vermeiden, dass Sie Ihre Arbeit verlieren.

### Komponente "Manager-Grid"

Diese Komponente wird aus einer einzigen Seite bestehen, und wir werden keine benutzerdefinierten Eigenschaften dafür erstellen. Diese Komponente wird nur von Managern verwendet, die Zugriff darauf haben, sodass sie alle Autos sehen können, die in die Deal-Phase verschoben und einem bestimmten Manager zugewiesen wurden.

Erstellen Sie ein Datenraster, verlinken Sie es mit der `Car fleet`-Komponente und fügen Sie eine Spalte für jede ihrer Eigenschaften hinzu. Das Ergebnis sollte wie folgt aussehen:

<br>

![Tutorial 2.24](../assets/images/tutorials/tut2.24.png)

<br>

Gehen Sie dann zur Gruppe der `Actions`-Einstellungen, setzen Sie den Befehlstyp auf `Open application`, die Komponente auf `Car fleet`, die Komponentenseite auf `Enter into a contract`, eine Seite, die wir als letzte Seite der `Car fleet`-Komponente erstellt haben.

Klicken Sie als Nächstes auf die `Action parameters`-Schaltfläche und ordnen Sie Id -> Id wie unten gezeigt zu.

<br>

![Tutorial 2.25](../assets/images/tutorials/tut2.25.png)

<br>

Lassen Sie uns die Komponente speichern und zu ihren Einstellungen gehen. Neben der Benennung und Auswahl der erforderlichen Domäne müssen wir das Kästchen `Restrict access` aktivieren, damit wir spezielle Sicherheitsberechtigungen für diese Komponente festlegen können.

Lassen Sie uns erneut speichern, die Komponente als bereit zur Veröffentlichung markieren und sie zur `Navigation menu` der von uns verwendeten Domäne hinzufügen.

<br>

**Zurück zur `Car fleet`-Komponente auf der `Enter into a contract`-Seite**

Es bleibt eine ungenutzte Schaltfläche übrig, `Back to all contracts`, lassen Sie uns deren `Command type` in der Gruppe der `Actions`-Einstellungen auf `Navigation back` setzen.

Als Nächstes müssen wir zum Datenfluss "Deal ist abgeschlossen" zurückkehren und die `Form action`-Schrittkonfiguration abschließen. Die endgültige Konfiguration des Schrittes sollte wie folgt aussehen:

<br>

![Tutorial 2.26](../assets/images/tutorials/tut2.26.png)

<br>

**Vergessen Sie nicht, die `source step` im `update entry`-Schritt auszuwählen**.

Speichern Sie, veröffentlichen Sie die Komponente, fügen Sie sie mit dem `Navigation menu` zum Arbeitsplatz hinzu und stellen Sie sicher, dass alle Komponenten an ihrem Platz sind.

<br>

### Zugriff auf die `Managers grid`-Komponente festlegen

Sie müssen zum Menü "Zugriff" im Abschnitt "Berechtigungen" gehen und auf die Schaltfläche "Hinzufügen" in der oberen rechten Ecke klicken.

Ein Fenster mit den Berechtigungseinstellungen öffnet sich auf Ihrem Bildschirm, in dem Sie die Domäne angeben und einen Namen für die Berechtigung vergeben müssen. Um den Zugriff auf die Manipulation der `Managers grid`-Komponente zu gewähren, gehen Sie zu `Permissions`, geben Sie den Abschnitt `Components` ein, finden Sie unsere `Managers grid`-Komponente und wählen Sie die vollständigen Zugriffsrechte dafür aus. Klicken Sie auf die Schaltfläche "Speichern" und fahren Sie mit dem nächsten Abschnitt "Rollen" fort.

Hier müssen Sie ebenfalls auf die Schaltfläche "HINZUFÜGEN" klicken, die erforderliche Domäne auswählen, benennen und die "Berechtigung" auswählen, die Sie zuvor erstellt haben. Fahren Sie dann mit dem Abschnitt `Users` fort.

Im Abschnitt `Users` sind alle Benutzer aufgelistet, die in Ihrem System registriert sind. Klicken Sie auf den Benutzer, dem Sie das Recht gewähren möchten, diese Komponente zu verwenden, wählen Sie in "Kontexte auswählen" "Plattform" -> "System" und suchen Sie in "Rollen auswählen" die Rolle, die Sie zuvor erstellt haben, klicken Sie dann auf das Kontrollkästchen und klicken Sie auf "Speichern".

<br>

### Fazit

Sie haben eine kleine und einfache Anwendung erstellt, in der Sie mit mehreren Komponenten gearbeitet und gelernt haben, wie man sie miteinander verknüpft. Sie haben gelernt, wie man modale Fenster erstellt und begonnen, die Interaktion zwischen Programmiersprachen und den Werkzeugen unserer Plattform zu erkunden.

Versuchen Sie, mehrere Manager zu erstellen, neue Autos zum Verkauf hinzuzufügen, Manager zuzuweisen und zu versuchen, Deals abzuschließen.
Natürlich ist diese Anwendung ein Test; sie kann endlos verbessert und komplexer gestaltet werden. Nach der Erstellung können Sie andere Werkzeuge eigenständig verwenden, unterschiedliche Logik aufbauen und das Design nach Ihren Wünschen anpassen. Die Plattform bietet Ihnen flexible Werkzeuge, die die Entwicklung spannender und einfacher machen!

Beschreibungen der im Tutorial verwendeten Werkzeuge finden Sie im Abschnitt "Anwendungsentwicklung".