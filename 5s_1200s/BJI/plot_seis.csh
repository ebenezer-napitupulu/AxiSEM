#!/bin/csh


gmt pscoast -Rg90/145/-11/6 -Jx0.14i -Bg10 -Dc -A4000 \
-G255/100/10 -S0/255/255 -W0.5p -X1 -Y15 -P -K > plot_seis.ps

#psxy kotak.txt -Rg -Jx -W1,255/0/0 -P -O -Am -K \
#
<< END >> plot_seis.ps
#END

#pstext disini akan mengeplot teks pada peta
gmt pstext -Rg -JX8i/11i -P -O -N -K << END >> plot_seis.ps
140 -48.0 8 0 1 1 Plotting Wiggle on Map
140 -93.0 7 0 1 1 Longitude
0.09 -75.0 7 90 1 1 Latitude
#mengeplot title pada peta
120 -30.0 14 0 1 1 Generating Mapping Tools
140 -33 12 0 1 1 Plot Timeseries
#mengeplot catatan diatas
0 -8.0 12 0 1 1 Tugas Pemograman Komputer Geofisika
0 -5.0 8 0 1 1 ebenezer napitupulu |13/349838/PA/15584
END
#psxy disini akan mengeplot seismogram pada peta dengan mengontrol seismogram dari koordinat
-X dan -Y.
gmt psxy CORRECTED.txt -JX1i/0.5i -R0/1000/-540000/-530000 -W0.5,0/0/255 -P \
-B5000g10000f50/50000g120000nSeW -X11.6 -Y2.0 -O -Am -K\
<< END \
>> plot_seis.ps
END
#pstext disini akan mengeplot label pada seismogram
gmt pstext -R0/8/0/11 -JX8i/11i -P -O -N << END >> plot_seis.ps
0.075 0.6 7 0 1 1 Wave Package
0.25 -0.1 6 0 1 1 Time (sec)
-0.09 0.02 6 90 1 1 Amplitude
END
gs -sDEVICE=x11 plot_seis.ps
