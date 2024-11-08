import os

from src.Observer import Observer
from src.configChange.ConfigChange import ConfigChange
from src.console.ConsolePrint import Console


class BaseCommandService(Observer):

    def __init__(self):
        self.configChange = ConfigChange()

    def init(self, path: str, name: str, git_path: str):

        command_start = f'cd {path} && '

        self.configChange.add_project(path, name)
        self.copy_patterns(self.get_pattern(), path)

        # self.github_init(command_start, name, git_path)

    def start(self, project_options: dict):
        for part_name in project_options:
            os.system(f'cd {part_name} && {project_options[part_name]["start_command"]}')

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

                result.append({'name': pattern_name,
                               'path': patterns[pattern_index]['sub_pattern'][pattern_name][sub_pattern_index]['path'],
                               'default_value': patterns[pattern_index]['sub_pattern'][pattern_name][sub_pattern_index]['default_value']})
        else:
            result.append(patterns[pattern_index])

        return result

    def copy_patterns(self, patterns, path):
        for pattern in patterns:
            self.event({'name': pattern['name'], 'value': pattern['default_value'], 'path': path})
            self.copy_directory(pattern['name'], pattern['path'], path)

    def copy_directory(self, dir_name: str, dir_source: str, dir_target: str):
        os.system(f'cd {dir_target} && mkdir {dir_name}')
        print(f'copy -r {dir_source}\\* {dir_target}/{dir_name}/'.replace('/', '\\'))
        os.system(f'copy {dir_source}/* {dir_target}/{dir_name}/'.replace('/', '\\'))

    def find_file(self, file_name: str, cur_dir: str):
        while True:
            file_list = os.listdir(cur_dir)
            parent_dir = os.path.dirname(cur_dir)
            if file_name in file_list:
                print("File Exists in: ", cur_dir)
                return f'{cur_dir}/{file_name}'
            else:
                if cur_dir == parent_dir:  # if dir is root dir
                    print("File not found")
                    return
                else:
                    cur_dir = parent_dir

    def github_init(self, command_start, name, git_path):
        os.system(command_start + f'echo # {name} >> README.md')
        os.system(command_start + 'git init')
        os.system(command_start + 'git add *')
        os.system(command_start + 'git commit -m "first commit"')
        os.system(command_start + 'git branch -M main')
        os.system(command_start + 'git remote add origin ' + git_path)
        os.system(command_start + 'git push -u origin main')
