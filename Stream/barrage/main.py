#! usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
from PySide2 import QtWidgets,QtCore,QtGui

     
class InfoWidget(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        Roomid = QtWidgets.QLabel(u'房间号')
        NickName = QtWidgets.QLabel(u'主播')
        Description = QtWidgets.QLabel(u'简介')
        Online = QtWidgets.QLabel(u'在线人数')

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(Roomid)
        layout.addWidget(NickName)
        layout.addWidget(Description)
        layout.addWidget(Online)
        self.setLayout(layout)







class MyWidget(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)

        self.setFixedSize(600,400)
        Roomid = QtWidgets.QLabel(u'房间号')
        Infowidget = InfoWidget()
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(Infowidget)
        layout.addWidget(Roomid)
        self.setLayout(layout)








app = QtWidgets.QApplication()
widget = MyWidget()
widget.show()
sys.exit(app.exec_())