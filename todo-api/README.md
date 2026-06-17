# todo-api

REST-API zur Verwaltung von Todo-Listen und deren Einträgen. Umgesetzt mit
Flask, ausführbar als Docker-Container über Docker Compose.

## Voraussetzungen

Docker und Docker Compose müssen installiert sein und laufen.

## Starten

```bash
docker-compose up -d
```

Der Befehl baut das Image aus dem Dockerfile und startet den Container im
Hintergrund. Die API ist anschließend unter `http://localhost:5000` erreichbar.

## Endpunkte

| Methode | Pfad              | Beschreibung                            |
| ------- | ----------------- | --------------------------------------- |
| GET     | `/`               | Alle Listen anzeigen                    |
| POST    | `/todo-list`      | Neue Liste anlegen                      |
| GET     | `/todo-list/<id>` | Alle Einträge einer Liste abrufen       |
| POST    | `/todo-list/<id>` | Neuen Eintrag zu einer Liste hinzufügen |
| DELETE  | `/todo-list/<id>` | Komplette Liste samt Einträgen löschen  |
| PATCH   | `/entry/<id>`     | Einzelnen Eintrag aktualisieren         |
| DELETE  | `/entry/<id>`     | Einzelnen Eintrag löschen               |

Die vollständige Schnittstellenbeschreibung liegt in `openapi.yaml`.

## Beispiel

Einträge der vorbefüllten Einkaufsliste abrufen:

```
http://localhost:5000/todo-list/1318d3d1-d979-47e1-a225-dab1751dbe75
```

## Hinweis

Die Daten werden nur im Arbeitsspeicher gehalten. Nach einem Neustart des
Containers gehen alle Änderungen verloren und der Beispiel-Datenbestand wird
neu erzeugt.

## Aufbau

```
todo-api/
├── docker-compose.yml      # Startkonfiguration
├── Dockerfile              # Bauanleitung des Images
├── main.py                 # Flask-Anwendung
├── requirements.txt        # Python-Abhängigkeiten
└── openapi.yaml            # API-Beschreibung
```
