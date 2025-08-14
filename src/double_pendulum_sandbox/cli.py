"""Console script for double_pendulum_sandbox."""

import typer
from rich.console import Console

from double_pendulum_sandbox import utils

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for double_pendulum_sandbox."""
    console.print("Replace this message by putting your code into "
               "double_pendulum_sandbox.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
