# Datenfluss

## Was ist Datenfluss? {: #dataflow }

Datenfluss, oder Datenfluss, in der Plattform ist ein Schlüsselkomponente, die es Benutzern ermöglicht, Daten innerhalb einer Anwendung zu verarbeiten und zu transformieren. Dies ist ein leistungsstarkes Werkzeug zur Integration von Daten, zur Verarbeitung von Ereignissen und zur Automatisierung von Geschäftsprozessen.

Datenfluss wird auf der Plattform mit einem 'visuellen Editor' des Datenflusses erstellt:

Der visuelle Datenfluss-Editor ist ein intuitiver Designer zum Erstellen und Verwalten von Datenflüssen. Dieses Tool ermöglicht es Benutzern, schrittweise eine Reihe von Stufen und Schritten zu erstellen, um komplexe Datenverarbeitungsskripte zu implementieren.

- **Stufe hinzufügen**: Dies geschieht durch Drücken des "+"-Symbols im Steuerfeld des Datenflusses. Sie können eine unbegrenzte Anzahl von Stufen hinzufügen, je nach den Anforderungen Ihres Skripts.
- **Stufe löschen**: Um eine Stufe zu löschen, verwenden Sie die "X"-Schaltfläche im ausgewählten Stufenblock.
- **Stufe bearbeiten**: Sie können nur den Namen der ausgewählten Stufe bearbeiten.
- **Schritt hinzufügen**: Ein neuer Schritt wird hinzugefügt, indem Sie die Schaltfläche "SCHRITT HINZUFÜGEN" an der entsprechenden Stufe drücken. Benutzer können Schrittarten aus den vorgeschlagenen Aktivitätsgruppen auswählen.
- **Schritt löschen**: Um einen Schritt zu löschen, klicken Sie auf das "X"-Symbol im ausgewählten Schrittblock.

## Eingangsgruppe

Komponenten zum Abrufen und Importieren von Daten:

- [Eingangsschritte](input-steps.md) - Übersicht über Eingangsschritte
- [Werte vom Connector abrufen](get-values-from-connector.md) - Daten von Connectors abrufen
- [Für Connector abonnieren](subscribe-to-connector.md) - Abonnieren von Datenaktualisierungen
- [Aktionsmodell abrufen](get-action-model.md) - Aktionsmodell abrufen
- [Workflow-Modell abrufen](get-workflow-model.md) - Workflow-Modell abrufen
- [Leeres Modell abrufen](get-empty-model.md) - Leeres Datenmodell erstellen
- [Proxy-Eintrag abrufen](proxy-get-entry.md) - Proxy-Eintrag abrufen
- [Proxy-Abfrageeintrag](proxy-query-entry.md) - Proxy-Abfrage ausführen
- [Rohmodell abrufen](get-raw-model.md) - Rohdatenmodell abrufen
- [Datei importieren](import-file.md) - Daten aus Dateien importieren

## Modelltransformationsgruppe

Komponenten zur Datenumwandlung und -verarbeitung:

- [Modelltransformationsschritte](model-transformation-steps.md) - Übersicht über Transformationsschritte
- [Modell transformieren](transform-model.md) - Datenmodelle transformieren
- [Modelle zusammenführen](join-modes.md) - Mehrere Datenmodelle zusammenführen
- [Sammlungen extrahieren](extract-collections.md) - Sammlungsdaten extrahieren
- [Datenquelle filtern](filter-source.md) - Datenquellen filtern
- [Referenz nachschlagen](lookup-reference.md) - Referenznachschlag
- [Skript ausführen](execute-script.md) - Benutzerdefinierte Skripte ausführen
- [Entität nach Filter abfragen](query-entity-by-filter.md) - Filterbasierte Abfragen
- [Mehrere auswählen](select-many.md) - Mehrfachauswahl
- [Entität nach ID abrufen](get-entity-by-id.md) - Nach Identifikator abrufen
- [Kataloge nach Schlüssel laden](load-catalogs-by-key.md) - Katalogdaten laden
- [Distinct](distinct.md) - Eindeutige Werte abrufen
- [Gruppieren nach](group-by.md) - Daten gruppieren
- [Array berechnen](calculate-array.md) - Array-Berechnungen
- [Einfache Mathematik](simple-math.md) - Mathematische Operationen
- [Datenfluss ausführen](execute-dataflow.md) - Verschachtelten Datenfluss ausführen
- [Dateiinformationen abrufen](get-file-info.md) - Dateiinformationen abrufen

## Benutzerkontextgruppe

Komponenten für Benutzerverwaltung und Authentifizierung:

- [Benutzerkontextschritte](user-contexts-steps.md) - Übersicht über Benutzerkontextschritte
- [Kontext für Modell registrieren](register-context-for-model.md) - Modellkontext registrieren
- [Externen Benutzer registrieren](register-external-user.md) - Registrierung externer Benutzer
- [Externe Schlüssel vorbereiten](prepare-external-keys.md) - Authentifizierungsschlüssel vorbereiten
- [Kontextrolle für Modell zuweisen](assign-context-role-for-model.md) - Rollen zuweisen
- [Einmalcode für Benutzer abrufen](get-one-time-code-for-user.md) - OTP generieren
- [Einmalcode für Benutzer bestätigen](confirm-one-time-code-for-user.md) - OTP verifizieren
- [Benutzerinformationen aktualisieren oder erstellen](update-or-create-user-info.md) - Benutzerinformationsverwaltung
- [Benutzerinformationen abrufen](get-user-info.md) - Benutzerdaten abrufen
- [Mit Passwort anmelden](login-with-password.md) - Passwortauthentifizierung
- [Anfrage zum Zurücksetzen des Benutzerpassworts](reset-user-password-request.md) - Passwort zurücksetzen
- [Anfrage zur Bestätigung der Benutzer-E-Mail](confirm-user-email-request.md) - E-Mail-Verifizierung
- [Vorlagenbenachrichtigung senden](send-templated-notification.md) - Vorlagenbasierte Benachrichtigungen
- [Benachrichtigung senden](send-notification.md) - Benachrichtigungen senden
- [Zugewiesene Rollen für Benutzer entfernen](remove-assigned-roles-for-user.md) - Benutzerrollen entfernen

## Ausgabengruppe

Komponenten für Datenoutput und Aktionen:

- [Ausgangsschritte](output-steps.md) - Übersicht über Ausgangsschritte
- [Store-Eintrag über Bus](store-entry-over-bus.md) - Daten über den Nachrichtenbus speichern
- [Eintrag aktualisieren](update-entry.md) - Daten Einträge aktualisieren
- [Aufgeschobenen Eintrag aktualisieren](deferred-update-entry.md) - Aufgeschobene Aktualisierungen
- [Aufgeschobene Aktualisierungsoperationen anwenden](apply-deferred-update-operations.md) - Aufgeschobene Operationen anwenden
- [API-Aufruf ausführen](execute-api-call.md) - Externe API-Aufrufe
- [Antwort schreiben](write-response.md) - Antwortdaten schreiben
- [Formularaktion](form-action.md) - Formularübermittlungsaktionen
- [Workflow ausführen](execute-workflow.md) - Workflow ausführen
- [In Datei exportieren](export-to-file.md) - Daten in Dateien exportieren
- [Vorlage rendern](render-template.md) - Vorlagenrendering