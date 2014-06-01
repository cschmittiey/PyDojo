from fredx import *
from msvcrt import getch

def fireItUp():
    loops(100,hexagon)
    loops(100,circle)    
    i = 100
    while i <= 200:
        loops(i,triangle)
        i = i+25
    i = 200
    while i <= 300:
        loops(i,hexagon)
        i = i+25
    loops(250,circle)

begin()
if raw_input("Press G when ready") == "g" or "G":
    fireItUp()


