# Benutzung von ode.py

## Installation
Damit das Programm funktioniert muss das folgende installiert sein:
- Python 2 oder 3
- Das Python Package "scipy" (z.B. durch die Anaconda Distribution)
- gnuplot 5 fuer die Visualisierung


Im Programmordner muessen sich die folgenden Dateien/Ordner befinden:
- das Hauptprogramm "ode.py"
- das GnuPlot-Skript "plot.plt" zur Visualisierung
- ein Ordner mit dem Namen "out"

## Ausfuehrung
Wenn Python und GnuPlot in der PATH-Umgebungsvariablen registriert sind (ggf. auf Haken bei der Installation achten), laesst sich das Programm mit dem Befehl

	python ode.py

ausfuehren.
Das Programm sollte abschliessend selber den Befehl

	gnuplot plot.plt

aufrufen, um eine Grafik zu erstellen. Alternativ kann man diesen auch selber ausfuehren, um GnuPlot die Grafik erstellen zu lassen.


Die Output-Daten sowie die Grafik befinden sich im "out"-Ordner.


## Weiteres
Das skript fancyplot.plt kann schönere Plots im PDF Format erstellen.

In der Datei terminalVessel.py versuche ich die Terminal Vessels zu simulieren.
