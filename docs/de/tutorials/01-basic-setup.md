# Tutorial №1

<br>

## Erstellen Ihrer ersten Anwendung — Rechnungsinventar

<br>

**Anwendungsbeschreibung: Rechnungsinventar**

Wir werden eine einfache Anwendung erstellen, die es Ihnen ermöglicht, Rechnungen hinzuzufügen, anzuzeigen und zu bearbeiten.

Jede Rechnung wird die folgenden Daten enthalten (siehe die Tabelle unten).

| Kurze Beschreibung    | Detaillierte Beschreibung                                         |
| --------------------- | --------------------------------------------------------------- |
| Rechnungsnummer       | Nummer, die der Rechnung vom Lieferanten zugewiesen wird.       |
| Rechnungsbezeichnung  | Beschreibung des Rechnungsgegenstands.                          |
| Gesamter Rechnungsbetrag | Zahl, die den in der Rechnung berechneten Geldbetrag angibt.   |
| Fälligkeitsdatum der Rechnung | Datum, an dem die Rechnung zur Zahlung fällig ist.         |

<br>

Zusätzlich werden wir den Rechnungsstatus wie folgt verfolgen (siehe die Tabelle unten).

| ID  | Lesbarer Titel       | Beschreibung                                                                          |
| --- | -------------------- | ------------------------------------------------------------------------------------ |
| 0   | In Überprüfung       | Wird sofort nach der Erstellung der Rechnung zugewiesen.                             |
| 1   | Zur Zahlung akzeptiert | Wird nach der Überprüfung und Genehmigung der Rechnung zur Zahlung zugewiesen.      |
| 2   | Abgelehnt            | Wird nach Abschluss der Überprüfung zugewiesen, aber die Rechnung wird nicht zur Zahlung akzeptiert. |
| 3   | Bezahlt              | Wird zugewiesen, nachdem die Rechnung bezahlt wurde.                                 |
| 4   | Überfällig           | Zeigt an, dass die Rechnung unbezahlt ist und das Fälligkeitsdatum überschritten wurde. |

<br>

Die Grundversion der Anwendung wird 2 Hauptbildschirme haben.

- Eine Liste aller Rechnungen im System, die mit allen oben beschriebenen Rechnungsfeldern gefiltert und/oder sortiert werden kann. Wir werden sie „Alle Rechnungen“ nennen.
- Einen Bildschirm zum Hinzufügen einer neuen oder Bearbeiten einer bestehenden Rechnung. Wir werden ihn „Rechnung bearbeiten/anzeigen“ nennen.

Nach der Erstellung wird die Anwendung wie im Screenshot unten aussehen.

<br>

![Tutorial 1](../assets/images/tutorials/tut1.png)

<br>

## Studio öffnen

Die Erstellung einer Anwendung auf der Plattform beginnt mit dem Öffnen von Studio und dem Hinzufügen einer Komponente.

Sie können Studio über den Link https://<your_hosting_name>/studio/ öffnen.

Wenn der Domainname, unter dem Sie Ihre Instanz der Plattform bereitgestellt haben, [my.platform.io](http://my.platform.io/) ist, können Sie Studio über die folgende URL aufrufen: “[https://my.platform.io/studio/”](https://my.platform.io/studio/%E2%80%9D).

Nach dem Anmelden bei Studio sehen Sie den folgenden Bildschirm mit einem Menü auf der linken Seite, das Home, Anwendungen und Zugriff auflistet. Wählen Sie Anwendungen→Komponenten.

<br>

![Tutorial 2](../assets/images/tutorials/tut2.png)

<br>

Sie sehen eine Liste aller vorhandenen Komponenten. Klicken Sie auf die Schaltfläche „Hinzufügen“ und wählen Sie die Option „Komponente“ aus, wie unten gezeigt.

<br>

![Tutorial 3](../assets/images/tutorials/tut3.png)

<br>

Herzlichen Glückwunsch, Sie haben jetzt Ihre erste Komponente! Nennen wir sie „Rechnungsinventar“ und setzen einige wichtige Parameter.

Um Ihrer Komponente einen Namen zu geben, klicken Sie auf die Schaltfläche „Einstellungen“ und geben Sie dann „Rechnungsinventar“ in das Feld „Name“ ein.

Da unsere Anwendung nur für Personen mit den entsprechenden Anmeldeinformationen zugänglich sein wird, müssen wir sicherstellen, dass das Feld „Zugriffsmodus“ auf „Privat“ eingestellt ist.

## Einrichten der erforderlichen Datenfelder

Klicken Sie auf Speichern, um sicherzustellen, dass Ihre Komponente gespeichert wird. Es wird eine Fehlermeldung angezeigt, da wir noch keine Daten in unserer Komponente haben. Lassen Sie uns einige Daten hinzufügen. Gehen Sie zum Tab „Definition“ und klicken Sie auf das „+“-Zeichen neben „Rechnungsinventar“. Die Plattform wird automatisch mehrere Systemfelder hinzufügen, die Sie im Screenshot sehen, sowie Ihr erstes Datenfeld — Property_1.

<br>

![Tutorial 4](../assets/images/tutorials/tut4.png)

<br>

Klicken Sie auf das Bearbeitungssymbol (Stift) bei Property_1. Sie sehen ein neues Panel auf der rechten Seite geöffnet. Hier definieren Sie, wie Ihre Datenfelder vom System interpretiert werden sollen.
Name — dies ist der interne Systemname für Ihr Datenfeld (Eigenschaft). Er sollte nur englische Buchstaben ohne Leerzeichen enthalten. Sie werden diesen Namen später verwenden, zum Beispiel in Python-Skripten, um einige erweiterte Logik in die Anwendung einzufügen.

_Hinweis: Ab Version 0.4.x gibt es auch eine Systemeigenschaft „name“, die automatisch hinzugefügt wird, wenn die erste Eigenschaft erstellt wird, und die verwendet wird, wenn Sie Benutzern Werte für Benutzer anzeigen müssen, wenn Sie Eigenschaften des Typs Katalog (Verknüpfung zu einer anderen Komponente; verwendet für 1:1- und M:1-Beziehungen) oder Array (Verknüpfung zu einem Array anderer Komponenten; verwendet für 1:M- und M:M-Beziehungen) verwenden. Im Gegensatz zum internen Systemnamen, der für jede Eigenschaft innerhalb der Komponente vorhanden ist, ist das Systemfeldname für die gesamte Komponente einheitlich._

Titel — so wird Ihr Datenfeld in der Benutzeroberfläche benannt. Hier können Sie alle benötigten Zeichen verwenden.

Für Datenfelder, die immer nicht leer sein müssen, stellen Sie sicher, dass das Kontrollkästchen „Erforderlich“ ausgewählt ist.

Der Eigenschaftstyp ermöglicht es Ihnen, einen der verfügbaren Datentypen für das Datenfeld auszuwählen.

Um zu beginnen, fügen wir das Datenfeld Rechnungsname hinzu und setzen den Eigenschaftstyp auf String. Da Rechnungsnamen theoretisch von externen Lieferanten stammen, können sie sich wiederholen, daher setzen wir hier nicht das Primärschlüssel-Flag.

<br>

![Tutorial 5](../assets/images/tutorials/tut5.png)

<br>

Sobald wir mit der Einrichtung unseres ersten Feldes fertig sind, klicken wir auf Speichern.

Jetzt fügen wir die anderen Felder hinzu, die wir in unserer Anwendung benötigen: Rechnungsnummer, Fälligkeitsdatum der Rechnung, Gesamtrechnungsbetrag und Rechnungsstatus.

**Rechnungsnummer** ist die interne Kontonummer jeder einzigartigen Rechnung, die im Allgemeinen mit dem Rechnungsnamen übereinstimmt, aber wir stellen sicher, dass sie mindestens 2 Zeichen lang ist, indem wir den Minimalwert auf 2 setzen, wie unten gezeigt. Sie muss auch einzigartig sein, um verschiedene Rechnungen zu unterscheiden, selbst wenn sie die gleichen Namen haben, daher setzen wir das Primärschlüssel-Flag. Dies teilt der Plattform mit, dass es nicht mehr als eine Rechnungsnummer-Eigenschaft mit dem gleichen Wert geben kann. Wenn versucht wird, einen doppelten Wert zu erstellen, gibt das System einen Fehler aus.

<br>

![Tutorial 6](../assets/images/tutorials/tut6.png)

<br>

Für das erwartete Fälligkeitsdatum der Rechnung setzen Sie den Eigenschaftstyp auf DateTime.

<br>

![Tutorial 7](../assets/images/tutorials/tut7.png)

<br>

Der Gesamtrechnungsbetrag sollte als Zahl festgelegt werden. Wir setzen auch das Minimalwertfeld auf 0, um sicherzustellen, dass es keine negativen Rechnungen gibt (dies könnte in einer echten Finanzanwendung anders sein, in der negative Werte verwendet werden, um beispielsweise Gutschriften von Lieferanten darzustellen).

<br>

![Tutorial 8](../assets/images/tutorials/tut8.png)

<br>

Schließlich fügen wir das Feld „Rechnungsstatus“ hinzu. Wie in der Anwendungsbeschreibung angegeben, wird dies eine Reihe von Status sein, die wie folgt aussehen sollten:

0|In Überprüfung  
1|Akzeptiert zur Zahlung  
2|Abgelehnt  
3|Bezahlt  
4|Überfällig  

Dafür müssen wir den Eigenschaftstyp auf Integer (ab Version 0.5.24 und höher) setzen und das Kontrollkästchen Enum aktivieren. Dann müssen wir alle verfügbaren Status im Format <Nummer>|<Name> hinzufügen, wie unten gezeigt.

<br>

![Tutorial 9](../assets/images/tutorials/tut9.png)

<br>

Klicken Sie auf „Speichern“. Sie sollten das vollständig konfigurierte Datenmodell sehen, wie unten gezeigt.

<br>

![Tutorial 10](../assets/images/tutorials/tut10.png)

<br>

## Einrichtung der Benutzeroberfläche für unsere Anwendung

Jetzt müssen wir die Benutzeroberfläche für unsere Anwendung einrichten. Wie oben beschrieben, benötigen wir 2 Bildschirme:

1. Einen Bildschirm zum Hinzufügen einer neuen oder Bearbeiten einer bestehenden Rechnung. Wir nennen ihn „Rechnung hinzufügen/anzeigen“.
2. Eine Liste aller Rechnungen im System, die gefiltert und/oder sortiert werden kann, indem alle oben beschriebenen Rechnungsfelder verwendet werden. Wir nennen ihn „Alle Rechnungen“.

## Einrichtung der Seite Rechnung hinzufügen/anzeigen

Wir haben bereits eine automatisch hinzugefügte Standardseite namens „Hauptseite“ oben.

In der aktuellen Version der Plattform wird die erste Seite der Komponente standardmäßig als Formular zum Anzeigen und Bearbeiten von Komponentendaten verwendet, wenn kein explizites Formular zum Anzeigen und Bearbeiten vorhanden ist. In unserem Fall wird die Data Grid UI-Steuerung, die wir für die Seite Alle Rechnungen verwenden, standardmäßig die erste Seite unserer Komponente öffnen.
Wir werden auch die erste Seite für das Formular zur Anzeige und Bearbeitung unserer Rechnung verwenden, und dafür werden wir sie von Hauptseite in Rechnungen hinzufügen/anzeigen umbenennen. Klicken Sie dazu auf Hauptseite und ändern Sie den Namen im sich öffnenden Dialog (Felder Name und Titel).

Das Ergebnis wird wie unten gezeigt aussehen.

<br>

![Tutorial 11](../assets/images/tutorials/tut11.png)

<br>

Als Nächstes, um die Datenansicht und das Bearbeitungsformular zu erstellen, ziehen Sie die Datenfelder (Eigenschaften) von links in den mittleren Bereich in derselben Reihenfolge wie im oben gezeigten Datenraster.

Die Ergebnisse sollten so aussehen.

<br>

![Tutorial 12](../assets/images/tutorials/tut12.png)

<br>

Klicken Sie auf die Schaltfläche Speichern. Lassen Sie uns nun eine Seite zur Anzeige aller Rechnungen hinzufügen.

## Einrichten der Seite Alle Rechnungen

Öffnen Sie dazu die UI-Komponenten im rechten Panel, wählen Sie Layout, klicken Sie auf Seite und ziehen Sie sie in den mittleren Bereich direkt über unser Rechnungsansichtsformular. Eine Seite mit dem Namen Neue Seite 1 sollte automatisch hinzugefügt werden, wie unten gezeigt.

<br>

![Tutorial 13](../assets/images/tutorials/tut13.png)

<br>

Gehen Sie zur Neuen Seite 1, indem Sie auf die Schaltfläche mit demselben Namen klicken, und benennen Sie sie in Alle Rechnungen um.

Klicken Sie auf Speichern. Wählen Sie in der Liste der UI-Komponenten auf der rechten Seite Layout aus, wählen Sie dann Seite und ziehen Sie sie in den mittleren Bereich. Gehen Sie dann zum Abschnitt Erweitert und ziehen Sie das DataGrid-Element in das neu erstellte Panel. Sie werden das Ergebnis wie unten gezeigt sehen.

<br>

![Tutorial 15](../assets/images/tutorials/tut15.png)

<br>

Klicken Sie auf das Einstellungen-Symbol (Zahnrad) in der oberen rechten Ecke des neuen DataGrid-Elements und wählen Sie Allgemein im rechten Panel. Sie werden die Auswahl der Komponente sehen, um Daten in diesem Datenraster anzuzeigen. Wählen Sie Rechnungsinventar.

<br>

![Tutorial 16](../assets/images/tutorials/tut16.png)

<br>

Wählen Sie dann das “+”-Symbol neben dem Label “Spalten” 5 Mal aus (da wir 5 Datenfelder haben, die wir hier anzeigen möchten).

<br>

![Tutorial 17](../assets/images/tutorials/tut17.png)

<br>

Jetzt klicken Sie für jede Spalte auf den Spaltenbereich. Ein neues Dialogfeld wird angezeigt, um die Spalte zu konfigurieren.

Für jede Spalte müssen Sie den Header mit dem Spaltennamen festlegen (z. B. “Rechnungsnummer”, “Rechnungsname” usw.).

Sie müssen auch die Option “Header anzeigen” auf “Ein” setzen.

Wenn die Optionen “Sortierbar” und/oder “Filterbar” auf “Ein” gesetzt sind, aktivieren Sie dynamisches Sortieren und Filtern (ähnlich wie es beispielsweise in Excel gemacht wird).

Schließlich müssen Sie auf die Schaltfläche “Feld hinzufügen” klicken und das entsprechende Datenfeld auswählen, das in dieser Spalte angezeigt werden soll.

Das folgende Beispiel zeigt die Einrichtung für das Feld “Rechnungsnummer”. Die anderen Spalten sind ähnlich eingerichtet.

<br>

![Tutorial 18](../assets/images/tutorials/tut18.png)

<br>

Nachdem Sie alle Spalten eingerichtet haben, gehen Sie zu Aktionen im Formular auf der rechten Seite und stellen Sie sicher, dass die Option “Hinzufügen-Schaltfläche anzeigen” ausgewählt ist. Dies ermöglicht das Hinzufügen neuer Rechnungen über dieses DataGrid.

Zusätzlich setzen Sie den Befehlstyp auf “Datensatz bearbeiten”, damit wir jede Rechnung in der Liste durch Klicken darauf anzeigen/bearbeiten können.

Siehe die Abbildung unten für die Ergebnisse.

<br>

![Tutorial 19](../assets/images/tutorials/tut19.png)

<br>

Klicken Sie auf die Schaltfläche Speichern.

## Hinzufügen von Aktionsschaltflächen und Datenfluss zum Speichern von Daten

Nachdem wir die Datenansicht und die Bearbeitungsformulare erstellt haben, müssen wir Logik hinzufügen, um die Formulardaten in der Datenbank zu speichern und es den Benutzern zu ermöglichen, dies auszulösen.

Dazu müssen wir zwei Dinge tun.

1. Schaltflächen hinzufügen, die wir entweder verwenden, um die Formulardaten zu speichern oder um alle Änderungen abzubrechen und zur Liste Alle Rechnungen zurückzukehren.
2. Um die Formulardaten zu speichern, fügen wir einen einfachen Workflow hinzu, der die Formulardaten nimmt und in der Datenbank speichert.

<br>

## Speichern und Zurück zu allen Rechnungen Schaltflächen hinzufügen

<br>

Klicken Sie auf “Werkzeugkasten”, wählen Sie das Feld “Schaltfläche” im Abschnitt “Basis” aus und ziehen Sie die Schaltfläche in den mittleren Bereich des Bildschirms. Setzen Sie den Titel der Schaltfläche auf Speichern. Gehen Sie dazu zum Abschnitt Allgemein und schreiben Sie im Feld Übersetzungswert Speichern.

Fügen Sie eine weitere Schaltfläche hinzu und setzen Sie den Titel auf “Zurück zu allen Rechnungen.” Das Ergebnis sollte wie das Bild unten aussehen.

<br>

![Tutorial 20](../assets/images/tutorials/tut20.png)

<br>
Jetzt werden wir den Button „Zurück zu allen Rechnungen“ so einstellen, dass die Benutzeroberfläche zum Haupt-Tab „Alle Rechnungen“ wechselt. Dazu wählen Sie im Einstellungsmenü für den unteren Button „Aktionen“ aus und setzen den „Befehls-Typ“ auf „Seite öffnen“ und die „Komponenten-Seite“ auf „Alle Rechnungen“. Klicken Sie auf Speichern.

<br>

![Tutorial 21](../assets/images/tutorials/tut21.png)

<br>

## Hinzufügen des Datenflusses zum Speichern

Um den Speichern-Button in der Anwendung so zu konfigurieren, dass die eingegebenen Daten als Rechnung gespeichert werden, müssen wir einen Datenfluss hinzufügen.

Klicken Sie auf „Werkzeugkasten“, wählen Sie das Feld „Datenfluss“ im Abschnitt „Fluss“ aus und ziehen Sie es in den mittleren Bereich des Bildschirms. Ein neuer Datenfluss mit dem Standardnamen „Datenfluss 1“ wird erscheinen, der über die Schaltfläche mit demselben Namen im Hauptmenü der Komponenteneinstellungen, rechts von der Schaltfläche Eingabedatenfluss, zugänglich ist. Klicken Sie auf die Schaltfläche Datenfluss 1 und benennen Sie Ihren Datenfluss in Speichern um.

Das Ergebnis sollte wie folgt aussehen.

<br>

![Tutorial 22](../assets/images/tutorials/tut22.png)

<br>

Klicken Sie als Nächstes auf die Schaltfläche „+ STUFE HINZUFÜGEN“, dann auf „Schritt hinzufügen“ und wählen Sie den Schritt „Aktionsmodell abrufen“ aus. Fügen Sie einen weiteren Schritt hinzu und wählen Sie „Eintrag aktualisieren“ aus, und gehen Sie dann zu den Einstellungen für diesen Schritt. Weitere Informationen zu diesem Schritt finden Sie im Abschnitt „Datenfluss“. Konfigurieren Sie den Schritt wie unten gezeigt:

<br>

![Tutorial 23](../assets/images/tutorials/tut23.png)

<br>

![Tutorial 24](../assets/images/tutorials/tut24.png)

<br>

Fügen Sie als Nächstes den Schritt „Antwort schreiben“ hinzu, geben Sie den Quellschritt in seinen Einstellungen an und speichern Sie die Komponente.

Danach wählen Sie im Einstellungsmenü für den Speichern-Button die Aktionen aus und setzen den Befehls-Typ auf Datenfluss ausführen und wählen Sie Ihr neues Speichern aus der Liste aus.

Klicken Sie auf die Schaltfläche Speichern. Das Ergebnis sollte wie folgt aussehen.

<br>

![Tutorial 25](../assets/images/tutorials/tut25.png)

<br>
 
Klicken Sie auf Speichern und Bereit zur Veröffentlichung. Ihre neue Komponente ist erstellt und bereit zur Veröffentlichung.

<br>

## Veröffentlichung und Testen Ihrer Anwendung

Sie sind jetzt bereit, Ihre Anwendung zu veröffentlichen und zu testen.

Um Ihre Anwendung zu veröffentlichen, klicken Sie auf die Schaltfläche Bereit zur Veröffentlichung innerhalb Ihrer Komponente, gehen Sie dann zu Studio→Anwendungen→Veröffentlichung. Wählen Sie Ihre Rechnungsinventar-Komponente aus der Liste der verfügbaren Komponenten zur Veröffentlichung aus und klicken Sie auf die Schaltfläche Veröffentlichen.

Sie können dann die Schaltfläche App anzeigen innerhalb Ihres Studios verwenden (nicht immer verfügbar) oder gehen Sie zur URL <your-host-name>, um Ihre Anwendung in Aktion zu sehen.

Füllen Sie die Rechnungsdetails aus und klicken Sie auf Speichern. Klicken Sie dann auf die Schaltfläche „Zurück zu allen Rechnungen“. Ihre erste Rechnung wird gespeichert, und Sie sehen die Liste aller verfügbaren Rechnungen.