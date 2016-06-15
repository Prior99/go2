import asyncio
import logging
import go2

logger = logging.getLogger('websockets.server')
logger.setLevel(logging.ERROR)
logger.addHandler(logging.StreamHandler())

loop = asyncio.get_event_loop()
server = loop.run_until_complete(go2.accept)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    server.close()
    go2.close()
    loop.close()
    print('Goodbye!')

