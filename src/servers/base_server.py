import asyncio
import threading
from loguru import logger

from aiohttp import web

class BaseServer:
    def __init__(self, port: int, name: str = "Unknown") -> None:
        self.distance = 100
        self._server_thread = None
        self.name = name
        self.port = port

    async def handle_get(self, request):
        return web.json_response({'distance': self.distance})

    async def handle_echo(self, request):
        try:
            data = await request.json()
            message = data.get('message', '')
        except:
            message = await request.text()
        return web.Response(text=f"Echo: {message}")

    def set_distance(self, distance: int):
        self.distance = distance

    async def create_server_coroutine(self):
        app = web.Application()
        app.router.add_get('/distance', self.handle_get)
        app.router.add_post('/echo', self.handle_echo)
 
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, 'localhost', self.port)
        await site.start()
        logger.info(f"Server {self.name} started at http://localhost:{self.port}")

        # Run the server until it is stopped
        try:
            while True:
                await asyncio.sleep(3600)  # sleep for an hour
        except asyncio.CancelledError:
            pass

    def start_server_thread(self):
        assert self._server_thread is None
        self._server_thread = threading.Thread(target=lambda: asyncio.run(self.create_server_coroutine()), daemon=True)
        self._server_thread.start()
