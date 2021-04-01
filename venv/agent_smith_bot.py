import aiogram
import constant
import asyncio

loop = asyncio.get_event_loop()
bot = aiogram.Bot(constant.token)
dp = aiogram.Dispatcher(bot, loop)

if __name__ == '__agent_smith_bot__':
    from handlers import dp, send_admin_ms
    aiogram.executor.start_polling(dp, on_startup=send_admin_ms)
