import asyncio
from autobahn.asyncio.websocket import WebSocketServerFactory
from protocol import Go2Protocol

factory = WebSocketServerFactory()
factory.protocol = Go2Protocol

loop = asyncio.get_event_loop()
accept = loop.create_server(factory, '0.0.0.0', 2338)
server = loop.run_until_complete(accept)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    server.close()
    loop.close()

