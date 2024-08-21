import typer, os
from typing_extensions import Annotated
from pathlib import Path
from tma_flutter.snippets.sources import flutter, template


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


def copy_template(interface_name: str):
    interface_path = _get_interface_path()
    lib_path = interface_path.joinpath("lib")
    test_path = interface_path.joinpath("test")
    template.prepare_copy(lib_path, test_path)

    template_path = Path(__file__).absolute().parent.joinpath("templates")
    template.copy(
        copy_path=template_path.joinpath("lib"),
        copy_file="interface.dart",
        paste_path=lib_path,
        paste_file=f"{interface_name}.dart",
    )


def add_dependency(
    target_name: str,
    target_path: str,
):
    interface_path = _get_interface_path()
    os.chdir(interface_path)
    flutter.add_dependency(
        target_name=target_name,
        target_path=target_path,
    )
    os.chdir(interface_path.parent)


def _get_interface_path() -> Path:
    return Path(os.getcwd()).joinpath("interfaces")


if __name__ == "__main__":
    app()
