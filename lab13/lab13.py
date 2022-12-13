from guietta import _, Gui
from package.laminat import *

class romont():
    def recalc(gui, *args):
        gui.result = float(gui.num)*2

    gui = Gui( [ 'Enter number' , '__num__' , ['Go'] ],
                [ 'Result ---> ' , 'result'  ,   _    ] )

    gui.events([       _        ,     _     ,  recalc ],
               [       _        ,     _     ,   _     ] )

    gui.run()