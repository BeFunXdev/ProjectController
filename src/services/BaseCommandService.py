import os

from src.configChange.ConfigChange import ConfigChange
from src.console.ConsolePrint import Console


class BaseCommandService:

    def __init__(self):
        self.configChange = ConfigChange()

    def init(self, path: str, name: str, git_path: str):

        command_start = f'cd {path} && '

        self.configChange.add_project(path, name)
        self.copy_patterns(self.get_pattern(), path)

        self.github_init(command_start, name, git_path)

    def get_pattern(self):
        patterns = self.configChange.get_patterns()
        pattern_names = []
        result = []

        for pattern_data in patterns:
            pattern_names.append(pattern_data['name'])

        pattern_index = Console.input_select(pattern_names, is_index=True)

        if len(patterns[pattern_index]['sub_pattern']) != 0:

            for pattern_name in patterns[pattern_index]['sub_pattern']:
                sub_patterns = []
                for sub_pattern_data in patterns[pattern_index]['sub_pattern'][pattern_name]:
                    sub_patterns.append(sub_pattern_data['name'])

                sub_pattern_index = Console.input_select(sub_patterns, is_index=True)

                result.append(patterns[pattern_index]['sub_pattern'][pattern_name][sub_pattern_index])
        else:
            result.append(patterns[pattern_index])

        return result

    def copy_patterns(self, patterns, path):
        for pattern in patterns:
            self.copy_directory(pattern['name'], pattern['path'], path)

    def copy_directory(self, dir_name: str, dir_source: str, dir_target: str):
        os.system(f'cd {dir_target} && mkdir {dir_name}')
        os.system(f'cd {dir_source} && copy . {dir_target}/{dir_name}')

    def github_init(self, command_start, name, git_path):
        os.system(command_start + f'echo # {name} >> README.md')
        os.system(command_start + 'git init')
        os.system(command_start + 'git add *')
        os.system(command_start + 'git commit -m "first commit"')
        os.system(command_start + 'git branch -M main')
        os.system(command_start + 'git remote add origin ' + git_path)
        os.system(command_start + 'git push -u origin main')
