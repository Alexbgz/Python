import asyncio


async def send_echo(reader, writer):
    while True:
        data = await reader.read(1024)
        if not data or data.decode('utf8') == 'close':
            break
        writer.write(data)

    writer.close()

loop = asyncio.get_event_loop()
coro = asyncio.start_server(send_echo, '127.0.0.1', 8181)

server = loop.run_until_complete(coro)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
