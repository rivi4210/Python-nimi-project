from typing import List
from command import Command


class Input:
    def __init__(self, infile, outfile):
        self.world: Command = Command(Command.WORLD)
        self.start: List[Command] = list()
        self.steps: List[Command] = list()
        self.asserts: List[str] = list()
        self.infile = infile
        self.lines: List[str] = None
        self.at_line: int = 0
        self.outfile = outfile

    def _start(self):
        if self.infile:
            self.lines = self.infile.readlines()
            self.at_line = 0
            self.infile.close()

    def _next_line(self) -> str:
        line: str = None
        if self.lines:
            if self.at_line < len(self.lines):
                line = self.lines[self.at_line]
                self.at_line += 1
        else:
            line = input()
        return line

    def parse_and_store(self):
        self._start()
        line:str = self._next_line()
        command_list: List[Command] = self.start
        parsing_world: bool = False
        asserts_reached: bool = False
        while line:
            line = line.strip()
            if line.startswith('+'):
                # command block reached (e.g.: World, Infrastructure, etc...)
                name = line[1:]
                parsing_world = False
                if name == Command.WORLD:
                    parsing_world = True
                elif name == Command.START:
                    command_list = self.start
                elif name == Command.INPUT:
                    command_list = self.steps
                elif name == Command.ASSERTS:
                    asserts_reached = True
                else:
                    raise KeyError("Unknown Input Command found: " + name)
            else:
                if asserts_reached:
                    self.asserts.append(line)
                elif parsing_world:
                    self.world.data.append(line.split())
                else:
                    command = Input.parse_command(line)
                    command_list.append(command)
            # read next input line
            line = self._next_line()

    @staticmethod
    def parse_command(line: str) -> Command:
        strings = line.split()
        command = Command(strings[0])
        command.arguments.extend(strings[1:])
        return command
