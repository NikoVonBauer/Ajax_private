import telebot
from token_main import token, chatId
from telegram import InputMediaPhoto
import telebot.types

bot = telebot.TeleBot(token)
bot.send_message(chatId, '~Lab~', parse_mode='MarkdownV2')
img = open("Photo_tipis.jpg", 'rb')
bot.send_photo(chatId, img)
audio = open("ZHIZN.mp3", 'rb')
bot.send_audio(chatId, audio)
audio_mess = open("audio_m.ogg", 'rb')
bot.send_audio(chatId, audio_mess)
video = open("Vidos.mp4", 'rb')
bot.send_video(chatId, video)
media_group = [telebot.types.InputMediaPhoto(open("Photo_tipis.jpg", 'rb')), 
               telebot.types.InputMediaPhoto(open("Photo_tipis.jpg", 'rb'))]
bot.send_media_group(chatId, media_group)
bot.send_contact(chatId, '+79126540111', 'Danon')