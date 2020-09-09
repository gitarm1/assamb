import smtplib
from email.message import EmailMessage

email = EmailMessage()

email ['from'] = "Assambleya live"

email ['subject'] = """Сообщение от Assambleya live"""

email.set_content("""Поздравляем!!!
Казино Assambleya Дарит вам подарок 5000₽ на первое пополнение!!!
Минимум пополнение 500 руб.
Моментальный вывод Выигрыша!!!!:
Желаю вам приятной игры: Assambleya.live""")



f = open("users.txt", "r")
list = f.read().splitlines()
f.close()


i = 0
while True:
    email ['to'] = list[i]
    with smtplib.SMTP(host = "smtp.gmail.com",port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("assambleyacasino@gmail.com", "Arm.551355")
        smtp.send_message(email)
        print(i)
        i = i + 1
