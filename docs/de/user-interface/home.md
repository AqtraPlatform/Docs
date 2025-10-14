# Home-Menü

<br>

Die Seite bietet Informationen über Ihre Lizenz und die bereitgestellten Anwendungsdomänen. Sie erhalten Zugriff auf die folgenden Funktionen und Informationen:

- **Plantyp**: Hier wird der Typ Ihres aktuellen Plans und das Ablauf- oder Verlängerungsdatum Ihres Abonnements angezeigt.
- **Anwendungsdomänen**: In diesem Abschnitt können Sie Anwendungskomponenten erstellen, Benutzer über bestimmte URLs verbinden und zum Abschnitt "Navigation Menu" navigieren.
- **Nutzungsstatistiken**: Zeigt Informationen über die aktuelle Anzahl von Anwendungen im Vergleich zum Gesamtlimit sowie die aktuelle und Gesamtanzahl von Benutzern, Workflows und Dataflows an.
  <br>

![Main dashboard](../assets/images/user-interface/main-dashboard.png)
<br>

## Erfahren Sie mehr über die Konfiguration von Anwendungsdomänen

Anwendungsdomänen sind externe Bereiche mit einer bestimmten URL (HTTP/HTTPS://<your-domain-name>), in denen Sie Ihre Komponenten bereitstellen können.

**Standardmäßig ist eine App verfügbar** mit dem Namen 'digital-workplace'. Sie können weitere Apps über die Schaltfläche 'Add application' in der oberen rechten Ecke der Symbolleiste hinzufügen. Jede App, die Sie hinzufügen, erscheint in der Liste der Apps unter Ihrer Planbeschreibung.

In der Anwendungsdomäne können die folgenden Parameter in den 'Haupteinstellungen' festgelegt werden:

| Einstellungsgruppe | Einstellungsfeld      | Wertoptionen                                      | Zweck                                                              |
| ------------------ | --------------------- | ------------------------------------------------- | ------------------------------------------------------------------ |
| Haupteinstellungen | Title                 | -                                                 | Browser-Tab-Titel                                                  |
|                    | Hide top bar          | true, false                                       | Ausblenden des oberen Menüs für Workplace                          |
|                    | Static menu           | true, false                                       | Konstante Anzeige von Menüs oder Anzeige bei Mouse-Hover           |
|                    | Hide breadcrumps      | true, false                                       | Anzeigen/Ausblenden hierarchischer Navigation                      |
|                    | Hide user login       | true, false                                       | Anzeigen/Ausblenden des Benutzerlogins                             |
|                    | Hide locale           | true, false                                       | Anzeigen/Ausblenden der Standortauswahl                            |
|                    | Choose logo           | Logo, Small logo, favicon, "No image" placeholder | Auswahl eines Logos für WorkPlace (verschiedene Typen)             |
|                    | User Session Storage  | local/session                                     | Speichern von Autorisierungsparametern in einer Sitzung oder lokal |
|                    | Default Idp provider  | Multiselect of Catalog                            | Auswahl einer Autorisierungsmethode                                |
|                    | Default locale        | Multiselect of Catalog                            | Standardlokalisierung                                              |
|                    | Default user info app | Multiselect of Catalog                            | Hauptanwendung zur Verwaltung von Benutzerdaten                    |
|                    | Default component     | Multiselect of Catalog                            | Standardkomponente                                                 |
|                    | Default page          | -                                                 | Standardkomponentenseite                                           |
|                    | Login component       | Multiselect of Catalog                            | Autorisierungsformularkomponente                                   |
|                    | Enable SIP            | True, False                                       | Integration mit SIP aufbauen                                       |

<br>

In dieser Gruppe können Sie die Einstellungen globaler Module über JavaScript und CSS festlegen, wodurch Sie die Plattform in ein Content-Management-System (CMS) verwandeln und beliebige Drittanbieter-Bibliotheken hochladen und verwenden können.

JS-Beispiel für globales JavaScript:

```javascript
loadScript([
  'https://code.jquery.com/jquery-3.7.1.min.js?integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo=&crossorigin="anonymous"',
])
  .then((res) => {
    return loadScript([
      'https://code.jquery.com/ui/1.13.2/jquery-ui.min.js?integrity="sha256-lSjKY0/srUM9BE3dPm+c4fBo1dky2v27Gdjm2uoZaL0="&crossorigin="anonymous"',
    ]);
  })
  .subcribe({
    complete: () => {
      console.log("Load scripts complete");
    },
    error: (err) => {
      console.log("Load scripts err:" + err);
    },
  });
```

<br>

Darüber hinaus gibt es eine Einstellungsgruppe 'Stileinstellungen':

| Einstellungsgruppe | Einstellungsfeld     | Zweck                   |
| ------------------ | -------------------- | ----------------------- |
| Hauptschriftart    | Font                 | Hauptschriftart der App |
| Farbschema         | Default theme        | Standardfarbschema      |
|                    | Primary light color  | Haupthelle Farbe        |
|                    | Primary color        | Hauptfarbe              |
|                    | Primary dark color   | Hauptdunkle Farbe       |
|                    | Primary darker color | Hauptdunklere Farbe     |
|                    | Primary text color   | Standardtextfarbe       |

<br>

Einstellungsgruppe 'Edit manifest':

| Einstellungsfeld      | Zweck                               |
| --------------------- | ----------------------------------- |
| Name                  | Name der App im Manifest            |
| Short name            | Kurzname der App                    |
| Choose Icon (192x192) | Auswahl eines 192x192px App-Symbols |
| Choose Icon (512x512) | Auswahl eines 512x512px App-Symbols |

<br>

## SIP-Integration

Wenn die Option 'Enable SIP' in den 'Haupteinstellungen' aktiviert ist, sind mehrere nachfolgende Einstellungen erforderlich, damit Anrufe vom Workplace korrekt funktionieren.

**Auf der Studio-Seite:**

| Einstellungsfeld     | Zweck                                                                |
| -------------------- | -------------------------------------------------------------------- |
| SIP WebSocket server | SIP WebSocket-Serveradresse (z.B. 'wss://test-pbx.aqtra.ru:8089/ws') |
| SIP realm            | SIP-Bereich (Realm)                                                  |

<br>

**Auf der Workplace-Seite:**

| Einstellungsfeld     | Zweck                                                                |
| -------------------- | -------------------------------------------------------------------- |
| SIP user name        | Name des SIP-Benutzers                                               |
| SIP user password    | Passwort des SIP-Benutzers                                           |
| SIP WebSocket server | SIP WebSocket-Serveradresse (z.B. 'wss://test-pbx.aqtra.ru:8089/ws') |
| SIP realm            | SIP-Bereich (Realm)                                                  |

<br>

Wenn alle Parameter korrekt eingestellt sind, können Sie Anrufe vom Workplace aus tätigen. Sie können über die Arbeit mit SIP innerhalb des Component Script hier lesen: [Python verwenden](../app-development/using-python.md).
