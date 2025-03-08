from art import tprint
from typer import Typer

from commands import (
    command_one_cli,
    command_one_metadata,
    command_two_cli,
    command_two_metadata,
)
from config import config

app = Typer(
    name=config.APP_NAME,
    no_args_is_help=config.NO_ARGS_IS_HELP,
    add_completion=False,
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["-h", "--help"]},
)

app.add_typer(
    command_one_cli,
    name=command_one_metadata.name,
    help=command_one_metadata.help,
    no_args_is_help=config.NO_ARGS_IS_HELP,
)

app.add_typer(
    command_two_cli,
    name=command_two_metadata.name,
    help=command_two_metadata.help,
    no_args_is_help=config.NO_ARGS_IS_HELP,
)

if __name__ == "__main__":
    tprint(config.APP_DISPLAY_NAME, font="cybermedium")
    app()
