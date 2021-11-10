import telebot
from telebot import TeleBot

import constants

bot: TeleBot = telebot.TeleBot(constants.token)

#  bot.send_message(348473859, "test")

#  upd = bot.get_updates()
#  print(upd)

#  last_upd = upd(-1)
#  message_from_user = last_upd.message
#  print(message_from_user)

print(bot.get_me())


def log(message, answer):
    print("\n -----")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от (0) (1). (id = (2)) \n Текст - (3)".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print(answer)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, constants.startAnswer)

@bot.message_handler(commands=["help"])
def handle_text(message):
    bot.send_message(message.chat.id, """Ну ничего себе у тебя запросы!""")

@bot.message_handler(commands=['whoareyou'])
def handle_start(message):
    bot.send_message(message.chat.id, constants.Whoareyou)

@bot.message_handler(content_types={"text"})
def handle_text(message):
    if "Кто солнышко" in message.text:
        answer = constants.random_message2
        bot.send_message(message.chat.id, constants.random_message2())
        log(message, answer)
    if "Совет дня" in message.text:
        answer = constants.random_message3
        bot.send_message(message.chat.id, constants.random_message3())
        log(message, answer)
    elif message.text == "А":
        answer = "Б"
        log(message, answer)
        bot.send_message(message.chat.id, "Б")
    elif message.text == "Б":
        answer = "Ты играть не умеешь?"
        bot.send_message(message.chat.id, "Ты играть не умеешь?")
        log(message, answer)
    elif message.text == "В":
        answer = "Г"
        bot.send_message(message.chat.id, "Г")
        log(message, answer)
    elif message.text == "Д":
        answer = "Прекращай уже"
        bot.send_message(message.chat.id, "Прекращай уже")
        log(message, answer)
    elif message.text == "1" or message.text == "2":
        answer = "Я гуманитарий"
        bot.send_message(message.chat.id, "Я гуманитарий")
        log(message, answer)
    elif message.text == "Кек":
        answer = "Тимур"
        bot.send_message(message.chat.id, "Тимур")
        log(message, answer)
    elif message.text == "Сука":
        answer = "Иди нахуй"
        bot.send_message(message.chat.id, "Иди нахуй")
        log(message, answer)
    elif "аха" in message.text:
        answer = "Ахахахахаха"
        bot.send_message(message.chat.id, "Ахахахахаха")
        log(message, answer)
    elif message.text == "Тимур":
        answer = "ДА ВЫ ДОСТАЛИ, ДАЙТЕ АНИМЕ ПОСМОТРЕТЬ НОРМАЛЬНО!"
        bot.send_message(message.chat.id, "ДА ВЫ ДОСТАЛИ, ДАЙТЕ АНИМЕ ПОСМОТРЕТЬ НОРМАЛЬНО!")
        log(message, answer)
    elif "Тимур ты кто" in message.text:
        answer = "Я репер"
        bot.send_message(message.chat.id, "Я репер")
        log(message, answer)
    elif "Влад" in message.text:
        answer = "плак"
        bot.send_message(message.chat.id, "плак")
        log(message, answer)
    elif "влад" in message.text:
        answer = "плаккк"
        bot.send_message(message.chat.id, "плаккк")
        log(message, answer)
    elif "Брак вознаграждение" in message.text or message.text == "брак вознаграждение":
        answer = "у меня тоже могла быть жабья семья..."
        bot.send_message(message.chat.id, "у меня тоже могла быть жабья семья...")
        log(message, answer)
    elif "никита" in message.text:
        answer = "@suiiyiux @Belyank1n @makaroshnaya @grustnyichai @RinnaTyan @youohomi @desbesh @youohomi"
        bot.send_message(message.chat.id, "@suiiyiux @Belyank1n @makaroshnaya @grustnyichai @RinnaTyan @youohomi @desbesh @youohomi")
        log(message, answer)
    elif message.text == "Роберт":
        answer = constants.random_message5
        bot.send_message(message.chat.id, constants.random_message5())
        log(message, answer)
    elif message.text == "Нет" or message.text == "нет":
        answer = "Пидора ответ"
        bot.send_message(message.chat.id, "Пидора ответ")
        log(message, answer)
    elif message.text == "Да" or message.text == "да":
        answer = "пизда"
        bot.send_message(message.chat.id, "пизда")
        log(message, answer)
    if "Какое пиво" in message.text:
        answer = constants.random_message1
        bot.send_message(message.chat.id, constants.random_message1())
        log(message, answer)

   

bot.polling(none_stop=True, interval=0)
