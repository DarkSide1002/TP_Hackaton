import os
import shutil
from pathlib import Path


class FileManager:
    def __init__(self, root: str):
        self.root = root

    def create(self, lst: list):
        for c in lst:
            Path(os.path.join(self.root, c)).mkdir(parents=True, exist_ok=True)

    def move(self, old_path: str, c: str) -> str:
        dest = os.path.join(self.root, c)
        name = os.path.basename(old_path)
        new_path = os.path.join(dest, name)
        shutil.copy2(old_path, new_path)
        return new_path