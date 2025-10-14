# Tutorial №1

<br>

## Erstellen Ihrer ersten Anwendung — Rechnungsinventar

<br>

**Anwendungsbeschreibung: Rechnungsinventar**

Wir werden eine einfache Anwendung erstellen, mit der Sie Rechnungen hinzufügen, anzeigen und bearbeiten können.

Jede Rechnung enthält die folgenden Daten (siehe Tabelle unten).

| Kurzbeschreibung          | Detaillierte Beschreibung                                                 |
| ------------------------- | ------------------------------------------------------------------------- |
| Rechnungsnummer           | Vom Lieferanten der Rechnung zugewiesene Nummer.                          |
| Rechnungstitel            | Beschreibung des Rechnungspostens.                                        |
| Rechnungsgesamtbetrag     | Nummer, die den in der Rechnung in Rechnung gestellten Geldbetrag angibt. |
| Rechnungsfälligkeitsdatum | Datum, an dem die Rechnung zur Zahlung fällig ist.                        |

<br>

Darüber hinaus verfolgen wir den Rechnungsstatus wie folgt (siehe Tabelle unten).

| ID  | Lesbarer Titel         | Beschreibung                                                                                     |
| --- | ---------------------- | ------------------------------------------------------------------------------------------------ |
| 0   | In Prüfung             | Wird sofort bei der Erstellung der Rechnung zugewiesen.                                          |
| 1   | Zur Zahlung akzeptiert | Wird nach der Rechnungsprüfung und Genehmigung zur Zahlung zugewiesen.                           |
| 2   | Abgelehnt              | Wird nach Abschluss der Prüfung zugewiesen, aber die Rechnung wird nicht zur Zahlung akzeptiert. |
| 3   | Bezahlt                | Wird nach der Bezahlung der Rechnung zugewiesen.                                                 |
| 4   | Überfällig             | Zeigt an, dass die Rechnung unbezahlt ist und das Fälligkeitsdatum überschritten wurde.          |

<br>

Die Basisversion der Anwendung hat 2 Hauptbildschirme.

- Eine Liste aller Rechnungen im System, die mit allen oben beschriebenen Rechnungsfeldern gefiltert und/oder sortiert werden kann. Wir nennen es "Alle Rechnungen".
- Ein Bildschirm zum Hinzufügen einer neuen oder Bearbeiten einer vorhandenen Rechnung. Wir nennen es "Rechnung bearbeiten/anzeigen".

Nach der Erstellung sieht die Anwendung wie der Screenshot unten aus.

<br>

![Tutorial 1](../assets/images/tutorials/tut1.png)

<br>

## Studio öffnen

Das Erstellen einer Anwendung auf der Plattform beginnt mit dem Öffnen von Studio und dem Hinzufügen einer Komponente.

Sie können Studio über den Link https://<your_hosting_name>/studio/ öffnen.

Wenn beispielsweise der Domänenname, unter dem Sie Ihre Instanz der Plattform bereitgestellt haben, [my.platform.io](http://my.platform.io/) lautet, können Sie über die folgende URL auf Studio zugreifen: "[https://my.platform.io/studio/"](https://my.platform.io/studio/%E2%80%9D).

Nach der Anmeldung bei Studio sehen Sie den folgenden Bildschirm mit einem Menü auf der linken Seite, in dem Home, Applications & Access aufgeführt sind. Wählen Sie Applications→Components.

<br>

![Tutorial 2](../assets/images/tutorials/tut2.png)

<br>

Sie sehen eine Liste aller vorhandenen Komponenten. Klicken Sie auf die Schaltfläche "Add" und wählen Sie die Option "Component", wie unten gezeigt.

<br>

![Tutorial 3](../assets/images/tutorials/tut3.png)

<br>

Herzlichen Glückwunsch, Sie haben jetzt Ihre erste Komponente! Benennen wir sie "Invoice Inventory" und legen Sie einige wichtige Parameter fest.

Um Ihre Komponente zu benennen, klicken Sie auf die Schaltfläche "Settings" und geben Sie dann "Invoice Inventory" in das Feld "Name" ein.

Da unsere Anwendung nur für Personen mit den entsprechenden Anmeldedaten zugänglich ist, müssen wir sicherstellen, dass das Feld "Access Mode" auf "Private" gesetzt ist.

## Einrichten der erforderlichen Datenfelder

Klicken Sie auf Save, um sicherzustellen, dass Ihre Komponente gespeichert wird. Es wird eine Fehlermeldung angezeigt, da wir noch keine Daten in unserer Komponente haben. Fügen wir einige Daten hinzu.
Gehen Sie zur Registerkarte "Definition" und klicken Sie auf das "+"-Zeichen neben "Invoice Inventory". Die Plattform fügt automatisch mehrere Systemfelder hinzu, die Sie im Screenshot sehen, sowie Ihr erstes Datenfeld — Property_1.

<br>

![Tutorial 4](../assets/images/tutorials/tut4.png)

<br>

Klicken Sie auf das Bearbeitungssymbol (Stift) auf Property_1. Sie sehen ein neues Panel auf der rechten Seite. Hier definieren Sie, wie Ihre Datenfelder vom System interpretiert werden sollen.

Name — dies ist der interne Systemname für Ihr Datenfeld (Eigenschaft). Er sollte nur englische Buchstaben ohne Leerzeichen enthalten. Sie werden diesen Namen später verwenden, beispielsweise in Python-Skripten, um der Anwendung erweiterte Logik hinzuzufügen.

_Hinweis: Ab Version 0.4.x gibt es auch eine Systemeigenschaft "name", die automatisch hinzugefügt wird, wenn die erste Eigenschaft erstellt wird, und verwendet wird, wenn Sie Benutzern Werte für Benutzer anzeigen müssen, wenn Sie Eigenschaften vom Typ Catalog (Link zu einer anderen Komponente; wird für 1:1- und M:1-Beziehungen verwendet) oder Array (Link zu einem Array anderer Komponenten; wird für 1:M- und M:M-Beziehungen verwendet) verwenden. Im Gegensatz zum internen System Name, der für jede Eigenschaft innerhalb der Komponente vorhanden ist, ist das Systemfeld name eines für die gesamte Komponente._

Title — so wird Ihr Datenfeld in der Benutzeroberfläche benannt. Hier können Sie alle benötigten Zeichen verwenden.

Für Datenfelder, die immer nicht leer sein müssen, stellen Sie sicher, dass das Kontrollkästchen "Required" ausgewählt ist.

Der Property Type ermöglicht es Ihnen, einen der verfügbaren Datenfeldtypen auszuwählen.

Zunächst fügen wir das Datenfeld Invoice Name hinzu und setzen den Eigenschaftstyp auf String. Da Rechnungsnamen theoretisch von externen Lieferanten stammen, können sie sich wiederholen, daher setzen wir hier nicht das Primary Key-Flag.

<br>

![Tutorial 5](../assets/images/tutorials/tut5.png)

<br>

Nachdem wir unser erstes Feld eingerichtet haben, klicken wir auf Save.

Fügen wir nun die anderen Felder hinzu, die wir in unserer Anwendung benötigen: Rechnungsnummer, Rechnungsfälligkeitsdatum, Rechnungsgesamtbetrag und Rechnungsstatus.

**Rechnungsnummer** ist die interne Kontonummer jeder eindeutigen Rechnung, die im Allgemeinen mit dem Rechnungsnamen übereinstimmt, aber wir stellen sicher, dass sie mindestens 2 Zeichen lang ist, indem wir den Min length-Wert auf 2 setzen, wie unten gezeigt. Sie muss auch eindeutig sein, um verschiedene Rechnungen zu unterscheiden, auch wenn sie dieselben Namen haben, daher setzen wir das Primary Key-Flag. Dies teilt der Plattform mit, dass es nicht mehr als eine Invoice Number-Eigenschaft mit demselben Wert geben kann. Wenn versucht wird, einen doppelten Wert zu erstellen, gibt das System einen Fehler aus.

<br>

![Tutorial 6](../assets/images/tutorials/tut6.png)

<br>

Für das erwartete Rechnungsfälligkeitsdatum setzen Sie den Property type auf DateTime.

<br>

![Tutorial 7](../assets/images/tutorials/tut7.png)

<br>

Der Rechnungsgesamtbetrag sollte als Zahl festgelegt werden. Wir setzen auch das Minimal value-Feld auf 0, um sicherzustellen, dass es keine negativen Rechnungen gibt (dies kann in einer echten Finanzanwendung anders sein, wo negative Werte beispielsweise zur Darstellung von Gutschriften von Lieferanten verwendet werden).

<br>

![Tutorial 8](../assets/images/tutorials/tut8.png)

<br>

Schließlich fügen wir das Feld "Invoice Status" hinzu. Wie in der Anwendungsbeschreibung angegeben, wird dies ein Satz von Status sein, der wie folgt aussehen sollte:

0|In Prüfung
1|Zur Zahlung akzeptiert
2|Abgelehnt
3|Bezahlt
4|Überfällig

Dazu müssen wir den Eigenschaftstyp auf Integer (ab Version 0.5.24 und höher) setzen und das Enum-Kontrollkästchen aktivieren. Dann müssen wir alle verfügbaren Status im Format <Nummer>|<Name> hinzufügen, wie unten gezeigt.

<br>

![Tutorial 9](../assets/images/tutorials/tut9.png)

<br>

Klicken Sie auf "Save". Sie sollten das vollständig konfigurierte Datenmodell sehen, wie unten gezeigt.

<br>

![Tutorial 10](../assets/images/tutorials/tut10.png)

<br>

## Einrichten der Benutzeroberfläche für unsere Anwendung

Jetzt müssen wir die Benutzeroberfläche für unsere Anwendung einrichten. Wie oben beschrieben, benötigen wir 2 Bildschirme:

1. Ein Bildschirm zum Hinzufügen einer neuen oder Bearbeiten einer vorhandenen Rechnung. Wir nennen es "Rechnung hinzufügen/anzeigen".
2. Eine Liste aller Rechnungen im System, die mit allen oben beschriebenen Rechnungsfeldern gefiltert und/oder sortiert werden kann. Wir nennen es "Alle Rechnungen".

## Einrichten der Seite Rechnung hinzufügen/anzeigen

Wir haben bereits eine automatisch hinzugefügte Standardseite namens "Main Page" oben.

In der aktuellen Version der Plattform wird die erste Seite der Komponente standardmäßig als Formular zum Anzeigen und Bearbeiten von Komponentendaten verwendet, wenn kein explizites Formular zum Anzeigen und Bearbeiten vorhanden ist. In unserem Fall öffnet beispielsweise das Data Grid-UI-Steuerelement, das wir für die Seite Alle Rechnungen verwenden, standardmäßig die erste Seite unserer Komponente.

Wir werden auch die erste Seite für das Formular zum Anzeigen und Bearbeiten unserer Rechnung verwenden, und dafür werden wir sie von Main Page in Add/View Invoices umbenennen. Klicken Sie dazu auf Main Page und ändern Sie den Namen im sich öffnenden Dialog (Felder Name und Title).

Das Ergebnis sieht wie unten gezeigt aus.

<br>

![Tutorial 11](../assets/images/tutorials/tut11.png)

<br>

Als Nächstes ziehen Sie zum Erstellen der Datenansicht und des Bearbeitungsformulars die Datenfelder (Eigenschaften) von links in den mittleren Bereich in derselben Reihenfolge wie im oben gezeigten Datengitter.

Die Ergebnisse sollten so aussehen.

<br>

![Tutorial 12](../assets/images/tutorials/tut12.png)

<br>

Klicken Sie auf die Schaltfläche Save. Fügen wir nun eine Seite zum Anzeigen aller Rechnungen hinzu.

## Einrichten der Seite Alle Rechnungen

Öffnen Sie dazu die UI Components im rechten Panel, wählen Sie Layout, klicken Sie auf Page und ziehen Sie es in den mittleren Bereich direkt über unserem Rechnungsanzeigeformular. Eine Seite namens New page 1 sollte automatisch hinzugefügt werden, wie unten gezeigt.

<br>

![Tutorial 13](../assets/images/tutorials/tut13.png)

<br>

Gehen Sie zur New page 1, indem Sie auf die Schaltfläche mit demselben Namen klicken, und benennen Sie sie in All Invoices um.

Klicken Sie auf Save. Wählen Sie in der UI Components-Liste auf der rechten Seite Layout aus, wählen Sie dann Page und ziehen Sie es in den mittleren Bereich. Gehen Sie dann zum Abschnitt Advanced und ziehen Sie das DataGrid-Element in das neu erstellte Panel. Sie sehen das Ergebnis wie unten gezeigt.

<br>

![Tutorial 15](../assets/images/tutorials/tut15.png)

<br>

Klicken Sie auf das Settings-Symbol (Zahnrad) in der oberen rechten Ecke des neuen DataGrid-Elements und wählen Sie Common im rechten Panel. Sie sehen die Auswahl der Komponente zum Anzeigen von Daten in diesem Datengitter. Wählen Sie Invoice Inventory.

<br>

![Tutorial 16](../assets/images/tutorials/tut16.png)

<br>

Wählen Sie dann das "+"-Symbol neben dem Label "Columns" 5 Mal aus (da wir 5 Datenfelder haben, die wir hier anzeigen möchten).

<br>

![Tutorial 17](../assets/images/tutorials/tut17.png)

<br>

Klicken Sie nun für jede Spalte auf den Spaltenbereich. Ein neues Dialogfeld wird angezeigt, um die Spalte zu konfigurieren.

Für jede Spalte müssen Sie den Header mit dem Spaltennamen festlegen (z. B. "Invoice Number", "Invoice Name" usw.).

Sie müssen auch die Option "Show Header" auf "On" setzen.

Wenn die Optionen "Sortable" und/oder "Filterable" auf "On" gesetzt sind, aktivieren Sie dynamisches Sortieren und Filtern (ähnlich wie in Excel).

Schließlich müssen Sie auf die Schaltfläche "Add field" klicken und das entsprechende Datenfeld auswählen, das in dieser Spalte angezeigt werden soll.

Das folgende Beispiel zeigt die Einrichtung für das Feld "Invoice Number". Die anderen Spalten werden ähnlich eingerichtet.

<br>

![Tutorial 18](../assets/images/tutorials/tut18.png)

<br>

Nachdem Sie alle Spalten eingerichtet haben, gehen Sie zu Actions im Formular auf der rechten Seite und stellen Sie sicher, dass "Show add button" ausgewählt ist. Dadurch können neue Rechnungen über dieses DataGrid hinzugefügt werden.

Setzen Sie außerdem den Command Type auf "Edit Record", damit wir jede Rechnung in der Liste anzeigen/bearbeiten können, indem wir darauf klicken.

Siehe die Abbildung unten für die Ergebnisse.

<br>

![Tutorial 19](../assets/images/tutorials/tut19.png)

<br>

Klicken Sie auf die Schaltfläche Save.

## Hinzufügen von Aktionsschaltflächen und Dataflow zum Speichern von Daten

Nachdem wir die Datenansichts- und Bearbeitungsformulare erstellt haben, müssen wir Logik hinzufügen, um die Formulardaten in der Datenbank zu speichern und Benutzern zu ermöglichen, sie auszulösen.

Dazu müssen wir zwei Dinge tun.

1. Schaltflächen hinzufügen, die wir entweder zum Speichern der Formulardaten oder zum Abbrechen aller Änderungen und zur Rückkehr zur Liste Alle Rechnungen verwenden.
2. Um die Formulardaten zu speichern, fügen wir einen einfachen Workflow hinzu, der die Formulardaten übernimmt und in der Datenbank speichert.

<br>

## Speichern und Zurück zu allen Rechnungen-Schaltflächen hinzufügen

<br>

Klicken Sie auf "Toolbox", wählen Sie das Feld "Button" im Abschnitt "Basic" und ziehen Sie die Schaltfläche in den mittleren Bereich des Bildschirms. Setzen Sie den Schaltflächentitel auf Save. Gehen Sie dazu zum Abschnitt Common und schreiben Sie im Feld Translation Value Save.

Fügen Sie eine weitere Schaltfläche hinzu und setzen Sie den Titel auf "Back to all invoices". Das Ergebnis sollte wie das Bild unten aussehen.

<br>

![Tutorial 20](../assets/images/tutorials/tut20.png)

<br>

Jetzt werden wir die Schaltfläche "Back to all invoices" so einstellen, dass die Benutzeroberfläche zur Hauptregisterkarte "All Invoices" wechselt. Wählen Sie dazu im Einstellungsmenü für die untere Schaltfläche "Actions" aus und setzen Sie den "Command Type" auf "Open Page" und die "Component Page" auf "All Invoices". Klicken Sie auf Save.

<br>

![Tutorial 21](../assets/images/tutorials/tut21.png)

<br>

## Hinzufügen von Data Flow zum Speichern

Damit die Schaltfläche Save in der Anwendung die eingegebenen Daten als Rechnung speichert, müssen wir einen Datenfluss hinzufügen.

Klicken Sie auf "Toolbox", wählen Sie das Feld "Data flow" im Abschnitt "Flow" und ziehen Sie es in den mittleren Bereich des Bildschirms. Ein neuer Datenfluss mit dem Standardnamen "Data flow 1" wird angezeigt, der über die Schaltfläche mit demselben Namen im Hauptkomponenteneinstellungsmenü rechts neben der Schaltfläche Input Data flow zugänglich ist. Klicken Sie auf die Schaltfläche Data flow 1 und benennen Sie Ihren Datenfluss in Save um.

Das Ergebnis sollte so aussehen.

<br>

![Tutorial 22](../assets/images/tutorials/tut22.png)

<br>

Klicken Sie als Nächstes auf die Schaltfläche "+ ADD STAGE", dann auf "Add step" und wählen Sie den Schritt "Get action model". Fügen Sie einen weiteren Schritt hinzu und wählen Sie "Update entry", gehen Sie dann zu den Einstellungen für diesen Schritt. Sie können mehr über diesen Schritt im Abschnitt "Dataflow" lesen. Konfigurieren Sie den Schritt wie unten gezeigt:

<br>

![Tutorial 23](../assets/images/tutorials/tut23.png)

<br>

![Tutorial 24](../assets/images/tutorials/tut24.png)

<br>

Fügen Sie als Nächstes den Schritt "Write response" hinzu, geben Sie den Quellschritt in seinen Einstellungen an und speichern Sie die Komponente.

Danach wählen Sie im Einstellungsmenü für die Schaltfläche Save Actions aus und setzen Sie den Command Type auf Execute dataflow und wählen Sie Ihren neuen Save aus der Liste.

Klicken Sie auf die Schaltfläche Save. Das Ergebnis sollte so aussehen.

<br>

![Tutorial 25](../assets/images/tutorials/tut25.png)

<br>
 
Klicken Sie auf Save und Ready to publish. Ihre neue Komponente wird erstellt und ist bereit zur Veröffentlichung.

<br>

## Veröffentlichen und Testen Ihrer Anwendung

Sie sind jetzt bereit, Ihre Anwendung zu veröffentlichen und zu testen.

Um Ihre Anwendung zu veröffentlichen, klicken Sie auf die Schaltfläche Ready to publish in Ihrer Komponente und gehen Sie dann zu Studio→Applications→Publication. Wählen Sie Ihre Invoice Inventory-Komponente aus der Liste der zur Veröffentlichung verfügbaren Komponenten aus und klicken Sie auf die Schaltfläche Publish.

Sie können dann die Schaltfläche View App in Ihrem Studio verwenden (nicht immer verfügbar) oder zur URL <your-host-name> gehen, um Ihre Anwendung in Aktion zu sehen.

Füllen Sie die Rechnungsdetails aus und klicken Sie auf Save. Klicken Sie dann auf die Schaltfläche "Back to all invoices". Ihre erste Rechnung wird gespeichert und Sie sehen die Liste aller verfügbaren Rechnungen.
