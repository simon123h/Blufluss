
###### CONFIGURATION #####

	## input file
		dataFile = "out/humanP.dat"

	## output terminal
		set terminal pngcairo
		set out 'out/plotP.png'

	## axis labels
		set xlabel ' '
		set ylabel 't [s]'
    set cblabel 'P'

	## axis range
		set xrange [-0.5:4.5]
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
  set label 1 "Herzvorhof" at -0.55,-0.2
  set label 2 "-kammer" at 0.65,-0.2
  set label 3 "Arterie" at 1.7,-0.2
  set label 4 "Muskel" at 2.7,-0.2
  set label 5 "Vene" at 3.8,-0.2
  plot dataFile matrix using 1:($2/100):3 notitle with image


  dataFile = "out/humanQ.dat"
  set out 'out/plotQ.png'
  set cblabel 'Q'
  replot
