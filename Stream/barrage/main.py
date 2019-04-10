#! usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
from PySide2 import QtWidgets,QtCore,QtGui

class Mywidget(QtWidgets.QtWidgets):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)

class InfoWidget():
    