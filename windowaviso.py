# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowaviso.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_windowaviso(object):
    def setupUi(self, windowaviso):
        windowaviso.setObjectName("windowaviso")
        windowaviso.resize(360, 200)
        windowaviso.setModal(True)
        self.btnrespuesta = QtWidgets.QDialogButtonBox(windowaviso)
        self.btnrespuesta.setGeometry(QtCore.QRect(0, 140, 341, 32))
        self.btnrespuesta.setOrientation(QtCore.Qt.Horizontal)
        self.btnrespuesta.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.btnrespuesta.setCenterButtons(True)
        self.btnrespuesta.setObjectName("btnrespuesta")
        self.lbnaviso = QtWidgets.QLabel(windowaviso)
        self.lbnaviso.setGeometry(QtCore.QRect(130, 0, 91, 81))
        self.lbnaviso.setText("")
        self.lbnaviso.setPixmap(QtGui.QPixmap("img/aviso.png"))
        self.lbnaviso.setScaledContents(True)
        self.lbnaviso.setObjectName("lbnaviso")
        self.lblpregunta = QtWidgets.QLabel(windowaviso)
        self.lblpregunta.setGeometry(QtCore.QRect(30, 80, 281, 41))
        self.lblpregunta.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lblpregunta.setAlignment(QtCore.Qt.AlignCenter)
        self.lblpregunta.setObjectName("lblpregunta")

        self.retranslateUi(windowaviso)
        self.btnrespuesta.accepted.connect(windowaviso.accept)
        self.btnrespuesta.rejected.connect(windowaviso.reject)
        QtCore.QMetaObject.connectSlotsByName(windowaviso)

    def retranslateUi(self, windowaviso):
        _translate = QtCore.QCoreApplication.translate
        windowaviso.setWindowTitle(_translate("windowaviso", "Dialog"))
        self.lblpregunta.setText(_translate("windowaviso", "Desea Salir?"))

