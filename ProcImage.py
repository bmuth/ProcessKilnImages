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
        self.ui.btnGreyScale.clicked.connect (self.OnGreyScaleClicked)
        self.ui.btnHistogram.clicked.connect (self.OnHistogramClicked)

        # create list of input files
        # --------------------------

        path = os.path.dirname (__file__) + '\\images'
        self.files = []
        for r, d, f in os.walk (path):
            for file in f:
                if ('.png' in file):
                    self.files.append (os.path.join(r, file))
        self.file_index = 0


#       a figure instance to plot on
        self.OrigFigure = plt.figure()
        ax = self.OrigFigure.add_subplot(311)
        ax.set_axis_off()
        # can use self.OrigFigure.clear() to clear 

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.OrigFigure)
        lay = QtWidgets.QVBoxLayout(self.ui.widget)  
        lay.setContentsMargins(0, 0, 0, 0)      
        lay.addWidget(self.canvas)
        # add toolbar
        #self.addToolBar(QtCore.Qt.BottomToolBarArea, NavigationToolbar(self.canvas, self))

        self.show()

    def OnHistogramClicked (self):
        print ("Histogram clicked")
        ax = plt.subplot (312)
        ax.cla()
        image = self.GreyImage

        ar = image.ravel()
        print (len(ar))
        print ("avg={0} std={1} max={2}".format (sum(ar)/len(ar), np.std(ar), ar.max()))
        ax.hist (image.ravel(), bins=256, range=(0.0, 1.0))
        #ax.set_axis_off()
        self.canvas.draw()

    def OnGreyScaleClicked (self):
        print ("grey scale clicked")
        self.GreyImage = rgb2grey (self.OrigImage)
        ax = plt.subplot (313)
        ax.cla()

        # plot data
        ax.imshow (self.GreyImage, cmap=plt.cm.gray)
        ax.set_axis_off()

        # refresh canvas
        self.canvas.draw()

    def OnNextClicked (self):
        print ("next clicked")
        # self.Plot()
        if (self.file_index > len(self.files)):
            return
        self.OrigImage = mpimg.imread (self.files[self.file_index])
        ax = plt.subplot (311)
        ax.cla()

        # plot data
        ax.imshow (self.OrigImage)
        ax.set_axis_off()

        # refresh canvas
        self.canvas.draw()

        self.file_index += 1

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
        if (self.file_index <= 0):
            return
        self.file_index -= 1
        pixmap = QtGui.QPixmap(self.files[self.file_index])
        OrigPixmap = pixmap.scaled(self.ui.labOriginal.size(), QtCore.Qt.KeepAspectRatio)
        self.ui.labOriginal.setPixmap (OrigPixmap)
 
# define greyscale conversion routine
# -----------------------------------

def rgb2grey(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

app = QtWidgets.QApplication(sys.argv)
app.setStyle ('Fusion') 
dlg = myDialog()
dlg.show()
 
sys.exit(app.exec())