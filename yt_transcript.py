from youtube_transcript_api import YouTubeTranscriptApi
import sys
import json
import requests

if len(sys.argv) < 3:
    print(json.dumps({"error": "Usage: yt_transcript.py <video_id> <webhook_url>"}))
    sys.exit(1)

video_id = sys.argv[1]
webhook_url = sys.argv[2]

try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['de', 'en'])
    text = " ".join([part['text'] for part in transcript])
    data = {"transcript": text, "video_id": video_id}
    # Sende an n8n-Webhook
    response = requests.post(webhook_url, json=data)
    print(f"Webhook Response: {response.status_code}")
except Exception as e:
    print(json.dumps({"error": str(e)}))
    sys.exit(1)
