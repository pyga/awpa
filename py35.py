class exec(object):
    pass

def f():
    yield from f

async def f():
    await f

x = f(
    x for x in y,
)
