# Home-Menü

<br>

Die Seite bietet Informationen über Ihre Lizenz und die bereitgestellten Anwendungsdomänen. Sie erhalten Zugriff auf die folgenden Funktionen und Informationen:

- **Planart**: Dies zeigt den Typ Ihres aktuellen Plans sowie das Ablauf- oder Erneuerungsdatum Ihres Abonnements an.
- **Anwendungsdomänen**: Dieser Abschnitt ermöglicht es Ihnen, Anwendungsbestandteile zu erstellen, Benutzer über spezifische URLs zu verbinden und zum Abschnitt „Navigationsmenü“ zu navigieren.
- **Nutzungsstatistiken**: Zeigt Informationen über die aktuelle Anzahl der Anwendungen im Vergleich zum Gesamtlimit sowie die aktuelle und die Gesamtzahl der Benutzer, Workflows und Datenflüsse an.
  <br>

![Haupt-Dashboard](../assets/images/user-interface/main-dashboard.png)
<br>

## Erfahren Sie mehr über die Konfiguration von Anwendungsdomänen

Anwendungsdomänen sind externe Bereiche mit einer spezifischen URL (HTTP/HTTPS://<your-domain-name>), in denen Sie Ihre Komponenten bereitstellen können.

**Standardmäßig ist eine App verfügbar**, die „digital-workplace“ heißt. Sie können weitere Apps hinzufügen, indem Sie die Schaltfläche „Anwendung hinzufügen“ in der oberen rechten Ecke der Symbolleiste verwenden. Jede App, die Sie hinzufügen, erscheint in der Liste der Apps unter Ihrer Planbeschreibung.

In der Anwendungsdomäne können die folgenden Parameter in den „Haupteinstellungen“ festgelegt werden:

| Einstellungsgruppe | Einstellungsfeld      | Wertoptionen                                     | Zweck                                                  |
| ------------------ | --------------------- | ------------------------------------------------ | ------------------------------------------------------ |
| Haupteinstellungen  | Titel                 | -                                                | Titel des Browser-Tabs                                 |
|                    | Obere Leiste ausblenden | true, false                                      | Ausblenden des oberen Menüs für den Arbeitsplatz       |
|                    | Statisches Menü       | true, false                                      | Ständige Anzeige von Menüs oder Anzeige bei Mouseover  |
|                    | Brotkrumen ausblenden | true, false                                      | Anzeigen/Ausblenden der hierarchischen Navigation       |
|                    | Benutzeranmeldung ausblenden | true, false                                      | Anzeigen/Ausblenden der Benutzeranmeldung               |
|                    | Standort ausblenden   | true, false                                      | Anzeigen/Ausblenden der Standortauswahl                 |
|                    | Logo auswählen        | Logo, Kleines Logo, Favicon, "Kein Bild" Platzhalter | Auswahl eines Logos für den Arbeitsplatz (verschiedene Typen) |
|                    | Benutzersitzungsspeicher | local/session                                    | Speichern von Autorisierungsparametern in einer Sitzung oder lokal |
|                    | Standard Idp-Anbieter | Mehrfachauswahl aus Katalog                      | Auswahl einer Autorisierungsmethode                     |
|                    | Standardlokalisierung | Mehrfachauswahl aus Katalog                      | Standardlokalisierung                                   |
|                    | Standardbenutzerinformations-App | Mehrfachauswahl aus Katalog                      | Hauptanwendung zur Verwaltung von Benutzerdaten        |
|                    | Standardkomponente    | Mehrfachauswahl aus Katalog                      | Standardkomponente                                      |
|                    | Standardseite         | -                                                | Standardkomponenten-Seite                              |
|                    | Anmeldekomponente     | Mehrfachauswahl aus Katalog                      | Autorisierungsformular-Komponente                       |
|                    | SIP aktivieren        | True, False                                      | Aufbau der Integration mit SIP                          |

<br>
In dieser Gruppe können Sie die Einstellungen globaler Module über JavaScript und CSS festlegen, was es Ihnen ermöglicht, die Plattform in ein Content-Management-System (CMS) zu verwandeln sowie beliebige Drittanbieter-Bibliotheken hochzuladen und zu verwenden.

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

Darüber hinaus gibt es eine Gruppe von Einstellungen für „Stileinstellungen“:

| Einstellungsgruppe   | Einstellungsfeld         | Zweck                  |
| -------------------- | ----------------------- | ---------------------- |
| Hauptschriftart      | Schriftart              | Hauptschriftart der App |
| Farbschema           | Standardthema           | Standardfarbschema     |
|                      | Primäre helle Farbe     | Haupthelle Farbe       |
|                      | Primäre Farbe           | Hauptfarbe             |
|                      | Primäre dunkle Farbe    | Hauptdunkle Farbe      |
|                      | Primäre dunklere Farbe   | Hauptdunklere Farbe    |
|                      | Primäre Textfarbe       | Standardtextfarbe      |

<br>

Einstellungsgruppe „Manifest bearbeiten“:

| Einstellungsfeld     | Zweck                             |
| ---------------------| --------------------------------- |
| Name                 | Name der App im Manifest          |
| Kurzname             | Kurzname der App                  |
| Icon auswählen (192x192) | Auswahl eines 192x192px App-Icons |
| Icon auswählen (512x512) | Auswahl eines 512x512px App-Icons |

<br>

## SIP-Integration

Wenn die Option „SIP aktivieren“ in den „Haupteinstellungen“ aktiviert ist, sind mehrere nachfolgende Einstellungen erforderlich, damit Anrufe vom Arbeitsplatz aus korrekt funktionieren.

**Auf der Studio-Seite:**

| Einstellungsfeld     | Zweck                                                               |
| ---------------------| ------------------------------------------------------------------- |
| SIP WebSocket-Server | SIP WebSocket-Serveradresse (z.B. 'wss://test-pbx.aqtra.ru:8089/ws') |
| SIP Realm            | SIP-Bereich (Realm)                                                |

<br>

**Auf der Arbeitsplatz-Seite:**

| Einstellungsfeld     | Zweck                                                               |
| ---------------------| ------------------------------------------------------------------- |
| SIP-Benutzername     | Name des SIP-Benutzers                                             |
| SIP-Benutzerpasswort | Passwort des SIP-Benutzers                                         |
| SIP WebSocket-Server | SIP WebSocket-Serveradresse (z.B. 'wss://test-pbx.aqtra.ru:8089/ws') |
| SIP Realm            | SIP-Bereich (Realm)                                                |

<br>

Wenn alle Parameter korrekt eingestellt sind, können Sie Anrufe vom Arbeitsplatz aus tätigen. Sie können hier über die Arbeit mit SIP im Komponentenskript lesen: [Using Python](../app-development/using-python.md).