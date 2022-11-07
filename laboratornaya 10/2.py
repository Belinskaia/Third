from collections import namedtuple
from asyncio import create_task
import asyncio
import aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)

async def fetch_ip(service):
    async with aiohttp.ClientSession() as session:
        async with session.get(service.url) as resp:
            text = await resp.text()
            print('{:.70}...'.format(text))


async def asynchronous(tpl):
    pending = []
    for s in tpl:
        t = create_task(fetch_ip(s))
        pending.append(t)
    await asyncio.wait(pending, return_when = asyncio.FIRST_COMPLETED)
asyncio.run(asynchronous(SERVICES))
