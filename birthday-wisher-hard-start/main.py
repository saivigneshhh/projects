import smtplib
import random
import datetime as dt
import pandas as pd

now=dt.datetime.now()
date=now.day
month=now.month
today_tupple=(month,date)

csv=pd.read_csv("birthdays.csv")
bday={(csv_row["month"],csv_row["day"]):csv_row for (index,csv_row) in csv.iterrows()}
if today_tupple in bday:
    file=f"letter_templates/letter_{random.randint(1,3)}.txt"
    birthday_person=bday[today_tupple]
    with open(file) as letter:
        content=letter.read()
        content=content.replace("NAME",birthday_person["name"])

    my_email = "teluguaivideo@gmail.com"
    my_password = "wizgfsubewcldguv"
    with smtplib.SMTP("smtp.gmail.com")as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="saivignesh0009@gmail.com",
                            msg=f"subject:HAPPY BIRTHDAY:) \n\n {content}"
                            )




