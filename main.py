import asyncio
import logging
from src import server

logger = logging.getLogger('websockets.server')
logger.setLevel(logging.ERROR)
logger.addHandler(logging.StreamHandler())

loop = asyncio.get_event_loop()
task = loop.run_until_complete(server.accept)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    task.close()
    server.close()
    loop.close()
    print('Goodbye!')

