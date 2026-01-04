from telethon import TelegramClient
import asyncio

api_id = 35569065
api_hash = "7a528cff62ca6b87f82be363e5430bac"
group_link = "https://t.me/+F4G3YDOcL381ZjRh"

client = TelegramClient("session", api_id, api_hash)

async def main():
    await client.start()
    saved = await client.get_entity("me")
    group = await client.get_entity(group_link)

    async for msg in client.iter_messages(saved):
        if msg.video:
            await client.send_file(group, msg.video)
            await asyncio.sleep(10)

with client:
    client.loop.run_until_complete(main())