#!/usr/bin/env python2
#coding: utf8

import os.path

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_desk import Ui_desknotify,_fromUtf8 as UTF8
import pynotify

def loadICON():
	p = os.path.join(os.path.dirname(os.path.realpath(__file__)),"01.gif")
	return QIcon(UTF8(p))

class Alert(QMainWindow,Ui_desknotify):
	def __init__(self,parent=None):
		super(Alert, self).__init__(parent)
		self.setupUi(self)
		#--systray--
		self._set_systray()
		#--set timer--
		QTimer.singleShot(50000,self._timeout)
	def _timeout(self):
		#alert something.
		self._dosomething()
		QTimer.singleShot(5000,self._timeout)
	def _dosomething(self):
		pynotify.init("Notify")
		n = pynotify.Notification("Hello DL",'More and More<strong><a href="http://blog.xgarden.net">...</a></strong>')
		n.show()
	def _set_systray(self):
		quit = QAction(QString("&Quit"),self);
		self.connect(quit,SIGNAL("triggered()"),self.close)
		menu = QMenu(self)
		menu.addAction(quit);
		self.icon = QSystemTrayIcon(loadICON(),self)
		self.icon.setToolTip(QString(u"A Alert Coming..."))
		self.icon.setContextMenu(menu)
		self.icon.show()

if __name__=="__main__":
	import sys
	app = QApplication(sys.argv)
	n = Alert()
	n.hide()
	app.exec_()
