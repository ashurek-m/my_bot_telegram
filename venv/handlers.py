from agent_smith_bot import bot, dp
from aiogram.types import Message
import constant

async def send_admin_ms():
    await bot.send_message(chat_id=massage.from_user.id, text='Бот запущен')