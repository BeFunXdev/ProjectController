from src.console.ConsolePrint import Console
from src.types.CommandTypes import Command, ExecuteCommand


class CommandParser:

    def __init__(self, args):
        self.args = self._parse(args)
        self.commands: {str: Command} = {}
        self.global_options = []

    def add_command(self, commands):
        if type(commands) is list:
            for command in commands:
                self.commands[command.command] = command
        else:
            self.commands[commands.command] = commands

    def add_option(self, options):
        if type(options) is list:
            for option in options:
                self.global_options.append(option)
        else:
            self.global_options.append(options)

    def execute(self):
        if self._validate(self.args):
            return

        command = self._get_command(self.args)

        command.function(command.arguments, command.options)

    def print_help(self):
        Console.print_doc(self.commands, self.global_options)

    @staticmethod
    def _parse(args):
        global_options = []
        command_options = []
        command = None
        arguments = []

        for arg in args:
            if arg.find('-') > 0:
                if command:
                    command_options.append(arg)
                else:
                    global_options.append(arg)
            elif not command:
                command = arg
            else:
                arguments.append(arg)

        return {'global_options': global_options, 'command': command,
                'arguments': arguments, 'command_options': command_options}

    def _validate(self, args):
        error = False
        command = self.commands[args['command']]

        if not command:
            Console.error('Not found command')
            error = True
        elif len(command.arguments) > len(args['arguments']):
            Console.error('There are fewer arguments than expected')
            error = True
        elif len(command.arguments) < len(args['arguments']):
            Console.error('There are more arguments than expected')
            error = True

        for arg in args['global_options']:
            if not (arg in self.global_options):
                Console.error('There are no such options')
                error = True

        for arg in args['command_options']:
            if not (arg in self.global_options):
                Console.error('There are no such options')
                error = True

        return error

    def _get_command(self, data):
        execute_command: ExecuteCommand = ExecuteCommand()

        com = self.commands[data['command']]

        if com.command == data['command']:
            execute_command.function = com.function

            counter = 0
            for arg_name in com.arguments:
                execute_command.arguments[arg_name] = data['arguments'][counter]
                counter += 1

            for option_name in com.options:
                if option_name in data['options']:
                    execute_command.options[option_name] = True
                else:
                    execute_command.options[option_name] = False

        return execute_command
