import asyncio
import threading
from loguru import logger

from aiohttp import web

# Этот сервер используется для имитации детектора расстояния
class BaseServer:
    def __init__(self, port: int, name: str = "Unknown") -> None:
        # Инициализируем расстояние до 100
        self.distance = 100
        # Инициализируем серверный поток до None
        self._server_thread = None
        # Инициализируем имя сервера
        self.name = name
        # Инициализируем порт сервера
        self.port = port

    # Обрабатываем GET-запрос
    async def handle_get(self, request):
        # Возвращаем JSON-ответ с текущим расстоянием
        return web.json_response({'distance': self.distance})

    # Устанавливаем расстояние
    def set_distance(self, distance: int):
        # Обновляем текущее расстояние
        self.distance = distance

    # Создаем корутину сервера
    async def create_server_coroutine(self):
        # Создаем веб-приложение
        app = web.Application()
        # Добавляем GET-маршрут для расстояния
        app.router.add_get('/distance', self.handle_get)
 
        # Создаем AppRunner
        runner = web.AppRunner(app)
        # Настраиваем AppRunner
        await runner.setup()
        # Создаем TCPSite
        site = web.TCPSite(runner, 'localhost', self.port)
        # Запускаем TCPSite
        await site.start()
        # Логируем запуск сервера
        logger.info(f"Server {self.name} started at http://localhost:{self.port}")

        # Запускаем сервер до его остановки
        try:
            # Спим час
            while True:
                await asyncio.sleep(3600)
        except asyncio.CancelledError:
            # Обрабатываем ошибку отмены
            pass

    # Запускаем поток сервера
    def start_server_thread(self):
        # Проверяем, что поток сервера не запущен ранее
        assert self._server_thread is None
        # Создаем поток сервера
        self._server_thread = threading.Thread(target=lambda: asyncio.run(self.create_server_coroutine()), daemon=True)
        # Запускаем поток сервера
        self._server_thread.start()
