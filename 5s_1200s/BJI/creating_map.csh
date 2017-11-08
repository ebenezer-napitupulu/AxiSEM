#!/bin/csh -f

gmt pscoast -R90/145/-11/6 -JM15c -Ba20g5 -G245/245/200 -S140/235/255 -Df -W0.5 -P -K >> creating_map.ps
#gv creating_map.ps

gs -sDEVICE=x11 creating_map.ps
