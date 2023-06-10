import glob
import os


def latest_strong_file(file=None) -> str:
    if file is None:
        file = glob.glob('data/strong*.csv')

    list_of_files: list[str] = file
    latest_file: str = max(list_of_files, key=os.path.getctime)
    return latest_file
