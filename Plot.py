import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
class Plot:
    style.use('fivethirtyeight')
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    id=1
    def _init_(self, id):
        self.id=id

    def animate(self):
        graph_data = open('Channel'+self.id+'.txt', 'r').read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:
            if len(line) > 1:
                x, y = line.split(',')
                xs.append(float(x))
                ys.append(float(y))
        self.ax1.clear()
        self.ax1.plot(xs, ys)
    def startPlot(self):
        ani = animation.FuncAnimation(self.fig, self.animate, interval=1000)
        plt.show()

    def savePlot(self):
        fn = "PlotChannel"+self.id+" "+datetime.datetime.now()+".txt"
        f = open(fn, "w")
        with open("Channel"+self.id+".txt", 'r') as f:
            for line in f:
                f.write(line)
        f.close()

