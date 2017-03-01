import asyncio
from aiohttp import web
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy)
loop = asyncio.get_event_loop()

app = web.Application(loop=loop, middlewares=[

])