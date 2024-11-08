import os

from src.Logger import Logger
from src.configChange.YamlModule import YamlModule
from src.console.CommandParser import CommandParser
from src.constaints.ConfigFiles import ConfigFiles
from src.constaints.Derictiories import Path
from src.services.BaseCommandService import BaseCommandService
from src.types.CommandTypes import Command


class Application:

    def __init__(self, args):
        self.args = args
        self.parser = CommandParser(args)
        self.baseCommandService = BaseCommandService()
        self.yamlModule = YamlModule(BaseCommandService)

    def command_execute(self):

        self.parser.add_command(Command(alias='i', command='init', description='Creates a new project',
                                        arguments=['git_path'], function=self._init))

        self.parser.add_command(Command(alias='s', command='start', description='Start project',
                                        arguments=[], function=self._start))

        # self.parser.add_command(Command(alias='p', command='print', description='Test function',
        #                                 arguments=['selected'], function=self._test))

        if len(self.args) == 0:
            self.parser.print_help()
        else:
            self.parser.execute()
            Logger.print_logs()

    def _init(self, args, options):
        name = args['git_path'].split('/')[-1].split('.')[0]
        path = f'{Path.PROJECTS}/{name}'

        self.is_dir(path)

        self.baseCommandService.init(path, name, args['git_path'])

    def _start(self, args, option):
        config_path = self.baseCommandService.find_file(ConfigFiles.PROJECT_CONFIG_FILE_NAME, os.getcwd())
        config = self.yamlModule.read_project_config(config_path)

    # def _test(self, args, options):
    #     print(Console.input_select(['data1', 'data2', 'data3']))

    def is_dir(self, path=Path.PROJECTS):
        if not os.path.isdir(path):
            os.makedirs(path)
