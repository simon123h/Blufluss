
###### CONFIGURATION #####

	## input file
		dataFile = "out/humanP.dat"

	## output terminal
		set terminal pngcairo
		set out 'out/plotP.png'

	## axis labels
		set xlabel ' '
		set ylabel 't [s]'
    set title "Blutdruck P"

	## axis range
		set xrange [-0.5:4.5]
		set yrange [0:*]

	## tics on the axes, background grid, key position
    set ytics nomirror
    set xtics 1 format ""
		# set grid
		# set key bmargin

	## fit log
		set fit logfile "fit.log"
		set fit quiet




##### COMMANDS #####
  set view map
  set label 1 "Arterie" at screen 0.15,0.05
  set label 2 "Vorhof" at screen 0.3,0.05
  set label 3 "Kammer" at screen 0.43,0.05
  set label 4 "Arterie" at screen 0.57,0.05
  set label 5 "Arterie" at screen 0.71,0.05
  plot dataFile matrix using 1:($2/100):3 notitle with image


    dataFile = "out/humanQ.dat"
    set out 'out/plotQ.png'
    set yrange[*:*]
    stats dataFile matrix nooutput
    set yrange[0:*]
    maxrange = (STATS_max > -STATS_min) ? STATS_max : -STATS_min
    set cbrange[-maxrange:maxrange]
    set palette defined (-1 "blue", 0 "white", 1 "red")
    set title "Durchflussrate Q"
    replot
