
###### CONFIGURATION #####

	## input file
		dataFile = "out/ringP.dat"

	## output terminal
		set terminal pngcairo
		set out 'out/plot.png'

	## axis labels
		set xlabel 't'
		set ylabel 'P1'

	## axis range
		set xrange [0:10]
		set yrange [*:*]

	## tics on the axes, background grid, key position
    set ytics nomirror
    set mxtics
    set mytics
		# set grid
		# set key bmargin

	## set comma as decimal value separator
		#set decimalsign locale "german"
		#set decimalsign ','

	## fit log
		set fit logfile "fit.log"
		set fit quiet



##### COMMANDS #####
  set view map
	splot dataFile matrix notitle  with image
