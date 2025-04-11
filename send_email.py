#!/usr/bin/env python3
import os
import smtplib
import datetime
from art import tprint
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.filedialog as fd

load_dotenv()

# variables
logo = tprint('SEND EMAIL', font='small')
send_from = os.getenv.get('SEND_FROM')
print(send_from)
password = os.getenv.get('MY_PASS')
addr_to = os.getenv.get('ADDR_TO')
bcc_to = os.getenv.get('BCC_TO')
time_now = datetime.datetime.now().strftime("%H:%M")
date_now = datetime.datetime.now().strftime("%d.%m.%y")


def gui():
    def send_email():
        cashless_payment = str(cashless.get())
        card_pay = str(card.get())
        cash_pay = str(cash.get())
        qr_pay = str(qr.get())
        # Изначально значения None
        body_cashless = ''
        body_card = ''
        body_cash = ''
        body_qr = ''
        # Проверка, является ли поле пустое
        if cashless_payment:
            body_cashless = f'Безналичная оплата: {cashless_payment}\n'
        if card_pay:
            body_card = f'На карту: {card_pay}\n'
        if cash_pay:
            body_cash = f'Наличные: {cash_pay}\n'
        if qr_pay:
            body_qr = f'QR-код: {qr_pay}\n'

        try:
            filepath = filename
            msg = MIMEMultipart()  # Создаем сообщение
            msg['From'] = send_from  # Адресат
            msg['To'] = addr_to  # Получатель
            msg['Subject'] = date_now  # Тема сообщения
            msg['Bcc'] = bcc_to # Скрытая копия

            body = (f'Добрый вечер!\n'  # Текст сообщения
                    f'\n'
                    f'{body_cashless}'
                    f'{body_card}'
                    f'{body_qr}'
                    f'{body_cash}'
                    '\n'
                    'С уважением, Анастасия\n'
                    'Администратор\n'
                    'ReInTa Clinic\n'
                    'ООО "ФЭМИЛИС"\n'
                    'Москва, Новолесной переулок 5\n'
                    'тел.: +7(499)1103777\n')
            msg.attach(MIMEText(body, 'plain'))  # Добавляем в сообщение текст
            excel = MIMEApplication(open(filepath, 'rb').read())  # Открываем файл
            excel.add_header('Content-Disposition', 'attachment', filename=date_now + '.xlsx')  # Добавляем заголовки письма
            msg.attach(excel)  # Добавляем в сообщение файл

            server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)  # SMTP
            server.login(send_from, password)
            server.send_message(msg)
            server.quit()
            messagebox.showinfo(title='Статус', message=f'Письмо успешно отправлено в {time_now}')
            window.destroy()

        # except

        except smtplib.SMTPAuthenticationError:
            messagebox.showinfo(title='Статус', message='Ошибка авторизации. Проверь пароль')

    # GUI

    window = Tk()
    window.title('Отправка отчета')
    window.geometry('400x350')

    frame = Frame(window, padx=10, pady=10)
    frame.pack(expand=True)

    # file
    def choose_file():
        global filename
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/")
        file_label.config(text=f'Файл выбран: %s' % filename)
        return filename

    # Подписи к кнопкам
    cashless_input = Label(frame, text="Безналичная оплата")
    cashless_input.grid(row=3, column=1)

    cash_input = Label(frame, text="На карту",)
    cash_input.grid(row=4, column=1)

    qr_input = Label(frame, text="QR-Код",)
    qr_input.grid(row=5, column=1)

    cash_input = Label(frame, text="Наличные",)
    cash_input.grid(row=6, column=1)

    cashless = Entry(frame)
    cashless.grid(row=3, column=2, pady=5)

    card = Entry(frame)
    card.grid(row=4, column=2, pady=5)

    qr = Entry(frame)
    qr.grid(row=5, column=2, pady=5)

    cash = Entry(frame)
    cash.grid(row=6, column=2, pady=5)

    file_label = Label(frame, text = "")
    file_label.grid(row = 8, column = 1, columnspan = 2)


    # Buttons
    btn_file = tk.Button(window, text='Отправить', command=send_email)
    btn_file.pack(pady=10)

    send_button = Button(frame, text="Выбрать файл", command=choose_file)
    send_button.grid(row=7, column=2)

    exit_button = Button(window, text="Выход", command=window.destroy)
    exit_button.pack(pady=10)

    window.mainloop()


if __name__ == '__main__':
    gui()
