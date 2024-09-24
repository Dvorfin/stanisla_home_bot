import sys
sys.path.append("/home/stanisla/PycharmProjects/stanisla_home_bot/venv/lib/python3.10/site-packages")


import playsound
import os
import telebot
from telebot.apihelper import ApiTelegramException
import datetime
from telebot import types
import logging
from config import token


bot=telebot.TeleBot(token)
logging.basicConfig(level=logging.INFO, filename="bot_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")


directory = os.getcwd() + "/sounds"
print(directory)
# Получаем список файлов
files = os.listdir(directory)
sound_files = list(map(lambda x: x[0:-4], files))


@bot.message_handler(commands=['start'])
def start_message(message):
    print(f"Someone entered bot, {datetime.datetime.now()}")
    start_foto = open('pictures/start_foto.jpg', 'rb')
    bot.send_photo(message.chat.id, start_foto, caption="Приветствуем тебя в Станисла хоум!")

    with open("users_id.txt", 'r+', encoding="utf-8") as file:
        user_id = str(message.chat.id)
        print(f"User_id: {user_id}")
        file.writelines(user_id)
        logging.info(f"New user with id {user_id} started bot")

    #bot.send_message(message.chat.id,"Приветствуем тебя в Станисла хоум!")

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_start = types.KeyboardButton("Open your ihome")
    keyboard.add(button_start)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=keyboard)

@bot.message_handler(commands=['menu'])
def menu(message):
    c1 = types.BotCommand(command='start', description='Start the Bot')
    c2 = types.BotCommand(command='menu', description='Menu')
    bot.set_my_commands([c1, c2])
    bot.set_chat_menu_button(message.chat.id, types.MenuButtonCommands('commands'))


@bot.message_handler(content_types=['text'])
def menu(message):
    if message.text == "Open your ihome":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_play_sound = types.KeyboardButton("button_play_sound")
        button_movement = types.KeyboardButton("button_movement")
        button_random = types.KeyboardButton("button_random")
        button_back = types.KeyboardButton('back')

        keyboard.add(button_play_sound, button_movement, button_random, button_back)
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.send_message(message.chat.id, 'Меню:', reply_markup=keyboard) # хендлим реплай
        print(f"Open your ihome clicked, {datetime.datetime.now()}")
        logging.info(f"Button Open your ihome clicked.")

    elif message.text == 'button_play_sound':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for sound_file in sound_files:
            sound = types.KeyboardButton(sound_file)
            keyboard.add(sound)

        button_back = types.KeyboardButton('back')
        keyboard.add(button_back)
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.send_message(message.chat.id, 'Выбираем смачный звук:', reply_markup=keyboard)  # хендлим реплай
        print(f"Button play sound clicked, {datetime.datetime.now()}")
        logging.info(f"Button play sound clicked.")

    elif message.text in sound_files:
        sound = message.text
        playsound.playsound(os.getcwd() + f"/sounds/{sound}.mp3")
        bot.delete_message(message.chat.id, message.message_id)
        print(f"Button {sound} clicked, {datetime.datetime.now()}")
        logging.info(f"Sound {sound} played.")

    elif message.text == "back":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_play_sound = types.KeyboardButton("button_play_sound")
        button_movement = types.KeyboardButton("button_movement")
        button_random = types.KeyboardButton("button_random")
        button_back = types.KeyboardButton('back')

        keyboard.add(button_play_sound, button_movement, button_random, button_back)
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, 'Меню:', reply_markup=keyboard)  # хендлим реплай
        print(f"Button back clicked, {datetime.datetime.now()}")
        logging.info(f"Button back clicked.")

# @bot.message_handler(content_types=['text'])
# def message_reply(message):
#     if message.text == "Кнопка_1":
#         bot.send_message(message.chat.id,"нажата кнопка 1")
#         # здесь сделать запрос на
#     elif message.text == "Кнопка_2":
#         #bot.send_message(message.chat.id, "нажата кнопка 2")
#         bot.register_next_step_handler(message, second_button_message)
#     elif message.text == "Кнопка_назад":
#         bot.register_next_step_handler(message, button_message)



if __name__ == '__main__':
    print(f"Bot started, {datetime.datetime.now()}")
    logging.info(f"Bot started.")

    with open("users_id.txt", 'r+', encoding="utf-8") as file:
        user_ids = file.readlines()
        for user_id in user_ids:
            try:
                bot.send_message(user_id, "Бот запущен.")
            except ApiTelegramException as e:
                print(f"Got error during sending msg to user {user_id}: {e}")
                logging.warning(f"Got error during sending msg to user {user_id}: {e}")

    bot.infinity_polling()

    with open("users_id.txt", 'r+', encoding="utf-8") as file:
        user_ids = file.readlines()
        for user_id in user_ids:
            try:
                bot.send_message(user_id, "Бот остановлен.")
            except ApiTelegramException as e:
                print(f"Got error during sending msg to user {user_id}: {e}")
                logging.warning(f"Got error during sending msg to user {user_id}: {e}")

    print(f"Bot stopped, {datetime.datetime.now()}")
    logging.info(f"Bot stoped.")