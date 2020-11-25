from io import StringIO
import sys, os

class Menu(object):
    def __init__(self, fullscreen, back, forebox, forefont):
        self.fullscreen = fullscreen
        self.SELECTED = 0

        BackColour = [107, 40, 41, 42, 43, 44, 45, 46]
        ForeColour = [97, 30, 31, 32, 33, 34, 35, 36]

        self.BACK = BackColour[back]
        self.FOREBOX = ForeColour[forebox]
        self.FOREFONT = ForeColour[forefont]

        '''
        Colour list:
        0 - WHITE
        1 - BLACK
        2 - RED
        3 - GREEN
        4 - YELLOW
        5 - BLUE
        6 - MAGENTA
        7 - CYAN
        '''

    def Show(self, items):
        while True:
            X = os.get_terminal_size()[0]
            Y = os.get_terminal_size()[1]

            # Generate the screen buffer
            MENU = StringIO()
            self.MENU = MENU

            if self.fullscreen == True:
                if len(items) < Y-4:
                    Visible = [0, Y-4]

                elif len(items) > Y-4 and self.SELECTED < Y-4:
                    Visible = [self.SELECTED - (Y-4), (Y-4)]

                else:
                    Visible = [self.SELECTED - (Y-5), self.SELECTED]

                self.MENU.write(f"\033[{self.FOREBOX};{self.BACK}m")
                self.MENU.write("╔" + "═" * (X-2) + "╗")

                for i in items:
                    ID = items.index(i)

                    if  ID == self.SELECTED:
                        self.MENU.write("║" + f"\033[{self.FOREFONT};{self.BACK};7m{i}" + " " * (X - 2 - len(i)) + "\033[0;0m" + f"\033[{self.FOREBOX};{self.BACK}m║")

                    elif ID >= Visible[0] and ID < Visible[1]:
                        self.MENU.write("║" + f"\033[{self.FOREFONT};{self.BACK}m{i}" + " " * (X - 2 - len(i)) + f"\033[{self.FOREBOX};{self.BACK}m║")

                    elif ID > Visible [1]:
                        self.MENU.write("║" + f"\033[{self.FOREFONT};{self.BACK}m..." + " " * (X - 5) + f"\033[{self.FOREBOX};{self.BACK}m║")
                        break

                self.MENU.write("╚" + "═" * (X-2) +"╝")

            elif self.fullscreen == False:
                SIZE = 0

                for i in items:
                    if len(i) > SIZE:
                        SIZE = len(i)

                self.MENU.write(f"\033[1;{self.FOREBOX};{self.BACK}m")
                self.MENU.write("╔" + "═" * SIZE + "╗" + "\n")

                for i in items:
                    if items.index(i) == self.SELECTED:
                        self.MENU.write("║" + f"\033[1;{self.FOREFONT};{self.BACK};7m{i}" + " " * (SIZE - len(i)) + "\033[0;0m" + f"\033[1;{self.FOREBOX};{self.BACK}m║" + "\n")

                    else:
                        self.MENU.write("║" + f"\033[1;{self.FOREFONT};{self.BACK}m{i}" + " " * (SIZE - len(i)) + f"\033[1;{self.FOREBOX};{self.BACK}m║" + "\n")

                self.MENU.write("╚" + "═" * SIZE + "╝")

            self.Update()
            key = self.Lectorem()

            if ord(key) == 72:
                if self.SELECTED > 0:
                    self.SELECTED -= 1

            elif ord(key) == 80:
                if self.SELECTED < len(items) - 1:
                    self.SELECTED += 1

            elif ord(key) == 13:
                return self.SELECTED


    def Lectorem(self):
        # Read the key pressed by the user

        try:
            import msvcrt

            READ = msvcrt.getch()
            return READ

        except ImportError:
            input("Il programma non è compatibile con il tuo sistema operativo!")
            exit()


    def Update(self):
        # Update the screen and it’s Buffer

        if "win" in sys.platform:
            os.system("cls")

            print(self.MENU.getvalue())
            self.MENU.close()

        else:
            os.system("clear")

            print(self.MENU.getvalue())
            self.MENU.close()