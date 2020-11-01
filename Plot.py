import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import  datetime
class Plot:
    style.use('fivethirtyeight')
    fig = None
    ax1 = None
    CH=1

    def startGUI(self,CH):
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1, 1, 1)
        self.CH=CH

    def animate(self,id):
        fn=" "

        try:
            if(self.CH==1):
                fn = "plots/Channel1.txt"
            elif (self.CH==2):
                fn = "plots/Channel2.txt"
            elif (self.CH==3):
                fn = "plots/Channel3.txt"
            graph_data = open(fn, 'r')
            dt=graph_data.read()
            lines = dt.split('\n')
            xs = []
            ys = []
            for line in lines:
                if len(line) > 1:
                    x, y = line.split(',')
                    xs.append(str(x))
                    ys.append(float(y))
            self.ax1.clear()
            self.ax1.plot(xs, ys)
            graph_data.close()
        except:
            print("file not found: "+str(self.CH))


    def startPlot(self):
        ani = animation.FuncAnimation(self.fig, self.animate, interval=1000)
        plt.show()
