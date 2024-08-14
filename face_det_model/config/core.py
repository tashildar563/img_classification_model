import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root=file.parent, file.parents[1]
sys.path.append(str(root))

from typing import Dict,List
from pydantic import BaseModel
from strictyaml import YAML, load
import face_det_model

PACKAGE_ROOT = Path(face_det_model.__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent
CONFIG_FILE_PATH = PACKAGE_ROOT / "config.yaml"

DATASET_DIR = PACKAGE_ROOT / "datasets"
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"

class AppConfig(BaseModel):
    package_name: str
    training_data_file: str
    pipeline_name: str
    pipeline_save_file: str
    
class ModelConfig(BaseModel):
    model_name: str
    model_save_file: str
    trained_model_dir: str

class Config(BaseModel):
    """Master config object."""

    app_config: AppConfig
    model_config: ModelConfig


def find_config_file() -> Path:
    """Locate the configuration file."""
    
    if CONFIG_FILE_PATH.is_file():
        return CONFIG_FILE_PATH
    
    raise Exception(f"Config not found at {CONFIG_FILE_PATH!r}")


def fetch_config_from_yaml(cfg_path: Path = None) -> YAML:
    """Parse YAML containing the package configuration."""

    if not cfg_path:
        cfg_path = find_config_file()

    if cfg_path:
        with open(cfg_path, "r") as conf_file:
            parsed_config = load(conf_file.read())
            return parsed_config
        
    raise OSError(f"Did not find config file at path: {cfg_path}")


def create_and_validate_config(parsed_config: YAML = None) -> Config:
    """Run validation on config values."""
    if parsed_config is None:
        parsed_config = fetch_config_from_yaml()

    # specify the data attribute from the strictyaml YAML type.
    _config = Config(
        app_config = AppConfig(**parsed_config.data),
        model_config = ModelConfig(**parsed_config.data),
    )

    return _config


config = create_and_validate_config()