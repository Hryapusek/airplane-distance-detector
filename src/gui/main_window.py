from .ui_main_window import Ui_MainWindow

from PyQt5.QtWidgets import QMainWindow
    

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
