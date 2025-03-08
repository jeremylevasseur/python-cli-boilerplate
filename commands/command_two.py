from typing import Annotated

from typer import Option as TyperOption
from typer import Typer

from models import TyperMetadata

command_two_cli = Typer()

command_two_metadata = TyperMetadata(
    name="command-two",
    help="Command two description",
)


@command_two_cli.callback(help=command_two_metadata.help)
def command_two(
    option_one: Annotated[str, TyperOption("--option-one", "-oo", help="Option one")],
    option_two: Annotated[
        str, TyperOption("--option-two", "-ot", help="Option two")
    ] = "option_two_default",
) -> None:
    """
    Command two description
    """
    print(f"Command two: {option_one}, {option_two}")
