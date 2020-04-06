#!/usr/bin/env python3
#coding:utf-8
"""
  Author:  jason.li, 184327932@qq.com
  wechat:  q184327932 or iJasonLee
  Purpose: using P4 in maya demo (test in Maya2020)
  Created: 04/06/20
"""

import os
import sys
import lib
import OpenP4File_ui as ui
#from PySide2 import QtGui, QtWidgets, QtCore
from Qt import QtGui, QtWidgets, QtCore

from P4 import P4, P4Exception
import pymel.core as pm

class Win(QtWidgets.QWidget, ui.Ui_Form):

    def __init__(self, parent=None):
        super(Win, self).__init__(parent)
        self.setupUi(self)
        if parent:
            self.setWindowFlags(parent.windowFlags())
        self.connect_actions()
        self.p4 = None
    
    def connect_actions(self):
        """"""
        self.btnP4Test.clicked.connect(self.btnP4Test_click)
        self.btnOpenFile.clicked.connect(self.btnOpenFile_click)
        self.btnSubmit.clicked.connect(self.btnSubmit_click)
        
    def initP4(self):
        """"""
        server = self.leServer.text().strip()
        workspace = self.leWorkspace.text().strip()
        user = self.leUser.text().strip()        
        p4 = P4()
        # perforce api need ascii string!!!
        p4.port = str(server)
        p4.user = str(user)
        p4.client = str(workspace)
        # using perforce local ticket login, so run perforce first! else may need input password
        try:
            p4.connect()
            # ignore "File(s) up-to-date"s
            p4.exception_level = 1         
            self.p4 = p4
        except:
            self.p4 = None
        
        
    def btnP4Test_click(self):
        """"""
        print('btnP4Test_click')
        
        if not self.p4:
            self.initP4()
        if self.p4.connected():
            self.btnP4Test.setStyleSheet('background-color: green')
            return
        try:
            info = self.p4.run('info')
            for k, v in info[0].items():
                print k, v
            self.btnP4Test.setStyleSheet('background-color: green')
        except P4Exception:
            for w in self.p4.warnings:
                print(w)
            for e in self.p4.errors:
                print(e)
            self.btnP4Test.setStyleSheet('background-color: red')
        finally:
            self.p4.disconnect()
        
        
    def btnOpenFile_click(self):
        """"""
        print('btnOpenFile_click')
        
        filename = self.leP4Filename.text().strip()
        if not self.p4:
            self.initP4()
        with self.p4.connect():
            try:
                # p4 sync [-f -L -n -N -k -q -r] [-m max] [file[revRange] ...]
                # p4 sync [-L -n -N -q -s] [-m max] [file[revRange] ...]
                # p4 sync [-L -n -N -p -q] [-m max] [file[revRange] ...]
                #         --parallel=threads=N[,batch=N][,batchsize=N][,min=N][,minsize=N]
                sync = self.p4.run('sync', filename)
                #print(sync)
                clientFile = sync[0]['clientFile']
                self.leLocalFilename.setText(clientFile)
                pm.openFile(clientFile, o=1, f=1)
                print(self.p4.run_edit(clientFile))
                self.btnOpenFile.setStyleSheet('background-color: green')
            except P4Exception:
                for w in self.p4.warnings:
                    print(w)
                for e in self.p4.errors:
                    print(e)
            except Exception as ex:
                print(ex.message)
        
        
    def btnSubmit_click(self):
        """"""
        print('btnSubmit_click')
        
        # right click get current maya filename
        key = QtWidgets.QApplication.keyboardModifiers()
        if key == QtCore.Qt.ControlModifier:
            sn = pm.sceneName()
            self.leLocalFilename.setText(sn)
            return
        
        filename = self.leLocalFilename.text().strip()
        if not os.path.exists(filename):
            QtWidgets.QMessageBox.critical(self, u'ERROR', u'文件不存在')
            return
        
        if not self.p4:
            self.initP4()
        with self.p4.connect():
            try:
                self.p4.run_add(filename)
                change = self.p4.fetch_change()
                change._description = str('+ %s'%os.path.basename(filename))
                self.p4.run_submit(change)
                self.btnSubmit.setStyleSheet('background-color: green')
            except P4Exception:
                for w in self.p4.warnings:
                    print(w)
                for e in self.p4.errors:
                    print(e)
                self.btnSubmit.setStyleSheet('background-color: red')
    

###########################################
def main():
    #import P4
    #print(P4.P4.identify())
    
    global win
    try:
        win.close()
    except:
        pass
    win = Win(lib.getMayaMainWindow())
    win.show()


if __name__ == '__main__':
    main()