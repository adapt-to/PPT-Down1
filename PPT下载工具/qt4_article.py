# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt4_article.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(737, 606)
        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 5, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 5, 2, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 13, 2, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 7, 1, 1, 1)
        self.pushButton_1 = QtGui.QPushButton(Form)
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.gridLayout.addWidget(self.pushButton_1, 2, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        self.textBrowser_1 = QtGui.QTextBrowser(Form)
        self.textBrowser_1.setObjectName(_fromUtf8("textBrowser_1"))
        self.gridLayout.addWidget(self.textBrowser_1, 13, 1, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 7, 2, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 13, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 9, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 8, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 4, 1, 1, 1)
        self.lineEdit_1 = QtGui.QLineEdit(Form)
        self.lineEdit_1.setObjectName(_fromUtf8("lineEdit_1"))
        self.gridLayout.addWidget(self.lineEdit_1, 2, 1, 2, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "优品PPT下载工具", None))
        self.label.setText(_translate("Form", "PPT保存地址：", None))
        self.label_3.setText(_translate("Form", "下载PPT数：", None))
        self.label_2.setText(_translate("Form", "PPT下载网址：", None))
        self.pushButton_2.setText(_translate("Form", "保存", None))
        self.pushButton_4.setText(_translate("Form", "开始下载", None))
        self.pushButton_1.setText(_translate("Form", "保存", None))
        self.pushButton_3.setText(_translate("Form", "保存", None))
        self.label_4.setText(_translate("Form", "运行窗口：", None))
        self.label_5.setText(_translate("Form", "PPT下载网址:http://www.ypppt.com/                                            谨作学习之用", None))
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
