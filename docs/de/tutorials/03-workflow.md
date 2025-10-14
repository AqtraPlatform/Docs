# Tutorial №3

<br>

## Python verwenden

### Einführung

<br>

Die Plattform bietet die Möglichkeit, Python für verschiedene Zwecke als praktische und weithin bekannte Skript-/Programmiersprache zu verwenden.

Von der Plattform unterstützte Python-Skripte müssen Python Version 3.0 verwenden, wie hier beschrieben: https://docs.python.org/3/. Der vollständige Entwicklerleitfaden finden Sie im Abschnitt "Using Python".

Die von der Plattform verwendete Version von Python heißt Iron Python, die eine Schnittstelle zu C#-Code bereitstellt. Sie bietet zwei wichtige Bibliotheken, die am Anfang des Skripts importiert werden müssen — `clr` und `system`. Diese Bibliotheken bieten Zugriff auf Plattformentitäten, die über das Skript abgefragt und gesteuert werden können.
<br>

### Möglichkeiten zur Verwendung von Python-Skripten auf der Plattform

<br>

Es gibt mehrere Möglichkeiten, Python auf der Plattform zu verwenden:

- Es ermöglicht die Steuerung von Anwendungsformularen, die mit der Plattform entworfen und ausgeführt wurden, sowie die Bereitstellung benutzerdefinierter Indizes, die als Reaktion auf ein Ereignis ausgelöst werden können, z. B. wenn ein Client eine Schaltfläche drückt.
  <br>

- Aufrufen einer Funktion innerhalb eines "Component Script", zum Beispiel, wenn eine Schaltfläche gedrückt wird:

  - Dazu müssen Sie eine Funktion innerhalb des Component Script definieren, dann zu einem UI-Steuerelement wie einer Schaltfläche gehen, zum Abschnitt "Actions" gehen und den Parameter "Command Type" auf "Execute Script" setzen. Dann müssen Sie den Namen und die Aufrufparameter (falls vorhanden) Ihres Skripts in den bereitgestellten Feldern eingeben.
    <br>

- Verwenden einer Funktion innerhalb eines Component Script für Werteänderungsereignisse:
  - Dazu müssen Sie eine Funktion innerhalb des Component Script definieren, dann zu einem UI-Steuerelement wie einem Textfeld usw. gehen, dann zum Abschnitt "Events" gehen und den Namen Ihres Skripts im Feld "On value change" eingeben.
  - Beachten Sie, dass diese Funktion nur aufgerufen wird, wenn sich die Daten im Feld geändert haben und der Fokus des UI-Steuerelements im Formular dieses UI-Steuerelement verlässt.

<br>

- Durch Abonnieren von Datenänderungen mit der Methode `context.DataModel.Model.Subscribe()`:
  - Der einfachste Weg, dies zu tun, besteht darin, eine Funktion zum Abfangen aller Änderungen (z. B. `def check_all_changes()`) in Ihrem Component Script zu definieren und sich dann darauf zu abonnieren.
  - Ihre Funktion wird jedes Mal aufgerufen, wenn es eine Änderung in den aktuellen Daten des UI-Steuerelements gibt, in dem Moment, in dem dieses UI-Steuerelement den Fokus verliert (z. B. wenn der Benutzer zu einem anderen UI-Steuerelement oder einer anderen Anwendung wechselt).

<br>

- Als Teil einer DataFlow-Aktion führen Sie ein Skript aus, um Entscheidungslogik zu definieren, Daten zu transformieren und interne Variablen festzulegen, die als Teil von DataFlow-Skripten verwendet werden. Beispiele für die Verwendung von Python-Skripten für DataFlow finden Sie im Abschnitt "Using Python".

<br>

### Verwenden von Python zum Zugriff auf Plattformkomponenten

<br>

Um auf Plattformkomponenten zuzugreifen, müssen Sie zuerst die clr-Bibliotheken von IronPython importieren, wie unten gezeigt.

```
#Add IronPython library that imports system CRL (.NET) names into Python
import clr
```

Nach dem Importieren können mehrere Objekte über die Systemvariable `context` innerhalb des Python-Skripts aufgerufen werden.

<br>

### Verwenden von context.Model & context.DataModel

<br>

`context.Model` & `context.DataModel` bieten Zugriff auf verschiedene Datenfelder des Plattformmodells.

Für context.Model umfassen Datenfelder sowohl die von der Plattform bereitgestellten Standard-Komponentenfelder als auch benutzerdefinierte Felder, die vom Komponentenentwickler hinzugefügt wurden.

Für context.DataModel sind nur benutzerdefinierte Felder verfügbar, die von Komponentenentwicklern hinzugefügt wurden.

Es wird empfohlen, context.DataModel zum Zugriff auf alle benutzerdefinierten Felder zu verwenden und context.Model nur zum Zugriff auf die internen Felder der Standardkomponente zu verwenden.

Wenn wir ein Component Script schreiben, das auf dieses Modell zugreift, sind die folgenden Systemmodellvariablen in unserem Skript über context.Model verfügbar:

- `Id` - interner Bezeichner, automatisch von der Plattform für jede Komponente generiert. Wenn Id == 0, bedeutet dies, dass die Komponentendaten noch nicht gespeichert wurden, was darauf hinweist, dass wir uns im Dateneingabemodus für diese bestimmte Instanz der Komponentendaten befinden, z. B. beim Hinzufügen einer neuen Rechnung in unserem Tutorial #1.
- `createDate` - intern festgelegtes Datum, wann die Dateninstanz dieser Komponente zum ersten Mal erstellt wurde
- `name` (String) - systemfreundlicher Name, der standardmäßig zur Anzeige von Links über Catalog-Typ-Felder verwendet wird
- `updateDate` - intern festgelegtes Datum der letzten Aktualisierung dieser Komponentendateninstanz.
- `CreatorSubject` - Daten, die anzeigen, welcher Benutzer die Dateninstanz dieser bestimmten Komponente hinzugefügt hat.
- `changeAuthor` - Daten, die anzeigen, welcher Benutzer diese bestimmte Komponente zuletzt aktualisiert hat

Darüber hinaus sind die folgenden komponentenspezifischen Attribute für unsere Tutorial #1-Komponente über context.DataModel (empfohlen) oder context.Model verfügbar:

- `InvoiceName` - eindeutiger Name für unsere neue Rechnung
- `InvoiceState` - aktueller Status unserer neuen Rechnung
- `InvoiceNumber` - eindeutige Nummernkennung für unsere Rechnung
- `InvoiceDueDate` - Fälligkeitsdatum unserer Rechnung
- `InvoiceTotalValue` - Gesamtwert unserer Rechnung

Schreiben wir nun ein Beispielskript, das einige Felder für eine neue Rechnung vorab ausfüllt.

<br>

```python
#Start of the script
#Add IronPython library that imports system CRL (.NET) names into Python
import clr

#Get Component's DataModel reference
datamodel = context.DataModel.Model
# context.Model.Id shows internal Id for the component data instance
if (context.Model.Id == 0):
# If context.Model.Id is 0, then the instance has not yet been created,
# That means we are creating a new invoice
# We will then set some fields with default values
# Since this is a new Invoice,
# We'll set it's status to Under Review and provide default number and name
datamodel.InvoiceNumber = 11111
datamodel.InvoiceName = 'PLEASE_SET_A_UNIQUE_NAME'
datamodel.InvoiceState = 0
#End of the script
```

<br>

Wenn wir jetzt die Tutorial #1-Anwendung öffnen und auf die Schaltfläche "Add" klicken, um eine neue Rechnung hinzuzufügen, sieht der Bildschirm so aus:

<br>

![Tutorial 3.1](../assets/images/tutorials/tut3.1.png)

<br>

### Verwenden von context.Properties

<br>

`context.Properties` ermöglicht den Zugriff auf alle Komponentenelemente und kann beispielsweise verwendet werden, um Formular-UI-Steuerelementfunktionen zu nutzen, um ein bestimmtes UI-Steuerelement zu verwalten.

Um auf ein UI-Steuerelement zuzugreifen, verwenden Sie `context.Properties` wie folgt:

```
context.Properties.<Internal_UI_Control_Name>.<UIControlProperty> = <Value>
```

Hier sollte `<Internal_UI_Control_Name>` durch den Namen Ihres UI-Steuerelements ersetzt werden, das Sie während des Designs konfiguriert haben. Im Fall von Tutorial #1 haben wir beispielsweise den internen Namen für das InvoiceState-UI-Steuerelement wie unten gezeigt festgelegt:

<br>

![Tutorial 3.2](../assets/images/tutorials/tut3.2.png)

<br>

Jetzt können wir diesen internen Namen verwenden, um die folgende Logik festzulegen:

1. Beim Erstellen einer neuen Rechnung wird der Status auf "Under Review" gesetzt.
2. Das Ändern des Statusfelds ist verboten, was bedeutet, dass dieses Feld deaktiviert, aber sichtbar sein sollte.

Der Weg, dies zu tun, besteht darin, die Eigenschaft `Disable` unseres UI-Steuerelements zu verwenden, um sie auf `True` zu setzen. Dadurch wird das Feld angezeigt, kann jedoch nicht vom Benutzer geändert werden, der die neue Rechnung erstellt. Dies wird durch Hinzufügen einer Codezeile wie unten gezeigt durchgeführt:

```
context.Properties.UI_InvoiceStatus.Disabled = True
```

Das Hinzufügen zu unserem Component Script führt zu den folgenden Änderungen in unserem neuen Rechnungshinzufügungsformular.

<br>

![Tutorial 3.3](../assets/images/tutorials/tut3.3.png)

<br>

Wie Sie sehen können, ist das Feld "Invoice Status" jetzt deaktiviert.

Ein weiteres häufig verwendetes `context.Properties`-Feld zur Verwaltung von UI-Steuerelementen ist `Visible`. Wenn es auf `False` gesetzt ist, wird dieses spezifische UI-Steuerelement nicht im Formular angezeigt. Es kann dann durch Setzen auf `True` wieder aktiviert werden. Dies kann für jedes UI-Steuerelement durchgeführt werden, einschließlich Panels, die mehrere verschiedene UI-Steuerelemente enthalten.

Ein Beispiel dafür, wie es im Kontext unseres Tutorial #1 verwendet werden kann, um das Feld "Invoice Status" anfänglich zu verbergen, ist unten gezeigt.

<br>

```python
if (context.Model.Id == 0):
    context.Properties.UI_InvoiceStatus.Visible = False
if (context.Model.Id > 0):
    context.Properties.UI_InvoiceStatus.Visible = True
```

<br>

Es gibt auch das Feld `Hidden`, das Benutzeroberflächenelemente verbirgt/zeigt, ähnlich wie das Feld `Visible`.

Ein weiteres häufig verwendetes `context.Properties`-Feld ist `Required`. Wenn es auf `True` gesetzt ist, wird das spezifische UI-Steuerelement obligatorisch (kann nicht leer sein), und wenn es auf `False` gesetzt ist, wird es optional. Beachten Sie, dass dies nur den Status des UI-Steuerelements für die benutzerdefinierte Eigenschaft in der aktuellen Formularinstanz ändert, nicht die benutzerdefinierte Eigenschaft selbst, die Formularvorlage oder UI-Steuerelemente für diese benutzerdefinierte Eigenschaft in anderen Formularen.

<br>

### Verwenden von context.Form

<br>

`context.Form` kann verwendet werden, um auf Formulardaten zuzugreifen (z. B. für Validierungszwecke während der Formularverarbeitung, bevor die Formulardaten im internen Speicher gespeichert werden) oder um die visuelle Darstellung des Formulars zu verwalten, z. B. durch Festlegen einer Fehlermeldung.

Verwenden Sie dazu `context.Form.Get(<CustomFieldName>)`, um ein Objekt zu erhalten, das ein bestimmtes Feld darstellt. Dann können Sie die folgenden Funktionen mit diesem Objekt verwenden.

- `context.Form.Get(<CustomFieldName>).SetValue(<Value>)` — setzt den Wert für ein bestimmtes UI-Steuerelement im aktuellen Formular.
- `context.Form.Get(<CustomFieldName>).AddError(<StringValue>)` — setzt eine Fehlermeldung, die unter einem bestimmten UI-Steuerelement im aktuellen Formular angezeigt wird.
- `context.Form.Get(<CustomFieldName>).ClearError()` — löscht die Fehlermeldung, die unter einem bestimmten UI-Steuerelement im aktuellen Formular angezeigt wird.

Das folgende Skripterweiterung zeigt, wie die Situation überprüft wird, in der der Benutzer den Standardrechnungsnamen nicht geändert hat, den wir oben in den Beispielen für Tutorial #1 festgelegt haben.

<br>

```python
if datamodel.InvoiceName == 'PLEASE_SET_A_UNIQUE_NAME':
    context.Form.Get("InvoiceName").AddError("Please set a unique invoice name")
else:
    context.Form.Get("InvoiceName").ClearError()
```

<br>

Das Ergebnis sieht wie der folgende Screenshot aus, wenn der Standardname nicht geändert wurde:

<br>

![Tutorial 3.4](../assets/images/tutorials/tut3.4.png)

<br>

### Verwenden von context.Commands

<br>

`context.Commands` kann verwendet werden, um die Benutzeroberfläche der aktuell ausgeführten Komponente zu verwalten, den Inhalt des aktuellen Formulars zu ändern, verschiedene Seiten zu öffnen, neue Komponenten zu öffnen, zur vorherigen Seite zurückzukehren oder sogar neue Workflows, Dataflows oder Skripte zu starten.

Diese Befehle werden normalerweise in Skripten verwendet, die von der ExecuteScript-Aktion mit Schaltflächen aufgerufen werden, und in ähnlichen Fällen. In unserem Tutorial #1 kann beispielsweise die Schaltfläche Back to All Invoices das folgende Skript verwenden, um zur vorherigen Seite zurückzukehren:

<br>

```python
def navigate_back():
    context.Commands.NavigationBack()
```

<br>

Dieses Skript sollte Teil des Component Script sein und für die Schaltfläche Back to All Invoices eingerichtet werden, im Abschnitt `Actions` → `Command Type`: `Execute Script` → `Method Name`: `navigate back`.

<br>

Andere verfügbare context.Commands-Funktionen:

- `context.Commands.AddItem(GUID)` - UI-Steuerelement zur Seite über die GUID hinzufügen.
- `context.Commands.ChangePageAsync(GUID)` - Seite über ihre GUID öffnen
- `context.Commands.ChangePageByName(«PageName»)` - aktuelle Komponentenseite zu einer neuen Seite mit dem internen Namen ändern
- `context.Commands.OpenComponent(GUID ComponentID, GUID PageID)` - neue Komponente und eine bestimmte Seite innerhalb der Komponente öffnen
- `context.Commands.EditItem(GUID UI_ControlID, EntityId)` - UI-Fokus auf ein bestimmtes UI-Steuerelement und bestimmte Daten (unter Verwendung seines internen Bezeichners) verschieben
- `context.Commands.ExecuteWorkflow(GUID WorkflowID)` - Workflow über seinen Bezeichner ausführen. Zusätzlich können Sie WaitComplete bei Bedarf auf true oder false setzen.
- `context.Commands.ExecuteDataflow(GUID dataflow identifier, ContextID)` - Dataflow über seine GUID und den angegebenen Datenkontext ausführen.
- `context.Commands.ExecuteScript(String ScriptName, StringParams Script)` - Skript (Funktion) aus dem Component Script mit einigen Parametern ausführen.
