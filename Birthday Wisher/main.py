import smtplib
import datetime as dt
import random

my_email = 'User Email'
password = 'Password'


now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open('quotes.txt') as quote_file
        all_quotes = quote_file.readline()
        quote = random.choice(all_quotes)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='Receiver Email', msg=f'subject:Monday motivation\n\n{quote}')
