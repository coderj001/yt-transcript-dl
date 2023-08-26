import os
from yt_transcript_dl.transcript import get_transcript
from unittest.mock import patch

MOCKED_RESPONSE = [
    {"start": 0.0, "duration": 5.0, "text": "Hello"},
    {"start": 5.0, "duration": 5.0, "text": "World"},
]


@patch(
    "youtube_transcript_api.YouTubeTranscriptApi.get_transcript",
    return_value=MOCKED_RESPONSE,
)
def test_get_transcript(mock_get_transcript) -> None:
    video_id = "dummyVideoId"
    get_transcript(video_id, timestamp=True)

    assert os.path.exists(f"{video_id}.txt"), "Transcript file was not created!"

    with open(f"{video_id}.txt", "r") as file:
        content = file.read()
        assert "Hello" in content, "Expected text was not found in the transcript file!"
        assert "Start:" in content, "Timestamps were not saved in the transcript file!"

    os.remove(f"{video_id}.txt")
