from abc import ABC, abstractmethod
from datetime import date
import animal

class Hamster(animal):
    def __init__(self, id: int, nick: str, birthd: date, commands: set):
        self.id: int = id
        self.type: str = 'hamster'
        self.nick: str = nick
        self.birthd: date = birthd
        self.commands: str = commands