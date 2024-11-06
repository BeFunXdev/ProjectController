from time import time

from src.console.ConsoleSwitcher import ConsoleSwitcher
from src.constaints.Colors import ConsoleColors
from src.types.CommandTypes import Command


class Console:

    @staticmethod
    def print(data):
        print(data)

    @staticmethod
    def log(data):
        print(ConsoleColors.WARNING + str(time()) + ' ' + data)

    @staticmethod
    def print_doc(commands: [Command], options, command=None):
        if command:
            print(f'pc {command} [arguments] [command_options]\n')
            print('List of subcommands')
        else:
            print(f'pc [global_options] command [arguments] [command_options]\n')
            print('List of commands')

        for com in commands:
            print(f'{commands[com].alias} {commands[com].command} {commands[com].description}')

        if len(options):
            print('List of options')

            for option in options:
                print(f'{option.alias} {option.name} {option.description}')

    @staticmethod
    def error(error):
        print(ConsoleColors.FAIL + str(time()) + ' ' + error)

    @staticmethod
    def input_select(input_select: [str], is_index: bool = False):
        menu = ConsoleSwitcher(input_select)

        return menu.start(is_index=is_index)

    @staticmethod
    def input_string():
        menu = ConsoleSwitcher()

        return menu.start()
