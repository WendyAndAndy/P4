# coding: utf-8
# convert *.ui to *_ui.py (using Maya2017 PySide2)
# WeChat: q184327932 or iJasonLee

import os
import sys
from pyside2uic import compileUi  # Maya2020 PySide2
# from pysideuic import compileUi     


def ui2py(uifile):
    pyfilename = '_'.join(uifile.rsplit('.', 1)) + '.py'
    print(uifile)
    print(pyfilename)
    with open(pyfilename, 'w') as pyfile:
        compileUi(uifile, pyfile)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        files = sys.argv[1:]
        for f in files:
            ui2py(f)
            print(f, 'ui2py Done')
