from guietta import Gui, _, ___, III, HS, VS

from package.laminat import *

class remont():
    def recalc(gui, *args):
        gui.result = float(gui.num)*2
        
    gui = Gui(
  [ 'Big label' ,    ___    ,       ___       ,  VS('slider1') ],
  [     III     ,    III    ,       III       ,       III      ],
  [     III     ,    III    ,       III       ,       III      ],
  [      _      , 'a label' , 'another label' ,        _       ],
  [HS('slider2'),    ___    ,       ___       ,        _       ]
)
    gui2 = Gui([G('my group')])

    gui.mygroup = another_gui

    gui.run()