import os
from click.testing import CliRunner
from yt_transcript_dl import main


def test_empty_paramaters() -> None:
    runner = CliRunner()
    result = runner.invoke(main, [])
    assert result.exit_code == 2


def test_help_paramaters() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0


def test_invalid_video_id() -> None:
    runner = CliRunner()
    invalid_video_id = "123456"
    result = runner.invoke(main, [invalid_video_id])
    assert result.exit_code == 1


def test_correct_paramaters() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["ArFQdvF8vDE"])
    assert result.exit_code == 0
    if os.path.exists("ArFQdvF8vDE.txt"):
        with open("ArFQdvF8vDE.txt", "r") as file:
            content = file.read()
            assert "coronaviruses are a type of virus the\n" in content

        os.remove("ArFQdvF8vDE.txt")
    else:
        assert False, "Transcript file was not created!"
