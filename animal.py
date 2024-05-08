from abc import ABC, abstractmethod
from datetime import date

class Animal(ABC):
    id: int
    type: str
    nick: str
    birthd: date
    commands: set

    def __init__(self, id, type, nick, birthd, commands):
        self.id: int = id
        self.type: str = type
        self.nick: str = nick
        self.birthd: date = birthd
        self.commands: set = commands
