import yaml

config_path = 'app/config.yaml'
def load_yaml(file_path: str):
    """Load a YAML file and return its content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file {file_path}: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
config = load_yaml(config_path)