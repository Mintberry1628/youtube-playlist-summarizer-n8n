```markdown
# YouTube Playlist Summarizer (n8n Workflow)

![Tool](https://img.shields.io/badge/tool-n8n-blue)
![Platform](https://img.shields.io/badge/platform-Docker-green)
![Platform](https://img.shields.io/badge/platform-RaspberryPi-green)
![API](https://img.shields.io/badge/API-OpenAI-orange)
![API](https://img.shields.io/badge/API-YouTube%20Data%20API-red)
![License](https://img.shields.io/github/license/Mintberry1628/youtube-playlist-summarizer-n8n)
![Languages](https://img.shields.io/github/languages/top/Mintberry1628/youtube-playlist-summarizer-n8n)
![Last Commit](https://img.shields.io/github/last-commit/Mintberry1628/youtube-playlist-summarizer-n8n)

Automated summaries for new YouTube videos in a playlist — discovered by n8n, transcripts fetched via Python, summarized by an LLM, and delivered to Telegram.

---

## Table of Contents
- [Quickstart (TL;DR)](#quickstart-tldr)
- [Folder Structure](#folder-structure)
- [Use Case](#use-case)
- [Workflow Overview](#workflow-overview)
- [Prerequisites](#prerequisites)
- [Setup & Configuration](#setup--configuration)
- [How it Works (Step by Step)](#how-it-works-step-by-step)
- [Screenshots](#screenshots)
- [Troubleshooting](#troubleshooting)
- [Known Limitations](#known-limitations)
- [Built With AI Assistance](#built-with-ai-assistance)
- [Lessons Learned](#lessons-learned)
- [Findings](#findings)
- [Credits](#credits)
- [License](#license)

---

## Quickstart (TL;DR)

~~~bash
# optional: create and activate a virtualenv for the helper script
python3 -m venv .venv && source .venv/bin/activate
pip install -U pip youtube-transcript-api requests

# import sanitized n8n workflows
# n8n/YouTube_Playlist_Summarizer.json
# n8n/YouTube_Transcript_Handler.json

# in n8n: set credentials (YouTube API, OpenAI, Telegram)
# set your Telegram chat ID and the YouTube playlist ID
# set the webhook URL argument in the ExecuteCommand node (localhost or your n8n base URL)

# run the summarizer on a schedule or manually to test
~~~

> **Note on `requests`:** The helper script posts the transcript to your n8n webhook. If you prefer, you can replace `requests` with Python’s built-in `urllib.request` and remove `requests` from your environment.

---

## Folder Structure

~~~
.
├── .gitignore
├── LICENSE
├── README.md
├── yt_transcript.py                 # Helper: fetch transcript, POST to n8n webhook
├── img/
│   ├── first_workflow.png
│   └── second_workflow.png
├── logs/                            # runtime state (ignored in Git)
│   └── yt_processed_ids.txt
└── n8n/
    ├── YouTube_Playlist_Summarizer.json
    └── YouTube_Transcript_Handler.json
~~~

---

## Use Case

Receive **concise summaries** of new videos added to a YouTube playlist — without watching every video end-to-end. Ideal for continuous learning, newsletters, or topic monitoring.

---

## Workflow Overview

Two n8n workflows work together:

1) **YouTube Playlist Summarizer**  
   - Runs on a schedule, queries playlist items, detects **new** videos (tracked via a simple local `logs/yt_processed_ids.txt`).  
   - Calls `yt_transcript.py` with `videoId` **and** a **webhook URL** to the second workflow.

2) **YouTube Transcript Handler**  
   - Receives the transcript payload via webhook.  
   - Summarizes with your **OpenAI** credentials.  
   - Sends result to **Telegram**.

*(Both JSON exports are sanitized and contain placeholders — replace them in n8n after import.)*

---

## Prerequisites

- A running **n8n** (Docker, cloud, or self-hosted)
- **YouTube Data API key**
- **OpenAI API key** (or another LLM provider if you adapt the node)
- **Telegram bot token** & your **chat ID**
- Python 3.9+ with:
  - `youtube-transcript-api`
  - `requests` *(only needed if the helper posts to the webhook via HTTP; you can swap for `urllib` if preferred)*

---

## Setup & Configuration

1. **Clone** this repository locally.
2. **Install helper deps** (optional venv recommended):
   ~~~bash
   python3 -m venv .venv && source .venv/bin/activate
   pip install youtube-transcript-api requests
   ~~~
3. **Import both workflows into n8n**:
   - `n8n/YouTube_Playlist_Summarizer.json`
   - `n8n/YouTube_Transcript_Handler.json`
4. **Set credentials in n8n**:
   - YouTube API (HTTP Request node)
   - OpenAI (LLM node)
   - Telegram (send message)
5. **Configure playlist & webhook**:
   - Set your **Playlist ID** in the Summarizer workflow.
   - In the ExecuteCommand node, set the **Webhook URL** of the Transcript Handler workflow.
6. **Schedule** a periodic run (e.g., every 10–15 minutes) and perform a **test run**.

---

## How it Works (Step by Step)

1. **Schedule Trigger** → fetch playlist items via YouTube API.  
2. **Split items** → for each video, extract `videoId`.  
3. **Deduplicate** → check `logs/yt_processed_ids.txt`; skip already processed IDs.  
4. **Transcript fetch** → call `yt_transcript.py <videoId> <webhookUrl>`;  
   - Script uses `youtube-transcript-api` and sends the transcript as JSON **via POST** to the **Webhook** of the second workflow.  
5. **Summarization (workflow #2)** → LLM produces bullet points and a short narrative.  
6. **Telegram** → send the summary to your chat.

---

## Screenshots

![Workflow Overview 1](img/first_workflow.png)  
![Workflow Overview 2](img/second_workflow.png)

---

## Troubleshooting

- **No transcript available:** Some videos disable transcripts; the helper should catch exceptions and optionally send a short “no transcript” message.  
- **Rate limits / YouTube quota:** Use moderate schedules (e.g., 10–15 min), cache processed IDs, and reduce requested fields.  
- **Telegram errors:** Ensure Chat ID and bot token are set; very long messages can be split or shortened.  
- **Webhook 401/404:** Verify base URL/port and the exact path from the Webhook trigger node.

---

## Known Limitations

- Videos without transcripts can’t be summarized (unless you add an ASR step).  
- Very long transcripts may require chunking or a smaller LLM context.

---

## Built With AI Assistance

This project was ideated, designed, tested and validated by **Mintberry1628**.  
Implementation was created **with assistance from AI coding partners**:
- **ChatGPT (GPT-5 Thinking)** for planning, refactoring and code generation  
- **Claude** for code reviews and alternative implementations

I (Mintberry1628) was responsible for the idea, concept, requirements, and hands-on testing/validation of the results.  
All code was produced under my direction and verified against real inputs before use.

---

## Lessons Learned

- **Transcripts are not guaranteed:** Many videos disable them; the workflow must handle this gracefully.  
- **Rate limits matter:** Modest schedules + processed-ID cache keep API usage reasonable.  
- **Delivery channel:** Telegram is fast/reliable; still cap message length and consider splitting.  
- **LLM prompts:** Short, structured prompts yield better summaries than long free-form prompts.

---

## Findings

- **Playlists produce bursts:** New uploads often arrive in clusters; batching logic prevents spam.  
- **Shorts vs. long-form:** Shorts frequently lack transcripts; long-form content benefits most from summarization.  
- **Topic drift:** Creator channels may shift topics — summaries help decide quickly what to watch in full.

---

## Credits

- Workflows & helper script by **Mintberry1628**.  
- Thanks to **n8n**, **youtube-transcript-api**, **OpenAI**, **Telegram**.

---

## License

This project is released under the **MIT License**. See [LICENSE](LICENSE) for details.
```
