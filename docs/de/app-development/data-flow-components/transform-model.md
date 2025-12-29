# Transformationsmodell

![](../../assets/images/app-development/transform-model.png)

## Allgemeine Informationen
Der Schritt „Transformationsmodell“ wird verwendet, um Felder im Datenmodell zuzuordnen und zu transformieren. Dies umfasst das Ändern von Feldnamen und das Entfernen unnötiger Felder aus dem Modell. Der Schritt erstellt eine neue Kopie des Datenflussmodells, die es Ihnen ermöglicht, dessen Struktur zu ändern, was oft verwendet wird, um die Antwort als Datenmodell zu minimieren. Es kann auch verwendet werden, um das Datenmodell nach mehreren Gruppierungsoperationen (Gruppieren nach) zu optimieren.

## Parameter
**Schritt Einstellungen:**

| Einstellungsfeld  | Wertoptionen | Zweck |
|-------------------|--------------|-------|
| Schrittname       | -            | Name des Schrittes |
| Quellenschritt    | -            | Auswahl des vorherigen Schrittes |
| Felderzuordnung    | -            | Zuordnung und Änderung von Feldern im Datenmodell |

## Fälle
- **Optimierung des Datenmodells**: Wird verwendet, um die Struktur des Datenmodells zu ändern, einschließlich Umbenennung oder Löschen von Feldern.

## Ausnahmen
- **Bedeutung einer genauen Zuordnung**: Fehler in der Einstellung „Felderzuordnung“ können zu unerwünschten Änderungen am Datenmodell führen.
- **Abhängigkeit von den Quelldaten**: Die korrekte Anwendung des Schrittes erfordert ein genaues Verständnis der Struktur der Quelldaten.

## Anwendungsszenario

Diese Komponente enthält einen Datenfluss, der für die Datenumwandlung gemäß den festgelegten Regeln verwendet wird. Der Datenfluss umfasst Schritte wie Sammlung extrahieren und Skript ausführen, die es ermöglichen, neue Datensätze zu den Kundendatenarrays hinzuzufügen.

- Sie können die Komponenten-Konfiguration [hier](https://drive.google.com/file/d/1buQNdkjcnY8wgIUM9TjjI7KoikEcSmv3/view?usp=sharing) herunterladen.