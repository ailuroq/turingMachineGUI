import threading

from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QTextEdit

from PlotCanvas import PlotCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class WidgetPlot(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setLayout(QGridLayout())
        self.canvas = PlotCanvas()
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().addWidget(self.canvas)

    def draw_chart(self):
        t1 = threading.Thread(target=self.canvas.plot)
        t1.start()
