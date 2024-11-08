import json
import os

from src.constaints.ConfigFiles import ConfigFiles
from src.constaints.Derictiories import Path


class ConfigChange:

    def __init__(self):
        self._is_dir_and_create()

    def add_project(self, path: str, name: str):
        data_path = Path.CONFIG + ConfigFiles.PROJECTS

        data = self.json_reader(data_path)

        data[name] = path

        self.json_write(Path.CONFIG + '/' + ConfigFiles.PROJECTS, data)

    def get_project(self, project_name: str):
        data_path = Path.CONFIG + '\\' + ConfigFiles.PROJECTS
        print(self.json_reader(data_path))
        return self.json_reader(data_path)[project_name]

    def add_pattern(self, pattern_name: str, sub_patterns: [str]):

        # TODO: Доделать функцию добавления патернов
        data_path = Path.CONFIG + ConfigFiles.PATTERNS

        data = self.json_reader(data_path)

        data[pattern_name] = {
            'path': Path.PATTERNS + f'/{pattern_name}',
            'sub_pattern': sub_patterns
        }

    def get_patterns(self, pattern_name: str = ''):
        data = self.json_reader(Path.CONFIG + '/' + ConfigFiles.PATTERNS)
        print(Path.CONFIG + '/' + ConfigFiles.PATTERNS)
        print(data)

        return data if pattern_name == '' else data[pattern_name]

    def json_reader(self, path: str):
        if os.path.isfile(path):
            with open(path, "r") as fh:
                return json.load(fh)
        else:
            return {}

    def json_write(self, path: str, data: any):
        with open(path, "w") as fh:
            json.dump(data, fh)

    def _is_dir_and_create(self, path=Path.CONFIG):
        if not os.path.isdir(path):
            os.makedirs(path)
