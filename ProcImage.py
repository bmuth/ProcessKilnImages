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
from scipy import ndimage
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
        self.ui.leThreshold.editingFinished.connect (self.OnThresholdChanged)
        self.ui.hsbThreshold.valueChanged.connect (self.OnThresholdScrollBarChanged)
        self.ui.leSigma.editingFinished.connect (self.OnSigmaChanged)
        self.ui.hsbSigma.valueChanged.connect (self.OnSigmaScrollBarChanged)
        self.ui.btnApplyMask.clicked.connect (self.OnApplyMaskClicked)
        self.ui.btnFindRegions.clicked.connect (self.OnFindRegionsClicked)

        # create list of input files
        # --------------------------

        path = os.path.dirname (__file__) + '\\images'
        self.files = []
        for r, _, f in os.walk (path):
            for file in f:
                if ('.png' in file):
                    self.files.append (os.path.join(r, file))
        self.file_index = 0


#       a figure instance to plot on
        self.OrigFigure = plt.figure()
        self.ax1 = self.OrigFigure.add_subplot(311)
        self.ax1.set_axis_off()
        self.ax2 = plt.subplot(312)
        self.ax3 = plt.subplot(313)
        self.ax3.set_axis_off ()
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

    def OnFindRegionsClicked (self):
        # label connected regions, and no. of regions
        label_im, nb_labels = ndimage.label(self.MaskImage)
        # locate bounding rectangles of each region
        tup = ndimage.find_objects(label_im)
        # sort from left to right
        tup.sort(key = sortregion)

        self.ax3.imshow (self.GaussianImage)
        lm = list()
        for v in tup:
            t = v[0].start
            b = v[0].stop
            l = v[1].start
            r = v[1].stop
            
            rect = Rectangle((l,t), r - l, b - t, edgecolor='g', facecolor='none')
            self.ax3.gca().add_patch(rect)
            print (t,l, r-l, b-t)
            lm.append(i5[v[0],v[1]])

        self.canvas.draw()
        
    def OnApplyMaskClicked  (self):
        plt.rc('image', cmap='gray')
        self.MaskImage = self.GaussianImage > self.GaussianImage.mean()
        self.ax3.cla()

        # plot data
        self.ax3.imshow (self.MaskImage)
        self.canvas.draw()

    def OnThresholdScrollBarChanged (self):
        self.threshold = self.ui.hsbThreshold.value () / 100.0
        self.ui.leThreshold.setText ("{:3.2f}".format (self.threshold))
        self.OnThresholdChanged ()

    def OnThresholdChanged (self):
        self.threshold = float(self.ui.leThreshold.text())
        print ("OnThresholdChanged: {0}".format (self.threshold))
        self.ui.hsbThreshold.setValue (self.threshold * 100)
        self.ThresholdImage = np.copy (self.GreyImage)
        threshold_indices = self.ThresholdImage < self.threshold
        self.ThresholdImage[threshold_indices] = 0
        self.ax3.cla()

        # plot data
        self.ax3.imshow (self.ThresholdImage, cmap=plt.cm.gray)
        self.canvas.draw()

    def OnSigmaChanged (self):
        self.sigma = int (self.ui.leSigma.text())
        print ("OnSigmaChanged: {0}".format (self.sigma))
        self.ui.hsbSigma.setValue (self.sigma * 10)
        self.GaussianImage = ndimage.gaussian_filter(self.ThresholdImage, sigma=self.sigma)
        self.ax3.cla()

        # plot data
        self.ax3.imshow (self.GaussianImage, cmap=plt.cm.gray)
        self.canvas.draw()
        print ("OnSigmaChanged done")

    def OnSigmaScrollBarChanged (self):
        self.sigma = self.ui.hsbSigma.value () // 10
        self.ui.leSigma.setText ("{:d}".format (self.sigma))
        self.OnSigmaChanged ()


    def OnHistogramClicked (self):
        print ("Histogram clicked")
        self.ax2.cla()
        image = self.GreyImage

        ar = image.ravel()
        print (len(ar))
        print ("avg={0} std={1} max={2}".format (sum(ar)/len(ar), np.std(ar), ar.max()))
        self.ax2.hist (image.ravel(), bins=256, range=(0.0, 1.0))
        self.canvas.draw()

    def OnGreyScaleClicked (self):
        print ("grey scale clicked")
        self.GreyImage = rgb2grey (self.OrigImage)
        self.ax3 = plt.subplot (313)
        self.ax3.cla()

        # plot data
        self.ax3.imshow (self.GreyImage, cmap=plt.cm.gray)
        self.ax3.set_axis_off ()

        # refresh canvas
        self.canvas.draw()

    def OnNextClicked (self):
        print ("next clicked")
        # self.Plot()
        if (self.file_index > len(self.files)):
            return
        self.OrigImage = mpimg.imread (self.files[self.file_index])
        self.ax1.cla()

        # plot data
        self.ax1.imshow (self.OrigImage)
        self.ax1.set_axis_off()

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

        self.OrigImage = mpimg.imread (self.files[self.file_index])
        self.ax1.cla()

        # plot data
        self.ax1.imshow (self.OrigImage)

        # refresh canvas
        self.canvas.draw()

# define greyscale conversion routine
# -----------------------------------

def rgb2grey(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def sortregion(r):
    return (r[1])

app = QtWidgets.QApplication(sys.argv)
app.setStyle ('Fusion') 
dlg = myDialog()
dlg.show()
 
sys.exit(app.exec())