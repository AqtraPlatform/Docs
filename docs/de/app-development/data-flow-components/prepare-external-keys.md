# Bereiten Sie externe Schlüssel vor

![](../../assets/images/app-development/prepare-external-keys.png)

## Allgemeine Informationen
Der Schritt „Externe Schlüssel vorbereiten“ wird verwendet, um die internen Identifikatoren der Komponente in externe Systemschlüssel zu konvertieren. Dieser Schritt wird häufig verwendet, um Daten für externe Systeme vorzubereiten und zu senden, einschließlich der Integration mit LDAP. Er erleichtert den Prozess der Übertragung von Benutzerinformationen an ein externes System, einschließlich des relevanten Kontexts.

Im Verlauf des Schrittes werden die internen IDs der Komponente durch die für diese Komponente angegebenen Primärschlüssel ersetzt, was die korrekte Zuordnung von Daten zwischen den internen und externen Systemen gewährleistet.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld | Wertoptionen | Zweck |
|------------------|--------------|-------|
| Schrittname      | -            | Name des Schrittes |
| Quellenschritt   | -            | Datenquelle für die Schlüsselkonvertierung |

## Fälle
- **Integration mit externen Systemen**: Wird verwendet, um interne Daten für die ordnungsgemäße Integration und den Versand an externe Systeme wie LDAP anzupassen.
- **Daten für den Export vorbereiten**: Geeignet für Skripte, bei denen interne IDs transformiert werden müssen, um den Standards und Anforderungen externer Systeme zu entsprechen.

## Ausnahmen
- **Anforderung an die Relevanz und Genauigkeit der Daten**: Die Effektivität des Schrittes hängt von der Genauigkeit und Relevanz der internen Daten und deren Übereinstimmung mit der Struktur des externen Systems ab.
- **Datenzuordnungsmanagement**: Sie müssen sicherstellen, dass alle internen IDs korrekt den Primärschlüsseln des externen Systems zugeordnet sind, um Integrationsfehler zu vermeiden.