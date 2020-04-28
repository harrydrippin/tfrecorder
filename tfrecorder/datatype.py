import enum
import json
from typing import Dict, List, NamedTuple, Union


class FeatureType(enum.Enum):
    STRING = "str"
    FLOAT = "float"
    BOOL = "bool"
    INT = "int"
    BYTES = "bytes"


class Column(NamedTuple):
    name: str
    feature_type: FeatureType


def parse_metadata(file_path: str) -> Dict[str, Union[str, List[Column]]]:
    """Parse JSON file by given path and generate a list of metadata."""
    with open(file_path, "r") as f:
        obj = json.load(f)
    obj["columns"] = [Column(column["name"], FeatureType(column["feature_type"])) for column in obj["columns"]]
    return obj
