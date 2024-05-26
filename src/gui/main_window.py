from servers.base_server import BaseServer
from .ui_main_window import Ui_MainWindow

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer

LEFT_WING_PORT = 32001
RIGHT_WING_PORT = LEFT_WING_PORT + 1
LEFT_STABILIZER = RIGHT_WING_PORT + 1
RIGHT_STABILIZER = LEFT_STABILIZER + 1


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self.left_wing_server = BaseServer(LEFT_WING_PORT, "Left Wing Server")
        self.right_wing_server = BaseServer(RIGHT_WING_PORT, "Right Wing Server")
        self.left_stabilizer_server = BaseServer(LEFT_STABILIZER, "Left Stabilizer Server")
        self.right_stabilizer_server = BaseServer(RIGHT_STABILIZER, "Right Stabilizer Server")
        
        self.left_wing_server.start_server_thread()
        self.right_wing_server.start_server_thread()
        self.left_stabilizer_server.start_server_thread()
        self.right_stabilizer_server.start_server_thread()
