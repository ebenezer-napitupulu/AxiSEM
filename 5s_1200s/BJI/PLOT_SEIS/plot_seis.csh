#!/bin/csh -f

set info = ‘minmax -f0T -I50 -C -H CORRECTED.txt‘
set R = "-R$info[1]/$info[2]/$info[3]/$info[4]"
gmt psbasemap $R -JX9iT/6i -Glightgreen -K -U"Example 21 in Cookbook" -Bs1Y/0WSen -Bpa3Of1o/50WSen:=\$::."RedHat (RHAT) Stock Price Trend since IPO": >! plot_seis.ps
