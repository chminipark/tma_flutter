import typer
from typing_extensions import Annotated
from tma_flutter.snippets.sources import flutter


app = typer.Typer()


@app.command(name="make")
def make_target(
    interface_name: Annotated[str, typer.Argument()],
    dir_name: Annotated[str, typer.Argument()] = "interfaces",
):
    flutter.create_package(
        package_name=interface_name,
        dir_name=dir_name,
    )


def name(project_name: str) -> str:
    return project_name + "_" + "interface"


if __name__ == "__main__":
    app()
