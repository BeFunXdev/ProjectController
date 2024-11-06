from dataclasses import dataclass, field


@dataclass
class Option:
    alias: str
    name: str
    description: str


@dataclass
class Command:
    alias: str
    description: str
    command: str
    arguments: [str]
    function: any
    options: [Option] = field(default_factory=list)


@dataclass
class ExecuteCommand:
    function: any = None
    arguments: {str: str} = field(default_factory=dict)
    options: {str: bool} = field(default_factory=dict)
