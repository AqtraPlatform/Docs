# Listenansicht

![](../../assets/images/app-development/list-view.png)

## Allgemeine Informationen
„Listenansicht“ ist eine UI-Komponente, die zur Anzeige und Konfiguration der „Karten“-Präsentation von Daten verwendet wird.

## Parameter
**Komponenten Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld   | Wertoptionen          | Zweck                         |
|---------------------|--------------------|------------------------|------------------------------------|
|                     | Name               | -                      | Name der UI-Komponente im System |
| Allgemein           | Komponente         | Mehrfachauswahl aus Katalog | Enthält eine Liste aller Komponenten |
|                     | Anzahl der Spalten | -                      | Anzahl der Container-Spalten      |
|                     | Anzahl der Zeilen   | -                      | Anzahl der Container-Zeilen       |
|                     | Spaltenabstand     | -                      | Spaltenabstand                   |
|                     | Zeilenabstand      | -                      | Zeilenabstand                    |
|                     | Seitengröße        | -                      | Containergröße                   |
|                     | Manuelles Neuladen | true, false            | Möglichkeit, Daten manuell neu zu laden |
|                     | Seitenauswahl ausblenden | true, false        | Seitenauswahl ausblenden         |
|                     | Drag-and-Drop aktivieren | true, false        | Drag-and-Drop-Funktion aktivieren |
|                     | Drag-and-Drop-Gruppe | -                    | Drag-and-Drop-Gruppe (falls vorhanden) |
|                     | Automatisierungs-ID | -                     | ID für Automatisierung           |
| Ereignisse          | Bei Datenquelle geladen | -                  | Ereignis beim Laden der Datenquelle |
|                     | Bei geladen        | -                      | Ereignis beim Laden der Komponente |
|                     | Bei Drop           | -                      | Drag-and-Drop-Ereignis          |

**CSS-Eigenschaften**

| Einstellungsgruppe | Einstellungsfeld   | Wertoptionen          | Zweck                         |
|---------------------|--------------------|------------------------|------------------------------------|
| Layout              | Breite             | -                      | Breite der Komponente            |
|                     | Höhe               | -                      | Höhe der Komponente              |
|                     | Rand               | -                      | Äußere Polsterung der Komponente  |
|                     | Innenabstand       | -                      | Innere Polsterung der Komponente  |
|                     | Sichtbar           | true, false            | Sichtbarkeit der Komponente       |
|                     | Ausgeblendet       | true, false            | Verbergung der Komponente         |
|                     | Orientierung       | Horizontal, Vertikal   | Orientierung der Komponente       |
| Erscheinung         | Eckenradius        | -                      | Radius der Eckenrundung          |
|                     | Randdicke          | -                      | Randdicke der Komponente         |
|                     | Opazität           | -                      | Transparenz der Komponente        |
| Pinsel              | Hintergrund        | -                      | Hintergrundfarbe der Komponente   |
|                     | Randpinsel         | -                      | Randfarbe der Komponente          |

## Verwendung der Drag-and-Drop-Funktion
Zuerst müssen Sie in der Gruppe „Allgemein“ die folgende Option auswählen:

![](../../assets/images/app-development/enable-drag-and-drop.png)

Nach dem Speichern und Veröffentlichen wird Drag-and-Drop bereits für diese Listenansicht am Arbeitsplatz verfügbar sein. Für den anschließenden korrekten Betrieb müssen Sie zum Komponentenskript gehen und die Funktion zur Verarbeitung des Drag-and-Drop (bei Drop) Ereignisses vorbereiten.
Hier ist ein Beispiel für die Funktion, die auf ein Kanban-Board angewendet wird, das aus einer Hauptlistenansicht und einer verschachtelten Listenansicht besteht. Die Hauptansicht erfüllt die Funktion der Phasen des Verkaufstrichters und befindet sich in horizontaler Position, während die verschachtelte Ansicht die Deals selbst enthält und in vertikaler Position ist. Die Funktion nimmt die ID des Objekts, das gezogen wird (in diesem Fall den Deal), und die Phase, in die der Deal übertragen wird, und ruft dann den Datenfluss auf und aktualisiert, falls erfolgreich abgeschlossen, die Listenansicht, indem der Deal in eine neue Phase verschoben wird:

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

## Fälle
- **Datenanzeige**: Effektiv zur Präsentation von Daten in Form von Karten oder Listen.
- **Benutzeroberfläche**: Geeignet für Schnittstellen, die eine Darstellung von Informationen in Form von Karten oder Listen erfordern.

## Ausnahmen
- **Eingeschränkte Flexibilität**: Nicht geeignet für die Anzeige von Daten über das Karten- oder Listenformat hinaus, da es sich auf eine spezifische visuelle Darstellung spezialisiert.
- **Visuelle Einschränkungen**: Der Stil und das Design können durch CSS-Einstellungen eingeschränkt sein, die möglicherweise nicht alle Designanforderungen erfüllen.