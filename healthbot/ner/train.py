from dataclasses import dataclass
import yaml
from pathlib import Path
import pandas as pd

from pipeline import NERPipeline

def load_config(path: str = "ner/config.yaml"):
    cfg_dict = yaml.safe_load(Path(path).read_text())
    return cfg_dict

dataset_config = load_config()['dataset']
print(dataset_config)

def get_data(path):
    return pd.read_csv(
            path,
            sep="\s+",
            names=["token","label"],
            header=None,
            engine="python",
            skip_blank_lines=True
    )

train_dataset = get_data(dataset_config['train_file'])
eval_dataset = get_data(dataset_config['dev_file'])

print(eval_dataset.head(30))

# ner_pipeline = NERPipeline()
# ner_pipeline()
