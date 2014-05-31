from fredx import *
begin()
loops(100,hexagon)
loops(100,circle)

i = 100
while i <= 350:
    loops(i,triangle)
    i = i+25
