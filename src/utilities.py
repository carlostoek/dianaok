import json

def load_configuration(file_path: str) -> dict:
    # Carga configuraciones desde un archivo JSON
    with open(file_path, 'r') as file:
        return json.load(file)