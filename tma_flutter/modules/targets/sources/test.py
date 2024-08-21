import typer
from typing_extensions import Annotated
from tma_flutter.snippets.sources import flutter


app = typer.Typer()


@app.command(name="make")
def make_target(
    test_name: Annotated[str, typer.Argument()],
    dir_name: Annotated[str, typer.Argument()] = "tests",
):
    flutter.create_package(
        package_name=test_name,
        dir_name=dir_name,
    )


def name(project_name: str) -> str:
    return project_name + "_" + "test"


if __name__ == "__main__":
    app()
