
###### CONFIGURATION #####

	## input file
		dataFile = "out/ringP.dat"

	## output terminal
		set terminal pngcairo
		set out 'out/plotP.png'

	## axis labels
		set xlabel 'compartment ID'
		set ylabel 't'
    set cblabel 'P'

	## axis range
		set xrange [*:50]
		set yrange [*:*]

	## tics on the axes, background grid, key position
    set ytics nomirror
    set mxtics
    set mytics
		# set grid
		# set key bmargin

	## fit log
		set fit logfile "fit.log"
		set fit quiet



##### COMMANDS #####
  set view map
	splot dataFile matrix using 1:($2/10):3 notitle with image



    dataFile = "out/ringQ.dat"
    set out 'out/plotQ.png'
    set cblabel 'Q'
    replot
