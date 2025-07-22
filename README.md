# YouTube Playlist Summarizer (n8n + OpenAI)

Automatisiert: Holt neue Videos aus einer YouTube-Playlist, erstellt Transkripte, fasst sie per OpenAI GPT zusammen und sendet das Ergebnis direkt per Telegram.

## Features & Technik

- Läuft auf Raspberry Pi in Docker mit n8n
- Holt neue Videos automatisch (YouTube Data API)
- Erstellt Transkript (youtube-transcript-api, Python)
- Zusammenfassung per OpenAI GPT (API)
- Telegram-Benachrichtigung bei Erfolg und Fehlern
- Log-Datei aller erfolgreichen Zusammenfassungen

**Technischer Überblick:**  
- Zwei separate n8n-Workflows: einer überwacht die Playlist, einer nimmt Webhook-Anfragen entgegen  
- Python-Skript holt das Transkript via Video-ID  
- Verarbeitete Video-IDs werden in `yt_processed_ids.txt` gespeichert


## Getting Started

### Voraussetzungen

- Raspberry Pi mit Docker & Docker Compose
- GitHub-Account (für Code-Download)
- Eigener Telegram-Bot (per BotFather) & Chat-ID
- OpenAI-API-Key (kostenpflichtig)
- YouTube Data API-Key (Google Cloud Platform)

## Installation (Kurzfassung)

1. **Repo klonen:**
   ```sh
   git clone https://github.com/Mintberry1628/youtube-playlist-summarizer-n8n.git

2.	Docker Compose konfigurieren und starten
(Umgebung anpassen, API-Keys eintragen)

3.	n8n Workflows importieren
(JSON-Dateien liegen im n8n-Ordner)

4.	Telegram-Bot und OpenAI integrieren


## Beispiel-Workflows

<img width="1440" height="739" alt="image" src="https://github.com/user-attachments/assets/6d7bfaeb-54fd-45d0-a223-e42cdc1e684b" />
<img width="1440" height="739" alt="image" src="https://github.com/user-attachments/assets/5664344c-13b8-493a-a72b-a7c92057fc66" />


## Ordnerstruktur

```
. 
├── README.md 
├── yt_transcript.py 
├── yt_processed_ids.txt 
├── n8n/ 
└── logs/ 
```

## Lessons Learned

- Erstes Mal: Raspberry Pi komplett eingerichtet und im Netzwerk erreichbar gemacht (SSH, VNC Viewer, Connect)
- Mein erster produktiver Docker-Einsatz (Container-Management, Volumes, Updates)
- Einstieg in n8n-Workflows und deren Export/Import, Error-Trigger
- Umgang mit API-Keys und Secrets
- Debugging von Fehlern rund um Dateirechte, Netzwerkzugriffe, u.v.m.
- Workflow-Design: Wie prüft man am besten, ob ein Task schon erledigt ist (Datei vs. Datenbank)?
- GitHub als Portfolio-Tool – und wie Doku & ReadMe den Unterschied machen

**Erkenntnis:**  
Gerade durch viele kleine Fehler unterwegs (Rechte, Pfade, Umgebungen) habe ich gelernt, Probleme systematisch einzugrenzen.


## Credits

- [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api)
- [n8n.io](https://n8n.io/)
- [OpenAI API](https://openai.com/api/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
