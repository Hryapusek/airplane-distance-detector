import time    
from gui.main_window import LEFT_WING_PORT, RIGHT_WING_PORT, LEFT_STABILIZER_PORT, RIGHT_STABILIZER_PORT
from servers.base_server import BaseServer
# Определение основной функции
def main():
    left_wing_server = BaseServer(LEFT_WING_PORT, "Левый крыльевой сервер")
    right_wing_server = BaseServer(RIGHT_WING_PORT, "Правый крыльевой сервер")
    left_stabilizer_server = BaseServer(LEFT_STABILIZER_PORT, "Левый стабилизаторный сервер")
    right_stabilizer_server = BaseServer(RIGHT_STABILIZER_PORT, "Правый стабилизаторный сервер")
    
    # Запускаем потоки серверов
    left_wing_server.start_server_thread()
    right_wing_server.start_server_thread()
    left_stabilizer_server.start_server_thread()
    right_stabilizer_server.start_server_thread()

    time.sleep(8)

    right_wing_server.set_distance(3)

    time.sleep(3)

    right_wing_server.set_distance(2)
    left_stabilizer_server.set_distance(3)

    time.sleep(3)

    right_wing_server.set_distance(1)
    left_stabilizer_server.set_distance(2)
    left_wing_server.set_distance(3)

    time.sleep(3)

    right_wing_server.set_distance(100)
    left_stabilizer_server.set_distance(1)
    left_wing_server.set_distance(2)
    right_stabilizer_server.set_distance(3)

    time.sleep(3)

    right_wing_server.set_distance(100)
    left_stabilizer_server.set_distance(100)
    left_wing_server.set_distance(1)
    right_stabilizer_server.set_distance(2)

    time.sleep(3)

    right_wing_server.set_distance(100)
    left_stabilizer_server.set_distance(100)
    left_wing_server.set_distance(100)
    right_stabilizer_server.set_distance(1)

    time.sleep(3)

    right_wing_server.set_distance(100)
    left_stabilizer_server.set_distance(100)
    left_wing_server.set_distance(100)
    right_stabilizer_server.set_distance(100)

    time.sleep(3)


# Проверка, запущен ли скрипт непосредственно
if __name__ == "__main__":
    # Вызов основной функции
    main()
