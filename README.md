# YouTube Playlist Summarizer (n8n Workflow)

![Tool](https://img.shields.io/badge/tool-n8n-blue)
![Platform](https://img.shields.io/badge/platform-Docker-green)
![Platform](https://img.shields.io/badge/platform-RaspberryPi-green)
![API](https://img.shields.io/badge/API-OpenAI-orange)
![License](https://img.shields.io/github/license/Mintberry1628/youtube-playlist-summarizer-n8n)
![Languages](https://img.shields.io/github/languages/top/Mintberry1628/youtube-playlist-summarizer-n8n)
![Last Commit](https://img.shields.io/github/last-commit/Mintberry1628/youtube-playlist-summarizer-n8n)


This project demonstrates how automation can save time and ensure up-to-date information without manual effort.

**Tech Stack:** n8n, Docker, OpenAI API, Telegram API, YouTube Data API

## Table of Contents

- [Folder Structure](#folder-structure)
- [Use Case](#use-case)
- [Workflow Overview](#workflow-overview)
- [Prerequisites](#prerequisites)
- [Setup & Configuration](#setup--configuration)
- [How it Works (Step by Step)](#how-it-works-step-by-step)
- [Screenshots](#screenshots)
- [Key Learnings & Next Steps](#key-learnings--next-steps)
- [Credits](#credits)

---

## Folder Structure

```
.
├── .gitignore
├── LICENSE
├── README.md
├── yt_transcript.py         # Script to fetch YouTube transcripts (optional, see Notes)
├── img/
│   ├── first_workflow.png
│   └── second_workflow.png
├── logs/
│   └── yt_processed_ids.txt
├── n8n/
│   ├── YouTube_Playlist_Summarizer.json
│   └── YouTube_Transcript_Handler.json
```

---

## Use Case

You want to receive regular, concise summaries of all new videos added to a YouTube playlist—without having to watch every video in full.

---

## Workflow Overview

This n8n workflow:

- Retrieves all new videos from a given YouTube playlist.
- Downloads the transcript for each video (if available).
- Uses AI (e.g., OpenAI) to summarize the content.
- Sends the summary (including the video title) via Telegram.

---

## Prerequisites

- A running [n8n](https://n8n.io/) instance (Docker, cloud, self-hosted, etc.)
- A YouTube Data API key
- An OpenAI API key (or alternative summarization service)
- A Telegram bot token and chat ID

---

## Setup & Configuration

1. **Clone or download this repository.**
2. **Import the `n8n/YouTube_Playlist_Summarizer.json` and `n8n/YouTube_Transcript_Handler.json` file into your n8n instance.**
3. **Set up credentials in n8n:**
    - YouTube API Key
    - OpenAI (or alternative) API Key
    - Telegram Bot Token and Chat ID
4. **Set your desired YouTube Playlist ID in the appropriate node.**
5. *(Optional)* Configure a schedule trigger to automate execution.

---

## How it Works (Step by Step)

1. **Trigger:** The workflow is started manually or by schedule.
2. **YouTube Playlist Check:** The playlist is checked for new videos.
3. **Transcript Retrieval:** For each new video, the transcript is downloaded (if available).
4. **Summarization:** The transcript is sent to OpenAI (or another LLM) for summarization.
5. **Telegram Notification:** The summary, including the video title, is sent as a Telegram message.
6. **(Optional) Logging & Error Handling:** The workflow can be expanded for better error management.

---

## Screenshots

![Workflow Overview](img/first_workflow.png)
![Workflow Overview](img/second_workflow.png)
*The full n8n workflow for summarizing YouTube playlists.*

---

## Key Learnings & Next Steps

- Flexible orchestration with n8n; Telegram works well as a fast and reliable delivery channel.
- Limitations: missing transcripts, YouTube API rate limits, and LLM output quality for very long texts.
- Fixes implemented: transcript availability check, retry/backoff logic, chunking and prompt tuning.
- Next steps: add a fallback for missing transcripts, support multi-channel output, and implement basic workflow monitoring.

---

## Credits

- Workflow developed and documented by [Mintberry1628](https://github.com/Mintberry1628).
- Powered by [n8n](https://n8n.io/), [OpenAI](https://openai.com), and the [YouTube Data API](https://developers.google.com/youtube/v3).
- Inspired by the open automation and productivity community.

---

**For questions or suggestions, feel free to open an issue or contact me via GitHub.**
