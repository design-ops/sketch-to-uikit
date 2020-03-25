from os import PathLike, path, rename
from zipfile import ZipFile
from shutil import rmtree

from utils import create_dir

def extract_file_with_name(zip_file: str, name: str, extract_to: PathLike):
    archive = ZipFile(zip_file)
    tmp_folder = path.join(extract_to, "tmp")
    create_dir(tmp_folder)
    # archive.extract(name, extract_to)
    exported = archive.extract(name,tmp_folder)
    basename = path.basename(exported)
    rename(exported, path.join(extract_to, basename))
    rmtree(tmp_folder)

