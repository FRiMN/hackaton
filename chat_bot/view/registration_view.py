from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove

class RegistrationView:

    def __init__(self, bot):
        self.bot = bot

    def build_menu(self,
                   buttons,
                   n_cols,
                   header_buttons=None,
                   footer_buttons=None):
        menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
        if header_buttons:
            menu.insert(0, [header_buttons])
        if footer_buttons:
            menu.append([footer_buttons])
        return menu

    def ask_adress(self, chat_id, user):
        answer = f"Здравствуйте, {user.first_name}! \nЧтобы получать уведомления сервиса 'Умный город',  укажите адрес дома"
        return self.bot.send_message(chat_id=chat_id, text=answer)


    def not_found(self, chat_id, adr):
        return self.bot.send_message(chat_id=chat_id,
                                        text=f'Не знаю в городе адреса похожего на "{adr}".Может опечатка?\nУточните адрес.')

    def too_many_found(self, chat_id, msg, count):
        return self.bot.send_message(chat_id=chat_id,
                                        text=f'Я знаю слишком много ({count}) адресов, похожих на "{msg}".\nУточните адрес.')

    def choose_address(self, chat_id, addresses):
        button_list = [InlineKeyboardButton(adr['address'], callback_data=adr['address'])
                       for adr in addresses]
        reply_markup = InlineKeyboardMarkup(self.build_menu(button_list, n_cols=2))
        return self.bot.send_message(chat_id=chat_id, text='Один из этих адресов?',
                                        reply_markup=reply_markup)

    def reply_success(self, chat_id, user):
        # delete menu
        address = user["address"]
        reply_markup = ReplyKeyboardRemove()
        self.bot.send_message(chat_id=chat_id,
                                 text=f'Ok, запишем: Что будет нового по адресу: {address} сообщить {user["first_name"]}',
                                 reply_markup=reply_markup)


    def not_found_user(self, chat_id):
        return self.bot.send_message(chat_id=chat_id, text='Мы знакомы?')

    def change_adress(self, chat_id):
        return self.bot.send_message(chat_id=chat_id, text='Функционал смены адреса в разработке.')