from typing import Optional
from youtube_transcript_api import YouTubeTranscriptApi


def get_transcript(
    video_id: str, timestamp: bool = False, output_dir: Optional[str] = None
) -> None:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    with open(f"{video_id}.txt", "w") as file:
        for entry in transcript:
            if timestamp:
                start_time = entry["start"]
                duration = entry["duration"]
            text = entry["text"]
            if timestamp:
                file.write(f"Start: {start_time}, Duration: {duration}\n")

            file.write(text + "\n\n")
        print(f"{video_id} ...DONE")
