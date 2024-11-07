import os

import keyboard

from src.constaints.Colors import ConsoleColors


class ConsoleSwitcher:

    def __init__(self, options: [str] = []):
        self.options = options
        self.selected = 0
        self.is_line = False

    def show(self):
        print("\n" * 30)

        if self.is_line:
            print('Choose an option: ', f'{ConsoleColors.UNDERLINE}Yes{ConsoleColors.ENDC}/No' if self.selected == 0 else f'{ConsoleColors.ENDC}Yes/{ConsoleColors.UNDERLINE}No{ConsoleColors.ENDC}')
        else:
            print("Choose an option:")
            for i in range(0, len(self.options)):
                print(
                    "{1} {0}. {3} {0} {2}".format(i, ">" if self.selected == i else " ",
                                                  "<" if self.selected == i else " ",
                                                  self.options[i]))

    def up(self):
        if self.selected == 0:
            return
        os.system('cls')
        self.selected -= 1
        self.show()

    def down(self):
        if self.selected == len(self.options) - 1:
            return

        if self.is_line and self.selected == 1:
            return
        os.system('cls')
        self.selected += 1
        self.show()

    def start(self, is_line: bool = False, is_index: bool = False):
        self.is_line = is_line
        self.show()
        if self.is_line:
            keyboard.add_hotkey('left', self.up, suppress=True)
            keyboard.add_hotkey('right', self.down, suppress=True)
            keyboard.wait('enter', suppress=True)
            os.system('cls')
            return True if self.selected == 0 else False
        else:
            keyboard.add_hotkey('up', self.up, suppress=True)
            keyboard.add_hotkey('down', self.down, suppress=True)
            keyboard.wait('enter', suppress=True)
            os.system('cls')
            return self.selected if is_index else self.options[self.selected]
