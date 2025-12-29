# Veröffentlichungen

Um eine Komponenten-Version, Lokalisierung, Erweiterung oder eine andere geeignete Anpassung über die Plattform zu erstellen, müssen Sie sie veröffentlichen. Damit eine Komponenten-Version veröffentlicht werden kann, muss sie als bereit zur Veröffentlichung markiert werden.

Der Veröffentlichungsprozess wird durch die Zustandsmaschine gesteuert, die es Ihnen ermöglicht, alle Phasen effektiv zu kontrollieren und im Falle von Fehlern das System in den vorherigen Zustand zurückzuführen. Eine globale Sperrfunktion wurde eingeführt, um zu verhindern, dass mehrere Veröffentlichungen gleichzeitig gestartet werden. Benutzer sehen den Status aktiver Veröffentlichungen, und nach Abschluss jeder Veröffentlichung werden die Status der Objekte, die bereit zur Veröffentlichung sind, automatisch aktualisiert.

**Schritte zur Veröffentlichung einer Komponente:**

- **„Speichern“**-Schaltfläche: Wird verwendet, um die aktuellen Änderungen an der Komponente zu speichern.
- **„Bereit zur Veröffentlichung“**: Markiert eine Komponente als bereit zur Veröffentlichung, nachdem alle Änderungen gespeichert wurden.

**Schritte zur Veröffentlichung von Lokalisierungen und Integrationen:**
- Werden automatisch verfügbar für die Veröffentlichung, nachdem Sie Änderungen vorgenommen haben.

**Veröffentlichungsprozess:**
1. **Gehe zu Veröffentlichungen**: Befindet sich unter ‚Studio→Anwendungen→Veröffentlichung.‘
2. **Auswahl der zu veröffentlichenden Elemente**: 
   - Komponenten, Lokalisierungen, Integrationen und Python-Module werden zur Veröffentlichung ausgewählt.
3. **Endgültige Veröffentlichung**: 
   - Das Verfahren wird durch Klicken auf die Schaltfläche „Veröffentlichen“ abgeschlossen.
   - Eine Benachrichtigung erscheint, wenn die Veröffentlichung erfolgreich ist.

![Veröffentlichungen](../assets/images/app-development/publication-example.png)