from src.core.converter import AppConverter


class GUIConsole:

    INFO = "info"
    COMMANDS = "commands"
    FORMAT = "format"
    PATH = "path"
    EXIT = "exit"

    def __init__(self) -> None:

        self.converter = AppConverter()

        self.is_run = True

        self.commands = {

            self.INFO: lambda: self.info_current_format(),
            self.COMMANDS: lambda: self.info_commands(),
            self.FORMAT: lambda: self.info_format(),
            self.PATH: "",
            self.EXIT: ""
        }

    def info_hello(self):

        print("\n            КОНВЕРТЕР ИЗОБРАЖЕНИЙ           \n")

    def info_format(self):

        print("Доступны следующие форматы для конвертации:\n")
        print("-", ("\n- ".join(self.converter.get_formats())), "\n")

    def info_current_format(self):

        print("Текущий формат: ", self.converter.get_converter_format(), "\n")

    def info_commands(self):

        print("\n              КОММАНДЫ\n\n"
              f"{self.COMMANDS} - инфо о доступных командах\n"
              f"{self.FORMAT} - сменить формат конвертации\n"
              f"{self.PATH} - выбрать путь файла\n"
              f"{self.EXIT} - закрыть программу\n")

    def check_command(self, command) -> bool:

        if command in list(self.commands.keys()):
            return True

        print("\n          ТАКОЙ КОМАНДЫ НЕТ!")
        self.info_commands()

    def run(self) -> None:

        self.info_hello()
        self.info_format()
        self.info_current_format()
        self.info_commands()

        while self.is_run:

            command = input("Введите команду >> ")

            if self.check_command(command): self.commands[command]()
