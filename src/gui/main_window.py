# Импортируем необходимые модули
from servers.base_server import BaseServer
from .ui_main_window import Ui_MainWindow

from PyQt5.QtWidgets import QMainWindow, QPushButton

# Определение констант для портов серверов
LEFT_WING_PORT = 32105
RIGHT_WING_PORT = LEFT_WING_PORT + 1
LEFT_STABILIZER_PORT = RIGHT_WING_PORT + 1
RIGHT_STABILIZER_PORT = LEFT_STABILIZER_PORT + 1

# Определение констант для цветов кнопок
M1_COLOR = "red"
M2_COLOR = "orange"
M3_COLOR = "yellow"
SAFE_COLOR = "green"
SAFE_TEXT_COLOR = "white"


class MainWindow(QMainWindow):
    def __init__(self):
        # Инициализируем суперкласс
        super(MainWindow, self).__init__()
        # Инициализируем UI
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        
        # Инициализируем серверы
        self.left_wing_server = BaseServer(LEFT_WING_PORT, "Левый крыльевой сервер")
        self.right_wing_server = BaseServer(RIGHT_WING_PORT, "Правый крыльевой сервер")
        self.left_stabilizer_server = BaseServer(LEFT_STABILIZER_PORT, "Левый стабилизаторный сервер")
        self.right_stabilizer_server = BaseServer(RIGHT_STABILIZER_PORT, "Правый стабилизаторный сервер")
        
        # Запускаем потоки серверов
        self.left_wing_server.start_server_thread()
        self.right_wing_server.start_server_thread()
        self.left_stabilizer_server.start_server_thread()
        self.right_stabilizer_server.start_server_thread()

        # Подключаем кнопки к их соответствующим функциям
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

        # Инициализируем кнопки в безопасном состоянии
        self.lw_safe_btn_clicked()
        self.rw_safe_btn_clicked()
        self.ls_safe_btn_clicked()
        self.rs_safe_btn_clicked()

    # Функция для установки цвета кнопки
    def set_button_color(self, btn: QPushButton, color: str):
        # Установка стиля кнопки для изменения ее цвета
        btn.setStyleSheet(btn.styleSheet() + f"background-color: {color};")

    # Функция для установки цвета текста кнопки
    def set_button_text_color(self, btn: QPushButton, color: str):
        # Установка стиля кнопки для изменения цвета ее текста
        btn.setStyleSheet(btn.styleSheet() + f"color: {color};")

    # Функция для очистки цветов кнопок для правого крыла
    def rw_clear_colors(self):
        # Сброс стилей кнопок правого крыла
        self._ui.rw_1m_btn.setStyleSheet(None)
        self._ui.rw_2m_btn.setStyleSheet(None)
        self._ui.rw_3m_btn.setStyleSheet(None)
        self._ui.rw_safe_btn.setStyleSheet(None)

    # Функция для очистки цветов кнопок для левого крыла
    def lw_clear_colors(self):
        # Сброс стилей кнопок левого крыла
        self._ui.lw_1m_btn.setStyleSheet(None)
        self._ui.lw_2m_btn.setStyleSheet(None)
        self._ui.lw_3m_btn.setStyleSheet(None)
        self._ui.lw_safe_btn.setStyleSheet(None)

    # Функция для очистки цветов кнопок для правого стабилизатора
    def rs_clear_colors(self):
        # Сброс стилей кнопок правого стабилизатора
        self._ui.rs_1m_btn.setStyleSheet(None)
        self._ui.rs_2m_btn.setStyleSheet(None)
        self._ui.rs_3m_btn.setStyleSheet(None)
        self._ui.rs_safe_btn.setStyleSheet(None)

    # Функция для очистки цветов кнопок для левого стабилизатора
    def ls_clear_colors(self):
        # Сброс стилей кнопок левого стабилизатора
        self._ui.ls_1m_btn.setStyleSheet(None)
        self._ui.ls_2m_btn.setStyleSheet(None)
        self._ui.ls_3m_btn.setStyleSheet(None)
        self._ui.ls_safe_btn.setStyleSheet(None)

    # Функции для кнопок левого крыла
    def lw_1m_btn_clicked(self):
        # Установка расстояния до 1 метра и обновление UI
        self.left_wing_server.set_distance(1)
        self.lw_clear_colors()
        self.set_button_color(self._ui.lw_1m_btn, M1_COLOR)
        self.update()

    def lw_2m_btn_clicked(self):
        # Установка расстояния до 2 метров и обновление UI
        self.left_wing_server.set_distance(2)
        self.lw_clear_colors()
        self.set_button_color(self._ui.lw_2m_btn, M2_COLOR)
        self.update()

    def lw_3m_btn_clicked(self):
        # Установка расстояния до 3 метров и обновление UI
        self.left_wing_server.set_distance(3)
        self.lw_clear_colors()
        self.set_button_color(self._ui.lw_3m_btn, M3_COLOR)
        self.update()

    def lw_safe_btn_clicked(self):
        # Установка расстояния до безопасного и обновление UI
        self.left_wing_server.set_distance(100)
        self.lw_clear_colors()
        self.set_button_color(self._ui.lw_safe_btn, SAFE_COLOR)
        self.set_button_text_color(self._ui.lw_safe_btn, SAFE_TEXT_COLOR)
        self.update()

    # Функции для кнопок правого крыла
    def rw_1m_btn_clicked(self):
        # Установка расстояния до 1 метра и обновление UI
        self.right_wing_server.set_distance(1)
        self.rw_clear_colors()
        self.set_button_color(self._ui.rw_1m_btn, M1_COLOR)
        self.update()

    def rw_2m_btn_clicked(self):
        # Установка расстояния до 2 метров и обновление UI
        self.right_wing_server.set_distance(2)
        self.rw_clear_colors()
        self.set_button_color(self._ui.rw_2m_btn, M2_COLOR)
        self.update()

    def rw_3m_btn_clicked(self):
        # Установка расстояния до 3 метров и обновление UI
        self.right_wing_server.set_distance(3)
        self.rw_clear_colors()
        self.set_button_color(self._ui.rw_3m_btn, M3_COLOR)
        self.update()

    def rw_safe_btn_clicked(self):
        # Установка расстояния до безопасного и обновление UI
        self.right_wing_server.set_distance(100)
        self.rw_clear_colors()
        self.set_button_color(self._ui.rw_safe_btn, SAFE_COLOR)
        self.set_button_text_color(self._ui.rw_safe_btn, SAFE_TEXT_COLOR)
        self.update()

    # Функции для кнопок левого стабилизатора
    def ls_1m_btn_clicked(self):
        # Установка расстояния до 1 метра и обновление UI
        self.left_stabilizer_server.set_distance(1)
        self.ls_clear_colors()
        self.set_button_color(self._ui.ls_1m_btn, M1_COLOR)
        self.update()

    def ls_2m_btn_clicked(self):
        # Установка расстояния до 2 метров и обновление UI
        self.left_stabilizer_server.set_distance(2)
        self.ls_clear_colors()
        self.set_button_color(self._ui.ls_2m_btn, M2_COLOR)
        self.update()

    def ls_3m_btn_clicked(self):
        # Установка расстояния до 3 метров и обновление UI
        self.left_stabilizer_server.set_distance(3)
        self.ls_clear_colors()
        self.set_button_color(self._ui.ls_3m_btn, M3_COLOR)
        self.update()

    def ls_safe_btn_clicked(self):
        # Установка расстояния до безопасного и обновление UI
        self.left_stabilizer_server.set_distance(100)
        self.ls_clear_colors()
        self.set_button_color(self._ui.ls_safe_btn, SAFE_COLOR)
        self.set_button_text_color(self._ui.ls_safe_btn, SAFE_TEXT_COLOR)
        self.update()

    # Функции для кнопок правого стабилизатора
    def rs_1m_btn_clicked(self):
        # Установка расстояния до 1 метра и обновление UI
        self.right_stabilizer_server.set_distance(1)
        self.rs_clear_colors()
        self.set_button_color(self._ui.rs_1m_btn, M1_COLOR)
        self.update()

    def rs_2m_btn_clicked(self):
        # Установка расстояния до 2 метров и обновление UI
        self.right_stabilizer_server.set_distance(2)
        self.rs_clear_colors()
        self.set_button_color(self._ui.rs_2m_btn, M2_COLOR)
        self.update()

    def rs_3m_btn_clicked(self):
        # Установка расстояния до 3 метров и обновление UI
        self.right_stabilizer_server.set_distance(3)
        self.rs_clear_colors()
        self.set_button_color(self._ui.rs_3m_btn, M3_COLOR)
        self.update()

    def rs_safe_btn_clicked(self):
        # Установка расстояния до безопасного и обновление UI
        self.right_stabilizer_server.set_distance(100)
        self.rs_clear_colors()
        self.set_button_color(self._ui.rs_safe_btn, SAFE_COLOR)
        self.set_button_text_color(self._ui.rs_safe_btn, SAFE_TEXT_COLOR)
        self.update()
