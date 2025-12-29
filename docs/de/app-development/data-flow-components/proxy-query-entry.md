# Proxy-Abfrageeintrag

![](../../assets/images/app-development/proxy-query-entry.png)

## Allgemeine Informationen
Der Schritt „Proxy-Abfrageeintrag“ wird verwendet, um ein Proxy-Abfragemodell mithilfe eines Filters (**Abfrage**) zu generieren, um einzelne oder mehrere Einträge abzurufen. Dieser Schritt funktioniert in Verbindung mit der Einstellung „Proxy-Modus“ im Abschnitt „Einstellungen“. Damit das Datenmodell der Komponente korrekt funktioniert, müssen Eigenschaften mit dem **Abfrage**-Flag definiert werden.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld      | Wertoptionen      | Zweck      |
|-----------------------|-------------------|------------|
| Schrittname           | -                 | Name des Schrittes |
| Abfragefilter         | -                 | Filter zur Definition eines bestimmten Eintrags für eine Abfrage |
| Proxy-Modus-Einstellungen | -              | Verweis auf die im Abschnitt „Einstellungen“ definierten Proxy-Modus-Einstellungen |

## Fälle
- **Gefilterte Abfragen im Proxy**: Wird im Eingabedatenfluss für als Proxy markierte Komponenten verwendet, um Abfragen mit Datenfilterung auszuführen.
- **Abrufen spezifischer Daten**: Ruft einen bestimmten Eintrag basierend auf bestimmten Filterkriterien ab.

## Ausnahmen
- **Abhängigkeit von der Komponenten-Konfiguration**: Erfordert bestimmte Eigenschaften mit dem **Abfrage**-Flag im Datenmodell der Komponente.
- **Eingeschränkte Verwendung**: Der Schritt ist darauf ausgelegt, Daten basierend auf Filtern abzurufen und ist nicht für allgemeine Abfragen ohne Spezifikation geeignet.