import os

import yaml

from src.Observer import Consumer
from src.constaints.ConfigFiles import ConfigFiles


class YamlModule(Consumer):

    def add_pattern(self, part_name: str, data: dict, path: str, project_data: dict):
        config = self.read(path)

        config['project'] = project_data

        config[part_name] = data

        self.write(path, config)

    def read_project_config(self, path):
        return self.read(path)

    def read(self, path):
        file_path = path + '\\' + ConfigFiles.PROJECT_CONFIG_FILE_NAME

        if os.path.isfile(file_path):
            with open(file_path, 'r') as fh:
                read_data = yaml.load(fh, Loader=yaml.FullLoader)
        else:
            return {}

        return read_data

    def write(self, path, data):
        file_path = path + '/' + ConfigFiles.PROJECT_CONFIG_FILE_NAME
        with open(file_path, 'w') as fh:
            yaml.dump(data, fh)

    def action(self, data: any):
        self.add_pattern(data['name'], data['value'], data['path'], data['project_data'])
