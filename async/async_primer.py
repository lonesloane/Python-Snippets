import asyncio


async def sleeper(delay):
    await asyncio.sleep(delay)
    print('Finished sleeper with delay {}'.format(delay))


loop = asyncio.get_event_loop()

results = loop.run_until_complete(asyncio.wait((
    sleeper(1),
    sleeper(3),
    sleeper(2)
)))
