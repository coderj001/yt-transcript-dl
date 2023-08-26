import os

import click

from yt_transcript_dl import transcript


@click.command()
@click.argument(
    "video_id",
    type=str,
)
@click.option(
    "--timestamp/--no-timestamp",
    default=False,
    help="""
    Include timestamps in the transcript. Default is to exclude timestamps.
    """,
)
def main(video_id: str, timestamp: bool) -> None:
    """
    CLI tool to fetch and save the transcript of a YouTube video.

    \n\t:param video_id: YouTube video ID
    \n\t:param timestamp: Flag to include timestamps in the transcript
    """
    # Get the current working directory
    output_dir = os.getcwd()

    transcript.get_transcript(
        video_id=video_id, timestamp=timestamp, output_dir=output_dir
    )


if __name__ == "__main__":
    main(obj={})
