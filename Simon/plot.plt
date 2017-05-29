
###### CONFIGURATION #####

	## input file
		dataFile = "out/output.dat"

	## output terminal
		set terminal pngcairo
		set out 'out/plot.png'

	## axis labels
		set xlabel 't'
		set ylabel 'P1'
		set y2label 'Q2'

	## axis range
		set xrange [0:10]
		set yrange [0:*]
		set y2range [0:*]

	## tics on the axes, background grid, key position
    set ytics nomirror
    set y2tics nomirror
    set mxtics
    set mytics
    set my2tics
		# set grid
		# set key bmargin

	## set comma as decimal value separator
		#set decimalsign locale "german"
		#set decimalsign ','

	## fit log
		set fit logfile "fit.log"
		set fit quiet



##### COMMANDS #####
	plot	dataFile using 1:2  axes x1y1 title "P1" with lines, \
        dataFile using 1:3  axes x1y2 title "Q2" with lines
