from aiogram import Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.dispatcher.filters.builtin import (
    Text
)

from bot.misc import (
    dp, 
    scheduler,
)
from bot.handlers import (
    commands as c,
    errors as e,
    inlines as i,
    messages as m,
    posts as p,
    queries as q,
    schedules as s,
)
from bot.utils import (
    example_cd,
    pagination_cd,
)


async def on_startup(dp: Dispatcher):
    # handle commands 
    #   register_message_handler
    #   register_edited_message_handler
    dp.register_message_handler(c.getid, commands=['id'])
    dp.register_message_handler(c.keyboard, commands=['kb'])
    dp.register_message_handler(c.lang, commands=['lang'])
    dp.register_message_handler(c.pagination, commands=['pages'])
    dp.register_message_handler(c.start, commands=['start'])
    
    # errors
    #   register_errors_handler
    
    # inlines
    #   register_inline_handler
    #   register_chosen_inline_handler

    # handle messages
    dp.register_message_handler(m.hello)

    # posts
    #   register_channel_post_handler
    #   register_edited_channel_post_handler
    
    # queries
    #   register_callback_query_handler
    #   register_shipping_query_handler
    #   register_pre_checkout_query_handler
    lcq = lambda callback_query: True
    dp.register_callback_query_handler(q.pagination, pagination_cd.filter())
    dp.register_callback_query_handler(q.example, example_cd.filter())
    
    # schedulers
    #   scheduler.add_job

    # scheduler.add_job(s.sch_hello, 'interval', seconds=10)