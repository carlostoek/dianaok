import pytest
from src.utilities import load_configuration

def test_load_configuration(tmp_path):
    # Crea un archivo de configuración temporal
    config_file = tmp_path / "config.json"
    config_file.write_text('{"key": "value"}')

    config = load_configuration(str(config_file))
    assert config["key"] == "value"