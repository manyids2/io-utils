import json
import yaml
from pathlib import Path
from typing import Any, Dict


def load_json(path: Path) -> Dict[str, Any]:
    with path.open("r") as f:
        data = json.load(f)
    return data


def save_json(
    data: Dict[str, Any],
    path: Path,
    # handle_types: Dict[str, Callable], # TODO
) -> None:
    path.write_text(json.dumps(data))


def load_yaml(path: Path) -> Dict[str, Any]:
    with path.open("r") as f:
        data = yaml.load(f, yaml.SafeLoader)
    return data


def save_yaml(
    data: Dict[str, Any],
    path: Path,
    # handle_types: Dict[str, Callable], # TODO
) -> None:
    path.write_text(yaml.dump(data))
