
###### CONFIGURATION #####

	## input file
		dataFile = "out/ringP.dat"

	## output terminal
		set terminal pngcairo
		set out 'out/plotP.png'

	## axis labels
		set xlabel ' '
		set ylabel 't'
    set cblabel 'P'

	## axis range
		set xrange [-0.5:3.5]
		set yrange [0:*]

	## tics on the axes, background grid, key position
    set ytics nomirror
    set mytics
    set xtics 1 format ""
		# set grid
		# set key bmargin

	## fit log
		set fit logfile "fit.log"
		set fit quiet



##### COMMANDS #####
  set view map
  set label 1 "Herz" at -0.2,-1
  set label 2 "Arterie" at 0.8,-1
  set label 3 "Muskel" at 1.8,-1
  set label 4 "Arterie" at 2.8,-1
  plot dataFile matrix using 1:($2/10):3 notitle with image


  dataFile = "out/ringQ.dat"
  set out 'out/plotQ.png'
  set cblabel 'Q'
  replot
