# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desknotify.ui'
#
# Created: Tue Nov  8 11:04:50 2011
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_desknotify(object):
    def setupUi(self, desknotify):
        desknotify.setObjectName(_fromUtf8("desknotify"))
        desknotify.resize(389, 331)
        desknotify.setWindowTitle(QtGui.QApplication.translate("desknotify", "任务通知", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(desknotify)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        desknotify.setCentralWidget(self.centralwidget)

        self.retranslateUi(desknotify)
        QtCore.QMetaObject.connectSlotsByName(desknotify)

    def retranslateUi(self, desknotify):
        pass

