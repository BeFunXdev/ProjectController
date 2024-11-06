import os


class Path:
    PROJECTS = os.path.expanduser("~") + "/ProjectSource"
    CONFIG = os.path.expanduser('C:/') + '/ProgramData/ProjectController'
    PATTERNS = CONFIG + '/Patterns'

