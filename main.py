import asyncio
from pyrogram import Client, filters, idle
from pyrogram.types import Message, ChatPrivileges
import os

app = Client(
    "userbot",
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
    session_string=os.environ["SESSION_STRING"],
)

@app.on_message(filters.command("addbot", prefixes=".") & filters.me)
async def add_bot(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.delete()
    username = message.command[1].lstrip("@")
    try:
        await client.add_chat_members(message.chat.id, username)
        await client.promote_chat_member(
            message.chat.id, username,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_promote_members=True,
                can_change_info=True,
                can_invite_users=True,
                can_pin_messages=True,
            )
        )
    except:
        pass
    await message.delete()

async def main():
    await app.start()
    await idle()
    await app.stop()

asyncio.run(main())
