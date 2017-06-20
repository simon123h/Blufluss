set table "main.pgf-plot.table"; set format "%.5f"
set samples 50.0; plot [x=-4:4] 0.6*(0.1*(x-1)**3 + 0.5*(x-1)**2 - 0.3*(x-1) + 0.5)
