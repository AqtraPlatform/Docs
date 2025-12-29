# Tutorial №3

<br>

## Verwendung von Python

### Einführung

<br>

Die Plattform bietet die Möglichkeit, Python für verschiedene Zwecke als eine bequeme und weit verbreitete Skript-/Programmiersprache zu verwenden.

Python-Skripte, die von der Plattform unterstützt werden, müssen die Python-Version 3.0 verwenden, wie hier beschrieben: https://docs.python.org/3/. Der vollständige Entwicklerleitfaden ist im Abschnitt "Verwendung von Python" zu finden.

Die von der Plattform verwendete Python-Version wird als Iron Python bezeichnet, die eine Schnittstelle zu C#-Code bereitstellt. Sie bietet zwei wichtige Bibliotheken, die zu Beginn des Skripts importiert werden müssen — `clr` und `system`. Diese Bibliotheken bieten Zugriff auf Plattformentitäten, die aus dem Skript abgefragt und gesteuert werden können.
<br>

### Möglichkeiten zur Verwendung von Python-Skripten auf der Plattform

<br>

Es gibt mehrere Möglichkeiten, Python auf der Plattform zu verwenden:

- Es ermöglicht die Steuerung von Anwendungsformularen, die mit der Plattform entworfen und ausgeführt wurden, sowie die Bereitstellung benutzerdefinierter Indizes, die als Reaktion auf ein Ereignis, wie z.B. das Drücken eines Buttons durch einen Client, ausgelöst werden können.
  <br>

- Aufrufen einer Funktion innerhalb eines "Komponenten-Skripts", zum Beispiel, wenn ein Button gedrückt wird:

  - Dazu müssen Sie eine Funktion innerhalb des Komponenten-Skripts definieren, dann zu einem UI-Steuerelement wie einem Button gehen, zum Abschnitt "Aktionen" wechseln und den Parameter "Befehlsart" auf "Skript ausführen" setzen. Dann müssen Sie den Namen und die Aufrufparameter (falls vorhanden) Ihres Skripts in die bereitgestellten Felder eingeben.
    <br>

- Verwenden einer Funktion innerhalb eines Komponenten-Skripts für Wertänderungsereignisse:
  - Dazu müssen Sie eine Funktion innerhalb des Komponenten-Skripts definieren, dann zu einem UI-Steuerelement wie einem Textfeld usw. gehen, dann zum Abschnitt "Ereignisse" wechseln und den Namen Ihres Skripts im Feld "Bei Wertänderung" eingeben.
  - Beachten Sie, dass diese Funktion nur aufgerufen wird, wenn sich die Daten im Feld geändert haben und der Fokus des UI-Steuerelements im Formular dieses UI-Steuerelement verlässt.

<br>

- Durch Abonnieren von Datenänderungen mit der `context.DataModel.Model.Subscribe()`-Methode:
  - Der einfachste Weg, dies zu tun, besteht darin, eine Funktion zu definieren, die alle Änderungen abfängt (z.B. `def check_all_changes()`) in Ihrem Komponenten-Skript, und sich dann dafür anzumelden.
  - Ihre Funktion wird jedes Mal aufgerufen, wenn es eine Änderung der aktuellen Daten des UI-Steuerelements gibt, in dem Moment, in dem dieses UI-Steuerelement den Fokus verliert (zum Beispiel, wenn der Benutzer zu einem anderen UI-Steuerelement oder einer anderen Anwendung wechselt).

<br>

- Im Rahmen einer DataFlow-Aktion ein Skript ausführen, um Entscheidungslogik zu definieren, Daten zu transformieren und interne Variablen festzulegen, die als Teil von DataFlow-Skripten verwendet werden. Sie können Beispiele für die Verwendung von Python-Skripten für DataFlow im Abschnitt "Verwendung von Python" sehen.

<br>

### Verwendung von Python zum Zugriff auf Plattformkomponenten

<br>

Um auf Plattformkomponenten zuzugreifen, müssen Sie zunächst die clr-Bibliotheken von IronPython importieren, wie unten gezeigt.

```
#Add IronPython library that imports system CRL (.NET) names into Python
import clr
```

Nach dem Import können mehrere Objekte von innerhalb des Python-Skripts über die Systemvariable `context` zugegriffen werden.

<br>

### Verwendung von context.Model & context.DataModel

<br>

`context.Model` & `context.DataModel` bieten Zugriff auf verschiedene Datenfelder des Plattformmodells.

Für context.Model umfassen die Datenfelder sowohl die standardmäßigen Komponentenfelder, die von der Plattform bereitgestellt werden, als auch benutzerdefinierte Felder, die vom Komponentenentwickler hinzugefügt wurden.

Für context.DataModel sind nur benutzerdefinierte Felder verfügbar, die von Komponentenentwicklern hinzugefügt wurden.

Es wird empfohlen, context.DataModel zu verwenden, um auf alle benutzerdefinierten Felder zuzugreifen, und context.Model nur zu verwenden, um auf die internen Felder der Standardkomponente zuzugreifen.

Wenn wir ein Komponenten-Skript schreiben, das auf dieses Modell zugreift, werden die folgenden Systemmodellvariablen in unserem Skript über context.Model verfügbar sein:
- `Id` - interner Bezeichner, der automatisch von der Plattform für jede Komponente generiert wird. Wenn Id == 0, bedeutet dies, dass die Komponentendaten noch nicht gespeichert wurden, was darauf hinweist, dass wir uns im Dateneingabemodus für diese spezielle Instanz der Komponentendaten befinden, wie zum Beispiel beim Hinzufügen einer neuen Rechnung in unserem Tutorial #1.
- `createDate` - intern festgelegtes Datum, an dem die Dateninstanz dieser Komponente erstmals erstellt wurde
- `name` (String) - benutzerfreundlicher Name des Systems, der standardmäßig verwendet wird, um Links über Katalogtypfelder anzuzeigen
- `updateDate` - intern festgelegtes Datum der letzten Aktualisierung der Dateninstanz dieser Komponente.
- `CreatorSubject` - Daten, die zeigen, welcher Benutzer die Dateninstanz dieser speziellen Komponente hinzugefügt hat.
- `changeAuthor` - Daten, die zeigen, welcher Benutzer diese spezielle Komponente zuletzt aktualisiert hat

Zusätzlich sind die folgenden komponentenspezifischen Attribute für unsere Tutorial #1-Komponente über context.DataModel (empfohlen) oder context.Model verfügbar:

- `InvoiceName` - eindeutiger Name für unsere neue Rechnung
- `InvoiceState` - aktueller Status unserer neuen Rechnung
- `InvoiceNumber` - eindeutige Nummernkennung für unsere Rechnung
- `InvoiceDueDate` - Fälligkeitsdatum unserer Rechnung
- `InvoiceTotalValue` - Gesamtwert unserer Rechnung

Lass uns nun ein Beispielskript schreiben, das einige Felder für eine neue Rechnung vorausfüllt.

<br>

```python
#Start of the script
#Add IronPython library that imports system CRL (.NET) names into Python
import clr

#Get Component’s DataModel reference
datamodel = context.DataModel.Model
# context.Model.Id shows internal Id for the component data instance
if (context.Model.Id == 0):
# If context.Model.Id is 0, then the instance has not yet been created,
# That means we are creating a new invoice
# We will then set some fields with default values
# Since this is a new Invoice,
# We’ll set it’s status to Under Review and provide default number and name
datamodel.InvoiceNumber = 11111
datamodel.InvoiceName = 'PLEASE_SET_A_UNIQUE_NAME'
datamodel.InvoiceState = 0
#End of the script
```

<br>

Wenn wir nun die Anwendung Tutorial #1 öffnen und auf die Schaltfläche "Hinzufügen" klicken, um eine neue Rechnung hinzuzufügen, wird der Bildschirm wie folgt aussehen:

<br>

![Tutorial 3.1](../assets/images/tutorials/tut3.1.png)

<br>

### Verwendung von context.Properties

<br>

`context.Properties` ermöglicht den Zugriff auf alle Komponentenelemente und kann beispielsweise verwendet werden, um Funktionen von UI-Steuerelementen zu nutzen, um ein bestimmtes UI-Steuerelement zu verwalten.

Um auf ein UI-Steuerelement zuzugreifen, verwenden Sie `context.Properties` wie folgt:

```
context.Properties.<Internal_UI_Control_Name>.<UIControlProperty> = <Value>
```

Hier sollte `<Internal_UI_Control_Name>` durch den Namen Ihres UI-Steuerelements ersetzt werden, den Sie während des Designs konfiguriert haben. Zum Beispiel haben wir im Fall von Tutorial #1 den internen Namen für das UI-Steuerelement InvoiceState wie unten gezeigt festgelegt:

<br>

![Tutorial 3.2](../assets/images/tutorials/tut3.2.png)

<br>

Jetzt können wir diesen internen Namen verwenden, um die folgende Logik festzulegen:

1. Beim Erstellen einer neuen Rechnung wird der Status auf "In Überprüfung" gesetzt.
2. Das Ändern des Statusfeldes ist untersagt, was bedeutet, dass dieses Feld deaktiviert, aber sichtbar sein sollte.

Der Weg, dies zu tun, besteht darin, die `Disable`-Eigenschaft unseres UI-Steuerelements so festzulegen, dass sie auf `True` gesetzt wird. Dadurch wird das Feld angezeigt, kann jedoch nicht vom Benutzer, der die neue Rechnung erstellt, geändert werden. Dies geschieht durch das Hinzufügen einer Codezeile, wie unten gezeigt:

```
context.Properties.UI_InvoiceStatus.Disabled = True
```

Das Hinzufügen dieses Codes zu unserem Komponentenskript führt zu den folgenden Änderungen in unserem Formular zum Hinzufügen einer neuen Rechnung.

<br>

![Tutorial 3.3](../assets/images/tutorials/tut3.3.png)

<br>

Wie Sie sehen können, ist das Feld "Rechnungsstatus" jetzt deaktiviert.

Ein weiteres häufig verwendetes `context.Properties`-Feld zur Verwaltung von UI-Steuerelementen ist `Visible`. Wenn es auf `False` gesetzt ist, wird dieses spezifische UI-Steuerelement nicht im Formular angezeigt. Es kann dann wieder aktiviert werden, indem es auf `True` gesetzt wird. Dies kann für jedes UI-Steuerelement, einschließlich Panels, die mehrere verschiedene UI-Steuerelemente enthalten, durchgeführt werden.

Ein Beispiel, wie es im Kontext unseres Tutorial #1 verwendet werden kann, um das Feld "Rechnungsstatus" zunächst auszublenden, ist unten gezeigt.

<br>

```python
if (context.Model.Id == 0):
    context.Properties.UI_InvoiceStatus.Visible = False
if (context.Model.Id > 0):
    context.Properties.UI_InvoiceStatus.Visible = True
```

<br>

Es gibt auch das `Hidden`-Feld, das Benutzeroberflächenelemente ausblendet/anzeigt, ähnlich dem `Visible`-Feld.

Ein weiteres häufig verwendetes `context.Properties`-Feld ist `Required`. Wenn es auf `True` gesetzt ist, wird das spezifische UI-Steuerelement obligatorisch (kann nicht leer sein), und wenn es auf `False` gesetzt ist, wird es optional. Beachten Sie, dass dies nur den Zustand des UI-Steuerelements für die benutzerdefinierte Eigenschaft in der aktuellen Formularinstanz ändert, nicht die benutzerdefinierte Eigenschaft selbst, die Formularvorlage oder UI-Steuerelemente für diese benutzerdefinierte Eigenschaft in anderen Formularen.

<br>
### Verwendung von context.Form

<br>

`context.Form` kann verwendet werden, um auf Formulardaten zuzugreifen (z. B. zu Validierungszwecken während der Formularverarbeitung, bevor die Formulardaten im internen Speicher gespeichert werden) oder um die visuelle Darstellung des Formulars zu verwalten, z. B. durch Setzen einer Fehlermeldung.

Um dies zu tun, verwenden Sie `context.Form.Get(<CustomFieldName>)`, um ein Objekt zu erhalten, das ein bestimmtes Feld darstellt. Dann können Sie die folgenden Funktionen mit diesem Objekt verwenden.

- `context.Form.Get(<CustomFieldName>).SetValue(<Value>)` — setzt den Wert für ein bestimmtes UI-Steuerelement im aktuellen Formular.
- `context.Form.Get(<CustomFieldName>).AddError(<StringValue>)` — setzt eine Fehlermeldung, die unter einem bestimmten UI-Steuerelement im aktuellen Formular angezeigt wird.
- `context.Form.Get(<CustomFieldName>).ClearError()` — löscht die Fehlermeldung, die unter einem bestimmten UI-Steuerelement im aktuellen Formular angezeigt wird.

Die folgende Skripterweiterung zeigt, wie man die Situation überprüft, in der der Benutzer den Standardrechnungsnamen, den wir oben in den Beispielen für Tutorial #1 festgelegt haben, nicht geändert hat.

<br>

```python
if datamodel.InvoiceName == 'PLEASE_SET_A_UNIQUE_NAME':
    context.Form.Get("InvoiceName").AddError("Please set a unique invoice name")
else:
    context.Form.Get("InvoiceName").ClearError()
```

<br>

Das Ergebnis wird wie der folgende Screenshot aussehen, wenn der Standardname nicht geändert wurde:

<br>

![Tutorial 3.4](../assets/images/tutorials/tut3.4.png)

<br>

### Verwendung von context.Commands

<br>

`context.Commands` kann verwendet werden, um die UI der aktuell ausgeführten Komponente zu verwalten, den Inhalt des aktuellen Formulars zu ändern, verschiedene Seiten zu öffnen, neue Komponenten zu öffnen, zur vorherigen Seite zurückzukehren oder sogar neue Workflows, Datenflüsse oder Skripte zu starten.

Diese Befehle werden typischerweise innerhalb von Skripten verwendet, die durch die ExecuteScript-Aktion mit Schaltflächen aufgerufen werden, und in ähnlichen Fällen. Zum Beispiel kann in unserem Tutorial #1 die Schaltfläche "Zurück zu allen Rechnungen" das folgende Skript verwenden, um zur vorherigen Seite zurückzukehren:

<br>

```python
def navigate_back():
    context.Commands.NavigationBack()
```

<br>

Dieses Skript sollte Teil des Komponentenskripts sein und für die Schaltfläche "Zurück zu allen Rechnungen" im `Actions` Abschnitt -> `Command Type`: `Execute Script` -> `Method Name`: `navigate back` eingerichtet werden.

<br>

Weitere verfügbare Funktionen von context.Commands:

- `context.Commands.AddItem(GUID)` - fügt ein UI-Steuerelementelement zur Seite unter Verwendung der GUID hinzu.
- `context.Commands.ChangePageAsync(GUID)` - öffnet eine Seite unter Verwendung ihrer GUID
- `context.Commands.ChangePageByName(«PageName»)` - ändert die aktuelle Komponentenseite zu einer neuen Seite unter Verwendung des internen Namens
- `context.Commands.OpenComponent(GUID ComponentID, GUID PageID)` - öffnet eine neue Komponente und eine spezifische Seite innerhalb der Komponente
- `context.Commands.EditItem(GUID UI_ControlID, EntityId)` - verschiebt den UI-Fokus zu einem bestimmten UI-Steuerelementelement und spezifischen Daten (unter Verwendung seiner internen Kennung)
- `context.Commands.ExecuteWorkflow(GUID WorkflowID)` - führt einen Workflow unter Verwendung seiner Kennung aus. Zusätzlich können Sie WaitComplete auf true oder false setzen, falls erforderlich.
- `context.Commands.ExecuteDataflow(GUID dataflow identifier, ContextID)` - führt einen Datenfluss unter Verwendung seiner GUID und des angegebenen Datenkontexts aus.
- `context.Commands.ExecuteScript(String ScriptName, StringParams Script)` - führt ein Skript (Funktion) aus dem Komponentenskript mit einigen Parametern aus.