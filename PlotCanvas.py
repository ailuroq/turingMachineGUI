import itertools
import random
import threading
import time

from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from MultiTuring import MultiTuring
from Turing import Turing


class PlotCanvas(FigureCanvas):
    def __init__(self):
        figure = plt.figure()
        FigureCanvas.__init__(self, figure)
        self.setParent(None)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.stop = False

    def plot(self):
        self.figure.clf()
        MT = Turing()
        MT.word_len.clear()
        MT.step_count.clear()
        counter = []
        word = '010101010101c101010101010'
        i = 0
        while not self.stop:
            list_of_words = set(itertools.combinations(word, i))
            MT.word_len.append(i)
            i += 1
            for j in list_of_words:
                counter = []
                counter.append(MT.start(''.join(j), None))
            MT.step_count.append(MT.maxCount)
            MT.maxCount = 0
            ax = self.figure.add_subplot(111)
            ax.set_title('PyQt Matplotlib Example')
            ax.plot(MT.word_len, MT.step_count)
            time.sleep(1)
            self.draw()
        return

    def plot2(self):
        self.figure.clf()
        MT = MultiTuring()
        MT.word_len.clear()
        MT.step_count.clear()
        counter = []
        word = '010101010101c101010101010'
        i = 0
        while not self.stop:
            list_of_words = set(itertools.combinations(word, i))
            MT.word_len.append(i)
            i += 1
            for j in list_of_words:
                counter = []
                counter.append(MT.start(''.join(j), None))
            MT.step_count.append(MT.maxCount)
            MT.maxCount = 0
            ax = self.figure.add_subplot(111)
            ax.set_title('PyQt Matplotlib Example')
            ax.plot(MT.word_len, MT.step_count)
            time.sleep(1)
            self.draw()
        return
