# Import necessary modules
from servers.base_server import BaseServer
from .ui_main_window import Ui_MainWindow

from PyQt5.QtWidgets import QMainWindow, QPushButton

# Define constants for server ports
LEFT_WING_PORT = 32105
RIGHT_WING_PORT = LEFT_WING_PORT + 1
LEFT_STABILIZER_PORT = RIGHT_WING_PORT + 1
RIGHT_STABILIZER_PORT = LEFT_STABILIZER_PORT + 1

# Define constants for button colors
M1_COLOR = "red"
M2_COLOR = "orange"
M3_COLOR = "yellow"
SAFE_COLOR = "green"
SAFE_TEXT_COLOR = "white"


class MainWindow(QMainWindow):
    def __init__(self):
        # Initialize the superclass
        super(MainWindow, self).__init__()
        # Initialize the UI
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        
        # Initialize servers
        self.left_wing_server = BaseServer(LEFT_WING_PORT, "Left Wing Server")
        self.right_wing_server = BaseServer(RIGHT_WING_PORT, "Right Wing Server")
        self.left_stabilizer_server = BaseServer(LEFT_STABILIZER_PORT, "Left Stabilizer Server")
        self.right_stabilizer_server = BaseServer(RIGHT_STABILIZER_PORT, "Right Stabilizer Server")
        
        # Start server threads
        self.left_wing_server.start_server_thread()
        self.right_wing_server.start_server_thread()
        self.left_stabilizer_server.start_server_thread()
        self.right_stabilizer_server.start_server_thread()

        # Connect buttons to their respective functions
        self._ui.lw_1m_btn.clicked.connect(self.lw_1m_btn_clicked)
        self._ui.lw_2m_btn.clicked.connect(self.lw_2m_btn_clicked)
        self._ui.lw_3m_btn.clicked.connect(self.lw_3m_btn_clicked)
        self._ui.lw_safe_btn.clicked.connect(self.lw_safe_btn_clicked)

        self._ui.rw_1m_btn.clicked.connect(self.rw_1m_btn_clicked)
        self._ui.rw_2m_btn.clicked.connect(self.rw_2m_btn_clicked)
        self._ui.rw_3m_btn.clicked.connect(self.rw_3m_btn_clicked)
        self._ui.rw_safe_btn.clicked.connect(self.rw_safe_btn_clicked)

        self._ui.ls_1m_btn.clicked.connect(self.ls_1m_btn_clicked)
        self._ui.ls_2m_btn.clicked.connect(self.ls_2m_btn_clicked)
        self._ui.ls_3m_btn.clicked.connect(self.ls_3m_btn_clicked)
        self._ui.ls_safe_btn.clicked.connect(self.ls_safe_btn_clicked)

        self._ui.rs_1m_btn.clicked.connect(self.rs_1m_btn_clicked)
        self._ui.rs_2m_btn.clicked.connect(self.rs_2m_btn_clicked)
        self._ui.rs_3m_btn.clicked.connect(self.rs_3m_btn_clicked)
        self._ui.rs_safe_btn.clicked.connect(self.rs_safe_btn_clicked)

        # Initialize buttons to safe state
        self.lw_safe_btn_clicked()
        self.rw_safe_btn_clicked()
        self.ls_safe_btn_clicked()
        self.rs_safe_btn_clicked()

    # Function to set button color
    def set_button_color(self, btn: QPushButton, color: str):
        # Set the button's stylesheet to change its color
        btn.setStyleSheet(btn.styleSheet() + f"background-color: {color};")

    # Function to set button text color
    def set_button_text_color(self, btn: QPushButton, color: str):
        # Set the button's stylesheet to change its text color
        btn.setStyleSheet(btn.styleSheet() + f"color: {color};")

    # Function to clear button colors for right wing
    def rw_clear_colors(self):
        # Reset the stylesheets of the right wing buttons
        self._ui.rw_1m_btn.setStyleSheet(None)
        self._ui.rw_2m_btn.setStyleSheet(None)
        self._ui.rw_3m_btn.setStyleSheet(None)
        self._ui.rw_safe_btn.setStyleSheet(None)

    # Function to clear button colors for left wing
    def lw_clear_colors(self):
        # Reset the stylesheets of the left wing buttons
        self._ui.lw_1m_btn.setStyleSheet(None)
        self._ui.lw_2m_btn.setStyleSheet(None)
        self._ui.lw_3m_btn.setStyleSheet(None)
        self._ui.lw_safe_btn.setStyleSheet(None)

    # Function to clear button colors for right stabilizer
    def rs_clear_colors(self):
        # Reset the stylesheets of the right stabilizer buttons
        self._ui.rs_1m_btn.setStyleSheet(None)
        self._ui.rs_2m_btn.setStyleSheet(None)
        self._ui.rs_3m_btn.setStyleSheet(None)
        self._ui.rs_safe_btn.setStyleSheet(None)

    # Function to clear button colors for left stabilizer
    def ls_clear_colors(self):
        # Reset the stylesheets of the left stabilizer buttons
        self._ui.ls_1m_btn.setStyleSheet(None)
        self._ui.ls_2m_btn.setStyleSheet(None)
        self._ui.ls_3m_btn.setStyleSheet(None)
        self._ui.ls_safe_btn.setStyleSheet(None)

    # Button click functions for left wing
    def lw_1m_btn_clicked(self):
        # Set distance to 1 meter and update the UI
        self.left_wing_server.set_distance(1)
        self.lw_clear_colors()
        self.set_button_color(self._ui.lw_1m_btn, M1_COLOR)
        self.update()

    def lw_2m_btn_clicked(self):
        # Set distance to 2 meters and update the UI
        self.left_wing_server.set_distance(2)
        self.lw_clear_colors()
        self.set_button_color(self._ui.lw_2m_btn, M2_COLOR)
        self.update()

    def lw_3m_btn_clicked(self):
        # Set distance to 3 meters and update the UI
        self.left_wing_server.set_distance(3)
        self.lw_clear_colors()
        self.set_button_color(self._ui.lw_3m_btn, M3_COLOR)
        self.update()

    def lw_safe_btn_clicked(self):
        # Set distance to safe and update the UI
        self.left_wing_server.set_distance(100)
        self.lw_clear_colors()
        self.set_button_color(self._ui.lw_safe_btn, SAFE_COLOR)
        self.set_button_text_color(self._ui.lw_safe_btn, SAFE_TEXT_COLOR)
        self.update()

    # Button click functions for right wing
    def rw_1m_btn_clicked(self):
        # Set distance to 1 meter and update the UI
        self.right_wing_server.set_distance(1)
        self.rw_clear_colors()
        self.set_button_color(self._ui.rw_1m_btn, M1_COLOR)
        self.update()

    def rw_2m_btn_clicked(self):
        # Set distance to 2 meters and update the UI
        self.right_wing_server.set_distance(2)
        self.rw_clear_colors()
        self.set_button_color(self._ui.rw_2m_btn, M2_COLOR)
        self.update()

    def rw_3m_btn_clicked(self):
        # Set distance to 3 meters and update the UI
        self.right_wing_server.set_distance(3)
        self.rw_clear_colors()
        self.set_button_color(self._ui.rw_3m_btn, M3_COLOR)
        self.update()

    def rw_safe_btn_clicked(self):
        # Set distance to safe and update the UI
        self.right_wing_server.set_distance(100)
        self.rw_clear_colors()
        self.set_button_color(self._ui.rw_safe_btn, SAFE_COLOR)
        self.set_button_text_color(self._ui.rw_safe_btn, SAFE_TEXT_COLOR)
        self.update()

    # Button click functions for left stabilizer
    def ls_1m_btn_clicked(self):
        # Set distance to 1 meter and update the UI
        self.left_stabilizer_server.set_distance(1)
        self.ls_clear_colors()
        self.set_button_color(self._ui.ls_1m_btn, M1_COLOR)
        self.update()

    def ls_2m_btn_clicked(self):
        # Set distance to 2 meters and update the UI
        self.left_stabilizer_server.set_distance(2)
        self.ls_clear_colors()
        self.set_button_color(self._ui.ls_2m_btn, M2_COLOR)
        self.update()

    def ls_3m_btn_clicked(self):
        # Set distance to 3 meters and update the UI
        self.left_stabilizer_server.set_distance(3)
        self.ls_clear_colors()
        self.set_button_color(self._ui.ls_3m_btn, M3_COLOR)
        self.update()

    def ls_safe_btn_clicked(self):
        # Set distance to safe and update the UI
        self.left_stabilizer_server.set_distance(100)
        self.ls_clear_colors()
        self.set_button_color(self._ui.ls_safe_btn, SAFE_COLOR)
        self.set_button_text_color(self._ui.ls_safe_btn, SAFE_TEXT_COLOR)
        self.update()

    # Button click functions for right stabilizer
    def rs_1m_btn_clicked(self):
        # Set distance to 1 meter and update the UI
        self.right_stabilizer_server.set_distance(1)
        self.rs_clear_colors()
        self.set_button_color(self._ui.rs_1m_btn, M1_COLOR)
        self.update()

    def rs_2m_btn_clicked(self):
        # Set distance to 2 meters and update the UI
        self.right_stabilizer_server.set_distance(2)
        self.rs_clear_colors()
        self.set_button_color(self._ui.rs_2m_btn, M2_COLOR)
        self.update()

    def rs_3m_btn_clicked(self):
        # Set distance to 3 meters and update the UI
        self.right_stabilizer_server.set_distance(3)
        self.rs_clear_colors()
        self.set_button_color(self._ui.rs_3m_btn, M3_COLOR)
        self.update()

    def rs_safe_btn_clicked(self):
        # Set distance to safe and update the UI
        self.right_stabilizer_server.set_distance(100)
        self.rs_clear_colors()
        self.set_button_color(self._ui.rs_safe_btn, SAFE_COLOR)
        self.set_button_text_color(self._ui.rs_safe_btn, SAFE_TEXT_COLOR)
        self.update()
