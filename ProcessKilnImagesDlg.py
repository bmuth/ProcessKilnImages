# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProcessKilnImages-dlg.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(533, 337)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 252, 310))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetOriginal = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widgetOriginal.setObjectName("widgetOriginal")
        self.verticalLayout.addWidget(self.widgetOriginal)
        self.labHistogram = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labHistogram.setMinimumSize(QtCore.QSize(250, 100))
        self.labHistogram.setObjectName("labHistogram")
        self.verticalLayout.addWidget(self.labHistogram)
        self.labFinal = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labFinal.setMinimumSize(QtCore.QSize(250, 100))
        self.labFinal.setObjectName("labFinal")
        self.verticalLayout.addWidget(self.labFinal)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(270, 10, 251, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnPrevious = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnPrevious.setObjectName("btnPrevious")
        self.horizontalLayout.addWidget(self.btnPrevious)
        self.btnNext = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnNext.setObjectName("btnNext")
        self.horizontalLayout.addWidget(self.btnNext)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.btnGreyScale = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnGreyScale.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnGreyScale.setObjectName("btnGreyScale")
        self.horizontalLayout_5.addWidget(self.btnGreyScale)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.btnHistogram = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnHistogram.setObjectName("btnHistogram")
        self.horizontalLayout_6.addWidget(self.btnHistogram)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(50, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.hsbThreshold = QtWidgets.QScrollBar(self.verticalLayoutWidget_2)
        self.hsbThreshold.setOrientation(QtCore.Qt.Horizontal)
        self.hsbThreshold.setObjectName("hsbThreshold")
        self.horizontalLayout_2.addWidget(self.hsbThreshold)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(50, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.hsbSigma = QtWidgets.QScrollBar(self.verticalLayoutWidget_2)
        self.hsbSigma.setOrientation(QtCore.Qt.Horizontal)
        self.hsbSigma.setObjectName("hsbSigma")
        self.horizontalLayout_3.addWidget(self.hsbSigma)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.btnApplyMask = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnApplyMask.setObjectName("btnApplyMask")
        self.horizontalLayout_7.addWidget(self.btnApplyMask)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.btnFindRegions = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnFindRegions.setObjectName("btnFindRegions")
        self.horizontalLayout_8.addWidget(self.btnFindRegions)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.leDigits = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.leDigits.setObjectName("leDigits")
        self.horizontalLayout_4.addWidget(self.leDigits)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_9.addWidget(self.pushButton_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labHistogram.setText(_translate("Dialog", "TextLabel"))
        self.labFinal.setText(_translate("Dialog", "TextLabel"))
        self.btnPrevious.setText(_translate("Dialog", "Previous"))
        self.btnNext.setText(_translate("Dialog", "Next"))
        self.btnGreyScale.setText(_translate("Dialog", "Grey Scale"))
        self.btnHistogram.setText(_translate("Dialog", "Histogram"))
        self.label_2.setText(_translate("Dialog", "Threshold: "))
        self.label_3.setText(_translate("Dialog", "Sigma:"))
        self.btnApplyMask.setText(_translate("Dialog", "Apply Mask"))
        self.btnFindRegions.setText(_translate("Dialog", "Find Regions"))
        self.label_5.setText(_translate("Dialog", "Digits:"))
        self.pushButton_5.setText(_translate("Dialog", "Split and Save"))

