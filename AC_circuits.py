'''
                _____    _____  _____  _____    _____  _    _  _____  _______  _____
         /\    / ____|  / ____||_   _||  __ \  / ____|| |  | ||_   _||__   __|/ ____|
        /  \  | |      | |       | |  | |__) || |     | |  | |  | |     | |  | (___
       / /\ \ | |      | |       | |  |  _  / | |     | |  | |  | |     | |   \___ \
      / ____ \| |____  | |____  _| |_ | | \ \ | |____ | |__| | _| |_    | |   ____) |
     /_/    \_\\_____|  \_____||_____||_|  \_\ \_____| \____/ |_____|   |_|  |_____/


    AC circuits for ParamSchemDraw

    A compilation of AC circutis schematics

    Author: Pedro Martins
    version: 0.1.3

    import matplotlib and make it run headless, otherwise in SchewDraw it will return and error
    when tries to connect to Xserver and $Display environmental variable
    matplotlib.pyplot enables controlling the number of active plots
    
'''
import matplotlib
matplotlib.use('Agg')

# Import numpy
import numpy as np
#Documentation:  https://bitbucket.org/cdelker/schemdraw
import SchemDraw as schem
import SchemDraw.elements as e

# Import library to parametrize the used of SchemDraw
from resistor import *
from vSource import *
from iSource import *

# Folder to save the schematics in server
path = "" #'/projects/15860edd-0fa5-4a0a-820c-2bb86b4c0cd5/ENUNCIADOS/IMAGENS/'

# Image extension
extension = '.png'

################################################################################
# Define sinusoidal source
sin_y = (np.linspace(.25,.75,num=25) - 0.5)
sin_x = .2 * np.sin((sin_y-.25)*np.pi*2/.5) + 0.5
sin_path = np.transpose(np.vstack((sin_x,sin_y)))

e.VSOURCE_SIN = {
    'name'  : 'SOURCE_SIN',
    'base'  : e.SOURCE_V,
    'paths' : [sin_path]
    }

e.ISOURCE_SIN = {
    'name'  : 'SOURCE_SIN',
    'base'  : e.SOURCE_I,
    'paths' : [sin_path]
    }

def AC_Thevenin(ekey, label=True, **kwargs):
    VTh = kwargs['VTh']
    RTh = kwargs['RTh']
    VTh.label = '$V_{Th}$'
    RTh.label = '$R_{Th}$'

    d = schem.Drawing()
    d.push()
    VTh.schem = d.add( e.SOURCE_SIN , label=VTh.label)
    RTh.schem = d.add( e.RES, d='right', label= RTh.label )
    d.add(e.DOT_OPEN)
    d.pop()
    d.add( e.GND )
    d.add(e.DOT)
    d.add(e.LINE, l=3)

    d.add( e.DOT_OPEN )


    if label:
        VTh.schem.add_label(VTh.voltageEng, loc='bot')
        RTh.schem.add_label(RTh.resistanceEng, loc='bot')

    d.draw(showplot = False)

    # save schematic (full path + Circuit ID  + parametrize identifier + extension)
    filename = 'DC_002_VTh_' + str(ekey) + extension
    d.save(path + filename)

    matplotlib.pyplot.close('all')

    return filename

def AC_Norton(ekey, label=True, **kwargs):
    Ino = kwargs['Ino']
    Rno = kwargs['Rno']
    Ino.label = '$I_{no}$'
    Rno.label = '$R_{no}$'


    d = schem.Drawing()
    Ino.schem = d.add( e.ISOURCE_SIN , label=Ino.label)
    d.add(e.LINE, l=4, d='right')
    d.push()
    Rno.schem = d.add( e.RES, d='down', label= Rno.label )
    d.push()
    d.add(e.LINE, to=Ino.schem.start)
    d.add( e.GND )
    d.add(e.DOT)
    d.pop()
    d.add(e.LINE, l=1, d='right')
    d.add(e.DOT_OPEN)
    d.pop()


    d.add(e.LINE, l=1)

    d.add( e.DOT_OPEN )


    if label:
        Ino.schem.add_label(Ino.currentEng, loc='bot')
        Rno.schem.add_label(Rno.resistanceEng, loc='bot')

    d.draw(showplot = False)

    # save schematic (full path + Circuit ID  + parametrize identifier + extension)
    filename = 'DC_002_Ino_' + str(ekey) + extension
    d.save(path + filename)

    matplotlib.pyplot.close('all')

    return filename
