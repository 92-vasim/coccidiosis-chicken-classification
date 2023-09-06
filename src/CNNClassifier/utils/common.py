import os 
from box.exceptions import BoxValueError
import yaml 
from CNNClassifier import logger 
import json 
import joblib 
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


# yaml file reading function 
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ 
    Reads yaml file and returns 

    Args:
        path_to_yaml (str): path like input 

    Raises:
        ValueError: if yaml is empty 
        e: empty file 

    Returns:
        ConfigBox: ConfigBox type 
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e 
    

# Function to create runtime directories
@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """ 
    Creates list of directories

    Args:
        path_to_directories (list): list of path of directories 

        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


# Function to save json output
@ensure_annotations
def save_json(path: Path, data: dict):
    """ 
    Saves json data

    Args:
        path (Path): path to json file 
        data (dict): data to be saved in json file 
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


# Function to load json 
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads json file data 

    Args:
        path (Path): path to json file 

    Returns:
        ConfigBox: data as class attributes instead of dict.
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"Json file loaded successfully from: {path}")

    return ConfigBox(content)


# Function to save binary files 
@ensure_annotations
def save_bin(data: Any, path: Path):
    """ 
    Saves binary file 

    Args:
        data (Any): data to be save as binary 
        path (Path): path to binary file 
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")


# Function to load binary file 
def load_bin(data: Any, path: Path) -> Any: 
    """ 
    Loads binary data

    Args: 
        path (Path): path to binary file 

    Returns:
        Any: object stored in the file 
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded form: {path}")

    return data 


# Function to get size of file 
@ensure_annotations
def get_size(path: Path) -> str:
    """ 
    Gets size in kb 

    Args: 
        path (Path): path of the file 

    Returns:
        str: size in kb 
    """

    size_in_kb = round(os.path.getsize(path)/1024)

    return f"~{size_in_kb} kb"


# Function to decode image
def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, "wb") as f:
        f.write(imgdata)
        f.close()


# Function to encode image 
def encodeImage(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
    

import shutil
import os 


class DocumentSearch:
    def __init__(self):
        self.document_search = None


def save_file(doc):

    data_folder = "temporary"

    if not os.path.exists(data_folder):
        os.mkdir(data_folder)

    # Specify the path for the destination file
    destination_file = os.path.join(data_folder+"/", doc.filename)


    with open(destination_file, "wb") as f:
        shutil.copyfileobj(doc.file, f)

    return destination_file


def delete_files_in_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    file_list = os.listdir(folder_path)
    if len(file_list) == 0:
        print(f"The folder '{folder_path}' is empty.")
    else:
        for file_name in file_list:
            file_path = os.path.join(folder_path, file_name)
            os.remove(file_path)
        print(f"All files in the folder '{folder_path}' have been deleted.")

if __name__ == "__main__":
    data_folder = "./temporary"
    delete_files_in_folder(data_folder)