import typer, os
from typing_extensions import Annotated
from pathlib import Path
from tma_flutter.snippets.sources import flutter, template


app = typer.Typer()


@app.command(name="make")
def make_target(
    feature_name: Annotated[str, typer.Argument()],
    dir_name: Annotated[str, typer.Argument()] = "features",
):
    flutter.create_package(
        package_name=feature_name,
        dir_name=dir_name,
    )


def name(project_name: str) -> str:
    return project_name + "_" + "feature"


def copy_template(feature_name: str):
    feature_path = Path(os.getcwd()).joinpath("features")
    lib_path = feature_path.joinpath("lib")
    test_path = feature_path.joinpath("test")
    template.remove_dir_content(lib_path)
    template.remove_dir_content(test_path)

    template_path = Path(__file__).absolute().parent.joinpath("templates")
    template.copy(
        copy_file_parent_path=template_path.joinpath("lib"),
        file_name="feature.dart",
        to_save_path=lib_path.joinpath(f"{feature_name}.dart"),
    )
    template.copy(
        copy_file_parent_path=template_path.joinpath("test"),
        file_name="feature_test.dart",
        to_save_path=lib_path.joinpath(f"{feature_name}_test.dart"),
        template_variables={
            "feature_snake": feature_name,
        },
    )


if __name__ == "__main__":
    app()
