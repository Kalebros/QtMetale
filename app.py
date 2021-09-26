# -coding: utf-8 -*-

import sys

from PySide2 import QtCore,QtWidgets,QtGui

from mainwindow import MainWindow

import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = 'Reproductor de vídeos de Youtube basado en Qt for Python')

    parser.add_argument('--config',help='Ruta a un archivo de configuración opcional')

    args = parser.parse_args()

    app = QtWidgets.QApplication([])

    mainWindow = MainWindow(startWithConfig = args.config)
    mainWindow.show()

    sys.exit(app.exec_())