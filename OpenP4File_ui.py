# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\git\WendyAndAndy\P4\OpenP4File.ui',
# licensing of 'D:\git\WendyAndAndy\P4\OpenP4File.ui' applies.
#
# Created: Mon Apr  6 21:12:17 2020
#      by: pyside2-uic  running on PySide2 5.12.5
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(624, 122)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.leServer = QtWidgets.QLineEdit(Form)
        self.leServer.setObjectName("leServer")
        self.horizontalLayout.addWidget(self.leServer)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.leWorkspace = QtWidgets.QLineEdit(Form)
        self.leWorkspace.setObjectName("leWorkspace")
        self.horizontalLayout.addWidget(self.leWorkspace)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.leUser = QtWidgets.QLineEdit(Form)
        self.leUser.setObjectName("leUser")
        self.horizontalLayout.addWidget(self.leUser)
        self.btnP4Test = QtWidgets.QPushButton(Form)
        self.btnP4Test.setObjectName("btnP4Test")
        self.horizontalLayout.addWidget(self.btnP4Test)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.leP4Filename = QtWidgets.QLineEdit(Form)
        self.leP4Filename.setObjectName("leP4Filename")
        self.horizontalLayout_2.addWidget(self.leP4Filename)
        self.btnOpenFile = QtWidgets.QPushButton(Form)
        self.btnOpenFile.setObjectName("btnOpenFile")
        self.horizontalLayout_2.addWidget(self.btnOpenFile)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.leLocalFilename = QtWidgets.QLineEdit(Form)
        self.leLocalFilename.setObjectName("leLocalFilename")
        self.horizontalLayout_3.addWidget(self.leLocalFilename)
        self.btnSubmit = QtWidgets.QPushButton(Form)
        self.btnSubmit.setObjectName("btnSubmit")
        self.horizontalLayout_3.addWidget(self.btnSubmit)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "usingP4", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Server:", None, -1))
        self.leServer.setText(QtWidgets.QApplication.translate("Form", "localhost:1666", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Workspace:", None, -1))
        self.leWorkspace.setText(QtWidgets.QApplication.translate("Form", "jason_test", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "User:", None, -1))
        self.leUser.setText(QtWidgets.QApplication.translate("Form", "jason", None, -1))
        self.btnP4Test.setText(QtWidgets.QApplication.translate("Form", "P4 Test", None, -1))
        self.leP4Filename.setText(QtWidgets.QApplication.translate("Form", "filename in P4", None, -1))
        self.btnOpenFile.setText(QtWidgets.QApplication.translate("Form", "Open File", None, -1))
        self.leLocalFilename.setText(QtWidgets.QApplication.translate("Form", "local filename", None, -1))
        self.btnSubmit.setText(QtWidgets.QApplication.translate("Form", "P4 Submit", None, -1))

