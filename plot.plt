
###### CONFIGURATION #####

	## input file
		dataFile = "out/humanP.dat"

	## output terminal
		set terminal pngcairo
		set out 'out/plotP.png'

	## axis labels
		set xlabel ' '
		set ylabel 't [s]'
    set title "Blutdruck P [kPa]"

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

  # labels
  if (!exist("labels")) labels = ""
  numberOfLabels = 0.0
  do for [l in labels] {numberOfLabels = numberOfLabels + 1.0}
  i = 0
  do for [l in labels] {
    set label i+1 "".l at graph 0.02+(1/numberOfLabels)*i, screen 0.05
    i = i + 1
  }
  plot dataFile matrix using 1:($2/100):($3/1000) notitle with image


  dataFile = "out/humanQ.dat"
  set out 'out/plotQ.png'
  set yrange[*:*]
  stats dataFile matrix nooutput
  set yrange[0:*]
  maxrange = (STATS_max > -STATS_min) ? STATS_max : -STATS_min
  set cbrange[-maxrange*1000:maxrange*1000]
  set palette defined (-1 "blue", 0 "white", 1 "red")
  set title "Durchflussrate Q [mm/s]"
  # set ylabel ''
  # set format y ''
  # set ytics
  plot dataFile matrix using 1:($2/100):($3*1000) notitle with image
