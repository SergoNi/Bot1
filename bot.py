import telebot
TOKEN = "1039905461:AAGaTTvHw5P1gV-sMw5WTRycDzBGKNh6Ink"
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, Сергей шлет вам салам')
@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "привет":
        bot.send_message(chat_id, 'Привет, я бот - собственность Сергея Николаева.')
    elif text == "как дела?":
        bot.send_message(chat_id, 'Хорошо, а у тебя?')
    elif text == "женя хоботин":
        bot.send_message(chat_id, 'Васек который не может найти код Вити')
    else:
        bot.send_message(chat_id, 'Простите, я вас не понял :(')
@bot.message_handler(content_types=['photo'])
def text_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Красиво.')

bot.polling()