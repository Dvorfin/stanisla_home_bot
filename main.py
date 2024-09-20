
import playsound
import os
import telebot
import datetime
from telebot import types
from config import token


bot=telebot.TeleBot(token)

directory = "./sounds"

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

    elif message.text in sound_files:
        playsound.playsound(os.getcwd() + f"/sounds/{message.text}.mp3")
        bot.delete_message(message.chat.id, message.message_id)

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

    with open("users_id.txt", 'r+', encoding="utf-8") as file:
        user_ids = file.readlines()
        for user_id in user_ids:
            bot.send_message(user_id, "Бот запущен.")

    bot.infinity_polling()

    with open("users_id.txt", 'r+', encoding="utf-8") as file:
        user_ids = file.readlines()
        for user_id in user_ids:
            bot.send_message(user_id, "Бот остановлен.")

    print(f"Bot stopped, {datetime.datetime.now()}")