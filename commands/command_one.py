from typing import Annotated

from typer import Option as TyperOption
from typer import Typer

from models import TyperMetadata

command_one_cli = Typer()

command_one_metadata = TyperMetadata(
    name="command-one",
    help="Command one description",
)


@command_one_cli.callback(help=command_one_metadata.help)
def command_one(
    option_one: Annotated[str, TyperOption("--option-one", "-oo", help="Option one")],
    option_two: Annotated[
        str, TyperOption("--option-two", "-ot", help="Option two")
    ] = "option_two_default",
) -> None:
    """
    Command one description
    """
    print(f"Command one: {option_one}, {option_two}")
