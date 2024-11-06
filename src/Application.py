import os

from src.console.CommandParser import CommandParser
from src.constaints.Derictiories import Path
from src.services.BaseCommandService import BaseCommandService
from src.types.CommandTypes import Command


class Application:

    def __init__(self, args):
        self.args = args
        self.parser = CommandParser(args)
        self.baseCommandService = BaseCommandService()

    def command_execute(self):

        self.parser.add_command(Command(alias='i', command='init', description='Creates a new project',
                                        arguments=['git_path'], function=self._init))

        # self.parser.add_command(Command(alias='p', command='print', description='Test function',
        #                                 arguments=['selected'], function=self._test))

        if len(self.args) == 0:
            self.parser.print_help()
        else:
            self.parser.execute()

    def _init(self, args, options):
        name = args['git_path'].split('/')[-1].split('.')[0]
        path = f'{Path.PROJECTS}/{name}'

        self.is_dir(path)

        self.baseCommandService.init(path, name, args['git_path'])

    # def _test(self, args, options):
    #     print(Console.input_select(['data1', 'data2', 'data3']))

    def is_dir(self, path=Path.PROJECTS):
        if not os.path.isdir(path):
            os.makedirs(path)
