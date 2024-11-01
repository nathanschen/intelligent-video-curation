import typer

from intelligent_video_curation.filters.filter import run as run_filtering
from intelligent_video_curation.helpers.output import output
from intelligent_video_curation.helpers.setup import setup
from intelligent_video_curation.preprocessors.preprocess import run as run_preprocessing

main = typer.Typer()


@main.command()
def run(*, config: str = typer.Option(..., help="Path to the YAML config file")) -> None:  # noqa: ANN
    setup(config)
    videos = run_preprocessing()
    videos = run_filtering(videos)
    output(videos)


if __name__ == "__main__":
    main()
