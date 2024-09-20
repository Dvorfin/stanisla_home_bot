from turtledemo.penrose import start
import playsound
import os
import telebot
import datetime
from telebot import types
from config import token


bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    print(f"Someone entered bot, {datetime.datetime.now()}")
    start_foto = open('pictures/start_foto.jpg', 'rb')
    bot.send_photo(message.chat.id, start_foto, caption="Приветствуем тебя в Станисла хоум!")
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

    elif message.text == 'button_play_sound':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        sound_1 = types.KeyboardButton("capuchino")
        sound_2 = types.KeyboardButton("chitir_chitir")
        sound_3 = types.KeyboardButton("dack_is_that")
        sound_4 = types.KeyboardButton("remont_starts_with_coffe")
        button_back = types.KeyboardButton('back')
        keyboard.add(sound_1, sound_2, sound_3, sound_4, button_back)
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.send_message(message.chat.id, 'Выбираем смачный звук:', reply_markup=keyboard)  # хендлим реплай

    elif message.text == 'capuchino':
        playsound.playsound(os.getcwd() + "\\sounds\\capuchino.mp3")
        bot.delete_message(message.chat.id, message.message_id)

    elif message.text == 'chitir_chitir':
        playsound.playsound(os.getcwd() + "\\sounds\\chitir_chitir.mp3")
        bot.delete_message(message.chat.id, message.message_id)

    elif message.text == 'dack_is_that':
        playsound.playsound(os.getcwd() + "\\sounds\\dack_is_that.mp3")
        bot.delete_message(message.chat.id, message.message_id)

    elif message.text == 'remont_starts_with_coffe':
        playsound.playsound(os.getcwd() + "\\sounds\\remont_starts_with_coffe.mp3")
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
    bot.infinity_polling()
    print(f"Bot stopped, {datetime.datetime.now()}")