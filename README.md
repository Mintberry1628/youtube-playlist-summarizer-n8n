# YouTube Playlist Summarizer (n8n Workflow)

![License](https://img.shields.io/github/license/Mintberry1628/youtube-playlist-summarizer-n8n)
![Languages](https://img.shields.io/github/languages/top/Mintberry1628/youtube-playlist-summarizer-n8n)
![Platform](https://img.shields.io/badge/platform-RaspberryPi-green)
![Last Commit](https://img.shields.io/github/last-commit/Mintberry1628/youtube-playlist-summarizer-n8n)


This project demonstrates how to automatically summarize new videos from a YouTube playlist using n8n. Summaries are delivered via Telegram.


## Table of Contents

- [Folder Structure](#folder-structure)
- [Use Case](#use-case)
- [Workflow Overview](#workflow-overview)
- [Prerequisites](#prerequisites)
- [Setup & Configuration](#setup--configuration)
- [How it Works (Step by Step)](#how-it-works-step-by-step)
- [Lessons Learned](#lessons-learned)
- [Findings](#findings)
- [Credits](#credits)

---

## Folder Structure

```
.
├── n8n_workflow.json         # n8n workflow export file
├── screenshots/              # Example screenshots
│   ├── overview.png
│   └── nodes_example.png
├── README.md
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
2. **Import the `n8n_workflow.json` file into your n8n instance.**
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
<<<<<<< HEAD

## Screenshots

![Workflow Overview](screenshots/overview.png)

*The full n8n workflow for summarizing YouTube playlists.*



---
=======
>>>>>>> 25fd6e0 (Update README.md)

## Screenshots

![Workflow Overview](screenshots/overview.png)

*The full n8n workflow for summarizing YouTube playlists.*



---

## Lessons Learned

- Not all YouTube videos offer transcripts—some videos (especially music or private uploads) have no transcript, which can interrupt the flow.
- The YouTube API limits how many requests you can make in a given time window.
- Handling API errors and timeouts is essential for robustness.
- The quality of AI-generated summaries varies—long transcripts or multi-part content can lead to less precise summaries.
- Telegram is fast and easy for notifications, but other integrations (Slack, Email, Notion, etc.) are possible.

---

## Findings

- **n8n** is very flexible for automating such data pipelines and can be extended with many services.
- **YouTube's transcript extraction** is not officially documented—sometimes transcripts are missing even when visible on YouTube.
- **LLM Summarization** is a powerful tool but can be improved with prompt engineering or by splitting longer transcripts.
- This workflow can serve as a base for other "summarize new content" automations (e.g., RSS feeds, Notion pages, articles, etc.).

---

## Credits

- Workflow developed and documented by [Mintberry1628](https://github.com/Mintberry1628).
- Powered by [n8n](https://n8n.io/), [OpenAI](https://openai.com), and the [YouTube Data API](https://developers.google.com/youtube/v3).
- Inspired by the open automation and productivity community.

---

**For questions or suggestions, feel free to open an issue or contact me via GitHub.**
