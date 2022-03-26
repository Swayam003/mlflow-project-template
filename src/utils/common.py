"The common.py file contains all the functions that are used more than ones and can be reused again & again"
import os
import yaml
import time
import json
import logging
import pandas as pd


# Necessary reusuable functions defined below
def read_yaml(path_to_yaml: str) -> dict:
    "Function to read the contents of the yaml file"

    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    logging.info(f"yaml file: {path_to_yaml} loaded successfully")
    return content

def create_directories(path_to_directories: list) -> None:
    "Function to create directories"

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logging.info(f"created directory at: {path}")


def save_json(path: str, data: dict) -> None:
    "Function to save the json data into a file"

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"json file saved at: {path}")