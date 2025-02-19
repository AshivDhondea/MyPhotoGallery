from typing import List, Union
import os


def check_directory(directory_path: str):
    if not os.path.isdir(directory_path):
        directory_error = f"{directory_path} is not a valid directory path."
        raise NotADirectoryError(directory_error)


def check_file(file_path: str):
    if not os.path.isfile(file_path):
        file_error = f"{file_path} is not a valid file path."
        raise FileNotFoundError(file_error)


def check_file_types_in_directory(directory_path: str, file_extension: Union[str, List[str]]) -> bool:
    if isinstance(file_extension, list):
        file_extension: List[str] = [e.lower() for e in file_extension]
    file_list = [f for f in os.listdir(directory_path) if f.endswith(file_extension)]
    return True if file_list else False

