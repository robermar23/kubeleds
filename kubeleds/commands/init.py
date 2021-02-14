"""
CLI initialization command.
"""
import click
from rich.prompt import Prompt

from kubeleds import console
from kubeleds.constants import WELCOME_MESSAGE


@click.command()
def init():
    """
    CLI Initialization demo.
    """
    console.print(WELCOME_MESSAGE)
