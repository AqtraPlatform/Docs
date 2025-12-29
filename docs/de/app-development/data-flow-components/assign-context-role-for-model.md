# Kontextrolle für Modell zuweisen

![](../../assets/images/app-development/assign-context-role-for-model.png)

## Allgemeine Informationen
Der Schritt „Kontextrolle für Modell zuweisen“ wird verwendet, um einen Benutzer oder eine Gruppe von Benutzern mit einer bestimmten Rolle und einem bestimmten Kontext zu verknüpfen. Dieser Prozess erfordert, dass mindestens eine Rolle im Abschnitt „Rollen“ des Menüs „Zugriff“ konfiguriert ist. Dieser Schritt ermöglicht es Ihnen, Beziehungen zwischen Benutzern und Rollen im Kontext eines bestimmten Datenmodells herzustellen, wodurch die Kontrolle über den Benutzerzugriff und die Berechtigungen bereitgestellt wird.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld  | Wertoptionen | Zweck |
|-------------------|--------------|-------|
| Schrittname       | -            | Name des Schrittes |
| Quellschritt      | -            | Auswahl des vorherigen Schrittes |
| Benutzer-ID-Feld  | -            | Benutzer-ID-Feld |
| Kontext-ID-Feld   | -            | Kontext-ID-Feld |
| Kontexte auswählen | -            | Auswahl der Kontexte, mit denen die Rolle verknüpft wird |

## Fälle
- **Benutzerzugriffsverwaltung**: Wird verwendet, um Rollen Benutzern zuzuweisen, die ihren Zugriff und ihre Berechtigungen im System bestimmen.
- **Dynamische Rollenverwaltung bei Interaktion mit der Benutzeroberfläche**: Dieser Schritt wird effektiv verwendet, um die Rollen der Benutzer in Echtzeit basierend auf ihren Aktionen und Interaktionen mit Elementen der Benutzeroberfläche zu ändern oder zu aktualisieren. Dies ermöglicht es, den Benutzerzugriff und die Berechtigungen je nach spezifischen Aktionen oder Szenarien bei der Nutzung des Systems anzupassen.

## Ausnahmen
- **Anforderung an konfigurierte Rollen**: Für eine erfolgreiche Verknüpfung muss das System die entsprechenden Rollen vorab konfiguriert haben.
- **Abhängigkeit von der ID-Genauigkeit**: Eine genaue Identifizierung der Benutzer-IDs und Kontexte ist entscheidend, damit der Schritt korrekt funktioniert.