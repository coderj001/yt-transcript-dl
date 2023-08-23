from click.testing import CliRunner
from yt_transcript_dl import main


def test_main() -> None:
    runner = CliRunner()
    result = runner.invoke(main, [])
    assert result.exit_code == 0


def test_example() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["example"])
    assert result.exit_code == 0
