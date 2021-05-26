## -*- coding: utf-8 -*-
import telebot, vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

token = "1720175651:AAGQePH6EBc1LD81ogaMbZE0ELkNCukGuRA"
bot = telebot.TeleBot(token)

vk_session = vk_api.VkApi(token="eafd22df108f95d1449ab77635650aa878d089231eb5ce40c09ac6e01ddbdbef5948c6c173abc886c01ca")
longpoll = VkBotLongPoll(vk_session, 204807373)
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_user:
            id = event.obj.from_id
            msg = event.obj.text

            bot.send_message(  
                1223383408,
                msg
            )