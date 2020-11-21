import telebot
import json

bot = telebot.TeleBot('1432118716:AAE-_JYwCRoGr8zAQbkr2i3vLpdHQZIzGqk')

with open('courses.txt', encoding="utf8") as file:
    courses = [item.split(',') for item in file]
with open('planning.json', encoding="utf8") as json_file:
    data = json.load(json_file)



@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(commands=['help'])
def help(message):
    res = '/courses - список курсов \n' \
          '/planning - расписание запуска курсов'
    bot.reply_to(message, res)


@bot.message_handler(commands=['courses'])
def echo_message_courses(message):

    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)

    for text, url in courses:
        url_button = telebot.types.InlineKeyboardButton(text=text, url=url.strip(' \n'))
        keyboard.add(url_button)
    bot.send_message(message.chat.id, "Привет! Выбери курс", reply_markup=keyboard)

@bot.message_handler(commands=['planning'])
def echo_message_plannin(message):

    res = ''
    for item in data['courses']:
        res += f"<b>{item['course']}</b>\n" \
                   f"<i>Online:</i> <code>{item['schedule']['online']}</code>\n" \
                   f"<i>Offline:</i> <code>{item['schedule']['offline']}</code>\n"
    bot.send_message(message.from_user.id, text=res, parse_mode='HTML')


if __name__ == '__main__':
	bot.polling()



