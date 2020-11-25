import PyMenu
import sys, os

class Box(object):
    def __init__(self):

        if 'win' in sys.platform:
            PATH = "C:" + os.sep + "users" + os.sep + os.getlogin() + os.sep + "desktop"
        else:
            PATH = os.sep + "home" + os.sep + os.getlogin()

        while True:
            if 'win' in sys.platform:
                os.system('title '+PATH)

            DIR = ['..']
            for i in os.listdir(PATH):
                DIR.append(i)

            BMenu = PyMenu.Menu(True, 1, 3, 5)
            OP = BMenu.Show(DIR)

            if OP == 0:
                CURR = os.path.split(PATH)
                PATH = CURR[0]

            else:
                PATH = PATH + os.sep + DIR[OP]

if __name__ == '__main__':
    Box()