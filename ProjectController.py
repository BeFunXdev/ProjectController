import sys

from src.Application import Application

app = Application(sys.argv[1:])

app.is_dir()

if __name__ == '__main__':
    app.command_execute()
