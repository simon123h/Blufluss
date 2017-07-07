
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
		set xrange [0:*]
		set yrange [0:*]
		set y2range [*:*]

	## tics on the axes, background grid, key position
    set ytics nomirror
    set y2tics nomirror
    set mxtics
    set mytics
    set my2tics
		# set grid
		# set key bmargin



##### COMMANDS #####
	plot	dataFile using 1:2  axes x1y1 title "P1" with lines, \
        dataFile using 1:3  axes x1y2 title "Q2" with lines
