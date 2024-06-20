import asyncio

from telethon import TelegramClient, events
from settings import settings


def upload_callback(current, total):
    print('Uploaded', current, 'out of', total, 'bytes: {:.2%}'.format(current / total))


async def main():
    async with TelegramClient(settings.SESSION, settings.API_ID, settings.API_HASH) as client:
        file = await client.upload_file(
            settings.ATTACH_FILE_PATH, progress_callback=upload_callback
        ) if settings.ATTACH_FILE_PATH else None

        @client.on(events.NewMessage(incoming=True, pattern=settings.PATTERN))
        async def handler(event):
            if event.is_private:
                await event.respond(settings.MESSAGE, file=file)

        await client.run_until_disconnected()


if __name__ == '__main__':
    asyncio.run(main())
