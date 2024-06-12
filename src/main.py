# Импорт необходимых модулей
import multiprocessing
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow

# Определение основной функции
def main():
    # Поддержка заморозки для многопроцессорности
    multiprocessing.freeze_support()
    # Создание нового приложения
    app = QApplication([])
    # Создание нового главного окна
    widget = MainWindow()
    # Показать главное окно
    widget.show()
    # Выполнить приложение
    app.exec_()

# Проверка, запущен ли скрипт непосредственно
if __name__ == "__main__":
    # Вызов основной функции
    main()
