
###### CONFIGURATION #####

	## input file
		dataFile = "out/output.dat"

	## output terminal
		set terminal pdf
		set out 'out/plot.pdf'

	## axis labels
		set xlabel 't [a.u.]'
		set ylabel 'P1 [a.u.]'
		set y2label 'Q2 [a.u.]'

	## axis range
		set xrange [*:*]
		set yrange [*:*]
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
	plot	dataFile using 1:2  axes x1y1 title "P1" with lines lw 3, \
        dataFile using 1:3  axes x1y2 title "Q2" with lines lw 3
