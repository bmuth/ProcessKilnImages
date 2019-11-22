import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from ProcessKilnImagesDlg import Ui_Dialog  # importing our generated file
import sys
import os 
import random

import matplotlib
matplotlib.use('QT5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvas 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from skimage import io
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
        self.ui.btnSplit.clicked.connect (self.OnSplitClicked)
        self.ui.btnSave.clicked.connect (self.OnSaveClicked)

        # create list of input files
        # --------------------------

        #path = os.getcwd() + '\\images'
        path = os.path.join (os.getcwd(), 'data\\Nov 04 2019')
        print (path)
        self.files = []
        for f in os.listdir (path):
            if ('.png' in f):
                self.files.append (os.path.join(path, f))
        self.file_index = 0
        self.files.sort ()

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

        if (len(self.files) == 0):
            self.Msg ("No files are loaded!")

    def AutoProcess (self):
        self.OnGreyScaleClicked ()
        self.OnHistogramClicked ()
        self.OnThresholdChanged ()
        self.OnSigmaChanged ()
        self.OnApplyMaskClicked ()
        self.OnFindRegionsClicked ()
        self.ui.leDigits.setText ("")
        self.ui.leDigits.setFocus ()

    def OnSaveClicked (self):
        if (len(self.digits) != len(self.ImgLst)):
            self.Msg ("SAVE ABORTED: no. digits don't match no. images")
            return

        i = 0

        for img in self.ImgLst:
            c = str(self.digits[i])
            if (c == "."):
                c = "-"
            path = os.path.join (os.getcwd(), 'data\\images\\') + c
            if (not os.path.isdir (path)):
                os.mkdir (path)
            try:
                filename = os.path.join (path, os.path.splitext (self.Filename)[0])
                filename += "_" + "_" * i
                filename += c
                filename += ".png"
                if (os.path.isfile (filename)):
                    self.Msg ("file {0} overwritten.".format (filename))
                io.imsave (filename, img)
            except:
                self.Msg ("Failed to save {0}".format (filename))
            finally:
                i += 1

    def OnSplitClicked (self):
        print ("OnSplitClicked clicked")
        no_images = len(self.ImgLst)
        if (no_images > 5):
            self.Msg ("Two many islands found. {0}".format (no_images))
            return

        # get a character for each image

        self.digits = list(self.ui.leDigits.text ())
        if (no_images != len(self.digits)):
            self.Msg ("No images {0} must match no digits {1}".format(no_images, len(self.digits)))
            return


        self.ax3 = None
        no = 0
        NewImgLst = list()
        for img in self.ImgLst:
            NewImgLst.append (self.Resize(img))
        self.ImgLst = NewImgLst

        for img in self.ImgLst:
            ax = plt.subplot (3,5,11 + no)
            #ax.set_axis_off()
            plt.setp(ax.get_yticklabels(), visible=False)
            plt.setp(ax.get_xticklabels(), visible=False)
            ax.xaxis.set_ticks_position('none') 
            ax.yaxis.set_ticks_position('none')
            plt.xlabel (str(self.digits[no]))
            if (type(img) is not None) :
                ax.imshow (img)
            no += 1

        self.canvas.draw()

    def Resize (self, img):
        target_width = int (self.ui.leWidth.text())
        target_height = int (self.ui.leHeight.text ())
        left = (target_width - img.shape[1]) // 2
        right = (target_width - img.shape[1] + 1) // 2
        top = (target_height - img.shape[0]) // 2
        bottom = (target_height - img.shape[0] + 1) // 2
        if (target_width < img.shape[1]) :
            self.Msg ("The image width is {0}. Specify a wider width".format (img.shape[1]))
            return None
        if (target_height < img.shape[0]) :
            self.Msg ("The image height is {0}. Specify a higher height".format (img.shape[0]))
            return None
        if (left + right + img.shape[1] != target_width):
            self.Msg ("width {0} + padding {1} doesn't match total width {2}".format (img.shape[1], left + right, total_width))
            return None
        if (top + bottom + img.shape[0] != target_height):
            self.Msg ("height {0} + padding {1} doesn't match total height {2}".format (img.shape[0], top+bottom, total_height))
            return None
        img = np.lib.pad (img, ((top, bottom), (left, right)), 'constant', constant_values = 0)
        return img

    def OnFindRegionsClicked (self):
        # label connected regions, and no. of regions
        label_im, nb_labels = ndimage.label(self.MaskImage)
        # locate bounding rectangles of each region
        tup = ndimage.find_objects(label_im)
        # sort from left to right
        tup.sort(key = sortregion)

        if (self.ax3 == None):
            self.ax3 = plt.subplot(313)

        self.ax3.imshow (self.GreyImage)
        self.ImgLst = list()
        for v in tup:
            t = v[0].start
            b = v[0].stop
            l = v[1].start
            r = v[1].stop
            
            rect = Rectangle((l,t), r - l, b - t, edgecolor='g', facecolor='none')
            self.ax3.add_patch(rect)
            print (t,l, r-l, b-t)
            self.ImgLst.append(self.GreyImage[v])

        self.canvas.draw()
        
    def OnApplyMaskClicked  (self):
        plt.rc('image', cmap='gray')
        self.MaskImage = self.GaussianImage > self.GaussianImage.mean()

        # plot data
        if (self.ax3 == None):
            self.ax3 = plt.subplot(313)
        self.ax3.cla()
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
        if (self.ax3 == None):
            self.ax3 = plt.subplot(313)
        self.ax3.cla()

        # plot data
        self.ax3.imshow (self.ThresholdImage, cmap=plt.cm.gray)
        self.canvas.draw()

    def OnSigmaChanged (self):
        self.sigma = float (self.ui.leSigma.text())
        print ("OnSigmaChanged: {0}".format (self.sigma))
        self.ui.hsbSigma.setValue (int (self.sigma * 10))
        self.GaussianImage = ndimage.gaussian_filter(self.ThresholdImage, sigma=self.sigma)
        if (self.ax3 == None):
            self.ax3 = plt.subplot(313)
        self.ax3.cla()

        # plot data
        self.ax3.imshow (self.GaussianImage, cmap=plt.cm.gray)
        self.canvas.draw()
        print ("OnSigmaChanged done")

    def OnSigmaScrollBarChanged (self):
        self.sigma = self.ui.hsbSigma.value () / 10
        self.ui.leSigma.setText ("{:f}".format (self.sigma))
        self.OnSigmaChanged ()


    def OnHistogramClicked (self):
        print ("Histogram clicked")
        self.ax2.cla()
        image = self.GreyImage

        ar = image.ravel()
        ar2 = ar[ar != 0]
        print ("original array size: {0} non-zero size {1}".format (len(ar), len(ar2)))
        print ("avg={0} std={1} max={2}".format (sum(ar2)/len(ar2), np.std(ar2), ar2.max()))
        self.ax2.hist (ar2, bins=255, range=(0.0, 1.0))
        self.canvas.draw()

    def OnGreyScaleClicked (self):
        print ("grey scale clicked")
        self.GreyImage = rgb2grey (self.OrigImage)
        if (self.ax3 == None):
            self.ax3 = plt.subplot(313)
        self.ax3.cla()

        # plot data
        self.ax3.imshow (self.GreyImage, cmap=plt.cm.gray)
        self.ax3.set_axis_off ()

        # refresh canvas
        self.canvas.draw()

    def OnNextClicked (self):
        self.Msg ("")
        print ("next clicked. file index={0}. No. Files={1}".format(self.file_index, len(self.files)))
        # self.Plot()
        if (self.file_index > len(self.files)):
            return
        filename = self.files[self.file_index]
        self.OrigImage = mpimg.imread (filename)
        self.Filename = os.path.basename (filename)
        self.ui.labFilename.setText (self.Filename)
        self.ax1.cla()

        # plot data
        self.ax1.imshow (self.OrigImage)
        self.ax1.set_axis_off()

        # refresh canvas
        self.canvas.draw()

        self.file_index += 1
        if (self.ui.cbAutoProcess.isChecked()) :
            self.AutoProcess ()

    def OnPreviousClicked (self):
        self.Msg ("")
        print ("previous clicked")
        if (self.file_index <= 0):
            return
        self.file_index -= 1

        filename = self.files[self.file_index]
        self.OrigImage = mpimg.imread (filename)
        self.Filename = os.path.basename (filename)
        self.ui.labFilename.setText (self.Filename)

        self.ax1.cla()

        # plot data
        self.ax1.imshow (self.OrigImage)

        # refresh canvas
        self.canvas.draw()

        if (self.ui.cbAutoProcess.isChecked()) :
            self.AutoProcess ()
    
    def Msg (self, msg):
        self.ui.leMsg.setText (msg)

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