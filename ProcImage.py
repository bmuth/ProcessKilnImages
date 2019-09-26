import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from ProcessKilnImagesDlg import Ui_Dialog  # importing our generated file
import sys
import os 
import random

import matplotlib
matplotlib.use('QT5Agg')

#import matplotlib.pylab as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
#from skimage import feature
#from scipy import ndimage
from matplotlib.patches import Rectangle

class myDialog (QtWidgets.QDialog):
 
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.btnNext.clicked.connect (self.OnNextClicked)
        self.ui.btnPrevious.clicked.connect (self.OnPreviousClicked)


#       a figure instance to plot on
        self.OrigFigure = plt.figure()
        # can use self.OrigFigure.clear() to clear 

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.OrigFigure)
        lay = QtWidgets.QVBoxLayout(self.ui.widgetOriginal)  
        lay.setContentsMargins(0, 0, 0, 0)      
        lay.addWidget(self.canvas)
        # add toolbar
        #self.addToolBar(QtCore.Qt.BottomToolBarArea, NavigationToolbar(self.canvas, self))

        self.show()

    def OnNextClicked (self):
        print ("next clicked")
        self.Plot()
        # if (file_index > len(files)):
        #     return
        # pixmap = QtGui.QPixmap(files[file_index])
        # OrigPixmap = pixmap.scaled(self.ui.labOriginal.size(), QtCore.Qt.KeepAspectRatio)
        # self.ui.labOriginal.setPixmap (OrigPixmap)
        # file_index += 1

    def Plot(self):
        ''' plot some random stuff '''
        # random data
        data = [random.random() for i in range(10)]

        # instead of ax.hold(False)
        self.OrigFigure.clear()
        # create an axis
        ax = self.OrigFigure.add_subplot(111)

        # plot data
        ax.plot(data, '*-')

        # refresh canvas
        self.canvas.draw()

    def OnPreviousClicked (self):
        print ("previous clicked")
        if (file_index <= 0):
            return
        file_index -= 1
        pixmap = QtGui.QPixmap(files[file_index])
        OrigPixmap = pixmap.scaled(self.ui.labOriginal.size(), QtCore.Qt.KeepAspectRatio)
        self.ui.labOriginal.setPixmap (OrigPixmap)
        file_index += 1

# create list of input files
# --------------------------

path = os.path.dirname (__file__) + '\\images'
files = []
for r, d, f in os.walk (path):
    for file in f:
        if ('.png' in file):
            files.append (os.path.join(r, file))
file_index = 0

app = QtWidgets.QApplication(sys.argv)
app.setStyle ('Fusion') 
dlg = myDialog()
dlg.show()
 
sys.exit(app.exec())