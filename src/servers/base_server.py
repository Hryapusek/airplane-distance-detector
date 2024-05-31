import asyncio
import threading
from loguru import logger

from aiohttp import web

# This server is used to immitate distance detector
class BaseServer:
    def __init__(self, port: int, name: str = "Unknown") -> None:
        # Initialize distance to 100
        self.distance = 100
        # Initialize server thread to None
        self._server_thread = None
        # Initialize server name
        self.name = name
        # Initialize server port
        self.port = port

    # Handle GET request
    async def handle_get(self, request):
        # Return JSON response with current distance
        return web.json_response({'distance': self.distance})

    # Set distance
    def set_distance(self, distance: int):
        # Update current distance
        self.distance = distance

    # Create server coroutine
    async def create_server_coroutine(self):
        # Create web application
        app = web.Application()
        # Add GET route for distance
        app.router.add_get('/distance', self.handle_get)
 
        # Create AppRunner
        runner = web.AppRunner(app)
        # Set up AppRunner
        await runner.setup()
        # Create TCPSite
        site = web.TCPSite(runner, 'localhost', self.port)
        # Start TCPSite
        await site.start()
        # Log server start
        logger.info(f"Server {self.name} started at http://localhost:{self.port}")

        # Run the server until it is stopped
        try:
            # Sleep for an hour
            while True:
                await asyncio.sleep(3600)
        except asyncio.CancelledError:
            # Handle cancelled error
            pass

    # Start server thread
    def start_server_thread(self):
        # Check if server thread is not already running
        assert self._server_thread is None
        # Create server thread
        self._server_thread = threading.Thread(target=lambda: asyncio.run(self.create_server_coroutine()), daemon=True)
        # Start server thread
        self._server_thread.start()
