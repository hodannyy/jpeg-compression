# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form.ui'
#
# Created: Wed Jun 29 22:06:01 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt4 import QtCore, QtGui
from Compression import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):

    def setupUi(self, Form):
        
        self.path = "/Users/danho/Desktop/Work/images/grey_320_320.jpg"
        #self.path = "/Users/danho/Desktop/Work/images/snowboard_300_300.jpg"
        #self.path = "/Users/danho/Desktop/Work/images/cat8.jpg"
        self.imageStack = Compression(self.path)

        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(683, 487)
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 671, 61))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.buttonOpen = QtGui.QPushButton(self.layoutWidget)
        self.buttonOpen.setObjectName(_fromUtf8("buttonOpen"))
        self.horizontalLayout_4.addWidget(self.buttonOpen)
        self.buttonCompress = QtGui.QPushButton(self.layoutWidget)
        self.buttonCompress.setObjectName(_fromUtf8("buttonCompress"))
        self.horizontalLayout_4.addWidget(self.buttonCompress)
        self.buttonDisplay = QtGui.QPushButton(self.layoutWidget)
        self.buttonDisplay.setObjectName(_fromUtf8("buttonDisplay"))
        self.horizontalLayout_4.addWidget(self.buttonDisplay)
        self.pushButton = QtGui.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(490, 70, 190, 411))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.q1Button = QtGui.QRadioButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.q1Button.setFont(font)
        self.q1Button.setChecked(True)
        self.q1Button.setObjectName(_fromUtf8("q1Button"))
        self.gridLayout.addWidget(self.q1Button, 0, 0, 1, 1)
        self.q2Button = QtGui.QRadioButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.q2Button.setFont(font)
        self.q2Button.setObjectName(_fromUtf8("q2Button"))
        self.gridLayout.addWidget(self.q2Button, 1, 0, 1, 1)
        self.q3Button = QtGui.QRadioButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.q3Button.setFont(font)
        self.q3Button.setObjectName(_fromUtf8("q3Button"))
        self.gridLayout.addWidget(self.q3Button, 2, 0, 1, 1)
        self.q4Button = QtGui.QRadioButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.q4Button.setFont(font)
        self.q4Button.setObjectName(_fromUtf8("q4Button"))
        self.gridLayout.addWidget(self.q4Button, 3, 0, 1, 1)
        self.q5Button = QtGui.QRadioButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.q5Button.setFont(font)
        self.q5Button.setObjectName(_fromUtf8("q5Button"))
        self.gridLayout.addWidget(self.q5Button, 4, 0, 1, 1)
        self.q6Button = QtGui.QRadioButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.q6Button.setFont(font)
        self.q6Button.setObjectName(_fromUtf8("q6Button"))
        self.gridLayout.addWidget(self.q6Button, 5, 0, 1, 1)
        self.q7Button = QtGui.QRadioButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.q7Button.setFont(font)
        self.q7Button.setObjectName(_fromUtf8("q7Button"))
        self.gridLayout.addWidget(self.q7Button, 6, 0, 1, 1)
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox_3)
        self.radioButton_4.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setCheckable(True)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.gridLayout.addWidget(self.radioButton_4, 7, 0, 1, 1)
        self.radioButton_5 = QtGui.QRadioButton(self.groupBox_3)
        self.radioButton_5.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setCheckable(True)
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.gridLayout.addWidget(self.radioButton_5, 8, 0, 1, 1)
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 260, 481, 221))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.widget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.formLayout = QtGui.QFormLayout(self.tab)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.console = QtGui.QPlainTextEdit(self.tab)
        self.console.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.console.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.console.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.console.setObjectName(_fromUtf8("console"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.console)
        self.buttonClear = QtGui.QPushButton(self.tab)
        self.buttonClear.setObjectName(_fromUtf8("buttonClear"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.buttonClear)
        self.buttonQuit = QtGui.QPushButton(self.tab)
        self.buttonQuit.setObjectName(_fromUtf8("buttonQuit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.buttonQuit)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.qMatrix = QtGui.QPlainTextEdit(self.tab_2)
        self.qMatrix.setObjectName(_fromUtf8("qMatrix"))
        self.gridLayout_2.addWidget(self.qMatrix, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.widget1 = QtGui.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(10, 70, 481, 191))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_2 = QtGui.QGroupBox(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.layoutWidget_3 = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget_3.setGeometry(QtCore.QRect(11, 31, 461, 50))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.imageRGB = QtGui.QRadioButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.imageRGB.setFont(font)
        self.imageRGB.setChecked(True)
        self.imageRGB.setObjectName(_fromUtf8("imageRGB"))
        self.horizontalLayout.addWidget(self.imageRGB)
        self.imageYUV = QtGui.QRadioButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.imageYUV.setFont(font)
        self.imageYUV.setObjectName(_fromUtf8("imageYUV"))
        self.horizontalLayout.addWidget(self.imageYUV)
        self.imageCSS = QtGui.QRadioButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.imageCSS.setFont(font)
        self.imageCSS.setObjectName(_fromUtf8("imageCSS"))
        self.horizontalLayout.addWidget(self.imageCSS)
        self.imageDCT = QtGui.QRadioButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.imageDCT.setFont(font)
        self.imageDCT.setObjectName(_fromUtf8("imageDCT"))
        self.horizontalLayout.addWidget(self.imageDCT)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.imageQuantized = QtGui.QRadioButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.imageQuantized.setFont(font)
        self.imageQuantized.setObjectName(_fromUtf8("imageQuantized"))
        self.horizontalLayout_2.addWidget(self.imageQuantized)
        self.imageDequantized = QtGui.QRadioButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.imageDequantized.setFont(font)
        self.imageDequantized.setObjectName(_fromUtf8("imageDequantized"))
        self.horizontalLayout_2.addWidget(self.imageDequantized)
        self.imageIDCT = QtGui.QRadioButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.imageIDCT.setFont(font)
        self.imageIDCT.setObjectName(_fromUtf8("imageIDCT"))
        self.horizontalLayout_2.addWidget(self.imageIDCT)
        self.imageFinal = QtGui.QRadioButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.imageFinal.setFont(font)
        self.imageFinal.setObjectName(_fromUtf8("imageFinal"))
        self.horizontalLayout_2.addWidget(self.imageFinal)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        self.groupBox = QtGui.QGroupBox(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.widget2 = QtGui.QWidget(self.groupBox)
        self.widget2.setGeometry(QtCore.QRect(15, 39, 441, 19))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.colorAll = QtGui.QRadioButton(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.colorAll.setFont(font)
        self.colorAll.setChecked(True)
        self.colorAll.setObjectName(_fromUtf8("colorAll"))
        self.horizontalLayout_3.addWidget(self.colorAll)
        self.colorRY = QtGui.QRadioButton(self.widget2)
        self.colorRY.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.colorRY.setFont(font)
        self.colorRY.setCheckable(False)
        self.colorRY.setObjectName(_fromUtf8("colorRY"))
        self.horizontalLayout_3.addWidget(self.colorRY)
        self.colorGU = QtGui.QRadioButton(self.widget2)
        self.colorGU.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.colorGU.setFont(font)
        self.colorGU.setCheckable(False)
        self.colorGU.setObjectName(_fromUtf8("colorGU"))
        self.horizontalLayout_3.addWidget(self.colorGU)
        self.colorBV = QtGui.QRadioButton(self.widget2)
        self.colorBV.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.colorBV.setFont(font)
        self.colorBV.setCheckable(False)
        self.colorBV.setObjectName(_fromUtf8("colorBV"))
        self.horizontalLayout_3.addWidget(self.colorBV)
        self.verticalLayout_7.addWidget(self.groupBox)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonQuit, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QObject.connect(self.buttonDisplay, QtCore.SIGNAL(_fromUtf8("clicked()")), self.loadImage)
        QtCore.QObject.connect(self.buttonOpen, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showDialog)
        QtCore.QObject.connect(self.buttonCompress, QtCore.SIGNAL(_fromUtf8("clicked()")), self.compressionProcess)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.saveToDisk)
        QtCore.QObject.connect(self.buttonClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clearConsole)

        QtCore.QObject.connect(self.q1Button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.printQuantizationMatrix)
        QtCore.QObject.connect(self.q2Button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.printQuantizationMatrix)
        QtCore.QObject.connect(self.q3Button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.printQuantizationMatrix)
        QtCore.QObject.connect(self.q4Button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.printQuantizationMatrix)
        QtCore.QObject.connect(self.q5Button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.printQuantizationMatrix)
        QtCore.QObject.connect(self.q6Button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.printQuantizationMatrix)
        QtCore.QObject.connect(self.q7Button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.printQuantizationMatrix)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def loadImage(self):
        if (self.imageRGB.isChecked() and self.colorAll.isChecked()==True):
            self.imageStack.originalImage.show()
            self.console.insertPlainText("Displaying original image.\n")

        elif (self.imageYUV.isChecked() and self.colorAll.isChecked()==True):
            self.imageStack.yuvImage.show()
            self.console.insertPlainText("Displaying YUV image.\n")

        elif (self.imageCSS.isChecked() and self.colorAll.isChecked()==True):
            self.imageStack.cssImage.show()
            self.console.insertPlainText("Displaying Chroma-Subsampled image.\n")

        elif (self.imageDCT.isChecked() and self.colorAll.isChecked()==True):
            self.imageStack.dctImage.show()
            self.console.insertPlainText("Displaying DCT image.\n")

        elif (self.imageQuantized.isChecked() and self.colorAll.isChecked()==True):
            self.imageStack.qImage.show()
            self.console.insertPlainText("Displaying Quantized image.\n")

        elif (self.imageDequantized.isChecked() and self.colorAll.isChecked()==True):
            self.imageStack.dqImage.show()
            self.console.insertPlainText("Displaying Dequantized image.\n")

        elif (self.imageIDCT.isChecked() and self.colorAll.isChecked()==True):
            self.imageStack.idctImage.show()
            self.console.insertPlainText("Displaying IDCT image.\n")

        elif (self.imageFinal.isChecked() and self.colorAll.isChecked()==True):
            self.imageStack.finalImage.show()
            self.console.insertPlainText("Displaying Final image.\n")

        else:
            self.console.insertPlainText("Select an image type to display!\n")

    def printQuantizationMatrix(self):
        #self.qMatrix.insertPlainText(self.imageStack.show(self.imageStack.qLuminance))
        if (self.q1Button.isChecked()==True):
            self.qMatrix.clear()
            for row in range(8):
                    self.qMatrix.insertPlainText(str(self.imageStack.qLuminance[row]) + "\n")
        if (self.q2Button.isChecked()==True):
            self.qMatrix.clear()
            for row in range(8):
                    self.qMatrix.insertPlainText(str(self.imageStack.constantLow[row]) + "\n")
        if (self.q3Button.isChecked()==True):
            self.qMatrix.clear()
            for row in range(8):
                    self.qMatrix.insertPlainText(str(self.imageStack.constantMedium[row]) + "\n")
        if (self.q4Button.isChecked()==True):
            self.qMatrix.clear()
            for row in range(8):
                    self.qMatrix.insertPlainText(str(self.imageStack.constantHigh[row]) + "\n")
        if (self.q5Button.isChecked()==True):
            self.qMatrix.clear()
            for row in range(8):
                    self.qMatrix.insertPlainText(str(self.imageStack.nonUniformLow[row]) + "\n")
        if (self.q6Button.isChecked()==True):
            self.qMatrix.clear()
            for row in range(8):
                    self.qMatrix.insertPlainText(str(self.imageStack.nonUniformMedium[row]) + "\n")
        if (self.q7Button.isChecked()==True):
            self.qMatrix.clear()
            for row in range(8):
                    self.qMatrix.insertPlainText(str(self.imageStack.nonUniformHigh[row]) + "\n")

    def compressionProcess(self):
        if (self.q1Button.isChecked()==True):
            self.imageStack.compression(self.imageStack.originalImage, self.imageStack.qLuminance, self.imageStack.qChrominance)
            self.console.insertPlainText(str(len(self.imageStack.yuvBlocks)) + " blocks were compressed successfully.\n")
            self.console.insertPlainText(str(self.imageStack.paddedRow) + " rows were padded.\n" + str(self.imageStack.paddedRow) + " columns were padded.\n")
        if (self.q2Button.isChecked()==True):
            self.imageStack.compression(self.imageStack.originalImage, self.imageStack.constantLow, self.imageStack.constantLow)
            self.console.insertPlainText(str(len(self.imageStack.yuvBlocks)) + " blocks were compressed successfully.\n")
            self.console.insertPlainText(str(self.imageStack.paddedRow) + " rows were padded.\n" + str(self.imageStack.paddedRow) + " columns were padded.\n")
        if (self.q3Button.isChecked()==True):
            self.imageStack.compression(self.imageStack.originalImage, self.imageStack.constantMedium, self.imageStack.constantMedium)
            self.console.insertPlainText(str(len(self.imageStack.yuvBlocks)) + " blocks were compressed successfully.\n")
            self.console.insertPlainText(str(self.imageStack.paddedRow) + " rows were padded.\n" + str(self.imageStack.paddedRow) + " columns were padded.\n")
        if (self.q4Button.isChecked()==True):
            self.imageStack.compression(self.imageStack.originalImage, self.imageStack.constantHigh, self.imageStack.constantHigh)
            self.console.insertPlainText(str(len(self.imageStack.yuvBlocks)) + " blocks were compressed successfully.\n")
            self.console.insertPlainText(str(self.imageStack.paddedRow) + " rows were padded.\n" + str(self.imageStack.paddedRow) + " columns were padded.\n")
        if (self.q5Button.isChecked()==True):
            self.imageStack.compression(self.imageStack.originalImage, self.imageStack.nonUniformLow, self.imageStack.nonUniformLow)
            self.console.insertPlainText(str(len(self.imageStack.yuvBlocks)) + " blocks were compressed successfully.\n")
            self.console.insertPlainText(str(self.imageStack.paddedRow) + " rows were padded.\n" + str(self.imageStack.paddedRow) + " columns were padded.\n")
        if (self.q6Button.isChecked()==True):
            self.imageStack.compression(self.imageStack.originalImage, self.imageStack.nonUniformMedium, self.imageStack.nonUniformMedium)
            self.console.insertPlainText(str(len(self.imageStack.yuvBlocks)) + " blocks were compressed successfully.\n")
            self.console.insertPlainText(str(self.imageStack.paddedRow) + " rows were padded.\n" + str(self.imageStack.paddedRow) + " columns were padded.\n")
        if (self.q7Button.isChecked()==True):
            self.imageStack.compression(self.imageStack.originalImage, self.imageStack.nonUniformHigh, self.imageStack.nonUniformHigh)
            self.console.insertPlainText(str(len(self.imageStack.yuvBlocks)) + " blocks were compressed successfully.\n")
            self.console.insertPlainText(str(self.imageStack.paddedRow) + " rows were padded.\n" + str(self.imageStack.paddedRow) + " columns were padded.\n")


    def saveToDisk(self):
	    self.imageStack.saveImages()
	    self.console.insertPlainText("Current images were saved to root directory.\n")

	
    def clearConsole(self):
	    self.console.clear()

    def showDialog(self):

        fileDialog = QtGui.QFileDialog()
        self.path = fileDialog.getOpenFileName(fileDialog, 'Open file', '/home')
        self.console.insertPlainText(self.path)

	
    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "CMPT365: Project Assignment 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "JPEG COMPRESSION v1.03: By Danny Ho", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonOpen.setText(QtGui.QApplication.translate("Form", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonCompress.setText(QtGui.QApplication.translate("Form", "Compress", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonDisplay.setText(QtGui.QApplication.translate("Form", "Display Image", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Form", "Quantization Matrices", None, QtGui.QApplication.UnicodeUTF8))
        self.q1Button.setText(QtGui.QApplication.translate("Form", "Q1: Standard Luma/Chroma", None, QtGui.QApplication.UnicodeUTF8))
        self.q2Button.setText(QtGui.QApplication.translate("Form", "Q2: Low Constant", None, QtGui.QApplication.UnicodeUTF8))
        self.q3Button.setText(QtGui.QApplication.translate("Form", "Q3: Medium Constant", None, QtGui.QApplication.UnicodeUTF8))
        self.q4Button.setText(QtGui.QApplication.translate("Form", "Q4: High Constant", None, QtGui.QApplication.UnicodeUTF8))
        self.q5Button.setText(QtGui.QApplication.translate("Form", "Q5: Low Non-Uniform", None, QtGui.QApplication.UnicodeUTF8))
        self.q6Button.setText(QtGui.QApplication.translate("Form", "Q6: Medium Non-Uniform", None, QtGui.QApplication.UnicodeUTF8))
        self.q7Button.setText(QtGui.QApplication.translate("Form", "Q7: High Non-Uniform", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_4.setText(QtGui.QApplication.translate("Form", "Q8: Additional 1", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_5.setText(QtGui.QApplication.translate("Form", "Q9: Additional 2", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonClear.setText(QtGui.QApplication.translate("Form", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonQuit.setText(QtGui.QApplication.translate("Form", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Form", "Console", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Form", "Current Quantization Matrix", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Image Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.imageRGB.setText(QtGui.QApplication.translate("Form", "Original (RGB)", None, QtGui.QApplication.UnicodeUTF8))
        self.imageYUV.setText(QtGui.QApplication.translate("Form", "RGB->YUV", None, QtGui.QApplication.UnicodeUTF8))
        self.imageCSS.setText(QtGui.QApplication.translate("Form", "CSS (YUV)", None, QtGui.QApplication.UnicodeUTF8))
        self.imageDCT.setText(QtGui.QApplication.translate("Form", "DCT", None, QtGui.QApplication.UnicodeUTF8))
        self.imageQuantized.setText(QtGui.QApplication.translate("Form", "Quantized", None, QtGui.QApplication.UnicodeUTF8))
        self.imageDequantized.setText(QtGui.QApplication.translate("Form", "De-Quantized", None, QtGui.QApplication.UnicodeUTF8))
        self.imageIDCT.setText(QtGui.QApplication.translate("Form", "IDCT", None, QtGui.QApplication.UnicodeUTF8))
        self.imageFinal.setText(QtGui.QApplication.translate("Form", "YUV -> RGB", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Color Channels:", None, QtGui.QApplication.UnicodeUTF8))
        self.colorAll.setText(QtGui.QApplication.translate("Form", "All", None, QtGui.QApplication.UnicodeUTF8))
        self.colorRY.setText(QtGui.QApplication.translate("Form", "R/Y", None, QtGui.QApplication.UnicodeUTF8))
        self.colorGU.setText(QtGui.QApplication.translate("Form", "G/U", None, QtGui.QApplication.UnicodeUTF8))
        self.colorBV.setText(QtGui.QApplication.translate("Form", "B/V", None, QtGui.QApplication.UnicodeUTF8))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

