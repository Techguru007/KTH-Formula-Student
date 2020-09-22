import matplotlib.pyplot as plt
import numpy as np

class Fungraph():

    def grph_values(self, x_val, y_val):
        self.x = x_val
        self.y = y_val

    
    def draw_graph(self):
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        plt.plot(graph.x_val, graph.y_val, "red", label=("3*pi*exp(-5*sin(2*pi*x))"))
        plt.legend(loc="upper left")
        plt.show()


graph = Fungraph()
graph.x_val = np.linspace(-np.pi, np.pi, 10000)
graph.y_val = 3*np.pi*np.exp(-5*np.sin(2*np.pi*graph.x_val))
graph.draw_graph()
