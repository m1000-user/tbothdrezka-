import smtplib
import config
from email.mime.text import MIMEText
from telebot import *
import threading
import imaplib
import email
import text
import logging

logger = telebot.logger
bot = telebot.TeleBot(token=config.token) # --> @BotFather

@bot.message_handler(commands=['start'])
def start_message(message):
    log(message)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Актуальное зеркало', callback_data='data1')
    markup.add(btn1)
    bot.send_message(message.chat.id, 'Привет я бот для получения актульного зеркала на HDREZKA',reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def cback(call):
    if call.data == 'data1':
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(config.email, config.password) # --> your email and password p.s APP-PASSWORD, NOT DEFAULT

        mail.list()

        mail.select('INBOX')

        result, data = mail.search(None, 'ALL')

        ids = data[0]
        id_list = ids.split()
        latest_email_id = id_list[-1] # ONLY LATEST EMAIL !!!
        result, data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]
        raw_email_string = raw_email.decode('utf-8')

        email_message = email.message_from_string(raw_email_string)

        if email_message.is_multipart():
            for payload in email_message.get_payload():
                body = payload.get_payload(decode=True).decode('utf-8')
                if 'hdrezka' not in body[817:834]:
                    pass
                else:
                    bot.send_message(call.message.chat.id, text.text_mirror + body[817:834]) # please, print body and
                    # check your 'hdrezka' positions with index() , or find()
        else:
            body = email_message.get_payload(decode=True).decode('utf-8')
            print(body[817:834])



def update(): # EVERY 15 MINUTES SEND MESSAGE TO HDREZKA
    threading.Timer(900.0, update).start()
    sender = config.email
    password = config.password
    hdrezka = 'mirror@hdrezka.org'

    server = smtplib.SMTP('smtp.gmail.com', 587) # dot required
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText('hdrezka')
        msg["Subject"] = 'get mirror'
        server.sendmail(sender, hdrezka, msg.as_string())
        print('message successfully send')
    except Exception as ex:
        print(ex)

def log(message):
    print("<!------!>")
    print(datetime.now())
    print("Message from {0} {1} (id = {2}) \n {3}".format(message.from_user.first_name,
                                                      message.from_user.last_name,
                                                      str(message.from_user.id), message.text))






if __name__ == "__main__":
    telebot.logger.setLevel(logging.INFO)
    update()
    bot.infinity_polling()