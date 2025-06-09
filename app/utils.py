import yaml

config_path = 'config.yaml'
prompt_path = 'prompt.yaml'
def load_config(file_path: str):
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
    
def load_prompt(file_path: str):
    """Load a prompt from a YAML file."""
    p = load_config(file_path)
    if p:
        return p['prompt']
    else:
        print(f"Prompt not found in {file_path}")
        return None
    
configs = load_config(config_path)
prompts = load_prompt(prompt_path)