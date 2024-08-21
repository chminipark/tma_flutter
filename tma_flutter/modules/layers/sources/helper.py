import os
from pathlib import Path
from tma_flutter.modules.targets.sources import test, interface
from tma_flutter.modules.targets.sources.view import view
from tma_flutter.modules.targets.sources.example import example
from tma_flutter.modules.targets.sources.feature import feature


def make_domain_module(
    project_name: str,
    layer_name: str,
):
    current_path = Path(os.getcwd())
    module_path = current_path.joinpath(layer_name).joinpath(project_name)
    Path(module_path).mkdir(parents=True, exist_ok=True)
    os.chdir(module_path)

    feature_name = feature.name(project_name)
    test_name = test.name(project_name)
    interface_name = interface.name(project_name)

    feature.make_target(feature_name)
    test.make_target(test_name)
    interface.make_target(interface_name)


def make_presentation_module(project_name: str):
    current_path = Path(os.getcwd())
    module_path = current_path.joinpath("presentation").joinpath(project_name)
    Path(module_path).mkdir(parents=True, exist_ok=True)
    os.chdir(module_path)

    example_name = example.name(project_name)
    view_name = view.name(project_name)
    feature_name = feature.name(project_name)
    test_name = test.name(project_name)
    interface_name = interface.name(project_name)

    example.make_target(example_name=example_name)
    view.make_target(view_name)
    feature.make_target(feature_name)
    # test.make_target(test_name)
    # interface.make_target(interface_name)

    example.copy_template(
        example_name=example_name,
        view_name=view_name,
    )
    view.copy_template(
        view_name=view_name,
        feature_name=feature_name,
    )

    example.add_view_dependency(view_name=view_name)
    view.add_feature_dependency(feature_name=feature_name)
