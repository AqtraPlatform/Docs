# Wartungsmenü

<br>

Das „Wartungs“-Menü ist ein leistungsstarkes Werkzeug zur Verwaltung von Daten und zur Wartung des Systems, insbesondere nach größeren Updates, Datenmigrationen oder Änderungen an der Datenbank.
<br>

## Allgemeine Beschreibung

- **Zweck**: Verwaltung von PostgreSQL-Daten über ODATA, Entfernen gelöschter Daten, Analysieren und Verwalten von Systemprotokollen.
- **Funktionen**: Das Tool wird hauptsächlich nach Plattformversionsupdates, Komponentenimporten oder massiven Datenänderungen verwendet.
  <br>

## Registerkarten des Wartungsmenüs

<br>

### Systemprotokolle

<br>

! [Systemprotokolle] (system-logs.png)
<br>

- **Funktionalität**: Aktuelle Systemprotokolle anzeigen und Protokollierungsstufen anpassen (Trace, Debug, Information, Warnung, Kritisch, Fehler, Keine).
  <br>

### Systemwartung

<br>

! [Systemwartung] (system-maintenance.png)
<br>

1. **Datenbankreferenzen neu aufbauen**: Überprüfen und Wiederherstellen von Querverweisen zwischen Komponenten oder innerhalb von Komponenten (Datenfluss/Workflow).
2. **RLS-Regeln neu aufbauen**: Wiederherstellen von Row-Level-Security-Regeln zur Anpassung des Datenzugriffs.
3. **Cache neu aufbauen**: Wiederherstellen des internen Caches der Plattform, um Probleme mit Updates zu lösen.
4. **Zur Löschung markierte Analyse**: Anzeigen und Verwalten von Datensätzen, die zur Löschung markiert sind, mithilfe des Flags „Eintrag zur Löschung markieren“ im Schritt „Eintrag aktualisieren“. Nach dem Klicken auf die Schaltfläche „Zur Löschung markierte Analyse“ werden alle markierten Einträge angezeigt. Einträge werden über „Ausgewählte Elemente löschen“ ausgewählt und gelöscht. Das System verhindert das Löschen von Einträgen, wenn es verwandte, nicht markierte Einträge gibt.
5. **Aktuelle Veröffentlichung zurücksetzen**: Setzt den Veröffentlichungsprozess zurück, wenn er fehlschlägt.
   <br>

### Dateispeicher

Dieser Abschnitt fügt die Möglichkeit hinzu, die folgenden Einstellungen für den Dateispeicher zu konfigurieren:

| Akzeptable Dateitypen | Dateigrößenlimit in Bytes |
| --------------------- | -------------------------- |
| .\* (alle Dateitypen) | ausgewählte Größe          |

<br>

Sie können Filtertypen angeben, die durch Kommas getrennt sind. Dies können Dateierweiterungen wie .jpg, .json, .docx oder Mime-Typen wie image/_, application/_ sein.

Sie können auch Filter kombinieren, zum Beispiel, `image/*`, `.docx`. Die Verwendung des `*/*`-Filters ermöglicht es Ihnen, beliebige Dateien hochzuladen.
<br>

![Wartung des Dateispeichers](../assets/images/user-interface/file-storage-maintenance.png)