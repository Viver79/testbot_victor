import telebot

bot

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