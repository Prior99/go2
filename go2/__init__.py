import asyncio
from autobahn.asyncio.websocket import WebSocketServerFactory

factory = WebSocketServerFactory()
factory.protocol = Go2Protocol

loop = asyncio.get_event_loop()
accept = loop.create_server(factory, '::1', 2338)
server = loop.run_until_complete(accept)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally
    server.close()
    loop.close()

